# Contributing to Child Immunization Tracking System

Thank you for considering contributing to the Child Immunization Tracking System! Your help is greatly appreciated. Please follow the guidelines below to make the contribution process smooth and effective.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Features](#suggesting-features)
    - [Contributing Code](#contributing-code)
3. [Development Process](#development-process)
    - [Setting Up the Development Environment](#setting-up-the-development-environment)
    - [Running the Application](#running-the-application)
    - [Testing](#testing)
4. [Style Guides](#style-guides)
    - [Git Commit Messages](#git-commit-messages)
    - [Python Style Guide](#python-style-guide)
    - [Frontend Style Guide](#frontend-style-guide)
5. [License](#license)

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [email@example.com](mailto:email@example.com).

## How to Contribute

### Reporting Bugs

If you find a bug, please report it by creating an issue on the GitHub repository. When reporting a bug, please include:

- A clear and descriptive title.
- A detailed description of the issue.
- Steps to reproduce the bug.
- Any relevant logs, screenshots, or other supporting information.

### Suggesting Features

We welcome feature suggestions! To suggest a new feature, please open an issue on GitHub and include:

- A clear and descriptive title.
- A detailed description of the proposed feature.
- Any benefits or use cases for the feature.
- Examples or mockups, if applicable.

### Contributing Code

To contribute code, follow these steps:

1. Fork the repository.
2. Create a new branch from `main` for your feature or bug fix.
3. Make your changes in the new branch.
4. Ensure your code follows the style guides and passes all tests.
5. Commit your changes with a descriptive commit message.
6. Push your branch to your forked repository.
7. Open a Pull Request (PR) to the `main` branch of the original repository.
8. Ensure your PR description clearly explains the changes and references any related issues.

## Development Process

### Setting Up the Development Environment

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd child-immunization-tracking-system/backend
    ```

2. **Install dependencies**:
    ```bash
    pipenv install
    ```

3. **Set up environment variables**:
    Create a `.env` file in the `backend` directory with the following content:
    ```dotenv
    DATABASE_URL="mongodb://localhost:27017"
    MAIL_USERNAME="your_email@example.com"
    MAIL_PASSWORD="your_password"
    MAIL_FROM="your_email@example.com"
    MAIL_PORT=587
    MAIL_SERVER="smtp.example.com"
    MAIL_FROM_NAME="Example"
    ```

### Running the Application

To start the FastAPI application, run:
```bash
pipenv run uvicorn app.main:app --reload
```

### Testing

Run tests using pytest:
```bash
pipenv run pytest
```

## Style Guides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Limit the first line to 72 characters or less.
- Reference issues and pull requests when applicable.

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- Use type hints as much as possible.
- Run `black` to format your code:
    ```bash
    pipenv run black .
    ```

### Frontend Style Guide

- Use [ESLint](https://eslint.org/) for JavaScript linting.
- Follow the guidelines for [React](https://reactjs.org/docs/getting-started.html).
- Use a consistent CSS style; consider using [Prettier](https://prettier.io/) for formatting.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
