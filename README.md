# MCU Capability Analyzer — ESP32-WROOM-32 (DevKit V1)

## 1. MCU-Level Analysis (ESP32-WROOM-32 Datasheet)
Based on the datasheet that I read through, I understood that there is more than just a physical board with gpio pins that communicate with the surroundings, for example Ethernet exsists in MCU level but its not supported by the board and needs external connection,gpio pins that take input only and all gpio can be used for multiple other application such as boot,strap,etc while some pins are confined only for spi communication and therefore there is alot of difference between MCU and a physical board.

## 2. Board-Level Analysis (DevKit V1 Pinout Diagram)
The physical pin diagram consists only of 30pins for this board, 14 GPIO pins can be used to interface the led and other components when required,4pins for input only, 5 pins which include the ground and power,6 pins used with flash memory and cannot be used as regular GPIO pins and one enable pin.

## 3. Capability Report (board_capabilities.json)
[What the JSON contains, how it's structured, and how each field traces back
to section 1 or 2 above. Maybe a short note: "run `analyze.py` to regenerate this."]

## 4. CLI Tool (analyze.py)
[How to run it: `python analyze.py --board esp32-devkitv1 --sdk <path>`
What it outputs, how it pulls from your verified data rather than inventing anything.]

## 5. SDK Example Recommendations
[How examples were matched — point to the actual ESP-IDF example paths you verified,
with your one-line reasoning for each.]

## 6. Validation Report
[Link or embed your answer to the UART/ADC/Ethernet question, with classifications.]

## Setup & Run Instructions
[Standard: clone, install deps if any, run command.]
