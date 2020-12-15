# Artificial_Intelligence
This project is for the minor Internet of Things (IoT) on Hanze UAS.
### The creators of this project are:
[DutchFakeTuber](https://github.com/DutchFakeTuber)\
[Emylvanderkooi](https://github.com/Emylvanderkooi)

---
## Function for the code:
This portion of the AI Assignment is for making the calculations made by the AI visible with webpages. \
Firstly, the user can add extra data by filling in a survey that consists of twelve questions regarding _Mental Health in the Tech Industry_.
Then, the AI will calculate all data and the calculated data gets displayed by the Django API.

The dataset that has been used is the [Mental Health in the Tech Industry](https://www.kaggle.com/anth7310/mental-health-in-the-tech-industry)

---
## How to run the code:
First, it is recommended, or even necessary, to create a _Python virtual environment_. \
In this case, Microsoft Visual Studio Code is used as IDE. \
Firstly, check if you have Python 3.x on your machine.
> Python 3.7.5 and Python 3.9.0 were used in this case, both functioned perfectly fine.

Secondly, type the following line in the terminal of your IDE (in this case VS Code)
```bash
py -m venv {name venv} # The name of the folder is up to you
```
If you are using VS Code, executing the virtual environment script can be tricky if the terminal is not allowed to run scripts. In order to tackle that problem, create a _.vscode_ folder in the project folder with a _settings.json_ file. In this file, enter the following:
```json
{
    "_comment": "Setting for allowing to run scripts in the terminal",
    "terminal.integrated.shellArgs.windows": ["-ExecutionPolicy", "Bypass"],
    "_comment": "Path for the virtual environment of python (from the base folder's perspective). Use '\\'",
    "python.pythonPath": "{path to your virtual environment folder}"
}
```
Close the current terminal and open a new one. VS Code should give a message for allowing scripts, click the button for allowance. Now you should be in the Python virtual environment.

For running the Django API enter the following:
```bash
cd ./Django <ENTER>
py manage.py runserver <ENTER>
```
## Changes made to the project:
| Version | Date       | Comments                                                                                                                  |
| :-----: | :--------: | ------------------------------------------------------------------------------------------------------------------------- |
| v0.1    | 03-12-2020 | Uploaded to GitHub.                                                                                                       |
| v0.1.1  | 03-12-2020 | Changed project name from AI to Artificial_Intelligence.                                                                  |
| v0.2    | 04-12-2020 | Changed look of the User Interface. Added links to the sidebar for easy redirects. Also added comments to finished files. |
| v0.3    | 05-12-2020 | Updated the Main page and added some content for the results page.                                                        |
| v0.3.1  | 07-12-2020 | Made some significant changes to the Results page.                                                                        |
| v0.4    | 08-12-2020 | Added Machine Learning elements to the code.                                                                              |
| v0.5    | 10-12-2020 | Made the Recommendations page functional with a chart and graph                                                           |