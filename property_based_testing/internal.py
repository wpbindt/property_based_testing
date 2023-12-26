from typing import Callable

from property_based_testing.make_property_test import make_property_test
from property_based_testing.test_result import Failure, Success, PropertyTestResult

FullyInjectedPropertyTest = Callable[[], None]


def run_test_suite(
    test_suite: list[FullyInjectedPropertyTest],
    iterations: int = 1,
) -> list[PropertyTestResult]:
    if len(test_suite) == 0:
        return []
    return [run_property_test(
        next(iter(test_suite)),
        iterations=iterations
    )]


def run_property_test(
    property_test: FullyInjectedPropertyTest,
    iterations: int = 1,
) -> PropertyTestResult:
    actual_property_test = make_property_test(property_test)
    for _ in range(iterations):
        test_result = actual_property_test()
        if isinstance(test_result, Failure):
            return test_result

    return Success()
