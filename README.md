# MCU Capability Analyzer — ESP32-WROOM-32 (DevKit V1)

## 1. MCU-Level Analysis (ESP32-WROOM-32 Datasheet)
Based on the datasheet that I read through, I understood that there is more than just a physical board with gpio pins that communicate with the surroundings, for example Ethernet exsists in MCU level but its not supported by the board and needs external connection,gpio pins that take input only and all gpio can be used for multiple other application such as boot,strap,etc while some pins are confined only for spi communication and therefore there is alot of difference between MCU and a physical board.

## 2. Board-Level Analysis (DevKit V1 Pinout Diagram)
The physical pin diagram consists only of 30pins for this board, 21 GPIO pins can be used to interface the led and other components when required,4pins for input only, 4 pins which include the ground and power and one enable pin.

## 3. Capability Report (board_capabilities.json)
There are two .json folders the first one contacting all the information about the board I am using in this assigment, the working gpio pins,uart pins, spi interface pins, I2C pins,adc pin and so on, this file also includes the various peripherals that exsit and those that aren't supported by this physical board, this is purely physical board based file and the next .json file consists of the exapmles like led blinking, spi protocol, so on which are mapped to the project references from the  official ESP-IDF path strings so we maintain a clean separation between our custom configuration and the core framework.

## 4. CLI Tool (analyze.py)
In the analyse.py code, first the libraries argparse for reading command-line flags and json for reading the JSON files are imported. Then next we define a fuction which takes the feature (ex: uart) and the loaded json data.Special case for "ethernet" returns a fixed explanation immediately, as mentioned before ethernet on the board needs external connection.The next if checks two things, that is the peripherals say this feature is true and it does an upperkey (like UART) exsist with the actual data pin, if both are true then it returns supported, the third if is when the peripherals say this feature is true but is not in uppercase pin data then its mcu level only and the final return catches anything else as unkown.

## 5. SDK Example Recommendations
In the sdk_example.json file,the board's hardware capabilities are mapped directly to official ESP-IDF (v5.0) example project paths.
LED Blink (examples/get-started/blink): Blink the onboard LED using standard GPIO logic.
UART Communication (examples/peripherals/uart/uart_echo): Communicate with the board via UART by echoing serial data.
ADC Read (examples/peripherals/adc/oneshot_read): Read analog values from ADC pins using the oneshot driver.
I2C Communication (examples/peripherals/i2c/i2c_simple): Communicate with I2C devices using the master bus configuration.
SPI Communication (examples/peripherals/spi_master/hd_eeprom): Communicate with external SPI devices (like an EEPROM).
Timer (examples/peripherals/timer_group/gptimer): Set up a periodic hardware timer interrupt using the modern GPTimer API.

## 6. Validation Report
From the above files,datasheet,json codes we can validate this report
#UART: Classified as "Supported" : The script verified that UART is marked true in the peripherals list and found an explicit UART block containing the board-level TX and RX pin mappings.
#ADC: Classified as "Supported by MCU but not supported by the physical board":The ESP32 chip supports ADC and therefore marked true in the periperals, but because ADC channels share standard GPIO pins rather than having dedicated breakout pins on the DevKit V1, no separate ADC pin block was recorded in the JSON root. The script accurately detects this.
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

