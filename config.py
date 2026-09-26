#!/usr/bin/env python3

from datetime import time


# ============================================================
# TIME PROTECTION
# ============================================================

WORK_START = time(0, 0)
WORK_END = time(22, 0)


# ============================================================
# OATH
# ============================================================

OATH = """When craving rises, I shall not obey.
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
# APPLICATION
# ============================================================

WINDOW_WIDTH_RATIO = 0.75
WINDOW_HEIGHT_RATIO = 0.75

CONFIRMATION_BUTTON_COUNTDOWN = 3 # IN SECONDS

APPLICATION_NAME = "Dopamine Gate"


# ============================================================
# EXIT MESSAGES
# ============================================================

NOT_READY_MESSAGE = (
    "Alright, you are not ready.\n\n"
    "Let's exit the application."
)