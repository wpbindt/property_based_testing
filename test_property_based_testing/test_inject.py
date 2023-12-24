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
