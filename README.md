# Package CI example repository [![Build Status](https://travis-ci.com/Aypac/Packaged_CI_and_unit_test_example.svg?branch=master)](https://travis-ci.com/Aypac/Packaged_CI_and_unit_test_example)
This repository is designed to illustrate how to create a pip-installable package (following [these minimal instructions](https://python-packaging.readthedocs.io/en/latest/minimal.html)) and add continuous integration (CI with [travis](http://travis-ci.com/)). It was created in a team-efford in a [Pythonista meeting](https://www.meetup.com/Pythonistas-NL).

The idea is, that you clone it and then first make it a pip-installable package and then add CI.

Here are the steps:
1. Fork this repository
2. Clone it onto your local machine
3. Edit the file `setup.py`
   - Change `url`, `author`, `author_email` and `packages`
4. If you want to also upload the example to [PyPi](http://pypi.python.org), follow the remaining examples [here](https://python-packaging.readthedocs.io/en/latest/minimal.html)
5. Head over to [travis](http://travis-ci.com/) and register with you Github account.
6. The CI should automatically start.
7. Edit the Build status button at the top of this `README.md` to point to your fork.

Now, you should have someone who explains all the relevant parts in the repo to you ;) Or you can use this as a template for future projects with CI and that are supposed to become a package.
