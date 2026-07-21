import argparse
import json


def classify(feature, board_data):
    if feature == "ethernet":
        return "Supported by MCU but not available on board (needs external PHY)"
    if board_data["peripherals"].get(feature) and feature.upper() in board_data:
        return "Supported"
    if board_data["peripherals"].get(feature):
        return "Supported by MCU (board-level pin data not recorded)"
    return "Not enough verified information"


def main():
    parser = argparse.ArgumentParser(description="MCU Capability Analyzer")
    parser.add_argument("--board", required=True, help="Board name")
    parser.add_argument("--sdk", required=True, help="Path to SDK repo")
    args = parser.parse_args()

    try:
        with open("mcu.json") as f:
            board_data = json.load(f)
        with open("sdk_example.json") as f:
            sdk_examples = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: Could not find configuration file - {e.filename}")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON syntax - {e}")
        return

    print(f"\n=== MCU Capability Report: {args.board} ===")
    print(json.dumps(board_data, indent=2))

    print(f"\n=== SDK Example Recommendations (SDK: {args.sdk}) ===")
    for req, info in sdk_examples.items():
        if req == "sdk":
            continue
        print(f"- {req}: {info['path']}\n  reason: {info['reason']}")

    print(f"\n=== Validation Report ===")
    for feature in ["uart", "adc", "ethernet"]:
        result = classify(feature, board_data)
        print(f"- {feature}: {result}")


if __name__ == "__main__":
    main()
