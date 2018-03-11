from typing import List, Tuple
from .problem import Problem

import random


class AdditionProblem(Problem):
    def __init__(self):
        Problem.__init__(self)

    def __repr__(self):
        return str.format("Addition Problem ({}): {}", self.level, self.prompt)


def addition(level: int = 1, min_digits: int = 1, max_digits: int = 2) -> AdditionProblem:
    """Creates a new Addition Problem

    Keyword arguments:
        level -- the difficulty level of this problem.
            level 1: addition with no carry.
            level 2: addition with possibility of carry.
        min_digits -- the minimum number of digits in each operand.  value should be >= 1
        max_digits -- the maximum number of digits in each operand.  value should be >= 1
    """

    if level < 1 or level > 2:
        raise ValueError("addition problems must be level 1 or 2")

    if min_digits < 1 or max_digits < 1:
        raise ValueError("min and max digits must both be >= 1")

    if max_digits < min_digits:
        raise ValueError("max_digits must be >= min_digits")

    operand_size = random.randint(min_digits, max_digits)

    if level is 1:
        operand1, operand2 = _generate_operands_level_1(operand_size)
    else:
        operand1, operand2 = _generate_operands_level_2(operand_size)

    p = AdditionProblem()
    p.prompt = str.format("{} + {}", operand1, operand2)
    p.steps = _generate_steps(operand1, operand2)
    p.answer = str(operand1 + operand2)
    p.level = level

    return p


def _generate_operands_level_1(operand_size: int) -> Tuple[int, int]:
    """Generates two operands that will not require a carry when added together"""

    operand1: int = 0
    operand2: int = 0

    for i in range(operand_size):
        if i == operand_size - 1:
            digit1 = random.randint(1, 8)
            digit2 = random.randint(1, 9 - digit1)
        else:
            digit1 = random.randint(0, 9)
            digit2 = random.randint(0, 9 - digit1)

        operand1 += 10 ** i * digit1
        operand2 += 10 ** i * digit2

    return operand1, operand2


def _generate_operands_level_2(operand_size: int) -> Tuple[int, int]:
    """Generates two operands that may require a carry when added together"""

    operand1: int = 0
    operand2: int = 0

    for i in range(operand_size):
        if i == operand_size - 1:
            digit1 = random.randint(1, 9)
            digit2 = random.randint(1, 9)
        else:
            digit1 = random.randint(0, 9)
            digit2 = random.randint(0, 9)

        operand1 += 10 ** i * digit1
        operand2 += 10 ** i * digit2

    return operand1, operand2


def _generate_steps(operand1: int, operand2: int) -> List[str]:
    """Generates a sequence of steps that are needed to solve the problem"""

    return list(str("Add each column of digits one at a time"))

