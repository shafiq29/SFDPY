# SFDPY
## _Simple Salesforce Object and Field Creator, Using Python_

This is a simple implementation of python simple salesforce library to deploy salesforce custom fields and objects to desired instance for example sandbox

## Requirements

- This process is highly discouraged in production env
- We need to elevate permission as shown in the snapshot
- Need a Connected App in Salesforce

## Features

- Read provided credentials
- Login to SalesForce Instance
- Create Custom Objects
- Create Custom Fieldsf

## Installation

SFDPY requires [simple-salesforce](https://github.com/simple-salesforce/simple-salesforce)

Install the dependencies and devDependencies and start the server.

```sh
cd project_dir
pip install simple_salesforce
```

#### Building for source

For production release:

```sh
just run the python main.py file
```


