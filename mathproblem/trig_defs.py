from enum import Enum


class RightAngleTrigFunction(Enum):
    Sin = 1
    Cos = 2
    Tan = 3
    Sec = 4
    Csc = 5
    Cot = 6


class RightAngleTrigSide(Enum):
    Nil = 0
    Opposite = 1
    Adjacent = 2
    Hypotenuse = 3
