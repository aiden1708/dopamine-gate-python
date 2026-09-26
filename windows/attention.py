#!/usr/bin/env python3

from PySide6.QtCore import Qt

from .base import BaseWindow


class AttentionWindow(BaseWindow):

    def __init__(self, on_continue, on_exit):

        super().__init__(
            "Don't be impatient.",
            "Read carefully. This is not something to click through.",
        )

        self.add_body(
            "Is your attention here?"
        )

        self.add_body(
            "Good. Then take a moment before you continue."
        )

        self.add_body(
            "Take a deep breath."
        )

        self.add_transition_button(
            "Yes, I'm here",
            on_continue,
        )

        self.add_button(
            "No — exit",
            on_exit,
            "dangerButton",
        )