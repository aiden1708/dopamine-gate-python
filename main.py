#!/usr/bin/env python3

import sys
from datetime import datetime
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from config import WORK_END, WORK_START
from flow import GateFlow
from launcher import launch_app


def is_work_time():

    now = datetime.now().time()

    return WORK_START <= now <= WORK_END


def main():

    if len(sys.argv) < 2:

        print(
            'Usage: focus_launcher.py "command"'
        )

        sys.exit(1)

    app_cmd = sys.argv[1]

    # ------------------------------------------------------------
    # Outside protected hours
    # ------------------------------------------------------------

    if not is_work_time():

        launch_app(app_cmd)

        return

    # ------------------------------------------------------------
    # Protected hours
    # ------------------------------------------------------------

    app = QApplication(sys.argv)

    # ------------------------------------------------------------
    # Application icon
    # ------------------------------------------------------------

    icon_path = Path(__file__).resolve().parent / "resources" / "icon.png"

    app.setWindowIcon(QIcon(str(icon_path)))

    # ------------------------------------------------------------
    # Start gate flow
    # ------------------------------------------------------------

    flow = GateFlow(
        app=app,
        app_cmd=app_cmd,
    )

    flow.start()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()