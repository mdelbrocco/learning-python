# Learning Python
What it says on the tin!

I decided to use VS Code as my editor so I followed [this tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

Created a simple hello world program and made sure debugging worked - easy enough!

Next created a standard plot, which needed the `matplotlib` package (which in turn has `numpy` and others as dependencies). We should avoid installing packages into a global interpreter environment. Use a project-specific `virtual environment` which contains a copy of a global environment instead!

1. Create and activate a virtual environment

`py -3 -m venv .venv`
`.venv\scripts\activate`

Once I ran the above (windows-specific) commands via terminal, I noticed `(.venv)` appeared before my path.

2. Select the new environment via the command palette (ctrl + shift + P).

There should be an option in the list that includes .venv now!

3. Install the packages

`python -m pip install matplotlib`

4. Run standardplot program!

5. When finished, type `deactivate` in the terminal to deactivate the virtual environment.

Note: PyPI = Python Package Index