# Task-CLI Project

A command-line interface (CLI) application written in Python for managing tasks stored in a JSON file.

## Overview

Task-CLI is a simple yet powerful command-line tool that helps you manage your tasks efficiently. It allows you to create, update, delete, and list tasks with different statuses, all stored in a local JSON file that is automatically generated.

## Features

- ✅ Create new tasks with descriptions

- 📝 Update existing task descriptions

- 🗑️ Delete tasks from your list

- 📋 List all tasks or filter by status

- 🏷️ Mark tasks with different statuses: "to-do", "in-process", and "done"

- 💾 Automatic JSON file storage

- 🧪 Comprehensive test coverage with pytest

## Installation

1. Ensure you have Python 3.6 or higher installed on your system

2. Clone or download this project to your local machine

3. Navigate to the project directory

## Usage

Run the application from the command line using the following syntax:
bash
```bash

    python app/task-cli.py [command] [arguments]

```

## Available Commands

- add "Your task description" - Add a new task

- list - List all tasks

- list-to-do - List tasks with a the status "to-do"

- list-done - List tasks with a the status "done"

- list-in-process - List tasks with a the status "in-process"

- update [task_id] "New description" - Update a task's description

- delete [task_id] - Delete a task

- mark-to-do [task_id] - Change a task's status to "to-do"

- mark-done [task_id] - Change a task's status to "done"

- mark-in-process [task_id] - Change a task's status to "in-process"

## Examples

```bash

# Add a new task
python app/task-cli.py add "Complete project documentation"

# List all tasks
python app/task-cli.py list

# List only tasks in process
python app/task-cli.py list-in-process

# Mark task 3 as done
python app/task-cli.py mark-done 3

# Update task 2's description
python app/task-cli.py update 2 "Review final draft"

# Delete task 5
python app/task-cli.py delete 5

```

## Project Structure

```text

task-cli-project/
├── app/
│   ├── task-cli.py          # Main CLI interface, handles command parsing
│   └── services.py          # Core logic for task management operations
├── tests/                   # Test suite for the application
│   └── test_services.py     # Unit tests for services.py functions
├── tasks.json               # Auto-generated task storage (created on first run)
└── README.md               # Project documentation

```

## File Details

- app/task-cli.py: The entry point of the application. Parses command line arguments using sys.argv and calls appropriate functions from services.py based on the provided flags and parameters.

- app/services.py: Contains all the business logic for task management:

    - Reading from and writing to the JSON file

    - Adding, updating, deleting, and listing tasks

    - Managing task status changes

    - Handling file operations and error checking

- tests/test_services.py: Comprehensive unit tests using pytest to verify all functionality in services.py works correctly.

## Technology Stack

- Python: Core programming language

- sys module: For command-line argument parsing

- json module: For data storage and retrieval

- pytest: Testing framework

## Development

### Running Tests

To run the test suite:

```bash

pytest tests/

```

### Adding New Features

- Add the core functionality to services.py

- Update the command parser in task-cli.py to handle new commands

- Add comprehensive tests in the tests/ directory

- Update this documentation to reflect new features

### License

This project is open source and available under the [MIT License](LICENSE).
