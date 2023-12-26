from property_based_testing.api import inject
from property_based_testing.internal import run_property_test, Success, Failure, make_property_test
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


def test_run_property_test_does_multiple_iterations() -> None:
    integers_to_return = [3, 2, 2]

    def positive_integer() -> int:
        return integers_to_return.pop()

    @inject(positive_integer)
    def property_test_all_squares_are_4(a: int) -> None:
        assert square(a) == 4

    test_result = run_property_test(
        property_test=property_test_all_squares_are_4,
        iterations=3,
    )
    assert test_result == Failure()


def test_make_property_test_turns_assertion_errors_into_failures() -> None:
    @make_property_test
    def property_test_failing_test() -> None:
        assert False

    assert property_test_failing_test() == Failure()
