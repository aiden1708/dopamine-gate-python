#!/usr/bin/env python3

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class BaseWindow(QWidget):
    """
    Base window used by all gate steps.

    Each child window implements its own interaction and calls
    the supplied callbacks when the user chooses how to proceed.
    """

    def __init__(self, title: str, subtitle: str = ""):
        super().__init__()

        self.setWindowTitle("Dopamine Gate")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 35, 40, 35)
        main_layout.setSpacing(24)

        # --------------------------------------------------------
        # Header
        # --------------------------------------------------------

        self.title_label = QLabel(title)
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_font = QFont()
        title_font.setPointSize(26)
        title_font.setBold(True)

        self.title_label.setFont(title_font)

        main_layout.addWidget(self.title_label)

        if subtitle:
            self.subtitle_label = QLabel(subtitle)
            self.subtitle_label.setObjectName("subtitle")
            self.subtitle_label.setWordWrap(True)
            self.subtitle_label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            main_layout.addWidget(self.subtitle_label)

        # --------------------------------------------------------
        # Content
        # --------------------------------------------------------

        self.content_layout = QVBoxLayout()
        self.content_layout.setSpacing(18)

        main_layout.addLayout(
            self.content_layout,
            stretch=1,
        )

        # --------------------------------------------------------
        # Buttons
        # --------------------------------------------------------

        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(12)

        main_layout.addLayout(self.button_layout)

        self.setLayout(main_layout)

    # ============================================================
    # HELPERS
    # ============================================================

    def add_body(self, text: str) -> QLabel:
        label = QLabel(text)
        label.setObjectName("body")
        label.setWordWrap(True)

        self.content_layout.addWidget(label)

        return label

    def add_panel(self) -> tuple[QFrame, QVBoxLayout]:
        panel = QFrame()
        panel.setObjectName("panel")

        layout = QVBoxLayout()
        layout.setContentsMargins(28, 28, 28, 28)
        layout.setSpacing(16)

        panel.setLayout(layout)

        self.content_layout.addWidget(
            panel,
            stretch=1,
        )

        return panel, layout

    def add_button(
        self,
        text: str,
        callback,
        object_name: str | None = None,
    ) -> QPushButton:

        button = QPushButton(text)

        if object_name:
            button.setObjectName(object_name)

        button.clicked.connect(callback)

        self.button_layout.addWidget(button)

        return button