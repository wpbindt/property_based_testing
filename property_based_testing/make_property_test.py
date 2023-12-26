from typing import Callable

from property_based_testing.dependency import Ts
from property_based_testing.test_result import PropertyTestResult, Failure, Success


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
