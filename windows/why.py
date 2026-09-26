#!/usr/bin/env python3

from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from .base import BaseWindow


class WhyWindow(BaseWindow):

    AGREEMENT_URL = (Path(__file__).resolve().parent.parent / "resources" / "agreement.html")

    def __init__(self, on_continue, on_exit):

        super().__init__(
            "Why are we doing this?",
            "There is a reason behind all these barriers.",
        )

        self.add_body(
            "Later in life, I discovered something important:"
        )

        self.add_body(
            "Our time, our attention, and our mental well-being "
            "are among the most important things we have for "
            "building a fulfilling life."
        )

        self.add_body(
            "This gate exists because protecting those things "
            "is more important than getting unrestricted access "
            "to another source of immediate pleasure."
        )

        agreement_button = self.add_button(
            "Read the reasoning",
            self.open_agreement,
            "secondaryButton",
        )

        self.add_button(
            "I understand",
            on_continue,
        )

        self.add_button(
            "No — exit",
            on_exit,
            "dangerButton",
        )

        self.on_continue = on_continue

    def open_agreement(self):
        QDesktopServices.openUrl(
            QUrl.fromLocalFile(self.AGREEMENT_URL)
        )