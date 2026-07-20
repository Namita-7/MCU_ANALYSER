# MCU Capability Analyzer — ESP32-WROOM-32 (DevKit V1)

## 1. MCU-Level Analysis (ESP32-WROOM-32 Datasheet)
[Your understanding of chip-level specs: CPU core, flash, RAM, peripheral list.
Mention key facts you flagged — e.g. Ethernet needs external PHY, GPIO6-11 reserved
for flash. Link to SOURCES.md or cite section numbers inline.]

## 2. Board-Level Analysis (DevKit V1 Pinout Diagram)
[What you learned from the physical pinout: onboard LED pin, debug UART pins,
any board-specific constraints not visible in the module datasheet alone.
This is where you explain MCU-vs-board distinction in your own words.]

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
