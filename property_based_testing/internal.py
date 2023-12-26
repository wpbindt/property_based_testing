from typing import Callable

from property_based_testing.api import Ts
from property_based_testing.test_result import Failure, Success, PropertyTestResult


def run_property_test(
    property_test: Callable[[], None],
    iterations: int = 1,
) -> PropertyTestResult:
    for _ in range(iterations):
        try:
            property_test()
        except AssertionError:
            return Failure()

    return Success()


def make_property_test(property_test: Callable[[*Ts], None]) -> Callable[[*Ts], PropertyTestResult]:
    def wrapped(*args: *Ts) -> PropertyTestResult:
        try:
            property_test(*args)
        except AssertionError:
            return Failure()
        return Success()
    return wrapped
