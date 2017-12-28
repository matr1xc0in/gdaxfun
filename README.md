# GDAX-v0.1

This is a playground to explose GDAX APIs. Let us have fun.

**DO NOT STORE API KEYS NOR SECRETS ON GITHUB, NEVER EVER!!!!!!!!!**

# Requirement

Please refer to Google Sheet and Drive, etc. for the Business requirement.

## Python

To use the Python module, you will need to install other Python modules:

* requests
* pony
* simplejson

As your system *admin* or *root*, use `pip` 

```
sudo pip install requests
sudo pip install pony
sudo pip install simplejson
```

If your system does not have `pip` installed, you can also use `easy_install` to install `pip` and
repeat the above steps.

```
sudo easy_install pip
```

or just simply use `easy_install` to install all of them, either way works.

```
sudo easy_install requests
sudo easy_install pony
sudo easy_install simplejson
```

## Others

To be added. If you have other implementations in other languages, feel free to create their
directory accordingly.

# How to use it

This section is broken down for each programming language implementation.

## Python

### Install the gdaxfun Python module

Checkout this repository, and simply go into `python/gdaxfun` and run the following commands.

```
pushd python/gdaxfun
sudo python setup.py install
popd
```

A `gdaxfun` python module is now installed on your system. You can use the Python moduel as you like.
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

To get a sense how to use the APIs, simply run the example code in `python/examples` directory.

```
pushd python/examples/
source mygdax.sh
python run_gdaxfun.py
popd
```

If something isn't quite working right, you can run the test cases provided by the module from
the follow commands to see if it works on your laptop. Simplely run the following:

```
pushd python/gdaxfun
source mygdax.sh
sudo python setup.py test
popd
```

# Code Conduct

## Python

### Use Python 2.7 or Higher

Your Mac OSX should come with default Python 2.7.10 or a higer version.

### Structuring Python Package

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
    ├── examples
    │   └── run_gdaxfun.py
    └── gdaxfun
        ├── CHANGES.txt
        ├── LICENSE.txt
        ├── MANIFEST.in
        ├── README.txt
        ├── gdaxfun
        │   ├── __init__.py
        │   ├── gdaxauth.py
        │   ├── gdaxdb.py
        │   ├── ...
        │   ├── gdaxtables.py
        │   ├── gdaxutils.py
        │   └── tests
        │       ├── __init__.py
        │       ├── btcusd_trades.txt
        │       ├── test_gdaxdb.py
        │       └── test_gdaxfun.py
        ├── requirements.txt
        └── setup.py
```

The python code should go into `gdaxfun/gdaxfun` as you can see, there are few files created and one of them `gdaxauth.py`
for authentication APIs and logics and another one `gdaxutils.py` to store all auxiliary utility functions to assist 
other classes and modules, etc. We store all python related code under `python` directory, just in case, 
we need to add other programming language such as Java, or C later in the same repository.

The `tests` directory provides the test case and examples on how to use the APIs and should be part of the module directory.
