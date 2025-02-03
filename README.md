<p align="center">
  <img width="250px" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/bash.png" alt="bash" title="bash"/>
</p>
<p align="center">
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/itonx/ezpyc">
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

- Python >=3.11
  - Add python.exe to PATH
- Windows >=10

# 🖥️ How to install ezpyc for Windows

Clone repo and run `python src/ezpyc.py install` as administrator:

```bash
git clone https://github.com/itonx/ezpyc
```

```bash
cd ezpyc
```

```bash
python src/ezpyc.py install
```

Output:

```
└─ ...
▒ Setup done. Create a new python script at C:\Users\wintermute\.ezpyc and try to run it. If you cannot execute it, restart your terminal or open a new one.
```

Once the installation's done you'll be able to execute your python scripts as if they were simple windows commands. All scripts must be added to `%USERPROFILE%\.ezpyc` if don't want to type the full path of your scripts.

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
└───ezpyc
    __init__.py
    clipboard.py
    command_decorators.py
    env_variable.py
    file.py
    folder.py
    installation_wizard.py
    os_decorators.py
    output.py
```

### Details:

- `%USERPROFILE%\.ezpyc\ezpyc` is a python package which contains shared code for `ezpyc.py`.
- `ezpyc.py` manages your ezpyc installation

`ezpyc` command accepts `-h` and `--help` args.

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

Open a terminal and run the command using the name of your script (no need to type the full path or restart the terminal if you add new scripts to `.ezpyc` folder):

```bash
mycommand
```

If you want to know how to process command line arguments with `click` see documentation: https://click.palletsprojects.com/en/stable/.

# 🖥️ How to uninstall

## Option 1: `ezpyc_installer.py`

Clone repo and run `python src/ezpyc.py uninstall` as administrator:

```bash
git clone https://github.com/itonx/ezpyc
```

```bash
cd ezpyc
```

```bash
python src/ezpyc.py uninstall
```

Output:

```
└─ ...
▒ ezpyc's been uninstalled. C:\Users\wintermute\.ezpyc needs to be deleted manually, don't forget to backup your scripts.
```

## Method 2: built-in `ezpyc` command

This will work only if you installed ezpyc.

Run as administrator:

```bash
ezpyc uninstall
```

Output:

```
└─ ...
▒ ezpyc's been uninstalled. C:\Users\wintermute\.ezpyc needs to be deleted manually, don't forget to backup your scripts.
```

> NOTE: Commands will be available until you restart your terminal or open a new one.
