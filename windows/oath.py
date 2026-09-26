#!/usr/bin/env python3

from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QColor,
    QKeyEvent,
    QTextCharFormat,
    QTextCursor,
)
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from config import OATH
from oath import find_first_mismatch

from .base import BaseWindow


class OathInput(QPlainTextEdit):

    def __init__(self, check_password, parent=None):

        super().__init__(parent)

        self.check_password = check_password

    def keyPressEvent(self, event: QKeyEvent):

        if (
            event.key()
            in (
                Qt.Key.Key_Return,
                Qt.Key.Key_Enter,
            )
            and event.modifiers()
            & Qt.KeyboardModifier.ControlModifier
        ):
            self.check_password()
            return

        super().keyPressEvent(event)


class OathWindow(BaseWindow):

    def __init__(self, on_complete, on_exit):

        super().__init__(
            "Now, slow down again.",
            "Read the oath. Then write it deliberately.",
        )

        self.on_complete = on_complete

        panels = QHBoxLayout()
        panels.setSpacing(20)

        # ========================================================
        # LEFT — OATH
        # ========================================================

        left_panel = QFrame()
        left_panel.setObjectName("panel")

        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(
            22,
            22,
            22,
            22,
        )

        left_layout.setSpacing(12)

        oath_title = QLabel("THE OATH")

        oath_title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.oath_display = QPlainTextEdit()

        self.oath_display.setPlainText(OATH)
        self.oath_display.setReadOnly(True)

        self.oath_display.setTextInteractionFlags(
            Qt.TextInteractionFlag.NoTextInteraction
        )

        self.oath_display.setLineWrapMode(
            QPlainTextEdit.LineWrapMode.WidgetWidth
        )

        self.oath_display.setObjectName(
            "oathDisplay"
        )

        left_layout.addWidget(
            oath_title
        )

        left_layout.addWidget(
            self.oath_display,
            stretch=1,
        )

        left_panel.setLayout(
            left_layout
        )

        # ========================================================
        # RIGHT — WRITING
        # ========================================================

        right_panel = QFrame()
        right_panel.setObjectName("panel")

        right_layout = QVBoxLayout()

        right_layout.setContentsMargins(
            22,
            22,
            22,
            22,
        )

        right_layout.setSpacing(12)

        write_title = QLabel("WRITE IT")

        write_title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        instruction = QLabel(
            "Do not copy and paste.<br>"
            "Write the oath deliberately."
        )

        instruction.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.password_input = OathInput(
            self.check_password,
            self,
        )

        self.password_input.setPlaceholderText(
            "Write the oath here..."
        )

        self.password_input.setLineWrapMode(
            QPlainTextEdit.LineWrapMode.WidgetWidth
        )

        self.password_input.setObjectName(
            "passwordInput"
        )

        self.password_input.textChanged.connect(
            self.check_typing
        )

        self.status_label = QLabel(
            "Begin writing the oath."
        )

        self.status_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.status_label.setWordWrap(True)

        self.unlock_button = QPushButton(
            "Continue"
        )

        self.unlock_button.setEnabled(
            False
        )

        self.unlock_button.clicked.connect(
            self.check_password
        )

        right_layout.addWidget(
            write_title
        )

        right_layout.addWidget(
            instruction
        )

        right_layout.addWidget(
            self.password_input,
            stretch=1,
        )

        right_layout.addWidget(
            self.status_label
        )

        right_layout.addWidget(
            self.unlock_button
        )

        right_panel.setLayout(
            right_layout
        )

        panels.addWidget(
            left_panel,
            stretch=11,
        )

        panels.addWidget(
            right_panel,
            stretch=9,
        )

        self.content_layout.addLayout(
            panels,
            stretch=1,
        )

        self.add_button(
            "Exit",
            on_exit,
            "dangerButton",
        )

        self.password_input.setFocus()

    # ============================================================
    # HIGHLIGHTING
    # ============================================================

    def clear_highlights(self):

        self.oath_display.setExtraSelections(
            []
        )

        self.password_input.setExtraSelections(
            []
        )

    def create_selection(
        self,
        editor: QPlainTextEdit,
        position: int,
        length: int = 1,
        background: str = "#7A3030",
        foreground: str = "#FFFFFF",
    ):

        cursor = editor.textCursor()

        cursor.setPosition(
            position
        )

        cursor.setPosition(
            position + length,
            QTextCursor.MoveMode.KeepAnchor,
        )

        selection = QTextEdit.ExtraSelection()

        selection.cursor = cursor

        format_ = QTextCharFormat()

        format_.setBackground(
            QColor(background)
        )

        format_.setForeground(
            QColor(foreground)
        )

        selection.format = format_

        return selection

    def highlight_character(
        self,
        editor: QPlainTextEdit,
        position: int,
        length: int = 1,
    ):

        selection = self.create_selection(
            editor=editor,
            position=position,
            length=length,
        )

        selections = editor.extraSelections()

        selections.append(
            selection
        )

        editor.setExtraSelections(
            selections
        )

    def highlight_line(
        self,
        editor: QPlainTextEdit,
        position: int,
    ):

        cursor = editor.textCursor()

        cursor.setPosition(
            position
        )

        cursor.select(
            QTextCursor.SelectionType.LineUnderCursor
        )

        selection = QTextEdit.ExtraSelection()

        selection.cursor = cursor

        format_ = QTextCharFormat()

        format_.setBackground(
            QColor("#4A2626")
        )

        selection.format = format_

        selections = editor.extraSelections()

        selections.append(
            selection
        )

        editor.setExtraSelections(
            selections
        )

    def show_mismatch(
        self,
        position: int,
        expected: str,
        actual: str,
        typed_length: int,
    ):

        self.clear_highlights()

        # --------------------------------------------------------
        # Highlight expected character in THE OATH
        # --------------------------------------------------------

        if expected:

            if expected == "\n":

                self.highlight_line(
                    self.oath_display,
                    position,
                )

            else:

                self.highlight_character(
                    self.oath_display,
                    position,
                )

        # --------------------------------------------------------
        # Highlight actual character in WRITE IT
        # --------------------------------------------------------

        if actual:

            if actual == "\n":

                self.highlight_line(
                    self.password_input,
                    position,
                )

            else:

                self.highlight_character(
                    self.password_input,
                    position,
                )

        # --------------------------------------------------------
        # Missing character
        # --------------------------------------------------------

        elif expected:

            insertion_position = min(
                position,
                typed_length,
            )

            self.highlight_line(
                self.password_input,
                insertion_position,
            )

            cursor = (
                self.password_input.textCursor()
            )

            cursor.setPosition(
                insertion_position
            )

            self.password_input.setTextCursor(
                cursor
            )

    # ============================================================
    # LIVE CHECKER
    # ============================================================

    def check_typing(self):

        typed = (
            self.password_input.toPlainText()
        )

        # --------------------------------------------------------
        # Empty
        # --------------------------------------------------------

        if not typed:

            self.clear_highlights()

            self.status_label.setText(
                "Begin writing the oath."
            )

            self.unlock_button.setEnabled(
                False
            )

            return

        # --------------------------------------------------------
        # Completely correct
        # --------------------------------------------------------

        if typed == OATH:

            self.clear_highlights()

            self.status_label.setText(
                "✓ The oath is complete."
            )

            self.unlock_button.setEnabled(
                True
            )

            return

        # --------------------------------------------------------
        # Find first mismatch
        # --------------------------------------------------------

        mismatch = find_first_mismatch(
            typed,
            OATH,
        )

        if mismatch is None:

            self.clear_highlights()

            return

        # --------------------------------------------------------
        # Correct prefix
        # --------------------------------------------------------

        if mismatch.actual == "":

            self.clear_highlights()

            remaining = (
                len(OATH)
                - len(typed)
            )

            self.status_label.setText(
                f"✓ Correct so far — "
                f"{remaining} characters remaining."
            )

            self.unlock_button.setEnabled(
                False
            )

            return

        # --------------------------------------------------------
        # Actual mismatch
        # --------------------------------------------------------

        expected = self.display_character(
            mismatch.expected
        )

        actual = self.display_character(
            mismatch.actual
        )

        self.show_mismatch(
            position=mismatch.position,
            expected=mismatch.expected,
            actual=mismatch.actual,
            typed_length=len(typed),
        )

        self.status_label.setText(
            f"Mismatch at character "
            f"{mismatch.position + 1}: "
            f"expected {expected}, "
            f"got {actual}"
        )

        self.unlock_button.setEnabled(
            False
        )

    # ============================================================
    # CHARACTER DISPLAY
    # ============================================================

    @staticmethod
    def display_character(character):

        if character == "":
            return "nothing"

        if character == "\n":
            return "↵"

        if character == " ":
            return "space"

        return repr(character)

    # ============================================================
    # FINAL CHECK
    # ============================================================

    def check_password(self):

        if (
            self.password_input.toPlainText()
            == OATH
        ):

            self.on_complete()