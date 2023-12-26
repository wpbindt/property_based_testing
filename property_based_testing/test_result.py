from dataclasses import dataclass


@dataclass(frozen=True)
class Failure:
    pass


@dataclass(frozen=True)
class Success:
    pass


PropertyTestResult = Failure | Success
