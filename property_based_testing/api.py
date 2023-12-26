from typing import TypeVar, Callable, TypeVarTuple

from property_based_testing.test_result import PropertyTestResult

T = TypeVar('T')
Ts = TypeVarTuple('Ts')


def inject(
    dependency_generator: Callable[[], T],
) -> Callable[[Callable[[T, *Ts], PropertyTestResult]], Callable[[*Ts], PropertyTestResult]]:
    def decorator(test: Callable[[T, *Ts], PropertyTestResult]) -> Callable[[*Ts], PropertyTestResult]:
        def curried_test(*remaining_dependencies: *Ts) -> PropertyTestResult:
            return test(dependency_generator(), *remaining_dependencies)
        return curried_test
    return decorator
