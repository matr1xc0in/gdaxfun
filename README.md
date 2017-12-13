# GDAX-v0.1

This is a playground to explose GDAX APIs. Let us have fun.

**DO NOT STORE API KEYS NOR SECRETS ON GITHUB, NEVER EVER!!!!!!!!!**

# Requirement

Please refer to Google Sheet and Drive, etc.

# Code Conduct
## Use Python 2.7 or Higher
Your Mac OSX should come with default Python 2.7.10 or a higer version.

## Structuring Python Package
Let's follow https://docs.python.org/3/tutorial/modules.html#packages to define our package structure
Reference: http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html

## Explanation on Directories

You will see something like this crated already to get started.

```
.
├── LICENSE
├── README.md
├── VERSION
└── python
    └── gdaxfun
        ├── CHANGES.txt
        ├── LICENSE.txt
        ├── MANIFEST.in
        ├── README.txt
        ├── docs
        ├── gdaxfun
        │   ├── __init__.py
        │   ├── gdaxauth.py
        │   └── gdaxutils.py
        ├── requirements.txt
        └── setup.py
```

The python code should go into `gdaxfun/gdaxfun` as you can see, there is 2 files created as an example `gdaxauth.py`
for authentication APIs and logics and `gdaxutils.py` to store all auxiliary utility functions to assist other classes
and modules, etc. We store all python related code under `python` directory, just in case, we add other programming language
such as Java, or C later in the same repository.


