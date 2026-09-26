#!/usr/bin/env python3


APP_STYLE = """
QWidget {
    background-color: #151515;
    color: #E8E8E8;
}

QFrame#panel {
    background-color: #1C1C1C;
    border: 1px solid #333333;
    border-radius: 14px;
}

QLabel#title {
    font-size: 26px;
    font-weight: bold;
}

QLabel#subtitle {
    color: #BDBDBD;
    font-size: 13px;
}

QLabel#body {
    color: #D5D5D5;
    font-size: 15px;
    line-height: 1.5;
}

QPushButton {
    min-height: 48px;
    border-radius: 10px;
    background-color: #E8E8E8;
    color: #151515;
    font-size: 14px;
    font-weight: bold;
    padding: 0 24px;
}

QPushButton:hover:enabled {
    background-color: #FFFFFF;
}

QPushButton:pressed:enabled {
    background-color: #CCCCCC;
}

QPushButton:disabled {
    background-color: #333333;
    color: #777777;
}

QPushButton#dangerButton {
    background-color: #3A2020;
    color: #E8B0B0;
}

QPushButton#secondaryButton {
    background-color: #292929;
    color: #D5D5D5;
}

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
"""
