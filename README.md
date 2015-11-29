Introduction
============

This is a demo for selenium and [holmium](http://holmiumcore.readthedocs.org)

Pre-Requisites
==============
* firefox

* On Windows
  * Download and install [python 2.7](https://www.python.org/download/releases/2.7.7/)
  * Install `pip`
      * Download [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py),\
        being careful to save it as a .py file rather than .txt.\
        Then, run it from the command prompt.
      * `python get-pip.py`
      * Add `C:\Python27\Scripts` to PATH
* On OSX

        sudo easy_install nose && \
        sudo easy_install pip && \
        sudo pip install -U selenium && \
        sudo pip install -U holmium.core
* On Ubuntu

        sudo apt-get install python-pip -y && \
        sudo pip install nose && \
        sudo pip install -U selenium && \
        sudo pip install -U holmium.core

Run
===
`nosetests test_albelli.py --with-holmium --holmium-browser=firefox --holmium-environment='http://albelli.nl'`
