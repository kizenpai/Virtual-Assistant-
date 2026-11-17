"""
Command Handler Module for EDITH.

Parses, normalizes, and executes built-in virtual assistant commands.
Implements safe computer automation and routes unmatched queries to the AI engine.
"""

from datetime import datetime
import os
import random
import re
import subprocess
import urllib.parse
import webbrowser
from typing import Any, Dict, Optional

from utils.calculator import calculate
from utils.notes_manager import save_note, get_notes_formatted, clear_notes
from utils.logger import get_logger

logger = get_logger("command_handler")

# Curated repository of programming, science, and AI jokes
JOKES_LIST = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "There are only 10 types of people in the world: those who understand binary, and those who don't.",
    "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why do Java programmers wear glasses? Because they can't C#!",
    "What is an algorithm? A word used by programmers when they don't want to explain what they did.",
    "An optimist says the glass is half full. A pessimist says the glass is half empty. A programmer says the glass is twice as large as necessary.",
    "Why did the neural network break up with the dataset? Too many overfitting issues!",
    "How many programmers does it take to change a light bulb? None, it's a hardware problem."
]

HELP_TEXT = (
    "Here are the commands I can help you with:\n\n"
    "• Greetings: 'Hello', 'Hi EDITH', 'Good morning'\n"
    "• Date & Time: 'What time is it?', 'What is today's date?'\n"
    "• Web Navigation: 'Open YouTube', 'Open Google', 'Open GitHub', 'Open Gmail'\n"
    "• Custom Website: 'Open website stackoverflow.com'\n"
    "• Web Search: 'Search Google for quantum computing'\n"
    "• Wikipedia: 'Wikipedia Alan Turing' or 'Who is Marie Curie?'\n"
    "• Math Calculator: 'Calculate 25 * 4', 'What is 100 divided by 5'\n"
    "• Applications: 'Open Notepad', 'Open Calculator', 'Open Browser'\n"
    "• Notes: 'Save note remember to submit project', 'Read notes', 'Clear notes'\n"
    "• Entertainment: 'Tell me a joke'\n"
    "• AI Mode: Ask any general question, programming query, or science topic!\n"
    "• Exit: 'Exit', 'Quit', or 'Goodbye'"
)

class CommandHandler:
    """
    Evaluates and processes user natural language commands.
    """

    def __init__(self):
        self.approved_apps = {
            "notepad": ["notepad.exe"],
            "calculator": ["calc.exe"],
            "calc": ["calc.exe"],
        }

    def normalize(self, text: str) -> str:
        """Normalizes string for case-insensitive matching."""
        if not text:
            return ""
        # Lowercase, strip punctuation except math symbols
        text = text.strip().lower()
        text = re.sub(r"^[!?,.\s]+|[!?,.\s]+$", "", text)
        return text

    def handle(self, raw_input: str) -> Dict[str, Any]:
        """
        Main entry point for command routing.
        Returns a dict describing whether a command matched, response string,
        action flags, and whether speech should be triggered.
        """
        text = self.normalize(raw_input)
        if not text:
            return {
                "matched": True,
                "response": "I didn't hear anything. How can I help you?",
                "action": None,
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # 1. Exit Commands
        if self._matches_exit(text):
            return {
                "matched": True,
                "response": "Goodbye! Have a great day ahead.",
                "action": "EXIT",
                "speak": True,
                "should_exit": True,
                "is_ai_candidate": False,
            }

        # 2. Help Commands
        if self._matches_help(text):
            return {
                "matched": True,
                "response": HELP_TEXT,
                "action": "SHOW_HELP",
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # 3. Greetings
        greeting_resp = self._handle_greetings(text)
        if greeting_resp:
            return {
                "matched": True,
                "response": greeting_resp,
                "action": None,
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # 4. Date and Time
        datetime_resp = self._handle_datetime(text)
        if datetime_resp:
            return {
                "matched": True,
                "response": datetime_resp,
                "action": None,
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # 5. Tell a Joke
        if re.search(r"\b(tell\s+(me\s+)?(a\s+)?joke|make\s+me\s+laugh|crack\s+a\s+joke)\b", text):
            joke = random.choice(JOKES_LIST)
            return {
                "matched": True,
                "response": joke,
                "action": None,
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # 6. Notes Management
        note_result = self._handle_notes(text, raw_input)
        if note_result:
            return note_result

        # 7. Safe Computer Automation (Launch approved desktop apps)
        app_result = self._handle_apps(text)
        if app_result:
            return app_result

        # 8. Web Browsing & Specific Websites
        web_result = self._handle_websites(text)
        if web_result:
            return web_result

        # 9. Google Search
        search_result = self._handle_google_search(text)
        if search_result:
            return search_result

        # 10. Wikipedia Retrieval
        wiki_result = self._handle_wikipedia(text)
        if wiki_result:
            return wiki_result

        # 11. Mathematical Calculations
        math_result = self._handle_calculator(text)
        if math_result:
            return math_result

        # 12. Unmatched -> Smartly flag for Gemini AI engine
        return {
            "matched": False,
            "response": "",
            "action": None,
            "speak": True,
            "should_exit": False,
            "is_ai_candidate": True,
        }

    # -------------------------------------------------------------------------
    # Helper Handlers
    # -------------------------------------------------------------------------

    def _matches_exit(self, text: str) -> bool:
        return bool(re.search(r"^(exit|quit|close(\s+(edith|nova))?|shutdown(\s+(edith|nova))?|bye|goodbye)$", text))

    def _matches_help(self, text: str) -> bool:
        return bool(re.search(r"^(help|what\s+can\s+you\s+do|commands|show\s+commands|available\s+commands)$", text))

    def _handle_greetings(self, text: str) -> Optional[str]:
        if re.search(r"\b(hello|hi|hey|greetings|howdy)\b", text):
            current_hour = datetime.now().hour
            time_greeting = "Good morning" if current_hour < 12 else ("Good afternoon" if current_hour < 18 else "Good evening")
            return f"{time_greeting}! I am EDITH, your virtual assistant. How can I assist you today?"

        if re.search(r"\b(good\s+morning)\b", text):
            return "Good morning! I hope you have a productive day ahead. How can I help?"

        if re.search(r"\b(good\s+afternoon)\b", text):
            return "Good afternoon! What can I do for you right now?"

        if re.search(r"\b(good\s+evening)\b", text):
            return "Good evening! Ready to assist you. What do you need?"

        if re.search(r"\b(how\s+are\s+you|how's\s+it\s+going|how\s+do\s+you\s+do)\b", text):
            return "I am functioning at peak performance and ready to assist you! How are you doing?"

        if re.search(r"\b(who\s+are\s+you|what\s+is\s+your\s+name|what\s+are\s+you)\b", text):
            return "I am EDITH (Even Dead, I'm The Hero), an AI-powered desktop virtual assistant built with Python and Google Gemini."

        if re.search(r"\b(who\s+(created|made|built|developed)\s+you)\b", text):
            return "I was created as an AI Virtual Assistant project for the B.Tech Artificial Intelligence Laboratory."

        if re.search(r"\b(can\s+you\s+hear\s+me|are\s+you\s+listening|test\s+mic|mic\s+test)\b", text):
            return "Yes, I can hear you loud and clear! What would you like me to do?"

        if re.search(r"\b(what\s+is\s+your\s+purpose|why\s+were\s+you\s+created)\b", text):
            return "My purpose is to be your desktop companion: executing computer automation, calculations, managing notes, and answering your questions."

        if re.search(r"\b(thank\s+you|thanks|thank\s+you\s+so\s+much)\b", text):
            return "You're very welcome! Happy to help. Let me know if you need anything else."

        if re.search(r"\b(great|awesome|cool|well\s+done|good\s+job)\b", text):
            return "Thank you! I strive to be as helpful as possible."

        return None

    def _handle_datetime(self, text: str) -> Optional[str]:
        now = datetime.now()

        # Time query
        if re.search(r"\b(time|what('s|\s+is)\s+the\s+time|current\s+time|tell\s+me\s+the\s+time)\b", text):
            time_str = now.strftime("%I:%M %p")
            return f"The current time is {time_str}."

        # Date query
        if re.search(r"\b(date|what('s|\s+is)\s+the\s+date|today's\s+date|current\s+date)\b", text):
            date_str = now.strftime("%A, %B %d, %Y")
            return f"Today is {date_str}."

        # Day query
        if re.search(r"\b(what\s+day\s+is\s+it|which\s+day\s+is\s+today)\b", text):
            day_str = now.strftime("%A")
            return f"Today is {day_str}."

        return None

    def _handle_notes(self, text: str, raw_input: str) -> Optional[Dict[str, Any]]:
        # Clear notes
        if re.search(r"\b(clear\s+notes|delete\s+all\s+notes|remove\s+notes)\b", text):
            success, msg = clear_notes()
            return {
                "matched": True,
                "response": msg,
                "action": "CLEAR_NOTES",
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # Read notes
        if re.search(r"\b(read\s+notes|show\s+notes|my\s+notes|get\s+notes|view\s+notes|list\s+notes)\b", text):
            notes_text = get_notes_formatted()
            return {
                "matched": True,
                "response": notes_text,
                "action": "READ_NOTES",
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # Save note (handles variations: "save note ...", "take a note ...", "note ...", "noate ...")
        save_match = re.search(r"\b(save\s+a?\s*note|take\s+a?\s*note|write\s+a?\s*note|add\s+a?\s*note|make\s+a?\s*note|create\s+a?\s*note|note\s+that|note|noate)\b\s*(.*)", text)
        if save_match:
            note_content = save_match.group(2).strip()
            if not note_content:
                return {
                    "matched": True,
                    "response": "What note would you like me to save? Please say 'save note' followed by your message.",
                    "action": None,
                    "speak": True,
                    "should_exit": False,
                    "is_ai_candidate": False,
                }
            success, msg = save_note(note_content)
            return {
                "matched": True,
                "response": msg,
                "action": "SAVE_NOTE",
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        return None

    def _handle_apps(self, text: str) -> Optional[Dict[str, Any]]:
        # Launch Notepad
        if re.search(r"\b(open\s+notepad|launch\s+notepad|start\s+notepad)\b", text):
            try:
                subprocess.Popen(["notepad.exe"])
                return {
                    "matched": True,
                    "response": "Opening Notepad for you.",
                    "action": "OPEN_NOTEPAD",
                    "speak": True,
                    "should_exit": False,
                    "is_ai_candidate": False,
                }
            except Exception as e:
                logger.error(f"Failed to launch Notepad: {e}")
                return {
                    "matched": True,
                    "response": f"Sorry, could not open Notepad: {e}",
                    "action": None,
                    "speak": True,
                    "should_exit": False,
                    "is_ai_candidate": False,
                }

        # Launch Calculator
        if re.search(r"\b(open\s+calculator|launch\s+calculator|start\s+calculator)\b", text):
            try:
                subprocess.Popen(["calc.exe"])
                return {
                    "matched": True,
                    "response": "Opening Calculator.",
                    "action": "OPEN_CALC",
                    "speak": True,
                    "should_exit": False,
                    "is_ai_candidate": False,
                }
            except Exception as e:
                logger.error(f"Failed to launch Calculator: {e}")
                return {
                    "matched": True,
                    "response": f"Sorry, could not open Calculator: {e}",
                    "action": None,
                    "speak": True,
                    "should_exit": False,
                    "is_ai_candidate": False,
                }

        # Launch Browser / Chrome
        if re.search(r"\b(open\s+(browser|chrome|edge))\b", text):
            try:
                webbrowser.open("https://www.google.com")
                return {
                    "matched": True,
                    "response": "Opening your web browser.",
                    "action": "OPEN_BROWSER",
                    "speak": True,
                    "should_exit": False,
                    "is_ai_candidate": False,
                }
            except Exception as e:
                return {
                    "matched": True,
                    "response": f"Could not launch browser: {e}",
                    "action": None,
                    "speak": True,
                    "should_exit": False,
                    "is_ai_candidate": False,
                }

        return None

    def _handle_websites(self, text: str) -> Optional[Dict[str, Any]]:
        # Open YouTube
        if re.search(r"\b(open\s+youtube)\b", text):
            webbrowser.open("https://www.youtube.com")
            return {
                "matched": True,
                "response": "Opening YouTube.",
                "action": "OPEN_YOUTUBE",
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # Open Google
        if re.search(r"^(open\s+google)$", text):
            webbrowser.open("https://www.google.com")
            return {
                "matched": True,
                "response": "Opening Google.",
                "action": "OPEN_GOOGLE",
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # Open GitHub
        if re.search(r"\b(open\s+github)\b", text):
            webbrowser.open("https://github.com")
            return {
                "matched": True,
                "response": "Opening GitHub.",
                "action": "OPEN_GITHUB",
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # Open Gmail
        if re.search(r"\b(open\s+(gmail|mail))\b", text):
            webbrowser.open("https://mail.google.com")
            return {
                "matched": True,
                "response": "Opening Gmail.",
                "action": "OPEN_GMAIL",
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        # Open specific website: 'open website example.com' or 'open example.com'
        website_match = re.search(r"\bopen\s+(?:website\s+)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?)\b", text)
        if website_match:
            site = website_match.group(1).strip()
            url = site if site.startswith("http") else f"https://{site}"
            webbrowser.open(url)
            return {
                "matched": True,
                "response": f"Opening {site}.",
                "action": "OPEN_WEBSITE",
                "speak": True,
                "should_exit": False,
                "is_ai_candidate": False,
            }

        return None

    def _handle_google_search(self, text: str) -> Optional[Dict[str, Any]]:
        patterns = [
            r"^(?:search\s+google\s+for|search\s+for|google\s+search\s+for|google)\s+(.+)",
            r"^search\s+(.+)\s+on\s+google$",
        ]
        for pat in patterns:
            match = re.search(pat, text)
            if match:
                query = match.group(1).strip()
                if query and not query.startswith("wikipedia"):
                    encoded_query = urllib.parse.quote_plus(query)
                    url = f"https://www.google.com/search?q={encoded_query}"
                    webbrowser.open(url)
                    return {
                        "matched": True,
                        "response": f"Searching Google for '{query}'.",
                        "action": "GOOGLE_SEARCH",
                        "speak": True,
                        "should_exit": False,
                        "is_ai_candidate": False,
                    }
        return None

    def _handle_wikipedia(self, text: str) -> Optional[Dict[str, Any]]:
        patterns = [
            r"^(?:search\s+)?wikipedia(?:\s+for)?\s+(.+)",
            r"^tell\s+me\s+about\s+(.+)\s+from\s+wikipedia$",
        ]
        for pat in patterns:
            match = re.search(pat, text)
            if match:
                query = match.group(1).strip()
                try:
                    import wikipedia
                    logger.info(f"Querying Wikipedia for '{query}'...")
                    summary = wikipedia.summary(query, sentences=2)
                    return {
                        "matched": True,
                        "response": f"According to Wikipedia: {summary}",
                        "action": "WIKIPEDIA_SUMMARY",
                        "speak": True,
                        "should_exit": False,
                        "is_ai_candidate": False,
                    }
                except ImportError:
                    return {
                        "matched": True,
                        "response": "Wikipedia module is not installed.",
                        "action": None,
                        "speak": True,
                        "should_exit": False,
                        "is_ai_candidate": False,
                    }
                except Exception as e:
                    logger.warning(f"Wikipedia lookup failed for '{query}': {e}")
                    return {
                        "matched": True,
                        "response": f"I couldn't find a Wikipedia article for '{query}'.",
                        "action": None,
                        "speak": True,
                        "should_exit": False,
                        "is_ai_candidate": False,
                    }
        return None

    def _handle_calculator(self, text: str) -> Optional[Dict[str, Any]]:
        # Matches explicit calculate keywords or direct arithmetic expressions
        has_calc_intent = bool(re.search(r"\b(calculate|compute|solve|evaluate|math|how\s+much\s+is|square\s+root)\b", text))
        has_math_pattern = bool(re.search(r"(?:[0-9]+|\bpi\b|\be\b)\s*(?:\+|\-|\*|\/|\*\*|\^|%|plus|minus|times|multiplied|divided|into|power)\s*[0-9]+", text))
        has_what_is_number = bool(re.search(r"what\s+is\s+(?:sqrt\([0-9.]+\)|[0-9]+)", text))

        if (has_calc_intent or has_math_pattern or has_what_is_number) and re.search(r"[0-9]", text):
            result = calculate(text)
            if not result.startswith("Could not parse"):
                return {
                    "matched": True,
                    "response": result,
                    "action": "CALCULATION",
                    "speak": True,
                    "should_exit": False,
                    "is_ai_candidate": False,
                }
        return None
