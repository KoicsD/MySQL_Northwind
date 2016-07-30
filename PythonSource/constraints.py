__author__ = 'KoicsD'
from abc import ABCMeta


class ConstraintWarning(Warning):
    pass


class SingleFieldConstraint(metaclass=ABCMeta):
    pass


class NotNull(SingleFieldConstraint):
    pass


class Max(SingleFieldConstraint):
    def __init__(self, value, equality_allowed):
        self.value = value
        self.equality_allowed = equality_allowed


class Min(SingleFieldConstraint):
    def __init__(self, value, equality_allowed: bool):
        self.value = value
        self.equality_allowed = equality_allowed


class Size(SingleFieldConstraint):
    def __init__(self, value: int):
        self.value = value
