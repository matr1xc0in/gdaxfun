=======
gdaxfun
=======

TODO

Example, assume you have defined a function `get_api_key` in `gdaxfun/gdaxauth.py` python file
and a variable to read API key from a file OR a hardcoded variable for the API key in your code, 
the following code example should print the API key on the screen by invoking the function `show_api_key`
defined in `gdaxfun/gdaxutils.py`.

    #!/usr/bin/env python

    from gdaxfun import gdaxauth
    from gdaxfun import gdaxutils

    if gdaxutils.show_api_key():
        print "Your API key is defined as:", gdaxauth.get_api_key()

(Note the double-colon and 4-space indent formatting above.)

Paragraphs are separated by blank lines. *Italics*, **bold**,
and ``monospace`` look like this.


A Section
=========

Lists look like this:

* First

* Second. Can be multiple lines
  but must be indented properly.

A Sub-Section
-------------

Numbered lists look like you'd expect:

1. list1

2. list2

Urls are http://like.this and links can be
written `like this <http://www.example.com/foo/bar>`_.
