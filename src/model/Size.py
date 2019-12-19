from enum import unique, Enum


@unique
class Size(Enum):
    TINY = "TINY"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    HUGE = "HUGE"
    GARGANTUAN = "GARGANTUAN"
