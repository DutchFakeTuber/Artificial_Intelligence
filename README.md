# Artificial_Intelligence
This project is for the minor Internet of Things (IoT) on Hanze UAS.
### The creators of this project are:
[DutchFakeTuber](https://github.com/DutchFakeTuber)\
[Emylvanderkooi](https://github.com/Emylvanderkooi)

### How to run the code:
First, it is recommended, or even necessary, to create a _Python virtual environment_. \
In this case, Microsoft Visual Studio Code is used as IDE. \
Firstly, check if you have Python 3.x on your machine.
> Python 3.7.5 and Python 3.9.0 were used in this case, both functioned perfectly fine.

Secondly, type the following in the terminal of your IDE (in this case VS Code)
```bash
py -m venv {name venv} #The name of the folder is up to you
```
If you are using VS Code, executing the virtual environment script can be tricky if the terminal is not allowed to run scripts. In order to tackle that problem, create a _.vscode_ folder in the project folder with a _settings.json_ file. In this file, enter the following:
```json
{
    // Setting for allowing to run scripts in the terminal
    "terminal.integrated.shellArgs.windows": ["-ExecutionPolicy", "Bypass"],
    // Path for the virtual environment of python (from the folder AI's perspective)
    "python.pythonPath": "{path to your virtual environment folder}" // Use '\\' instead of single '\'
}
```
Close the current terminal and open a new one. VS Code should give a message for allowing scripts, click the button for allowance. Now you should be in the Python virtual environment.

For running the Django API enter the following:
```bash
cd ./Django <ENTER>
py manage.py runserver <ENTER>
```
### This section of the AI is for the Django webserver;
It displays the survey made for the AI, \
Prints the generated results.

## Changes made to the project:
> v1.0: Uploaded to GitHub; _03-12-2020_ \
> v1.0.1: Changed project name from AI to Artificial Intelligence; _03-12-2020_ \
> v1.1: _Not yet posted_