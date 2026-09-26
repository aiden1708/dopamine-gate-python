#!/usr/bin/env python3

from .base import BaseWindow


class LiabilityWindow(BaseWindow):

    def __init__(self, on_continue, on_exit):

        super().__init__(
            "Confidence is not enough.",
            "There must be accountability.",
        )

        self.add_body(
            "If you think you can handle this and want to "
            "progress further, then you are confident in yourself."
        )

        self.add_body(
            "That's reasonable."
        )

        self.add_body(
            "But the thing is..."
        )

        self.add_body(
            "No one can be trusted completely — including "
            "the version of yourself who is making this promise "
            "right now."
        )

        self.add_body(
            "So I don't trust your words alone."
        )

        self.add_body(
            "There must be accountability."
        )

        self.add_body(
            "If you break the rules and lose control, "
            "you must accept the agreed consequence as compensation."
        )

        self.add_body(
            "Read the liability rules carefully before proceeding."
        )

        self.add_transition_button(
            "I accept the liability",
            on_continue,
        )

        self.add_button(
            "No — exit",
            on_exit,
            "dangerButton",
        )