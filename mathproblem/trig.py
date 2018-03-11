import random

from typing import List, Tuple
from enum import Enum

from .problem import Problem
from.right_triangle_diagram import RightAngleDiagram, RightAngleThetaVertex


class RightAngleTrigFunction(Enum):
    Sin = 1
    Cos = 2
    Tan = 3
    Sec = 4
    Csc = 5
    Cot = 6


class RightAngleProblem(Problem):
    def __init__(self):
        Problem.__init__(self)

    def __repr__(self):
        return str.format("Right Angle Problem ({}): {}", self.level, self.prompt)


def _get_triple() -> Tuple[int, int, int]:
    a = random.randint(3, 15)  # a < 3 results in b = 0.  This is not a triangle

    if a % 2 == 0:
        b = ((a / 2) ** 2) - 1
        c = b + 2
    else:
        b = (a ** 2 - 1) / 2
        c = b + 1

    return a, b, c


def _get_steps(trig_func: RightAngleTrigFunction, adjacent: str, hypotenuse: str, opposite: str) -> List[str]:
    if trig_func == RightAngleTrigFunction.Sin:
        return [
            "Identify opposite side: {}.".format(opposite),
            "Identify hypotenuse: {}.".format(hypotenuse),
            "Divide opposite ({}) / hypotenuse ({}).".format(opposite, hypotenuse)
        ]
    elif trig_func == RightAngleTrigFunction.Cos:
        return [
            "Identify adjacent side: {}.".format(adjacent),
            "Identify hypotenuse: {}.".format(hypotenuse),
            "Divide adjacent ({}) / hypotenuse ({}).".format(adjacent, hypotenuse)
        ]
    elif trig_func == RightAngleTrigFunction.Tan:
        return [
            "Identify opposite side: {}.".format(opposite),
            "Identify adjacent side: {}.".format(adjacent),
            "Divide opposite ({}) / adjacent ({}).".format(opposite, adjacent)
        ]
    elif trig_func == RightAngleTrigFunction.Sec:
        return [
            "Identify hypotenuse: {}.".format(hypotenuse),
            "Identify adjacent side: {}.".format(adjacent),
            "Divide hypotenuse ({}) / adjacent ({}).".format(hypotenuse, adjacent)
        ]
    elif trig_func == RightAngleTrigFunction.Csc:
        return [
            "Identify hypotenuse: {}.".format(hypotenuse),
            "Identify opposite side: {}.".format(opposite),
            "Divide hypotenuse ({}) / adjacent ({}).".format(hypotenuse, opposite)
        ]
    elif trig_func == RightAngleTrigFunction.Cot:
        return [
            "Identify adjacent side: {}.".format(adjacent),
            "Identify opposite side: {}.".format(opposite),
            "Divide adjacent ({}) / opposite ({}).".format(adjacent, opposite)
        ]

    return []


def _get_answer(trig_func: RightAngleTrigFunction, adjacent: str, hypotenuse: str, opposite: str) -> str:
    if trig_func == RightAngleTrigFunction.Sin:
        return "{}/{}.".format(opposite, hypotenuse)
    elif trig_func == RightAngleTrigFunction.Cos:
        return "{}/{}.".format(adjacent, hypotenuse)
    elif trig_func == RightAngleTrigFunction.Tan:
        return "{}/{}.".format(opposite, adjacent)
    elif trig_func == RightAngleTrigFunction.Sec:
        return "{}/{}.".format(hypotenuse, adjacent)
    elif trig_func == RightAngleTrigFunction.Csc:
        return "{}/{}.".format(hypotenuse, opposite)
    elif trig_func == RightAngleTrigFunction.Cot:
        return "{}/{}.".format(adjacent, opposite)

    return ""


def right_angle(level: int = 1) -> RightAngleProblem:
    """Creates a new Right Angle Trigonometry Problem
        Keyword arguments:
        level -- the difficulty level of this problem.
            level 1: Right triangle measurements are a Pythagorean Triple
    """

    if level != 1:
        raise ValueError("right angle problems must be level 1")

    a, b, c = _get_triple()

    print(a, b, c)
    scale = 150.0
    min_side_length = 35.0

    a_value = max((a / c) * scale, min_side_length)
    b_value = max((b / c) * scale, min_side_length)

    if random.randint(0, 1) == 1:
        theta_vertex = RightAngleThetaVertex.VertexB
    else:
        theta_vertex = RightAngleThetaVertex.VertexC

    trig_function = RightAngleTrigFunction(random.randint(RightAngleTrigFunction.Sin.value, RightAngleTrigFunction.Cot.value))

    labels = str(a), str(b), str(c)

    problem_data = RightAngleDiagram(a_value, b_value, random.randint(0, 360), theta_vertex)
    problem_data.a_label = labels[0]
    problem_data.b_label = labels[1]
    problem_data.c_label = labels[2]
    problem_data.reposition()

    if theta_vertex == RightAngleThetaVertex.VertexB:
        adjacent = labels[0]
        hypotenuse = labels[2]
        opposite = labels[1]
    else:
        adjacent = labels[1]
        hypotenuse = labels[2]
        opposite = labels[0]

    p = RightAngleProblem()
    p.level = level
    p.prompt = "Find {} &theta;".format(trig_function.name)
    p.steps = _get_steps(trig_function, adjacent, hypotenuse, opposite)
    p.answer = _get_answer(trig_function, adjacent, hypotenuse, opposite)
    p.diagrams.append(problem_data.generate_diagram_svg())

    return p

