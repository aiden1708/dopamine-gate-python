#!/usr/bin/env python3

from .base import BaseWindow


class ConfirmationWindow(BaseWindow):

    def __init__(self, on_continue, on_exit):

        super().__init__(
            "One final question.",
            "You have read the conditions.",
        )

        self.add_body(
            "You understand the risks."
        )

        self.add_body(
            "You have decided when and why you will stop."
        )

        self.add_body(
            "You have accepted responsibility for what happens "
            "if you lose control."
        )

        self.add_body(
            "Are you ready to continue?"
        )

        self.add_button(
            "Yes",
            on_continue,
        )

        self.add_button(
            "No",
            on_exit,
            "dangerButton",
        )