#!/usr/bin/env python3

from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from config import CONFIRMATION_BUTTON_COUNTDOWN


class BaseWindow(QWidget):
    """
    Base window used by all gate steps.

    Child windows provide their own content and call the
    supplied callbacks when the user chooses how to proceed.
    """

    def __init__(
        self,
        title: str,
        subtitle: str = "",
    ):
        super().__init__()

        self.setWindowTitle("Dopamine Gate")

        # --------------------------------------------------------
        # Transition state
        # --------------------------------------------------------

        self._transition_timer = None
        self._transition_callback = None
        self._transition_button = None
        self._transition_remaining = 0

        # --------------------------------------------------------
        # Main layout
        # --------------------------------------------------------

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            40,
            35,
            40,
            35,
        )

        main_layout.setSpacing(24)

        # --------------------------------------------------------
        # Header
        # --------------------------------------------------------

        self.title_label = QLabel(title)
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title_font = QFont()
        title_font.setPointSize(26)
        title_font.setBold(True)

        self.title_label.setFont(title_font)

        main_layout.addWidget(
            self.title_label
        )

        if subtitle:

            self.subtitle_label = QLabel(subtitle)
            self.subtitle_label.setObjectName(
                "subtitle"
            )

            self.subtitle_label.setWordWrap(True)
            self.subtitle_label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            main_layout.addWidget(
                self.subtitle_label
            )

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

        main_layout.addLayout(
            self.button_layout
        )

        self.setLayout(main_layout)

    # ============================================================
    # CONTENT HELPERS
    # ============================================================

    def add_body(self, text: str) -> QLabel:

        label = QLabel(text)
        label.setObjectName("body")
        label.setWordWrap(True)

        self.content_layout.addWidget(label)

        return label

    def add_panel(
        self,
    ) -> tuple[QFrame, QVBoxLayout]:

        panel = QFrame()
        panel.setObjectName("panel")

        layout = QVBoxLayout()

        layout.setContentsMargins(
            28,
            28,
            28,
            28,
        )

        layout.setSpacing(16)

        panel.setLayout(layout)

        self.content_layout.addWidget(
            panel,
            stretch=1,
        )

        return panel, layout

    # ============================================================
    # BUTTON HELPERS
    # ============================================================

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

        self.button_layout.addWidget(
            button
        )

        return button

    def add_transition_button(
        self,
        text: str,
        callback,
        seconds: int = CONFIRMATION_BUTTON_COUNTDOWN,
        object_name: str | None = None,
    ) -> QPushButton:

        button = QPushButton(text)

        if object_name:
            button.setObjectName(object_name)

        button.clicked.connect(
            lambda: self.start_transition(
                callback,
                seconds,
                button,
            )
        )

        self.button_layout.addWidget(
            button
        )

        return button

    # ============================================================
    # TRANSITION
    # ============================================================

    def start_transition(
        self,
        callback,
        seconds: int = 5, # 5 SECONDS (DEFAULT)
        button: QPushButton | None = None,
    ):

        if self._transition_timer is not None:
            return

        self._transition_callback = callback
        self._transition_button = button
        self._transition_remaining = seconds

        for child in self.findChildren(QPushButton):
            child.setEnabled(False)

        if button is not None:
            button.setText(
                f"Continuing in {seconds}..."
            )

        self._transition_timer = QTimer(self)
        self._transition_timer.setInterval(1000)
        self._transition_timer.timeout.connect(
            self._transition_tick
        )
        self._transition_timer.start()

    def _transition_tick(self):

        self._transition_remaining -= 1

        if self._transition_remaining > 0:

            if self._transition_button is not None:
                self._transition_button.setText(
                    f"Continuing in "
                    f"{self._transition_remaining}..."
                )

            return

        self._transition_timer.stop()
        self._transition_timer.deleteLater()
        self._transition_timer = None

        callback = self._transition_callback

        self._transition_callback = None
        self._transition_button = None

        if callback is not None:
            callback()