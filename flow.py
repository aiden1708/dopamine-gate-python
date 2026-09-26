#!/usr/bin/env python3

from PySide6.QtWidgets import QApplication

from styles import APP_STYLE

from windows.attention import AttentionWindow
from windows.confirmation import ConfirmationWindow
from windows.liability import LiabilityWindow
from windows.oath import OathWindow
from windows.risk import RiskWindow
from windows.self_control import SelfControlWindow
from windows.stopping_plan import StoppingPlanWindow
from windows.why import WhyWindow


class GateFlow:

    def __init__(self, app: QApplication, app_cmd: str):
        self.app = app
        self.app_cmd = app_cmd

        self.current_window = None

    # ============================================================
    # START
    # ============================================================

    def start(self):

        self.app.setStyleSheet(APP_STYLE)

        self.show_attention()

    # ============================================================
    # WINDOW MANAGEMENT
    # ============================================================

    def show(self, window):

        if self.current_window is not None:
            self.current_window.close()

        self.current_window = window

        if isinstance(window, OathWindow):
            window.showFullScreen()
        else:
            window.show()

    # ============================================================
    # EXIT
    # ============================================================

    def exit(self):

        self.app.quit()

    # ============================================================
    # FLOW
    # ============================================================

    def show_attention(self):

        self.show(
            AttentionWindow(
                on_continue=self.show_risk,
                on_exit=self.exit,
            )
        )

    def show_risk(self):

        self.show(
            RiskWindow(
                on_continue=self.show_stopping_plan,
                on_exit=self.exit,
            )
        )

    def show_stopping_plan(self):

        self.show(
            StoppingPlanWindow(
                on_continue=self.show_self_control,
                on_exit=self.exit,
            )
        )

    def show_self_control(self):

        self.show(
            SelfControlWindow(
                on_continue=self.show_why,
                on_exit=self.exit,
            )
        )

    def show_why(self):

        self.show(
            WhyWindow(
                on_continue=self.show_liability,
                on_exit=self.exit,
            )
        )

    def show_liability(self):

        self.show(
            LiabilityWindow(
                on_continue=self.show_confirmation,
                on_exit=self.exit,
            )
        )

    def show_confirmation(self):

        self.show(
            ConfirmationWindow(
                on_continue=self.show_oath,
                on_exit=self.exit,
            )
        )

    def show_oath(self):

        self.show(
            OathWindow(
                on_complete=self.complete,
                on_exit=self.exit,
            )
        )


    # ============================================================
    # COMPLETE
    # ============================================================

    def complete(self):

        from launcher import launch_app


        self.app.quit()
        launch_app(self.app_cmd)
