from property_based_testing.discovery.parse_test_suite import parse_test_suite
from test_property_based_testing.test_discovery import empty_test_suite


def test_parsing_suite_without_tests_succeeds() -> None:
    assert parse_test_suite(empty_test_suite) == []
