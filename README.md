# Package CI example repository
This repository is designed to illustrate how to create a pip-installable package (following [these minimal instructions](https://python-packaging.readthedocs.io/en/latest/minimal.html)) and add continuous integration (CI with [travis](http://travis-ci.com/)).

The idea is, that you clone it and then first make it a pip-installable package and then add CI.

Here are the steps:
1. Fork this repository
2. Clone it onto your local machine
3. Edit the file `setup.py`
   - Change the name of the repo (I recommend to change the `aypac` part to your username)
   - Also change `url`, `author`, `author_email` and `packages`
4. If you want to also upload the example to [PyPi](http://pypi.python.org), follow the remaining examples [here](https://python-packaging.readthedocs.io/en/latest/minimal.html)
5. ...
