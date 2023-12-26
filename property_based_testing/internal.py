from typing import Callable

from property_based_testing.api import Ts
from property_based_testing.test_result import Failure, Success, PropertyTestResult


def run_property_test(
    property_test: Callable[[], PropertyTestResult],
    iterations: int = 1,
) -> PropertyTestResult:
    for _ in range(iterations):
        test_result = property_test()
        if isinstance(test_result, Failure):
            return test_result

    return Success()


def make_property_test(property_test: Callable[[*Ts], None]) -> Callable[[*Ts], PropertyTestResult]:
    def wrapped(*args: *Ts) -> PropertyTestResult:
        try:
            property_test(*args)
        except AssertionError as e:
            return Failure(message=get_message_from_assertion_error(e))
        return Success()
    return wrapped


def get_message_from_assertion_error(error: AssertionError) -> str | None:
    assertion_message_lines = error.args[0].split('\n')
    if len(assertion_message_lines) == 2:
        return None
    return assertion_message_lines[0]
