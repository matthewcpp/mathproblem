from .problem import Problem
from .trig_defs import RightAngleTrigFunction

from enum import Enum
from typing import List
import random


class TransformationType(Enum):
    VerticalTranslation = 1
    HorizontalTranslation = 2
    VerticalStretchCompression = 3
    HorizontalStretchCompression = 4


class GraphTransformProblem(Problem):
    def __init__(self):
        Problem.__init__(self)

    def __repr__(self):
        return str.format("Graph Transform Problem ({}): {}", self.level, self.prompt)


def _get_trig_func_text(trig_func: RightAngleTrigFunction) -> str:
    if trig_func == RightAngleTrigFunction.Sin:
        return "sin"
    else:
        return "cos"


class GraphTransformData:
    def __init__(self):
        self.trig_func: RightAngleTrigFunction = RightAngleTrigFunction.Sin
        self.hints: List[str] = []
        self.answer: str = ""

        self.vert_translation_mod: str = ""
        self.horiz_translation_mod: str = ""
        self.vert_stretch_mod: str = ""
        self.horiz_stretch_mod: str = ""

    def _append_to_answer(self, val: str):
        if len(self.answer) > 0:
            self.answer += ";"

        self.answer += val

    def add_horiz_translation(self):
        val = random.randint(0, 3)

        horiz_translation = "&pi;"
        if val > 1:
            horiz_translation = "{}{}".format(val, horiz_translation)

        if random.randint(0, 1) is 1:
            self.horiz_translation_mod = " + {}".format(horiz_translation)
            hint_text = horiz_translation
        else:
            self.horiz_translation_mod = " - {}".format(horiz_translation)
            hint_text = "-{}".format(horiz_translation)

        self.hints.append("Observe horizontal translation: {}".format(hint_text))
        self._append_to_answer("ht")

    def add_vertical_translation(self):
        val = random.randint(1, 3)

        if random.randint(0, 1) is 1:
            self.vert_translation_mod = " + {}".format(val)
            hint_text = val
        else:
            self.vert_translation_mod = " - {}".format(val)
            hint_text = "-{}".format(val)

        self.hints.append("Observe vertical translation: {}".format(hint_text))
        self._append_to_answer("vt")

    def add_vertical_stretch(self):
        val = random.randint(2, 5)

        if random.randint(0, 1) is 1:
            val *= -1

        self.vert_stretch_mod = str(val)
        self.hints.append("Observe vertical stretch: {}".format(self.vert_stretch_mod))
        self._append_to_answer("vs")

    def add_horiz_stretch(self):
        val = random.randint(2, 5)

        if random.randint(0, 1) is 1:
            val *= -1

        self.horiz_stretch_mod = str(val)
        self.hints.append("Observe horizontal stretch: {}".format(self.horiz_stretch_mod))
        self._append_to_answer("hs")

    def get_prompt(self):
        x = "x"

        if self.horiz_stretch_mod != "":
            x = "{}/{}".format(x, self.horiz_stretch_mod)

        if self.horiz_translation_mod != "":
            x = "{}{}".format(x, self.horiz_translation_mod)

        x = "{}({})".format(self.trig_func.name, x)

        if self.vert_stretch_mod != "":
            x = "{}{}".format(self.vert_stretch_mod, x)

        if self.vert_translation_mod != "":
            x = "{}{}".format(x, self.vert_translation_mod)

        return x


def generate_graph_transform_problem(level: int = 1):
    graph_data = GraphTransformData()
    graph_data.trig_func = RightAngleTrigFunction(random.randint(1, 2))

    # pick some random transforms to add to the graph
    transforms = list(range(4))
    random.shuffle(transforms)

    for i in range(level):
        xform = transforms.pop()

        if xform == 0 and graph_data.horiz_translation_mod is "":
            graph_data.add_horiz_stretch()
        elif xform == 1 and graph_data.horiz_stretch_mod is "":
            graph_data.add_horiz_translation()
        elif xform == 2:
            graph_data.add_horiz_stretch()
        else:
            graph_data.add_vertical_stretch()

    problem = GraphTransformProblem()
    problem.prompt = graph_data.get_prompt()
    problem.steps = graph_data.hints
    problem.level = level
    problem.answer = graph_data.answer

    return problem



