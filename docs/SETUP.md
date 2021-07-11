## pyenv

Install [`pyenv`](https://github.com/pyenv/pyenv) and set it to version `3.8.8`.

## `virtualenvwrapper`

✸ Make a virtual environment `mkvirtualenv itzhak`

✸ Activate the virtual environment `workon itzhak`

The above commands require the package [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/). `virtualenvwrapper` is a framework that organizes virtual environments in a centralized place in your system.

You do _not_ need `virtualenvwrapper` to run Itzhak. It does however make things easier.

Make sure to configure the following in your shell configuration file (`.bashrc`, `.bash_profile`, `.zshrc`, `.zprofile`)

```sh
# where virtual environments will be stored
export WORKON_HOME=$HOME/.virtualenvs
# path to python
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
# path to virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper.sh
```

## Django

✸ Run Itzhak `runserver 9000`

✸ Generate migrations `mkmigrations`

✸ Apply migrations `manage.py migrate`

✸ Load data fixtures `manage.py loaddata`

✸ The above commands must be run with `manage.py`.

```sh
# example
<path-to-manage.py> command
```

## Pytest and `pytest-watch`

Create `pytest.ini` in your project root.

Pytest displays deprecation warnings from internal packages by default. To disable these warnings (which are often irrelevant or unactionable) we have to add a configuration in this file.

```py
[pytest]
DJANGO_SETTINGS_MODULE = <your Django settings file>
filterwarnings =
    ignore::DeprecationWarning
```

✸ Run tests `py.test -s`

✸ Run tests in watch mode `ptw`
