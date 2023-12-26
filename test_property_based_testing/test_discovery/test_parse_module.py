from property_based_testing.discovery.parse_test_suite import parse_test_suite
from test_property_based_testing.test_discovery import empty_test_suite, property_test_suite_with_one_test


def test_parsing_suite_without_tests_succeeds() -> None:
    assert parse_test_suite(empty_test_suite) == []


def test_parsing_suite_with_one_test_finds_one_test() -> None:
    assert len(parse_test_suite(property_test_suite_with_one_test)) == 1
