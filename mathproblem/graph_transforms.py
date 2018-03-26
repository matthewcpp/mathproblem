from .problem import Problem
from .trig_defs import RightAngleTrigFunction

from enum import Enum

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
    trig_func: RightAngleTrigFunction = RightAngleTrigFunction.Sin

    vert_translation_mod: str = ""
    horiz_translation_mod: str = ""
    vert_stretch_mod: str = ""
    horiz_stretch_mod: str = ""

    def add_horiz_translation(self):
        val = random.randint(0, 3)

        horiz_translation = "&pi;"
        if val is not 0:
            horiz_translation = "{}{}".format(val, horiz_translation)

        if random.randint(0, 1) is 1:
            horiz_translation = " + {}".format(horiz_translation)
        else:
            horiz_translation = " - {}".format(horiz_translation)

        self.horiz_translation_mod = horiz_translation

    def add_vertical_translation(self):
        val = random.randint(1, 3)

        if random.randint(0, 1) is 1:
            self.vert_translation_mod = " + {}".format(val)
        else:
            self.vert_translation_mod = " - {}".format(val)

    def add_vertal_stretch(self):
        val = random.randint(2, 5)

        if random.randint(0, 1) is 1:
            val *= -1

        self.vert_stretch_mod = str(val)

    def add_horiz_stretch(self):
        val = random.randint(2, 5)

        if random.randint(0, 1) is 1:
            val *= -1

        self.horiz_stretch_mod = str(val)

    def get_prompt(self):
        p = "x"

        if self.horiz_translation_mod is not "":
            p += self.horiz_translation_mod
        if self.horiz_stretch_mod is not "":
            p = "({} / {}) ".format(p, self.horiz_stretch_mod)

        p = _get_trig_func_text(self.trig_func) + p

        p = self.vert_stretch_mod + p
        p += self.vert_translation_mod



def generate_graph_transform_problem(level: int = 1):
    graph_data = GraphTransformData()
    graph_data.trig_func = RightAngleTrigFunction(random.randint(0, 1))

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
            graph_data.add_vertal_stretch()





