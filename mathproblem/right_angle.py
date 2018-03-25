import random

from typing import List, Tuple

from .problem import Problem
from.right_triangle_diagram import RightAngleDiagram, RightAngleThetaVertex
from .trig_defs import RightAngleTrigFunction, RightAngleTrigSide

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

    return int(a), int(b), int(c)


def _get_steps_level1(trig_func: RightAngleTrigFunction, adjacent: str, hypotenuse: str, opposite: str) -> List[str]:
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


def _get_steps_level2(trig_func: RightAngleTrigFunction, missing_side: RightAngleTrigSide,
                      adjacent: str, hypotenuse: str, opposite: str) ->List[str]:

    level1_steps = _get_steps_level1(trig_func, adjacent, hypotenuse, opposite)

    if _side_needed(trig_func, missing_side):
        steps: List[str] = []

        if missing_side == RightAngleTrigSide.Hypotenuse:
            steps.append("Calculate missing hypotenuse side: C&sup2; = {}&sup2; + {}&sup2;.".format(opposite, adjacent))
        elif missing_side == RightAngleTrigSide.Opposite:
            steps.append("Calculate missing opposite side: {}&sup2 = A&sup2; + {}&sup2;.".format(hypotenuse, adjacent))
        else:
            steps.append("Calculate missing adjacent side: {}&sup2 = {}&sup2; + B&sup2;.".format(hypotenuse, opposite))

        return steps + level1_steps
    else:
        return level1_steps


def _get_answer(trig_func: RightAngleTrigFunction, adjacent: str, hypotenuse: str, opposite: str) -> str:
    if trig_func == RightAngleTrigFunction.Sin:
        return "{}/{}".format(opposite, hypotenuse)
    elif trig_func == RightAngleTrigFunction.Cos:
        return "{}/{}".format(adjacent, hypotenuse)
    elif trig_func == RightAngleTrigFunction.Tan:
        return "{}/{}".format(opposite, adjacent)
    elif trig_func == RightAngleTrigFunction.Sec:
        return "{}/{}".format(hypotenuse, adjacent)
    elif trig_func == RightAngleTrigFunction.Csc:
        return "{}/{}".format(hypotenuse, opposite)
    elif trig_func == RightAngleTrigFunction.Cot:
        return "{}/{}".format(adjacent, opposite)

    return ""


def _side_needed(trig_func: RightAngleTrigFunction, triangle_side: RightAngleTrigSide) -> bool:
    if trig_func == RightAngleTrigFunction.Sin:
        return triangle_side != RightAngleTrigSide.Adjacent
    elif trig_func == RightAngleTrigFunction.Cos:
        return triangle_side != RightAngleTrigSide.Opposite
    elif trig_func == RightAngleTrigFunction.Tan:
        return triangle_side != RightAngleTrigSide.Hypotenuse
    elif trig_func == RightAngleTrigFunction.Sec:
        return triangle_side != RightAngleTrigSide.Opposite
    elif trig_func == RightAngleTrigFunction.Csc:
        return triangle_side != RightAngleTrigSide.Adjacent
    elif trig_func == RightAngleTrigFunction.Cot:
        return triangle_side != RightAngleTrigSide.Hypotenuse

    return False


def gen_right_angle_problem(level: int = 1) -> RightAngleProblem:
    """Creates a new Right Angle Trigonometry Problem
        Keyword arguments:
        level -- the difficulty level of this problem.
            level 1: Right triangle measurements are a Pythagorean Triple
            Level 2: Hypotenuse value not given
            Level 3: Random side value not given
    """

    if level < 1 or level > 3:
        raise ValueError("right angle problems must be level 1 - 3")

    a, b, c = _get_triple()

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

    if level == 1:
        missing_side = RightAngleTrigSide.Nil
    elif level == 2:
        missing_side = RightAngleTrigSide.Hypotenuse
    else:
        missing_side = RightAngleTrigSide(random.randint(RightAngleTrigSide.Opposite.value, RightAngleTrigSide.Hypotenuse.value))

    if missing_side == RightAngleTrigSide.Hypotenuse:
        problem_data.c_label = None
    elif theta_vertex == RightAngleThetaVertex.VertexB:
        if missing_side == RightAngleTrigSide.Adjacent:
            problem_data.a_label = None
        elif missing_side == RightAngleTrigSide.Opposite:
            problem_data.b_label = None
    elif theta_vertex == RightAngleThetaVertex.VertexC:
        if missing_side == RightAngleTrigSide.Adjacent:
            problem_data.b_label = None
        elif missing_side == RightAngleTrigSide.Opposite:
            problem_data.a_label = None

    p = RightAngleProblem()
    p.level = level
    p.prompt = "Find {} &theta;".format(trig_function.name)
    p.answer = _get_answer(trig_function, adjacent, hypotenuse, opposite)
    p.diagram = problem_data.generate_diagram_svg()

    if level == 1:
        p.steps = _get_steps_level1(trig_function, adjacent, hypotenuse, opposite)
    else:
        p.steps = _get_steps_level2(trig_function, missing_side, adjacent, hypotenuse, opposite)

    return p

