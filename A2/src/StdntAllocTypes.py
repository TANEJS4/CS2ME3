## @file StdntAllocTypes.py
#  @author Shivam Taneja
#  @brief Creates custom datatypes
#  @date 01/02/2019
from SeqADT import *
from typing import NamedTuple
from enum import Enum

## @brief An abstract data type that represents gender


class GenT(Enum):

    male = 0
    female = 1

## @brief An abstract data type that represents department name


class DeptT(Enum):

    civil = 0
    chemical = 1
    electrical = 2
    mechanical = 3
    software = 4
    materials = 5
    engphys = 6

## @brief An abstract data type that represents all student info except macid


class SInfoT(NamedTuple):

    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT
    freechoice: bool
