"""
Main Entry Point for EDITH – AI-Powered Virtual Assistant.

Launches the CustomTkinter graphical dashboard or terminal CLI interface.
"""

import argparse
import sys
import config
from utils.logger import setup_logger

logger = setup_logger("main")

def run_cli_mode():
    """Fallback interactive command-line interface for headless or quick testing."""
    print("=" * 65)
    print(f"  {config.APP_TITLE} (CLI Mode) v{config.APP_VERSION}")
    print("  Type 'help' for commands, or 'exit' to quit.")
    print("=" * 65)

    from core.assistant import EdithAssistant
    assistant = EdithAssistant()

    if assistant.ai_engine.is_configured():
        print(f"[AI Mode]: Active (Model: {assistant.ai_engine.model_name})")
    else:
        print("[AI Mode]: Offline (Add GEMINI_API_KEY to .env to enable AI mode)")

    print()

    while True:
        try:
            user_input = input("You > ").strip()
            if not user_input:
                continue

            result = assistant.process_input(user_input)
            print(f"EDITH > {result['response']}\n")

            if result.get("should_exit"):
                break

        except (KeyboardInterrupt, EOFError):
            print("\nExiting EDITH. Goodbye!")
            assistant.shutdown()
            break
        except Exception as e:
            print(f"[Error]: {e}\n")

def run_gui_mode():
    """Launches the primary CustomTkinter desktop graphical user interface."""
    logger.info("Starting EDITH GUI Application...")
    from gui.interface import EdithGUI

    app = EdithGUI()
    app.mainloop()

def main():
    """Parses command-line arguments and starts EDITH."""
    parser = argparse.ArgumentParser(description=config.APP_TITLE)
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run EDITH in terminal/CLI mode without opening the GUI."
    )
    args = parser.parse_args()

    if args.cli:
        run_cli_mode()
    else:
        run_gui_mode()

if __name__ == "__main__":
    main()

