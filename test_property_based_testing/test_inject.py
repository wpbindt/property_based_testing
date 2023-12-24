from property_based_testing.api import inject
from property_based_testing.internal import run_property_test, Success, Failure
from test_property_based_testing.code_to_test_with import square


def test_run_property_based_test_runs_successful_tests_without_arguments() -> None:
    def property_test_that_1_squared_is_one() -> None:
        assert square(1) == 1

    assert run_property_test(property_test_that_1_squared_is_one) == Success()


def test_run_property_based_test_runs_unsuccessful_tests_without_arguments() -> None:
    def property_test_that_1_squared_is_19() -> None:
        assert square(1) == 19

    assert run_property_test(property_test_that_1_squared_is_19) == Failure()


def test_inject_actually_injects_arguments() -> None:
    def positive_integer() -> int:
        return 3

    @inject(positive_integer)
    def property_test_squares_are_nonnegative(a: int) -> None:
        assert square(a) >= 0

    assert run_property_test(property_test_squares_are_nonnegative) == Success()
