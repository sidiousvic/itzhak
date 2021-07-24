
# itzhak

<h2>A humanitarian expense manager app.</h2>

<h2>Setting up python</h2>
<ul>
<li>This project uses python 3.x</li>
<li>For windows, visit the official download page at https://www.python.org/downloads/windows/ and choose either the 32 or 64 bit installer based on your architecture. Launch the executable and follow install instructions.</li>
<li>For linux python will usually be accessible via the existing package manager eg. apt, yay, pacman as a package named python 3.\{MINOR\-NUMBER<=latest} or build from source with cpython or c compiler distribution.
On mac install with the brew package manager or build from source with pyenv or cpython.</li>
</ul>

<h2>Configuring the vitualenv wrapper</h2>
<ul>
<li>Its essential you don't pollute your global environment with the required packages.</li>
<li>This neccessitates setting up an environment from where the project will centrally acquire module resources.
Python provides its venv module for this. Install it via the command `python [optional-MAJOR-VERSION] -m venv {dir/and/name_of_venv}`. </li>
</ul>

<h2>Making use of virtualenv wrapper</h2>
<ul>
<li>Use `source [venv_name/bin/activate]` for mac and linux and `.\[venv_name/bin/[activate.ps1 or activate.bat]` for windows everytime you want to install new dependencies. The shell prompt or session name should change to reflect that you are using the python wrapper.</li>
<li>Your python distribution should come with pip python package manager installed. If not use curl to get the get-pip script and proceed to execute it with python via python get-pip.py.</li>
<li>Use `python[optional-MAJOR-VERSION] -m pip install [package-name[==optional_version]]` or  `python[optional-MAJOR-VERSION] -m pip install -r requirements.txt` to download the packages required by the project in one command.</li>
</ul>

<h2>Using shell plus</h2>
<ul>
<li>Install shell plus which comes with django and allows importation of models created as well as running tests. Use "pip install django-shell-plus" to install shell plus.</li>

<li>Once installed use either `$ django-admin {command} [options]` `$ manage.py {command} [options]` `$ python -m django {command} [options]` to perform django tasks.</li>
<li>For example you can create a file.json file to store data and then use " django admin file.json" to load the data in it as a fixture, that is as a serialized version of that database.</li>
</ul>
