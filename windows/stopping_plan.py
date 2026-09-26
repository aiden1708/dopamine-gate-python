#!/usr/bin/env python3

from .base import BaseWindow


class StoppingPlanWindow(BaseWindow):

    def __init__(self, on_continue, on_exit):

        super().__init__(
            "Decide when you will stop.",
            "Don't leave the stopping decision to your future self.",
        )

        self.add_body(
            "Here's what we should do."
        )

        self.add_body(
            "Set a timer. When the alarm rings, no drama and "
            "no exceptions — stop immediately."
        )

        self.add_body(
            "Or, you came here for a reason, right?"
        )

        self.add_body(
            "There must be a task to finish. Focus on that task. "
            "Don't get distracted. When the task is done, "
            "quit the application."
        )

        self.add_body(
            "That's it."
        )

        self.add_transition_button(
            "I accept the stopping rule",
            on_continue,
        )

        self.add_button(
            "No — exit",
            on_exit,
            "dangerButton",
        )