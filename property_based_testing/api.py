from typing import TypeVar, Callable, TypeVarTuple

T = TypeVar('T')
Ts = TypeVarTuple('Ts')


def inject(
    dependency_generator: Callable[[], T],
) -> Callable[[Callable[[T, *Ts], None]], Callable[[*Ts], None]]:
    def decorator(test: Callable[[T, *Ts], None]) -> Callable[[*Ts], None]:
        def curried_test(*remaining_dependencies: *Ts) -> None:
            test(dependency_generator(), *remaining_dependencies)
        return curried_test
    return decorator
