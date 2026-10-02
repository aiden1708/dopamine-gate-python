# Dopamine Gate

> **A gatekeeper launcher that puts a pause between impulse and action.**

Dopamine Gate is a lightweight Python desktop application that intercepts the launch of distracting applications and gives you an opportunity to stop before opening them.

Instead of modifying or blocking applications directly, Dopamine Gate works as a **command wrapper**:

```text
User runs application
        ↓
Dopamine Gate
        ↓
Should this application be allowed?
        ↓
   ┌────┴────┐
   ↓         ↓
 Allow     Block
   ↓         ↓
Launch     Stop
```

The idea is simple:

> **Don't rely entirely on willpower. Put friction between the impulse and the action.**

---

# Features

* 🛡️ Intercepts application launch commands
* 🐍 Written in Python
* 🖥️ Designed for Linux desktop environments
* ⏰ Can be used to enforce productive hours
* 🚧 Prevents configured applications from launching directly
* 🔌 Works without modifying the target applications
* 🪶 Lightweight command-line launcher architecture
* 🔧 Can be integrated directly into shell aliases/functions

---

# How It Works

Dopamine Gate is not itself a replacement for Firefox, Telegram, Chrome, etc.

Instead, you replace the normal executable command with a small wrapper.

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

This means the target application does not need to know that Dopamine Gate exists.

---

# Requirements

## Operating System

The current desktop implementation is intended primarily for **Linux** systems.

You need:

* Python 3.9 or newer
* `pip`
* A POSIX-compatible shell such as Bash or Zsh
* The target application's executable path

Check your Python version:

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
git clone https://github.com/YOUR_USERNAME/dopamine-gate.git
cd dopamine-gate
```

Replace `YOUR_USERNAME` with the GitHub account containing the repository.

---

## Recommended: Create a Virtual Environment

Using a virtual environment keeps Dopamine Gate's Python dependencies isolated from your system Python installation.

Create the environment:

```bash
python3 -m venv .venv
```

Activate it:

### Bash / Zsh

```bash
source .venv/bin/activate
```

You should now see something similar to:

```text
(.venv) user@computer:~/dopamine-gate$
```

---

## Install Dependencies

If the project contains a `requirements.txt` file:

```bash
python3 -m pip install -r requirements.txt
```

For development dependencies:

```bash
python3 -m pip install -r requirements-dev.txt
```

If you are developing the project from scratch, keep the application's dependencies in `requirements.txt` rather than asking users to install packages manually.

---

# Running Dopamine Gate Directly

You can test the application before configuring shell commands:

```bash
python3 main.py /usr/bin/firefox
```

The argument passed to `main.py` is the executable that Dopamine Gate should eventually launch.

For example:

```bash
python3 main.py /usr/bin/google-chrome-stable
```

or:

```bash
python3 main.py /bin/Telegram
```

This is useful for testing the gate before modifying your shell configuration.

---

# Setting Up Command Interception

The most important part of the desktop version is replacing the normal application commands with Dopamine Gate wrappers.

You can do this using a shell function and aliases.

## 1. Set the Dopamine Gate Script Path

First, define the location of `main.py`.

For example:

```bash
export DOPAMINE_GATE_SCRIPT="$HOME/Programming/Aiden's Git Repos/focus-launcher/main.py"
```

This environment variable tells the wrapper where Dopamine Gate is installed.

If you cloned the project somewhere else, change the path accordingly.

For example:

```bash
export DOPAMINE_GATE_SCRIPT="$HOME/Projects/dopamine-gate/main.py"
```

---

# 2. Create the Wrapper Function

Add the following function to your shell configuration:

```bash
gate_run() {
    python3 "$DOPAMINE_GATE_SCRIPT" "$1"
}
```

This function receives the target executable and passes it to Dopamine Gate.

For example:

```bash
gate_run /usr/bin/firefox
```

is equivalent to:

```bash
python3 "$DOPAMINE_GATE_SCRIPT" /usr/bin/firefox
```

---

# 3. Create Application Aliases

You can now replace the normal commands with aliases.

Example:

```bash
alias firefox="gate_run /usr/bin/firefox"
alias Telegram="gate_run /bin/Telegram"
alias google-chrome-stable="gate_run /bin/google-chrome-stable"
```

Now, when you type:

```bash
firefox
```

your shell does not directly execute Firefox.

Instead:

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

The following is the complete setup used in one Linux environment:

```bash
# Dopamine Gate Script Path
export DOPAMINE_GATE_SCRIPT="$HOME/Programming/Aiden's Git Repos/focus-launcher/main.py"

# A reusable wrapper function that handles the Python execution safely
gate_run() {
    python3 "$DOPAMINE_GATE_SCRIPT" "$1"
}

# Pointing aliases to the function, passing the target binary path
alias firefox="gate_run /usr/bin/firefox"
alias Telegram="gate_run /bin/Telegram"
alias google-chrome-stable="gate_run /bin/google-chrome-stable"
```

---

# Making the Configuration Permanent

If you use **Bash**, put the configuration in:

```text
~/.bashrc
```

If you use **Zsh**, put it in:

```text
~/.zshrc
```

For example:

```bash
nano ~/.zshrc
```

Add:

```bash
# Dopamine Gate
export DOPAMINE_GATE_SCRIPT="$HOME/Programming/Aiden's Git Repos/focus-launcher/main.py"

gate_run() {
    python3 "$DOPAMINE_GATE_SCRIPT" "$1"
}

alias firefox="gate_run /usr/bin/firefox"
alias Telegram="gate_run /bin/Telegram"
alias google-chrome-stable="gate_run /bin/google-chrome-stable"
```

Then reload your shell:

```bash
source ~/.zshrc
```

For Bash:

```bash
source ~/.bashrc
```

---

# Finding Application Executable Paths

You need to know the actual executable path of the application you want to intercept.

Use:

```bash
which firefox
```

Example:

```text
/usr/bin/firefox
```

You can then use:

```bash
alias firefox="gate_run /usr/bin/firefox"
```

For another application:

```bash
which google-chrome-stable
```

Or:

```bash
command -v google-chrome-stable
```

---

# Important: The Alias Name Must Match the Command

Suppose the normal command is:

```bash
google-chrome-stable
```

Your alias should therefore be:

```bash
alias google-chrome-stable="gate_run /usr/bin/google-chrome-stable"
```

The left side is the command you normally type.

The right side is the real executable that Dopamine Gate eventually launches.

---

# Testing the Setup

After configuring the aliases, check that the shell recognizes them.

For example:

```bash
type firefox
```

You should see something similar to:

```text
firefox is aliased to `gate_run /usr/bin/firefox'
```

You can also inspect the alias directly:

```bash
alias firefox
```

Then run:

```bash
firefox
```

Dopamine Gate should receive:

```text
/usr/bin/firefox
```

instead of Firefox being launched directly.

---

# Bypassing the Gate

Because Dopamine Gate works at the shell-command level, users should understand that this is **not a security boundary**.

If the real executable is still accessible, it can generally be launched directly.

For example, if:

```bash
firefox
```

is intercepted by the alias, directly running:

```bash
/usr/bin/firefox
```

may bypass the alias.

This is intentional.

Dopamine Gate is designed as a **self-control and friction system**, not a tamper-proof parental-control system.

Its purpose is to make impulsive behavior harder, not to make intentional bypassing impossible.

---

# Why Use Command Wrappers?

There are several ways to build an application blocker.

One approach is to continuously monitor every running process:

```text
Monitor processes
       ↓
Find distracting application
       ↓
Kill application
```

Dopamine Gate takes a different approach:

```text
User attempts launch
       ↓
Intercept command
       ↓
Gate
       ↓
Launch only after decision
```

This means the system can intervene **before** the application is intentionally launched through the configured command.

---

# Architecture

The desktop version is intentionally simple:

```text
┌─────────────────────┐
│      Shell          │
│                     │
│  firefox            │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     gate_run()      │
│                     │
│   Python launcher   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Dopamine Gate     │
│                     │
│  Decide whether     │
│  launch is allowed  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Target executable  │
│                     │
│ /usr/bin/firefox    │
└─────────────────────┘
```

---

# Project Structure

A typical project structure:

```text
dopamine-gate/
├── main.py
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── .gitignore
├── .venv/
└── ...
```

The `.venv/` directory should **not** be committed to Git.

Add it to `.gitignore`:

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

# Python Dependencies

Keep runtime dependencies in:

```text
requirements.txt
```

For example:

```text
# Runtime dependencies
```

Add packages here as the application actually requires them.

Development-only packages should go into:

```text
requirements-dev.txt
```

For example:

```text
-r requirements.txt

pytest
ruff
```

Then install development dependencies with:

```bash
python3 -m pip install -r requirements-dev.txt
```

Avoid installing random packages globally just to make the project work.

---

# Recommended Development Setup

After cloning:

```bash
cd dopamine-gate

python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install --upgrade pip

python3 -m pip install -r requirements.txt
```

For development:

```bash
python3 -m pip install -r requirements-dev.txt
```

Then run:

```bash
python3 main.py /usr/bin/firefox
```

---

# Troubleshooting

## `python3: command not found`

Install Python 3 using your distribution's package manager.

Verify:

```bash
python3 --version
```

---

## `pip: command not found`

Prefer:

```bash
python3 -m pip
```

instead of relying on a standalone `pip` command.

For example:

```bash
python3 -m pip install -r requirements.txt
```

---

## The alias does not work

Check:

```bash
type firefox
```

If it says:

```text
firefox is /usr/bin/firefox
```

instead of:

```text
firefox is aliased to ...
```

your alias has not been loaded.

Reload your shell configuration:

```bash
source ~/.zshrc
```

or:

```bash
source ~/.bashrc
```

---

## Dopamine Gate cannot find the script

Check:

```bash
echo "$DOPAMINE_GATE_SCRIPT"
```

Then verify the file exists:

```bash
ls -l "$DOPAMINE_GATE_SCRIPT"
```

You can also run it directly:

```bash
python3 "$DOPAMINE_GATE_SCRIPT" /usr/bin/firefox
```

---

## The application path is incorrect

Find the executable:

```bash
command -v firefox
```

Then use the returned path in your alias.

---

# Security and Limitations

Dopamine Gate should **not** be considered a security or access-control system.

Shell aliases can be bypassed.

For example:

```bash
/usr/bin/firefox
```

can bypass:

```bash
firefox
```

if the alias is the only interception mechanism.

Users can also potentially:

* Remove the alias
* Open the application from a desktop launcher
* Use another shell
* Launch the executable directly
* Start the application through another program

This is acceptable for the project's intended purpose.

Dopamine Gate is about **behavioral friction**, not enforcement.

---

# Philosophy

Dopamine Gate is built around a simple idea:

> **Knowing what you should do is not always enough to make you do it.**

When an impulse appears, the easiest path is often to follow it immediately.

Dopamine Gate changes the environment:

```text
Without Dopamine Gate:

Impulse → Application
```

With Dopamine Gate:

```text
Impulse → Gate → Awareness → Choice → Application
```

The gate is not supposed to make the decision for you.

It exists to give you enough time to make the decision yourself.

---

# Relationship to the Android Version

The desktop and Android versions share the same basic philosophy but use different mechanisms.

### Desktop

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

The desktop version relies on the operating system's command environment, while the Android version uses Android's system-level accessibility capabilities.

---

# Roadmap

Potential future improvements include:

* [ ] Configuration file for blocked applications
* [ ] Configurable productive hours
* [ ] GUI configuration interface
* [ ] Better desktop-launcher integration
* [ ] Support for `.desktop` application entries
* [ ] More robust command argument forwarding
* [ ] Multiple levels of interruption
* [ ] Usage statistics
* [ ] Temporary override system
* [ ] Cooldown periods
* [ ] Better support for different Linux desktop environments
* [ ] Packaging as a standalone Linux application

---

# Contributing

Contributions and experiments are welcome.

When submitting a bug report, include:

* Linux distribution
* Desktop environment
* Python version
* Shell (`bash`, `zsh`, etc.)
* Target application
* Target executable path
* Exact command used
* Error output

For example:

```bash
python3 --version
echo "$SHELL"
command -v firefox
```

---

# License

Add the project's chosen open-source license here.

For example:

```text
MIT License
```

Choose a license deliberately before publishing the repository.

---

# Dopamine Gate

**Put a gate between the impulse and the action.**
