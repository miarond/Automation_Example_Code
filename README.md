[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/miarond/Automation_Example_Code)
# Automation Example Code

This repository contains a collection of example code in various formats which help demonstrate automation capabilities and API usage.
Each example project will be self-contained in a sub-directory inside this repository.  

## Preparation

Some projects may require the installation of externally available Packages from the Python Package Index (https://pypi.org) - in these 
cases, you will find a text file inside the sub-directory titled `requirements.txt`.  You can use this requirements file with the `pip`
command line program to install all of the necessary external packages, using a command similar to this:

```bash
pip install -r requirements.txt
```

Although it is not required, we highly recommend that you create a "Python Virtual Environment" first, before installing any of these
required packages.  Virtual Environments act like partitions that keep a project's dependencies (packages) separpate from the 
packages and other software installed globally on your system.  In this way, you can have multiple versions of the same package 
installed on your system without causing any conflicts.

To create a Virtual Environment, issue the follow commands (or similar, depending on your operating system):

```bash
cd <project_directory> (i.e. cd "./Timezone Converter")

python3 -m venv <virtual_environment_name> (i.e. python3 -m venv myvenv)

source <virtual_environment_name>/bin/activate (MacOS / Linux)
OR
<virtual_environment_name>\Scripts\activate.bat (Windows)
```

While the Virtual Environment is activated, you can run any `pip` or `python` commands and they will redirect to copies of the 
programs and packages that are stored in the new Virtual Environment sub-directory inside the project folder.

When you are finished with the project, deactivate your Virtual Environment by issuing the command `deactivate`.