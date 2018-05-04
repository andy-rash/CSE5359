# CSE 5359 - Semester Project: Telephone Listing CLI

This is a semester project for Software Security (CSE 5359), wherein I've implemented a command line telephone listing program. The overarching goal of this assignment is input validation: ensure that only those names and phone numbers that meet the desired specifications are entered into the database.

## Requirements

* `Python` — see [here](https://www.python.org/downloads/release/python-365/) for installation instructions
	* must be version >= 3.6 	
* `Pipenv` — see [here](https://github.com/pypa/pipenv) for installation instructions
* `SQLite` — see [here](https://www.sqlite.org/download.html) for installation instructions

## Getting started

Once requirements are installed, create the proper virtual environment with

```bash
pipenv --three
```

Then install dependencies with

```bash
pipenv install
```

After this has completed, run the application with

```bash
(SemesterProject-FlrlsoRi) python address_book.py
```