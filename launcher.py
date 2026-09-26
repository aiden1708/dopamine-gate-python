#!/usr/bin/env python3

import shlex
import subprocess


def launch_app(app_cmd: str) -> None:
    """Launch the requested application."""

    try:
        subprocess.Popen(shlex.split(app_cmd))
    except Exception as exc:
        print(f"Error launching application: {exc}")