import pytest

from property_based_testing.internal import run_property_test, Success
from test_property_based_testing.code_to_test_with import square


def test_run_property_based_test_runs_tests_without_arguments() -> None:
    def property_test_that_1_squared_is_one() -> None:
        assert square(1) == 1

    assert run_property_test(property_test_that_1_squared_is_one) == Success()
