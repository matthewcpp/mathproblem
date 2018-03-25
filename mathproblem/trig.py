from .right_angle import gen_right_angle_problem, RightAngleProblem


def right_angle(level: int = 1) -> RightAngleProblem:
    return gen_right_angle_problem(level)
