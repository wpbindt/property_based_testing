from inspect import getmembers, isfunction
from types import ModuleType
from typing import Any

from property_based_testing.internal import FullyInjectedPropertyTest


def parse_test_suite(module: ModuleType) -> list[FullyInjectedPropertyTest]:
    return [
        lambda: None
        for name, value in getmembers(module)
        if is_property_test((name, value))
    ]


def is_property_test(module_member: tuple[str, Any]) -> bool:
    name, value = module_member
    return isfunction(value) and name.startswith('property_test')
