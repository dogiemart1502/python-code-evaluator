
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class TestCase:
    name: str
    inputs: tuple
    expected: Any


def evaluate_solution(
    solution: Callable,
    test_cases: list[TestCase],
) -> dict:
    """Evaluate a Python function against test cases."""
    results = []

    for case in test_cases:
        try:
            actual = solution(*case.inputs)
            passed = actual == case.expected

            results.append({
                "test": case.name,
                "passed": passed,
                "expected": case.expected,
                "actual": actual,
            })

        except Exception as error:
            results.append({
                "test": case.name,
                "passed": False,
                "expected": case.expected,
                "error": str(error),
            })

    passed_count = sum(
        result["passed"] for result in results
    )

    return {
        "total": len(test_cases),
        "passed": passed_count,
        "failed": len(test_cases) - passed_count,
        "results": results,
    }


def add_numbers(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    cases = [
        TestCase("Positive numbers", (2, 3), 5),
        TestCase("Negative numbers", (-2, -3), -5),
        TestCase("Zero", (0, 0), 0),
    ]

    report = evaluate_solution(add_numbers, cases)

    print("Python Code Evaluation Report")
    print(f"Passed: {report['passed']}/{report['total']}")

    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"{status}: {result['test']}")
