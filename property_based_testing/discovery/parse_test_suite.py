from inspect import getmembers, isfunction
from types import ModuleType

from property_based_testing.internal import FullyInjectedPropertyTest


def parse_test_suite(module: ModuleType) -> list[FullyInjectedPropertyTest]:
    return [
        lambda: None
        for _ in getmembers(module, predicate=isfunction)
    ]
