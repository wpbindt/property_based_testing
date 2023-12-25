from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Failure:
    pass


@dataclass(frozen=True)
class Success:
    pass


PropertyTestResult = Failure | Success


def run_property_test(
    property_test: Callable[[], None],
    iterations: int = 1,
) -> PropertyTestResult:
    for _ in range(iterations):
        try:
            property_test()
        except AssertionError:
            return Failure()

    return Success()
