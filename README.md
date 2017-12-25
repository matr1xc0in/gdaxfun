# GDAX-v0.1

This is a playground to explose GDAX APIs. Let us have fun.

**DO NOT STORE API KEYS NOR SECRETS ON GITHUB, NEVER EVER!!!!!!!!!**

# Requirement

Please refer to Google Sheet and Drive, etc.

# How to use it

You will need to define the following environment variables in your system before invoking this module.

* `GDAX_PASSPHRASE`
* `GDAX_API_KEY`
* `GDAX_API_SECRET`

Store these environment variables in a file e.g. `mygdax.sh`

```
#!/bin/bash

export GDAX_PASSPHRASE=replace_me_with_your_passphrase
export GDAX_API_KEY=replace_me_with_your_api_key
export GDAX_API_SECRET="replace_me_with_your_secret_key_with_quotes"
```

To get a sense how to use the APIs, simply run the test code in `tests` directory.

```
pushd python/tests/
source mygdax.sh
python t_gdaxfun.py
```

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
        ├── setup.py
        └── tests
```

The python code should go into `gdaxfun/gdaxfun` as you can see, there is 2 files created as an example `gdaxauth.py`
for authentication APIs and logics and `gdaxutils.py` to store all auxiliary utility functions to assist other classes
and modules, etc. We store all python related code under `python` directory, just in case, we add other programming language
such as Java, or C later in the same repository.

The `tests` directory provides the test case and examples on how to use the APIs from `gdaxfun/gdaxauth.py` and `gdaxfun/gdaxutils.py`.

