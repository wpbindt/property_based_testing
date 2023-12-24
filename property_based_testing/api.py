from typing import TypeVar, Callable

T = TypeVar('T')


def inject(
    dependency_generator: Callable[[], T ],
) -> Callable[[Callable[..., None]], Callable[..., None]]:
    def decorator(test: Callable[..., None]) -> Callable[..., None]:
        return lambda *args, **kwargs: test(dependency_generator(), *args, **kwargs)
    return decorator
