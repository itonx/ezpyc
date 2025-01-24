<p align="center">
  <img width="250px" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/bash.png" alt="bash" title="bash"/>
</p>

# <div align="center">ezpyc</div>

Easy Python Commands allows you to execute your python scripts as if they were system commands.

Without ezpyc:

```bash
python mycommand.py
# or
python C:\Users\wintermute\dev\mycommand.py
```

With ezpyc:

```bash
mycommand
```

# ✅ Requirements

- Python >=3.11.2
  - Add python.exe to PATH
- Windows >=10

# 🖥️ How to install

Clone repo and run `python setup.py` as administrator:

```bash
git clone https://github.com/itonx/ezpyc
```

```bash
cd ezpyc
```

```bash
python setup.py
```

Output:

```
└─ ...
▒ Setup done!
└─ Try 'hworld' or 'hworld -h' command. If you cannot execute it, restart your terminal or open a new one.
```

Once the installation's done you'll be able to execute your python scripts as if they were simple windows commands. All scripts must be added to `%USERPROFILE%\.ezpyc`.

## Installation details

The installation will make the next changes on your system:

- Create .ezpyc folder: `%USERPROFILE%\.ezpyc`
- Add .ezpyc folder to PATH environment variable for CURRENT_USER
- Add .PY extension to PATHEXT environment variable for LOCAL_MACHINE
- Add built-in ezpyc scripts

## Built-in ezpyc scripts

```bash
%USERPROFILE%\.ezpyc
│   ezpyc.py
│   homec.py
│   hworld.py
│   pwdc.py
│
└───ezpyc
    clipboard.py
    env_variable.py
    ezpyc.py
    file.py
    folder.py
    os_decorators.py
    output.py
    __init__.py
```

### Details:

Built-in scripts are created to help you getting started with your own python script commands. All scripts use `click` to manage command line arguments. `hworld` is the simplest script, you might want to follow its structure to create simple scripts/commands. The rest of built-in files are a simple abstraction of `click`, you could follow their structure to create your own abstraction for complex scripts/commands with your own python packages.

- `%USERPROFILE%\.ezpyc\ezpyc` is a python package which contains shared code for `ezpyc`, `homec`, and `pwdc` commands. `hworld` doesn't depend on ezpyc shared code.
- `ezpyc` manages your ezpyc installation
- `homec` prints home dir and copy it to clipboard
- `hworld` prints a simple hello world message
- `pwdc` prints current working dir and copy it to clipboard

All commands accept `-h` and `--help` args.

> NOTE: Feel free to delete built-in ezpyc files if you don't use them.

# ⚒️ Create your first script/command

This process is as simple as creating a new file with a `print`.

mycommand.py

```python
print('mycommand works')
```

Magic happends once you place your scripts at `%USERPROFILE%\.ezpyc`.

```
%USERPROFILE%\.ezpyc
└───mycommand.py
```

Open a terminal and run the command using the name of your script (no need to type the full path or restart the terminal if you add new scripts):

```bash
mycommand
```

If you want to know how to process command line arguments with `click` see `hworld` built-in script or review `click` documentation: https://click.palletsprojects.com/en/stable/.
