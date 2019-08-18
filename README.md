# Kaffa-test
A repository to do some chalanges to Kaffa Mobile

**Author**: Vinícius Viana dos Santos

**Objective**: Complete at least 2 of the exercises from the Kaffa- pre-qualification test (2019/2S) pdf. 

# Settings
## Install environment
To configure all the project its needed to create an environment and install all the required libraries.

To do this, first install `virtualenv` library with *pip*.

`sudo apt install python3-venv`

`python3 -m pip install --user virtualenv`

### Creating a virtual environment

Then, to create the environment, inside the _simple-todo_ directory run:

`python3 -m venv env`

### Activating a virtual environment

Finally, activate the environment. Execute:

`source env/bin/activate`

## Requirements
Once a virtual environment was created and activated, install all the libraries that the project require.

All the requirements are listed in the `requirements.txt` file.

To install all the requirements run: `pip install -r requirements.txt`

# Instruction to  exercises 1 and 2 - CNPJ validate

Run the following command: `python cnpj.py`

# Instructions to exercise 4 - Todo List

## Build a database

A model of a database was designed to use in this exercise. To build it, open the _Python interpreter_ and run:

```python
    >>> from app import db

    >>> db.create_all()

    >>> exit()
```

## Run

To execute the project, inside the _simple-todo_ directory, run the following command: `python app.py`

# Instructions to exercises 5 and 6 - REST client and server

Run the following command: `python rest.py`

# Instructions to exercises 7 - Entity Relationship Diagram - Simple Order Manager

The answer is available inside the Simple Order Manager pdf. 
