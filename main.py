#!/usr/bin/env python3

import shlex
import subprocess
import sys
from datetime import datetime, time

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# ============================================================
# CONFIG
# ============================================================

WORK_START = time(0, 0)
WORK_END = time(22, 0)

PASSWORD = """When craving rises, I shall not obey.
When pleasure calls, I shall not cling.
When discomfort comes, I shall not flee.

I shall watch the mind without hatred,
observe the feeling without becoming it,
and let the impulse arise and pass.

I shall not trade lasting freedom
for momentary satisfaction.
I shall remember that craving feeds on attention,
and what I feed becomes stronger.

Let mindfulness be my pause,
wisdom be my guide,
and compassion be my strength.

Today I choose deliberately.
Tomorrow I shall choose again.
Through each mindful choice,
I loosen craving's grasp
and walk one step closer to freedom."""


# ============================================================
# TIME CHECK
# ============================================================

def is_work_time():
    now = datetime.now().time()
    return WORK_START <= now <= WORK_END


def launch_app(app_cmd):
    try:
        subprocess.Popen(shlex.split(app_cmd))
    except Exception as e:
        print(f"Error launching app: {e}")


# ============================================================
# GUI
# ============================================================

class BlockWindow(QWidget):

    def __init__(self, app_cmd):
        super().__init__()

        self.app_cmd = app_cmd

        self.setWindowTitle("Pause")

        # --------------------------------------------------------
        # 75% of available screen
        # --------------------------------------------------------

        screen = QApplication.primaryScreen()
        geometry = screen.availableGeometry()

        self.resize(
            int(geometry.width() * 0.75),
            int(geometry.height() * 0.75),
        )

        # --------------------------------------------------------
        # Main layout
        # --------------------------------------------------------

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 25, 30, 25)
        main_layout.setSpacing(18)

        # --------------------------------------------------------
        # Header
        # --------------------------------------------------------

        title = QLabel("Pause.")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title.setFont(title_font)

        subtitle = QLabel(
            f"Before entering <b>{app_cmd}</b>, take a moment.<br>"
            "Read the oath. Then write it deliberately."
        )

        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setWordWrap(True)

        subtitle_font = QFont()
        subtitle_font.setPointSize(11)
        subtitle.setFont(subtitle_font)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # ========================================================
        # TWO PANELS
        # ========================================================

        panels = QHBoxLayout()
        panels.setSpacing(20)

        # ========================================================
        # LEFT PANEL — OATH
        # ========================================================

        left_panel = QFrame()
        left_panel.setObjectName("leftPanel")

        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(22, 22, 22, 22)
        left_layout.setSpacing(12)

        oath_title = QLabel("THE OATH")
        oath_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        oath_font = QFont()
        oath_font.setPointSize(13)
        oath_font.setBold(True)
        oath_title.setFont(oath_font)

        self.oath_display = QPlainTextEdit()
        self.oath_display.setPlainText(PASSWORD)
        self.oath_display.setReadOnly(True)
        self.oath_display.setLineWrapMode(
            QPlainTextEdit.LineWrapMode.WidgetWidth
        )
        self.oath_display.setObjectName("oathDisplay")

        left_layout.addWidget(oath_title)
        left_layout.addWidget(self.oath_display, stretch=1)

        left_panel.setLayout(left_layout)

        # ========================================================
        # RIGHT PANEL — WRITING
        # ========================================================

        right_panel = QFrame()
        right_panel.setObjectName("rightPanel")

        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(22, 22, 22, 22)
        right_layout.setSpacing(12)

        write_title = QLabel("WRITE IT")
        write_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        write_font = QFont()
        write_font.setPointSize(13)
        write_font.setBold(True)
        write_title.setFont(write_font)

        instruction = QLabel(
            "Do not copy and paste.<br>"
            "Write the oath deliberately."
        )

        instruction.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --------------------------------------------------------
        # Large typing area
        # --------------------------------------------------------

        self.password_input = QPlainTextEdit()

        self.password_input.setPlaceholderText(
            "Write the oath here..."
        )

        self.password_input.setLineWrapMode(
            QPlainTextEdit.LineWrapMode.WidgetWidth
        )

        self.password_input.setObjectName("passwordInput")

        self.password_input.textChanged.connect(
            self.check_typing
        )

        # --------------------------------------------------------
        # Progress / feedback
        # --------------------------------------------------------

        self.status_label = QLabel(
            "Begin writing the oath."
        )

        self.status_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.status_label.setWordWrap(True)

        # --------------------------------------------------------
        # Continue button
        # --------------------------------------------------------

        self.unlock_button = QPushButton("Continue")

        self.unlock_button.setObjectName("unlockButton")

        self.unlock_button.setEnabled(False)

        self.unlock_button.clicked.connect(
            self.check_password
        )

        # --------------------------------------------------------
        # Layout
        # --------------------------------------------------------

        right_layout.addWidget(write_title)
        right_layout.addWidget(instruction)
        right_layout.addWidget(
            self.password_input,
            stretch=1,
        )
        right_layout.addWidget(self.status_label)
        right_layout.addWidget(self.unlock_button)

        right_panel.setLayout(right_layout)

        # --------------------------------------------------------
        # Panel proportions
        # --------------------------------------------------------

        panels.addWidget(left_panel, stretch=11)
        panels.addWidget(right_panel, stretch=9)

        main_layout.addLayout(
            panels,
            stretch=1,
        )

        self.setLayout(main_layout)

        # --------------------------------------------------------
        # Styling
        # --------------------------------------------------------

        self.setStyleSheet("""
            QWidget {
                background-color: #151515;
                color: #E8E8E8;
            }

            #leftPanel {
                background-color: #1C1C1C;
                border: 1px solid #333333;
                border-radius: 14px;
            }

            #rightPanel {
                background-color: #191919;
                border: 1px solid #333333;
                border-radius: 14px;
            }

            #oathDisplay {
                background-color: #121212;
                border: none;
                border-radius: 10px;
                padding: 18px;
                font-size: 15px;
                selection-background-color: #444444;
            }

            #passwordInput {
                background-color: #101010;
                border: 2px solid #333333;
                border-radius: 10px;
                padding: 18px;
                font-size: 15px;
                selection-background-color: #555555;
            }

            #passwordInput:focus {
                border: 2px solid #777777;
            }

            #unlockButton {
                min-height: 48px;
                border-radius: 10px;
                background-color: #E8E8E8;
                color: #151515;
                font-size: 14px;
                font-weight: bold;
            }

            #unlockButton:disabled {
                background-color: #333333;
                color: #777777;
            }

            #unlockButton:hover:enabled {
                background-color: #FFFFFF;
            }

            #unlockButton:pressed:enabled {
                background-color: #CCCCCC;
            }
        """)

        self.password_input.setFocus()

    # ============================================================
    # LIVE TYPING CHECKER
    # ============================================================

    def check_typing(self):

        typed = self.password_input.toPlainText()

        # --------------------------------------------------------
        # Empty
        # --------------------------------------------------------

        if not typed:
            self.status_label.setText(
                "Begin writing the oath."
            )

            self.unlock_button.setEnabled(False)

            self.set_input_border("normal")

            return

        # --------------------------------------------------------
        # Exact match
        # --------------------------------------------------------

        if typed == PASSWORD:

            self.status_label.setText(
                "✓ The oath is complete."
            )

            self.unlock_button.setEnabled(True)

            self.set_input_border("correct")

            return

        # --------------------------------------------------------
        # Find the first mismatch
        # --------------------------------------------------------

        mismatch = self.find_first_mismatch(
            typed,
            PASSWORD,
        )

        position = mismatch["position"]
        expected = mismatch["expected"]
        actual = mismatch["actual"]

        # --------------------------------------------------------
        # Determine whether the user is simply incomplete
        # --------------------------------------------------------

        if position == len(typed):

            remaining = len(PASSWORD) - len(typed)

            self.status_label.setText(
                f"✓ Correct so far — {remaining} characters remaining."
            )

            self.set_input_border("normal")

            self.unlock_button.setEnabled(False)

            return

        # --------------------------------------------------------
        # Show mismatch
        # --------------------------------------------------------

        if actual == "":
            actual_display = "nothing"
        elif actual == "\n":
            actual_display = "↵"
        elif actual == " ":
            actual_display = "space"
        else:
            actual_display = repr(actual)

        if expected == "\n":
            expected_display = "↵"
        elif expected == " ":
            expected_display = "space"
        else:
            expected_display = repr(expected)

        self.status_label.setText(
            f"Mismatch at character {position + 1}: "
            f"expected {expected_display}, "
            f"got {actual_display}"
        )

        self.set_input_border("error")

        self.unlock_button.setEnabled(False)

    # ============================================================
    # FIND FIRST MISMATCH
    # ============================================================

    @staticmethod
    def find_first_mismatch(typed, expected):

        minimum = min(
            len(typed),
            len(expected),
        )

        # --------------------------------------------------------
        # Direct character comparison
        # --------------------------------------------------------

        for i in range(minimum):

            if typed[i] != expected[i]:

                return {
                    "position": i,
                    "expected": expected[i],
                    "actual": typed[i],
                }

        # --------------------------------------------------------
        # Typed text is longer
        # --------------------------------------------------------

        if len(typed) > len(expected):

            return {
                "position": len(expected),
                "expected": "",
                "actual": typed[len(expected)],
            }

        # --------------------------------------------------------
        # Typed text is shorter
        # --------------------------------------------------------

        return {
            "position": len(typed),
            "expected": expected[len(typed)],
            "actual": "",
        }

    # ============================================================
    # INPUT BORDER
    # ============================================================

    def set_input_border(self, state):

        if state == "correct":

            self.password_input.setStyleSheet("""
                QPlainTextEdit {
                    background-color: #101010;
                    border: 2px solid #5A9A68;
                    border-radius: 10px;
                    padding: 18px;
                    font-size: 15px;
                }
            """)

        elif state == "error":

            self.password_input.setStyleSheet("""
                QPlainTextEdit {
                    background-color: #101010;
                    border: 2px solid #A84A4A;
                    border-radius: 10px;
                    padding: 18px;
                    font-size: 15px;
                }
            """)

        else:

            self.password_input.setStyleSheet("""
                QPlainTextEdit {
                    background-color: #101010;
                    border: 2px solid #333333;
                    border-radius: 10px;
                    padding: 18px;
                    font-size: 15px;
                }

                QPlainTextEdit:focus {
                    border: 2px solid #777777;
                }
            """)

    # ============================================================
    # FINAL PASSWORD CHECK
    # ============================================================

    def check_password(self):

        if self.password_input.toPlainText() == PASSWORD:

            launch_app(self.app_cmd)

            QApplication.quit()


# ============================================================
# MAIN LOGIC
# ============================================================

def main():

    if len(sys.argv) < 2:
        print('Usage: focus_launcher.py "command"')
        sys.exit(1)

    app_cmd = sys.argv[1]

    if is_work_time():

        app = QApplication(sys.argv)

        window = BlockWindow(app_cmd)
        window.show()

        sys.exit(app.exec())

    launch_app(app_cmd)


if __name__ == "__main__":
    main()
