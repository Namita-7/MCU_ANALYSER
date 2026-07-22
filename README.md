# MCU Capability Analyzer — ESP32-WROOM-32 (DevKit V1)

## 1. MCU-Level Analysis (ESP32-WROOM-32 Datasheet)
Based on the datasheet that I read through, I understood that there is more than just a physical board with gpio pins that communicate with the surroundings, for example The ESP32 MCU supports Ethernet at the silicon level, but the DevKit V1 board does not provide the external PHY and connector required for native Ethernet operation,gpio pins that take input only and all gpio can be used for multiple other application such as boot,strap,etc while some pins are confined only for spi communication and therefore there is alot of difference between MCU and a physical board.

## 2. Board-Level Analysis (DevKit V1 Pinout Diagram)
The DevKit V1 exposes a limited set of GPIOs on the board header, while some ESP32 pins remain reserved, input-only, or unsuitable for general use, 21 GPIO pins can be used to interface the led and other components when required,4pins for input only, 4 pins which include the ground and power and one enable pin.

## 3. Capability Report (board_capabilities.json)
There are two json folders the first one connecting all the information about the board I am using in this assigment, the working gpio pins,uart pins, spi interface pins, I2C pins,adc pin and so on,this JSON records which peripherals are supported by the MCU and which are actually available through the DevKit V1 board’s exposed pins and onboard components, this is purely physical board based file and the next .json file consists of the exapmles like led blinking, spi protocol, so on which are mapped to the project references from the  official ESP-IDF path strings so we maintain a clean separation between our custom configuration and the core framework.

## 4. CLI Tool (analyze.py)
In the analyse.py code, first the libraries argparse for reading command-line flags and json for reading the JSON files are imported. Then next we define a fuction which takes the feature (ex: uart) and the loaded json data.Special case for "ethernet" returns a fixed explanation immediately, as mentioned before ethernet on the board needs external connection.The next if checks two things, that is the peripherals say this feature is true and it does an upperkey (like UART) exsist with the actual data pin, if both are true then it returns supported, the feature is marked as supported in the MCU capabilities but no explicit board-level pin mapping is present, the script treats it as MCU-supported but not fully confirmed at board level.

## 5. SDK Example Recommendations
In the sdk_example.json file,the board's hardware capabilities are mapped directly to official ESP-IDF (v5.0) example project paths.
* **LED Blink** (`https://github.com/espressif/esp-idf/blob/v5.0/examples/get-started/blink/main/blink_example_main.c`): Blink the onboard LED using standard GPIO logic.
* **UART Communication** (`https://github.com/espressif/esp-idf/blob/v5.0/examples/peripherals/uart/uart_echo/main/uart_echo_example_main.c`): Communicate with the board via UART by echoing serial data.
* **ADC Read** (`https://github.com/espressif/esp-idf/blob/v5.0/examples/peripherals/adc/oneshot_read/main/oneshot_read_main.c`): Read analog values from ADC pins using the oneshot driver.
* **I2C Communication** (`https://github.com/espressif/esp-idf/blob/v5.0/examples/peripherals/i2c/i2c_simple/main/i2c_simple_main.c`): Communicate with I2C devices using the master bus configuration.
* **SPI Communication** (`https://github.com/espressif/esp-idf/blob/v5.0/examples/peripherals/spi_master/hd_eeprom/main/spi_eeprom_main.c`): Communicate with external SPI devices (like an EEPROM).
* **Timer** (`https://github.com/espressif/esp-idf/blob/v5.0/examples/peripherals/timer_group/gptimer/main/gptimer_example_main.c`): Set up a periodic hardware timer interrupt using the modern GPTimer API.

## 6. Validation Report
From the above files,datasheet,json codes we can validate this report
#UART: Classified as "Supported" : The script verified that UART is marked true in the peripherals list and found an explicit UART block containing the board-level TX and RX pin mappings.
#ADC: Classified as "Supported by MCU, but board-level pin exposure not verified":The ESP32 chip supports ADC and therefore marked true in the periperals, but because ADC channels share standard GPIO pins rather than having dedicated breakout pins on the DevKit V1, no separate ADC pin block was recorded in the JSON root. The script accurately detects this.
#Ethernet: Classified as "Supported by MCU but not available on board (needs external PHY)" : While the ESP32 silicon contains a built-in Ethernet MAC, the DevKit V1 physical board lacks the required external PHY chip and RJ-45 jack. The script correctly identifies this hardware limitation via a targeted check.

## Setup & Run Instructions
**1.Clone the repository:**
git clone: [https://github.com/Namita-7/MCU_ANALYSER.git](https://github.com/Namita-7/MCU_ANALYSER.git)
cd MCU_ANALYSER 
**2.Dependencies:
This tool uses Python's standard library (argparse and json). No external installations or virtual environments are required. Just ensure you have Python 3.x installed.
**3.Run the Analyzer:
The script requires command-line flags to specify the board and the SDK path. Run the following command in your terminal:
python analyze.py --board esp32-devkitv1 --sdk ./esp-idf

## Extending to Other MCUs and Boards (Reusability)
This tool was designed with a strictly data-driven architecture, meaning the core logic (`analyze.py`) is completely decoupled from the hardware specifications. It can be easily extended to analyze entirely different MCUs (such as an STM32, RP2040, or nRF52) or different board configurations without modifying the underlying Python code.
To extend the tool for a new board, you only need to follow these two steps:
*Update the Hardware Data : ** Replace the contents with the new MCU's datasheet specifications and the new physical board's pinout mappings. As long as the standardized keys (like `"peripherals"` and `"supported_by_mcu"`) are maintained, the `classify()` function will process it automatically.
*Update the SDK Mappings (`sdk_example.json`):** Swap the ESP-IDF example paths with the relevant SDK paths for the new architecture (e.g., STM32Cube HAL examples or Pico SDK paths).
Because the CLI tool dynamically loads these JSON files and parses the `--board` and `--sdk` arguments at runtime, it makes it very easy at the time of excecution.
Example:`python analyze.py --board stm32-nucleo --sdk ./stm32cube`
No changes to the `analyze.py` script are required to evaluate new hardware.

**Video Explanation Link
Google Drive : `https://drive.google.com/drive/folders/1qVW8KxdPs3kpvTYVIMqCb9oO6mFbTtVu?usp=drive_link`

## Ai Usage
AI tools (Claude, GitHub Copilot) were used to assist with code structuring, debugging, and reducing code size making it more robust. All technical claims — MCU specifications, pin mappings, and SDK example paths — were independently verified against the official ESP32-WROOM-32 datasheet and the ESP-IDF GitHub repository.
