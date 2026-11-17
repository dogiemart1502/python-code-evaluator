
# Python Code Evaluator

[![Python Tests](https://github.com/dogiemart1502/python-code-evaluator/actions/workflows/python-tests.yml/badge.svg)](https://github.com/dogiemart1502/python-code-evaluator/actions/workflows/python-tests.yml)

A lightweight Python project for evaluating function outputs against expected test cases.

This project demonstrates automated testing, debugging, result validation, and clear reporting—skills relevant to software engineering and AI coding evaluation.

## Features

- Evaluate Python functions against predefined test cases
- Compare actual and expected outputs
- Report passed and failed tests
- Capture exceptions without stopping the evaluation
- Handle empty test collections
- Run automated tests using pytest and GitHub Actions

## Technologies

- Python 3
- pytest
- GitHub Actions
- Python dataclasses

## Project Structure

- `evaluator.py` — Core evaluation logic and examples
- `test_evaluator.py` — Automated unit tests
- `.github/workflows/python-tests.yml` — CI workflow

## Getting Started

Clone the repository:

```bash
git clone https://github.com/dogiemart1502/python-code-evaluator.git
cd python-code-evaluator
```

Run the evaluator:

```bash
python evaluator.py
```

Install pytest and run the tests:

```bash
python -m pip install pytest
python -m pytest -v
```

## Test Coverage

The project includes tests for:

1. Correct solutions
2. Incorrect solutions
3. Exception handling
4. Empty test collections

All four tests passed in the GitHub Actions workflow.

## Current Limitations

This is a small demonstration project, not a secure sandbox for executing untrusted code. Only run functions and code you trust.

## Future Improvements

- Add support for structured evaluation reports
- Expand edge-case testing
- Add JSON report export
- Introduce configurable evaluation criteria

## Author

**Dogie Mar Taripe**

Software Engineer | Python | AI & LLM Evaluation

[GitHub](https://github.com/dogiemart1502) | [LinkedIn](https://www.linkedin.com/in/dogie-mar-taripe-35b309437)
