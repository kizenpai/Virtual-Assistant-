"""
GUI Interface Module for EDITH Virtual Assistant.

Implements the Kombai 'Prism' gallery-minimalist aesthetic:
- Pure black canvas (#050505) with soft ivory typography and iridescent glass chromatic artifact.
- Seamless two-stage experience:
    Stage 1: Pinned-corner minimal landing sequence with centered iridescent ring & manifesto.
    Stage 2: Automatic smooth transition to the high-functionality working workspace.
"""

from datetime import datetime
from pathlib import Path
import threading
import time
import tkinter as tk
from typing import Optional

try:
    import customtkinter as ctk
    CTK_AVAILABLE = True
except ImportError:
    CTK_AVAILABLE = False
    import tkinter as ctk

from PIL import Image

import config
from core.assistant import EdithAssistant, NovaAssistant
from utils.logger import get_logger

logger = get_logger("gui")

# Primary typography definitions matching the Prism aesthetic (Consistent Georgia Serif across the entire UI)
FONT_FAMILY = "Georgia"

FONT_SERIF_DISPLAY = (FONT_FAMILY, 40, "bold")
FONT_SERIF_TITLE = (FONT_FAMILY, 16, "bold")
FONT_SERIF_MANIFESTO = (FONT_FAMILY, 13, "italic")
FONT_SERIF_CAPS = (FONT_FAMILY, 10, "bold")
FONT_SERIF_BODY = (FONT_FAMILY, 13)
FONT_SERIF_INPUT = (FONT_FAMILY, 12)
FONT_SERIF_MUTED = (FONT_FAMILY, 9, "italic")


class EdithGUI(ctk.CTk if CTK_AVAILABLE else tk.Tk):
    """
    Main Desktop Window for EDITH with the Kombai 'Prism' exhibition aesthetic.
    """

    def __init__(self):
        super().__init__()

        # Appearance & Window Config
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.title(f"{config.APP_TITLE} v{config.APP_VERSION}")
        self.geometry("1040x760")
        self.minsize(860, 620)
        self.configure(fg_color=config.COLOR_BG_PRIMARY)

        # Initialize Backend Assistant with thread-safe callbacks
        self.assistant = EdithAssistant(
            on_status_change=self._on_status_change_threadsafe,
            on_speech_start=self._on_speech_start_threadsafe,
            on_speech_finish=self._on_speech_finish_threadsafe,
        )

        self._is_listening = False
        self._is_processing = False
        self._current_view = "landing"  # 'landing' or 'workspace'
        self._auto_transition_job = None

        # Load iridescent ring artifacts
        self._load_art_assets()

        # Root Container Frame
        self.container = ctk.CTkFrame(self, fg_color=config.COLOR_BG_PRIMARY, corner_radius=0)
        self.container.pack(fill="both", expand=True)

        # Build Stage 1: Exhibition Landing Screen
        self._build_landing_view()

        # Bindings
        self.bind("<Return>", lambda event: self._on_send_clicked() if self._current_view == "workspace" else None)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        logger.info("EDITH Desktop GUI (Prism Edition) initialized.")

    # -------------------------------------------------------------------------
    # Asset Loading
    # -------------------------------------------------------------------------

    def _load_art_assets(self):
        """Loads or generates the iridescent glass ring images."""
        self.prism_img_large = None
        self.prism_img_small = None
        ring_path = config.ASSETS_DIR / "prism_ring.png"

        try:
            if ring_path.exists():
                pil_large = Image.open(str(ring_path))
                self.prism_img_large = ctk.CTkImage(
                    light_image=pil_large,
                    dark_image=pil_large,
                    size=(280, 280)
                )
                pil_small = pil_large.resize((28, 28), Image.LANCZOS)
                self.prism_img_small = ctk.CTkImage(
                    light_image=pil_small,
                    dark_image=pil_small,
                    size=(24, 24)
                )
                logger.info("Prism ring assets loaded successfully.")
        except Exception as e:
            logger.warning(f"Could not load prism_ring.png: {e}")

    # =========================================================================
    # STAGE 1: PRISM GALLERY LANDING PAGE
    # =========================================================================

    def _build_landing_view(self):
        """
        Constructs the Kombai 'Prism' exhibition landing page:
        - Pure black canvas
        - Metadata pinned to four corners
        - Dead-centered 3D iridescent glass ring
        - Wordmark threaded through center: E D I T H
        - Italic serif manifesto line
        - Automatic entrance countdown bar
        """
        self._current_view = "landing"

        self.landing_frame = ctk.CTkFrame(self.container, fg_color=config.COLOR_BG_PRIMARY, corner_radius=0)
        self.landing_frame.pack(fill="both", expand=True)

        # 1. Pinned Top Corner Metadata
        top_bar = ctk.CTkFrame(self.landing_frame, fg_color="transparent")
        top_bar.pack(fill="x", padx=32, pady=(28, 0))

        # Top-Left: Letterspaced Caps Title
        lbl_top_left = ctk.CTkLabel(
            top_bar,
            text="E D I T H  //  S Y S T E M  0 1",
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, weight="bold"),
            text_color=config.COLOR_TEXT_SECONDARY,
        )
        lbl_top_left.pack(side="left")

        # Top-Right: Academic Lab & Engine
        lbl_top_right = ctk.CTkLabel(
            top_bar,
            text="B.TECH AI LAB  //  AUTONOMOUS COGNITION",
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, weight="bold"),
            text_color=config.COLOR_TEXT_MUTED,
        )
        lbl_top_right.pack(side="right")

        # 2. Dead-Centered 3D Artifact & Wordmark Hub
        center_hub = ctk.CTkFrame(self.landing_frame, fg_color="transparent")
        center_hub.pack(fill="both", expand=True)

        center_content = ctk.CTkFrame(center_hub, fg_color="transparent")
        center_content.place(relx=0.5, rely=0.48, anchor="center")

        # Iridescent Glass Ring Visual
        if self.prism_img_large:
            ring_label = ctk.CTkLabel(center_content, image=self.prism_img_large, text="")
            ring_label.pack(pady=(0, 6))

        # Majestic Serif Wordmark threaded through
        wordmark = ctk.CTkLabel(
            center_content,
            text="E  D  I  T  H",
            font=ctk.CTkFont(family=FONT_FAMILY, size=40, weight="bold"),
            text_color=config.COLOR_TEXT_PRIMARY,
        )
        wordmark.pack(pady=(0, 4))

        # Italic Serif Manifesto line
        manifesto = ctk.CTkLabel(
            center_content,
            text="“Even Dead, I'm The Hero” — Intelligence beyond presence.",
            font=ctk.CTkFont(family=FONT_FAMILY, size=13, slant="italic"),
            text_color=config.COLOR_TEXT_SECONDARY,
        )
        manifesto.pack(pady=(2, 18))

        # Subtle Progress Bar for Automatic Transition
        self.landing_progress = ctk.CTkProgressBar(
            center_content,
            width=220,
            height=2,
            fg_color="#181818",
            progress_color=config.COLOR_ACCENT_CYAN,
        )
        self.landing_progress.set(0.0)
        self.landing_progress.pack(pady=(0, 10))

        # Interactive "Enter System" Button
        enter_btn = ctk.CTkButton(
            center_content,
            text="ENTER WORKSPACE  →",
            width=180,
            height=32,
            font=ctk.CTkFont(family=FONT_FAMILY, size=11, weight="bold"),
            fg_color="#0E0E0E",
            hover_color="#1A1A1A",
            border_width=1,
            border_color="#2A2A2A",
            text_color=config.COLOR_TEXT_PRIMARY,
            corner_radius=4,
            command=self._transition_to_workspace,
        )
        enter_btn.pack()

        # 3. Pinned Bottom Corner Metadata
        bottom_bar = ctk.CTkFrame(self.landing_frame, fg_color="transparent")
        bottom_bar.pack(fill="x", padx=32, pady=(0, 24))

        # Bottom-Left: Edition Index
        lbl_bot_left = ctk.CTkLabel(
            bottom_bar,
            text="EDITION 2026.11  //  CHROMATIC PRISM",
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, slant="italic"),
            text_color=config.COLOR_TEXT_MUTED,
        )
        lbl_bot_left.pack(side="left")

        # Bottom-Right: Ambient Status
        self.lbl_bot_right = ctk.CTkLabel(
            bottom_bar,
            text="SYNCHRONIZING NEURAL CORES... [ 0% ]",
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, weight="bold"),
            text_color=config.COLOR_TEXT_SECONDARY,
        )
        self.lbl_bot_right.pack(side="right")

        # Start automatic progressive entrance transition
        self._start_automatic_entrance()

    def _start_automatic_entrance(self, step: int = 1):
        """Smoothly steps the progress bar and transitions to workspace on main event loop."""
        if self._current_view != "landing":
            return

        val = step / 100.0
        self._update_entrance_progress(val, step)

        if step < 100:
            self._auto_transition_job = self.after(25, lambda: self._start_automatic_entrance(step + 2))
        else:
            self._auto_transition_job = self.after(350, self._transition_to_workspace)

    def _update_entrance_progress(self, val: float, step: int):
        """Updates the progress visual during landing sequence."""
        if self._current_view == "landing" and hasattr(self, "landing_progress"):
            try:
                self.landing_progress.set(val)
                self.lbl_bot_right.configure(text=f"NEURAL CORES ONLINE [ {step}% ]")
            except Exception:
                pass

    # =========================================================================
    # STAGE 2: PRISM MAIN WORKING AREA
    # =========================================================================

    def _transition_to_workspace(self):
        """Smoothly swaps the exhibition landing page for the full interactive workspace."""
        if self._current_view == "workspace":
            return

        if self._auto_transition_job:
            try:
                self.after_cancel(self._auto_transition_job)
            except Exception:
                pass
            self._auto_transition_job = None

        self._current_view = "workspace"

        # Destroy landing view
        if hasattr(self, "landing_frame") and self.landing_frame:
            self.landing_frame.destroy()

        # Build Main Working Area
        self._build_workspace_view()
        logger.info("Transitioned to EDITH main working workspace.")

    def _build_workspace_view(self):
        """
        Builds the gallery-minimalist working workspace:
        - Pure black canvas
        - Hairline 1px architectural dividers (#1E1E1E)
        - Soft ivory typography & metadata
        - Gallery conversation cards
        - Chromatic floating mic and input island
        """
        self.workspace_frame = ctk.CTkFrame(self.container, fg_color=config.COLOR_BG_PRIMARY, corner_radius=0)
        self.workspace_frame.pack(fill="both", expand=True)

        # 1. Top Architectural Header
        self._build_workspace_header()

        # 2. Minimalist Status Indicator & Action Bar
        self._build_workspace_status_bar()

        # 3. Main Exhibition Conversation Feed
        self._build_workspace_chat_area()

        # 4. Floating Minimalist Quick Action Chips
        self._build_workspace_quick_actions()

        # 5. Floating Bottom Interaction Dock
        self._build_workspace_input_dock()

        # Initial Welcome Message
        self._display_welcome_message()

    def _build_workspace_header(self):
        """Constructs the architectural top navigation bar."""
        header_frame = ctk.CTkFrame(
            self.workspace_frame,
            fg_color=config.COLOR_BG_SECONDARY,
            corner_radius=8,
            border_width=1,
            border_color=config.COLOR_BORDER_HAIRLINE,
        )
        header_frame.pack(fill="x", padx=20, pady=(16, 8))

        # Left Branding Hub
        brand_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        brand_frame.pack(side="left", padx=16, pady=10)

        if self.prism_img_small:
            icon_badge = ctk.CTkLabel(brand_frame, image=self.prism_img_small, text="")
            icon_badge.pack(side="left", padx=(0, 10))

        brand_text_box = ctk.CTkFrame(brand_frame, fg_color="transparent")
        brand_text_box.pack(side="left")

        title_label = ctk.CTkLabel(
            brand_text_box,
            text="E D I T H",
            font=ctk.CTkFont(family=FONT_FAMILY, size=16, weight="bold"),
            text_color=config.COLOR_TEXT_PRIMARY,
        )
        title_label.pack(anchor="w")

        subtitle_label = ctk.CTkLabel(
            brand_text_box,
            text="AUTONOMOUS COGNITIVE WORKSPACE  //  EDITION 01",
            font=ctk.CTkFont(family=FONT_FAMILY, size=9, slant="italic"),
            text_color=config.COLOR_TEXT_MUTED,
        )
        subtitle_label.pack(anchor="w")

        # Right Controls Group
        controls_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        controls_frame.pack(side="right", padx=16, pady=10)

        # AI Status Badge
        self.ai_badge = ctk.CTkLabel(
            controls_frame,
            text=self._get_ai_status_text(),
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, weight="bold"),
            fg_color="#121212",
            text_color=config.STATUS_ONLINE if self.assistant.ai_engine.is_configured() else "#F59E0B",
            corner_radius=4,
            padx=10,
            pady=3,
        )
        self.ai_badge.pack(side="left", padx=(0, 12))

        # Voice Output Switch
        self.speech_switch = ctk.CTkSwitch(
            controls_frame,
            text="VOICE",
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, weight="bold"),
            text_color=config.COLOR_TEXT_SECONDARY,
            progress_color=config.COLOR_ACCENT_CYAN,
            command=self._on_speech_toggle,
        )
        self.speech_switch.select() if config.TTS_ENABLED_DEFAULT else self.speech_switch.deselect()
        self.speech_switch.pack(side="left", padx=(0, 10))

        # Re-enter Landing Page Button
        view_landing_btn = ctk.CTkButton(
            controls_frame,
            text="ARTIFACT ↺",
            width=80,
            height=24,
            font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
            fg_color="#121212",
            hover_color="#1E1E1E",
            text_color=config.COLOR_TEXT_MUTED,
            border_width=1,
            border_color="#222222",
            corner_radius=4,
            command=self._return_to_landing,
        )
        view_landing_btn.pack(side="left")

    def _build_workspace_status_bar(self):
        """Displays real-time assistant state."""
        status_frame = ctk.CTkFrame(self.workspace_frame, fg_color="transparent")
        status_frame.pack(fill="x", padx=24, pady=(0, 4))

        # Minimalist LED indicator
        self.status_dot = ctk.CTkLabel(
            status_frame,
            text="●",
            font=ctk.CTkFont(size=12),
            text_color=config.STATUS_ONLINE,
        )
        self.status_dot.pack(side="left", padx=(0, 6))

        # Status text
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="SYSTEM READY  //  LISTENER STANDBY",
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, weight="bold"),
            text_color=config.COLOR_TEXT_MUTED,
        )
        self.status_label.pack(side="left")

        # Clear Chat Button
        clear_btn = ctk.CTkButton(
            status_frame,
            text="CLEAR ARCHIVE",
            width=86,
            height=20,
            font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
            fg_color="transparent",
            hover_color="#161616",
            text_color=config.COLOR_TEXT_MUTED,
            corner_radius=3,
            command=self._clear_chat_history,
        )
        clear_btn.pack(side="right")

    def _build_workspace_chat_area(self):
        """Scrollable conversation container holding exhibition-grade message cards."""
        chat_container = ctk.CTkFrame(
            self.workspace_frame,
            fg_color=config.COLOR_BG_PRIMARY,
            corner_radius=8,
            border_width=1,
            border_color=config.COLOR_BORDER_HAIRLINE,
        )
        chat_container.pack(fill="both", expand=True, padx=20, pady=4)

        self.chat_scroll = ctk.CTkScrollableFrame(
            chat_container,
            fg_color="transparent",
        )
        self.chat_scroll.pack(fill="both", expand=True, padx=14, pady=14)

    def _build_workspace_quick_actions(self):
        """Letterspaced minimalist quick action pills."""
        quick_frame = ctk.CTkFrame(self.workspace_frame, fg_color="transparent")
        quick_frame.pack(fill="x", padx=22, pady=(4, 6))

        actions = [
            ("COMMANDS", "help"),
            ("TIME", "what time is it"),
            ("DATE", "what is today's date"),
            ("NOTES", "read notes"),
            ("JOKE", "tell me a joke"),
            ("CALCULATOR", "open calculator"),
            ("NOTEPAD", "open notepad"),
            ("YOUTUBE", "open youtube"),
        ]

        lbl = ctk.CTkLabel(
            quick_frame,
            text="PROMPTS:",
            font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
            text_color=config.COLOR_TEXT_MUTED,
        )
        lbl.pack(side="left", padx=(2, 6))

        for label_text, cmd_text in actions:
            btn = ctk.CTkButton(
                quick_frame,
                text=label_text,
                height=22,
                font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
                fg_color="#0F0F0F",
                hover_color="#1C1C1C",
                text_color=config.COLOR_TEXT_SECONDARY,
                border_width=1,
                border_color="#1E1E1E",
                corner_radius=3,
                command=lambda cmd=cmd_text: self._submit_text_input(cmd),
            )
            btn.pack(side="left", padx=2)

    def _build_workspace_input_dock(self):
        """Minimalist floating dock with microphone, text field, and transmit trigger."""
        dock_frame = ctk.CTkFrame(
            self.workspace_frame,
            fg_color=config.COLOR_BG_SECONDARY,
            corner_radius=10,
            border_width=1,
            border_color=config.COLOR_BORDER_HAIRLINE,
        )
        dock_frame.pack(fill="x", padx=20, pady=(4, 16))

        # Circular Microphone Trigger with Iridescent Ring Style
        self.mic_btn = ctk.CTkButton(
            dock_frame,
            text="🎤",
            width=46,
            height=46,
            corner_radius=23,
            font=ctk.CTkFont(family=FONT_FAMILY, size=16),
            fg_color="#161616",
            hover_color="#222222",
            border_width=1,
            border_color=config.COLOR_ACCENT_CYAN,
            command=self._on_mic_clicked,
        )
        self.mic_btn.pack(side="left", padx=(10, 8), pady=8)

        # Soft Ivory Text Entry Field in Georgia Serif
        self.entry_field = ctk.CTkEntry(
            dock_frame,
            placeholder_text="Speak or transcribe an inquiry... (e.g. 'what is quantum computing', 'calculate 25*16')",
            placeholder_text_color=config.COLOR_TEXT_MUTED,
            font=ctk.CTkFont(family=FONT_FAMILY, size=12),
            fg_color=config.COLOR_BG_INPUT,
            border_color="#1E1E1E",
            text_color=config.COLOR_TEXT_PRIMARY,
            corner_radius=6,
            height=44,
        )
        self.entry_field.pack(side="left", fill="x", expand=True, padx=(0, 8), pady=8)
        self.entry_field.focus_set()

        # Minimalist Transmit Button
        self.send_btn = ctk.CTkButton(
            dock_frame,
            text="TRANSMIT ➤",
            width=96,
            height=44,
            corner_radius=6,
            font=ctk.CTkFont(family=FONT_FAMILY, size=10, weight="bold"),
            fg_color="#161616",
            hover_color="#222222",
            border_width=1,
            border_color="#282828",
            text_color=config.COLOR_TEXT_PRIMARY,
            command=self._on_send_clicked,
        )
        self.send_btn.pack(side="right", padx=(0, 10), pady=8)

    # -------------------------------------------------------------------------
    # Helper & Display Logic
    # -------------------------------------------------------------------------

    def _get_ai_status_text(self) -> str:
        """Returns concise Gemini status label."""
        if self.assistant.ai_engine.is_configured():
            model = self.assistant.ai_engine.model_name
            return f"GEMINI // {model.upper()}"
        return "OFFLINE (ADD KEY IN .ENV)"

    def _display_welcome_message(self):
        """Displays introduction from EDITH."""
        welcome_text = (
            "Hello. I am EDITH (Even Dead, I'm The Hero), your AI-powered Virtual Assistant.\n\n"
            "• Press the 🎤 Microphone button to speak, or type any request below.\n"
            "• Ask about date, time, weather concepts, or open desktop applications.\n"
            "• Compute safe mathematical expressions (e.g. 'calculate 25 * 14').\n"
            "• Record, list, and clear personal notes.\n"
            "• Powered by Google Gemini for conversational reasoning.\n"
            "Type 'help' to review all system commands."
        )
        self._add_message_bubble("EDITH", welcome_text, is_user=False)

    def _add_message_bubble(self, sender: str, text: str, is_user: bool = False):
        """Renders an exhibition-grade message card in the conversation feed."""
        timestamp = datetime.now().strftime("%I:%M %p")

        row = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        row.pack(fill="x", pady=5)

        bubble_color = config.BUBBLE_USER if is_user else config.BUBBLE_EDITH
        anchor_side = "right" if is_user else "left"
        sender_color = "#E0E0DC" if is_user else config.COLOR_ACCENT_CYAN
        border_color = "#242424" if is_user else "#202020"

        bubble = ctk.CTkFrame(
            row,
            fg_color=bubble_color,
            corner_radius=6,
            border_width=1,
            border_color=border_color,
        )
        bubble.pack(side=anchor_side, padx=6, fill="none")

        # Header: Sender tag and timestamp
        header = ctk.CTkFrame(bubble, fg_color="transparent")
        header.pack(fill="x", padx=12, pady=(6, 2))

        sender_label = ctk.CTkLabel(
            header,
            text=f"{'👤 YOU' if is_user else '◆ EDITH'}",
            font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
            text_color=sender_color,
        )
        sender_label.pack(side="left")

        time_label = ctk.CTkLabel(
            header,
            text=timestamp,
            font=ctk.CTkFont(family=FONT_FAMILY, size=9, slant="italic"),
            text_color=config.COLOR_TEXT_MUTED,
        )
        time_label.pack(side="right", padx=(14, 0))

        # Message Text in Georgia Serif (Soft Ivory)
        msg_label = ctk.CTkLabel(
            bubble,
            text=text,
            font=ctk.CTkFont(family=FONT_FAMILY, size=13),
            text_color=config.COLOR_TEXT_PRIMARY,
            justify="left",
            wraplength=640,
        )
        msg_label.pack(padx=12, pady=(2, 8), anchor="w")

        # Auto-scroll
        self.after(50, lambda: self.chat_scroll._parent_canvas.yview_moveto(1.0))

    def _clear_chat_history(self):
        """Clears all message cards."""
        for widget in self.chat_scroll.winfo_children():
            widget.destroy()
        self._display_welcome_message()

    def _return_to_landing(self):
        """Swaps back to the exhibition landing artifact."""
        if hasattr(self, "workspace_frame") and self.workspace_frame:
            self.workspace_frame.destroy()
        self._build_landing_view()

    # -------------------------------------------------------------------------
    # Event Handlers & Background Workers
    # -------------------------------------------------------------------------

    def _on_speech_toggle(self):
        """Toggles TTS enabled state."""
        enabled = self.speech_switch.get() == 1
        self.assistant.set_speech_enabled(enabled)

    def _on_send_clicked(self):
        """Handles submission from text entry box."""
        user_text = self.entry_field.get().strip()
        if not user_text:
            return

        self.entry_field.delete(0, tk.END)
        self._submit_text_input(user_text)

    def _submit_text_input(self, text: str):
        """Submits inquiry asynchronously."""
        if self._is_processing or self._is_listening:
            return

        self._is_processing = True
        self._add_message_bubble("You", text, is_user=True)

        def worker():
            try:
                result = self.assistant.process_input(text)
                self.after(0, lambda: self._handle_assistant_result(result))
            except Exception as e:
                logger.error(f"Error during input processing: {e}")
                self.after(0, lambda: self._add_message_bubble("EDITH", f"System error: {e}", is_user=False))
            finally:
                self._is_processing = False

        threading.Thread(target=worker, daemon=True, name="EDITH_InputWorker").start()

    def _on_mic_clicked(self):
        """Activates microphone listening asynchronously."""
        if self._is_listening or self._is_processing:
            return

        self._is_listening = True
        self.mic_btn.configure(border_color=config.STATUS_LISTENING, text="●")
        self.status_dot.configure(text_color=config.STATUS_LISTENING)
        self.status_label.configure(text="LISTENING FOR SPEECH... (SPEAK NOW)")

        def worker():
            try:
                result = self.assistant.listen_and_process()
                self.after(0, lambda: self._handle_voice_result(result))
            except Exception as e:
                logger.error(f"Error during voice listening: {e}")
                self.after(0, lambda: self._add_message_bubble("EDITH", f"Voice error: {e}", is_user=False))
            finally:
                self._is_listening = False
                self.after(0, self._reset_mic_button)

        threading.Thread(target=worker, daemon=True, name="EDITH_VoiceWorker").start()

    def _reset_mic_button(self):
        """Restores mic button styling after listening finishes."""
        self.mic_btn.configure(border_color=config.COLOR_ACCENT_CYAN, text="🎤")
        if not self.assistant.tts.is_speaking:
            self.status_dot.configure(text_color=config.STATUS_ONLINE)
            self.status_label.configure(text="SYSTEM READY  //  LISTENER STANDBY")

    def _handle_voice_result(self, result: dict):
        """Processes voice recognition result."""
        user_text = result.get("user_text")
        if user_text:
            self._add_message_bubble("You", user_text, is_user=True)
        self._handle_assistant_result(result)

    def _handle_assistant_result(self, result: dict):
        """Renders assistant response."""
        response = result.get("response", "")
        if response:
            self._add_message_bubble("EDITH", response, is_user=False)

        # Refresh AI pill
        self.ai_badge.configure(
            text=self._get_ai_status_text(),
            text_color=config.STATUS_ONLINE if self.assistant.ai_engine.is_configured() else "#F59E0B"
        )

        if result.get("should_exit"):
            self.after(2000, self.destroy)

    # -------------------------------------------------------------------------
    # Thread-Safe Status Callbacks
    # -------------------------------------------------------------------------

    def _on_status_change_threadsafe(self, status: str, color_hex: str):
        self.after(0, lambda: self._update_status_ui(status, color_hex))

    def _update_status_ui(self, status: str, color_hex: str):
        if hasattr(self, "status_dot") and hasattr(self, "status_label"):
            self.status_dot.configure(text_color=color_hex)
            self.status_label.configure(text=f"EDITH STATUS: {status.upper()}")

    def _on_speech_start_threadsafe(self):
        self.after(0, lambda: self._update_status_ui("Speaking", config.STATUS_SPEAKING))

    def _on_speech_finish_threadsafe(self):
        self.after(0, lambda: self._update_status_ui("Online", config.STATUS_ONLINE))

    def _on_close(self):
        """Cleans up on window close."""
        logger.info("Application close requested.")
        try:
            self.assistant.shutdown()
        except Exception:
            pass
        self.destroy()

# Backward-compatibility alias
NovaGUI = EdithGUI
