from .right_angle import gen_right_angle_problem, RightAngleProblem
from .graph_transforms import generate_graph_transform_problem, GraphTransformProblem


def right_angle(level: int = 1) -> RightAngleProblem:
    return gen_right_angle_problem(level)


def graph_transform(level: int = 1) -> GraphTransformProblem:
    return generate_graph_transform_problem(level)(level)