
import pytest

from evaluator import TestCase, evaluate_solution


def test_correct_solution():
    """Check that correct answers pass."""
    cases = [
        TestCase("Positive", (2, 3), 5),
        TestCase("Negative", (-2, -3), -5),
        TestCase("Zero", (0, 0), 0),
    ]

    report = evaluate_solution(lambda a, b: a + b, cases)

    assert report["total"] == 3
    assert report["passed"] == 3
    assert report["failed"] == 0


def test_incorrect_solution():
    """Check that incorrect answers fail."""
    cases = [
        TestCase("Addition", (2, 3), 5),
    ]

    report = evaluate_solution(lambda a, b: a - b, cases)

    assert report["failed"] == 1
    assert report["results"][0]["passed"] is False


def test_exception_handling():
    """Check that runtime errors are recorded."""
    def divide(a, b):
        return a / b

    cases = [
        TestCase("Division by zero", (10, 0), None),
    ]

    report = evaluate_solution(divide, cases)

    assert report["failed"] == 1
    assert "error" in report["results"][0]


def test_empty_cases():
    """Check that an empty test list is handled."""
    report = evaluate_solution(lambda x: x, [])

    assert report["total"] == 0
    assert report["passed"] == 0
    assert report["failed"] == 0
