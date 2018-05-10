# CSE 5359 - Semester Project: Address Book CLI

This is a semester project for Software Security (CSE 5359), wherein I've implemented a command line address book program. The overarching goal of this assignment is input validation: ensure that only those names and phone numbers that meet the desired specifications are entered into the database.

## Requirements

* `Python` — see [here](https://www.python.org/downloads/release/python-365/) for installation instructions
	* preferred version >= 3.6
	* may work with earlier versions, but this is untested
* `Pipenv` — see [here](https://github.com/pypa/pipenv) for installation instructions
* `SQLite` — see [here](https://www.sqlite.org/download.html) for installation instructions

## Getting started

Once requirements are installed, create the proper virtual environment with:

```bash
pipenv --three
```

Then, create a virtualenv shell with:

```bash
pipenv shell
```

Then, install dependencies with:

```bash
pipenv install
```

After this has completed, run the application with:

```bash
python main.py
```

...making sure to give a proper command line flag.

## Command Line Interface

Only one command may be entered at a time.

The commands are as follows:

* `-a "<person>" "<phone number>"`, `--add "<person>" "<phone number>"`
	* adds a listing to the address book 

* `-dp "<person>"`, `--delete-person "<person>"`
	* deletes a listing from the address book by name
	 
* `-dn "<phone number>"`, `--delete-number "<phone number>"`
	* deletes a listing from the address book by phone number 

* `-l`, `--list`
	* lists all listings in the database in tabular form

## Documentation

See the `doc/` directory for all documentation, including a [report](./doc/REPORT.md) describing the program's architecture, assumptions that have been made, as well as an evaluation as to the pros and cons of these design decisions.