# Dopamine Gate

> **A gatekeeper launcher that puts a pause between impulse and action.**

Dopamine Gate is a lightweight Python application for **Linux desktop systems** that intercepts the launch of distracting applications during protected hours.

It is built around a simple problem:

> **When craving arises, knowing what you should do is not always enough to control what you actually do.**

Dopamine Gate introduces friction at exactly that moment.

```text
Impulse
   ↓
Dopamine Gate
   ↓
Pause
   ↓
Awareness
   ↓
Choice
```

The goal is not to make distraction impossible.

The goal is to make **impulsive distraction harder**.

---

# How It Works

Dopamine Gate works as a command wrapper rather than modifying the applications themselves.

Normally:

```bash
firefox
```

launches:

```text
/usr/bin/firefox
```

With Dopamine Gate:

```text
firefox
   ↓
gate_run
   ↓
main.py
   ↓
Dopamine Gate
   ↓
Decision
   ↓
/usr/bin/firefox
```

The target application does not need to know that Dopamine Gate exists.

---

# The Idea Behind the Gate

Dopamine Gate is based on a behavioral observation:

```text
Craving → Impulsive action → Immediate reward
```

When craving becomes strong, the mind can become highly biased toward immediate satisfaction. At that point, simply remembering *"I shouldn't do this"* may not be enough.

So instead of relying entirely on willpower, Dopamine Gate changes the environment.

```text
Without a gate:

Craving → Action
```

```text
With Dopamine Gate:

Craving → Gate → Effort → Awareness → Choice
```

The interruption itself is the point.

---

# The Oath

The final step of the gate requires the user to **type an oath** before continuing.

This is intentional.

Craving wants the easiest and fastest path to satisfaction. Typing a deliberate statement requires effort, attention, and conscious participation.

The idea is simple:

> **If you are genuinely making a deliberate choice, you should be willing to spend a few seconds making it.**

The default oath is:

> *When craving rises, I shall not obey.*

It continues with reminders to observe craving and feelings without automatically acting on them.

This is not intended as a magical psychological cure. It is a deliberate **friction mechanism**: turn an automatic action into a conscious action.

You can change the oath in `config.py`.

---

# Configuration

Most personal settings are kept in:

```text
config.py
```

You can edit the variables there without changing the core application.

For example:

```python
WORK_START = time(0, 0)
WORK_END = time(22, 0)
```

These define the protected period.

You can change them to something such as:

```python
WORK_START = time(8, 0)
WORK_END = time(18, 0)
```

You can also customize:

```python
OATH
WINDOW_WIDTH_RATIO
WINDOW_HEIGHT_RATIO
CONFIRMATION_BUTTON_COUNTDOWN
APPLICATION_NAME
NOT_READY_MESSAGE
```

In other words, **`config.py` is the place to personalize Dopamine Gate's behavior and appearance.**

---

# Features

* 🛡️ Intercepts application launch commands
* ⏰ Protects configurable productive hours
* 🧠 Creates deliberate friction before distraction
* ✍️ Requires an intentional oath before continuing
* 🐍 Written in Python
* 🖥️ Designed for Linux desktop environments
* 🔌 Works without modifying target applications
* 🪶 Lightweight command-wrapper architecture
* 🔧 Works with Bash, Zsh, and other compatible shells

---

# Requirements

Dopamine Gate is currently developed for **Linux**.

Windows is **not currently supported**. I have not yet tested or figured out a reliable Windows workflow for the command interception mechanism.

You need:

* Python 3.9+
* `pip`
* Bash, Zsh, or another compatible shell
* The executable path of applications you want to protect

Check Python:

```bash
python3 --version
```

Check pip:

```bash
python3 -m pip --version
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/aiden1708/dopamine-gate.git
cd dopamine-gate
```

## Create a Virtual Environment

Recommended:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Then install the dependencies:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

For development dependencies, if provided:

```bash
python3 -m pip install -r requirements-dev.txt
```

---

# Test Dopamine Gate Directly

Before configuring your shell, test it directly:

```bash
python3 main.py /usr/bin/firefox
```

For example:

```bash
python3 main.py /usr/bin/google-chrome-stable
```

or:

```bash
python3 main.py /bin/Telegram
```

The executable path is passed to Dopamine Gate so that it can launch the application when the user is allowed to continue.

---

# Configure Your Shell

The desktop version works by replacing the normal application command with a wrapper.

## 1. Set the Script Path

Add:

```bash
export DOPAMINE_GATE_SCRIPT="$HOME/Projects/dopamine-gate/main.py"
```

Change the path to wherever you cloned the repository.

---

## 2. Create the Wrapper

Add:

```bash
gate_run() {
    python3 "$DOPAMINE_GATE_SCRIPT" "$@"
}
```

**Use `"$@"`, not `"$1"`**.

This preserves additional arguments passed to the application.

For example:

```bash
firefox --private-window https://example.com
```

can pass all of its arguments through Dopamine Gate.

---

## 3. Create Aliases

For example:

```bash
alias firefox="gate_run /usr/bin/firefox"
alias Telegram="gate_run /bin/Telegram"
alias google-chrome-stable="gate_run /bin/google-chrome-stable"
```

Now:

```bash
firefox
```

becomes:

```text
firefox
   ↓
gate_run /usr/bin/firefox
   ↓
python3 main.py /usr/bin/firefox
   ↓
Dopamine Gate
   ↓
Decision
   ↓
/usr/bin/firefox
```

---

# Complete Example

Here is a complete example:

```bash
# Dopamine Gate Script Path
export DOPAMINE_GATE_SCRIPT="$HOME/Programming/Aiden's Git Repos/focus-launcher/main.py"

# Reusable wrapper
gate_run() {
    python3 "$DOPAMINE_GATE_SCRIPT" "$@"
}

# Protected applications
alias firefox="gate_run /usr/bin/firefox"
alias Telegram="gate_run /bin/Telegram"
alias google-chrome-stable="gate_run /bin/google-chrome-stable"
```

---

# Make It Permanent

For **Zsh**, add the configuration to:

```text
~/.zshrc
```

For **Bash**:

```text
~/.bashrc
```

Then reload:

```bash
source ~/.zshrc
```

or:

```bash
source ~/.bashrc
```

---

# Find Application Paths

Use:

```bash
command -v firefox
```

or:

```bash
which firefox
```

Example:

```text
/usr/bin/firefox
```

Then:

```bash
alias firefox="gate_run /usr/bin/firefox"
```

---

# Verify the Alias

Run:

```bash
type firefox
```

You should see something similar to:

```text
firefox is aliased to `gate_run /usr/bin/firefox'
```

Then:

```bash
firefox
```

should pass the request through Dopamine Gate.

---

# Bypassing the Gate

Dopamine Gate is **not a security system**.

Because it operates at the shell-command level, it can be intentionally bypassed.

For example:

```bash
/usr/bin/firefox
```

may launch Firefox without going through:

```bash
firefox
```

You could also bypass it by:

* Removing the alias
* Using another shell
* Launching the application from a desktop launcher
* Running the executable directly
* Starting the application through another program

This is intentional.

Dopamine Gate is a **self-control tool**, not parental-control software.

The purpose is not to make cheating impossible.

The purpose is to make **impulsive behavior require effort**.

---

# Architecture

```text
┌─────────────────────┐
│       Shell         │
│                     │
│      firefox        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     gate_run()      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      main.py        │
│                     │
│   Dopamine Gate     │
└──────────┬──────────┘
           │
           ▼
      ┌────┴────┐
      │         │
   Continue    Exit
      │
      ▼
/usr/bin/firefox
```

---

# Project Structure

```text
dopamine-gate/
├── main.py
├── config.py
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── .gitignore
└── ...
```

If using a virtual environment:

```text
.venv/
```

should **not** be committed.

Recommended `.gitignore`:

```gitignore
.venv/
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.env
```

---

# Dependencies

Runtime dependencies belong in:

```text
requirements.txt
```

Development dependencies belong in:

```text
requirements-dev.txt
```

Install runtime dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Install development dependencies:

```bash
python3 -m pip install -r requirements-dev.txt
```

---

# Troubleshooting

### Python is not installed

```bash
python3 --version
```

Install Python using your Linux distribution's package manager.

### The alias is not working

Check:

```bash
type firefox
```

If the shell reports:

```text
firefox is /usr/bin/firefox
```

instead of an alias, reload your shell configuration:

```bash
source ~/.zshrc
```

or:

```bash
source ~/.bashrc
```

### Dopamine Gate cannot find the script

Check:

```bash
echo "$DOPAMINE_GATE_SCRIPT"
```

Then:

```bash
ls -l "$DOPAMINE_GATE_SCRIPT"
```

### The executable path is wrong

Run:

```bash
command -v firefox
```

and use the returned path in your alias.

---

# Philosophy

Dopamine Gate is built around one central idea:

> **When craving takes control, create enough friction to regain choice.**

The gate does not decide what you should do.

It gives you a moment in which you can decide **while you still have a choice**.

The oath adds another layer: if you really want to proceed, you must consciously invest effort into that decision.

Craving seeks immediate reward with minimal effort.

Dopamine Gate deliberately does the opposite:

```text
Craving → Effort → Awareness → Choice
```

Even a small interruption can break an automatic behavioral loop.

---

# Android Version

Dopamine Gate is also available as an Android application, built with **Flutter and Kotlin**.

The Android version uses Android's **Accessibility Service** to intercept distracting applications at the system level, while the Linux version uses shell command wrappers.

**Android repository:**
[Dopamine Gate Mobile](https://github.com/aiden1708/dopamine-gate-mobile?utm_source=chatgpt.com)

Both versions share the same core philosophy:

> **Put a deliberate gate between craving and action.**

The implementation is different because each operating system provides different ways to intercept application launches.

### Linux

```text
Shell command
      ↓
Python wrapper
      ↓
Dopamine Gate
      ↓
Executable
```

### Android

```text
Application launch
      ↓
Accessibility Service
      ↓
Dopamine Gate
      ↓
Application / Gate
```

---

# Roadmap

* [ ] More robust configuration
* [ ] GUI configuration
* [ ] Better desktop-launcher integration
* [ ] `.desktop` entry support
* [ ] Usage statistics
* [ ] Temporary overrides
* [ ] More sophisticated productive-hour rules
* [ ] Improved Linux desktop compatibility
* [ ] Investigate a reliable Windows workflow

---

# License

```text
MIT License
```

---

# Dopamine Gate

**Don't try to eliminate every craving.**

**Build a gate between craving and action.**
