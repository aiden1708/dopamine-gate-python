#!/usr/bin/env python3

from .base import BaseWindow


class SelfControlWindow(BaseWindow):

    def __init__(self, on_continue, on_exit):

        super().__init__(
            "Can you handle it alone?",
            "Be honest with yourself.",
        )

        self.add_body(
            "Are you sure you can handle this application alone?"
        )

        self.add_body(
            "If you already know that you are likely to lose control, "
            "there is nothing shameful about stopping here."
        )

        self.add_body(
            "If you cannot reliably control your use, "
            "then perhaps it is better not to use it at all."
        )

        self.add_body(
            "It is risky. You should know that before entering."
        )

        self.add_button(
            "Yes, I can handle it",
            on_continue,
        )

        self.add_button(
            "No — exit",
            on_exit,
            "dangerButton",
        )