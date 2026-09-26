#!/usr/bin/env python3

from .base import BaseWindow


class RiskWindow(BaseWindow):

    def __init__(self, on_continue, on_exit):

        super().__init__(
            "Are you sure?",
            "Understand what you are about to enter.",
        )

        self.add_body(
            "This application can easily consume your attention "
            "and encourage repeated, compulsive use."
        )

        self.add_body(
            "It can feel harmless while you are using it, "
            "but it can become very difficult to stop once you "
            "lose track of time."
        )

        self.add_body(
            "It is risky."
        )

        self.add_body(
            "Are you sure you will be able to control yourself "
            "and not get lost while using it?"
        )

        self.add_transition_button(
            "Yes, I understand",
            on_continue,
        )

        self.add_button(
            "No — exit",
            on_exit,
            "dangerButton",
        )