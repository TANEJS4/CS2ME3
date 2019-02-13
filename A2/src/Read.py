## @file Read.py
#  @author Shivam Taneja
#  @brief functions for retrieving data from file
#  @date 01/02

from StdntAllocTypes import *
from DCapALst import *
from SALst import *
import re


## @brief load_stdnt_data reads in data from a file, storing it in SALst
#  @param s the name of the file to be read
def load_stdnt_data(s):
    with open(s, 'r') as infile:
        contents = infile.readlines()

    fname = []
    lname = []
    macids = []
    gpalist = []
    genderl = []
    freechoicel = []
    dept = []

    other = [x.strip().split(',') for x in contents]

    department = [re.findall("\[(.*?)\]", x) for x in contents]
    for i in range(len(other)):
        department[i] = [x.strip().split(', ') for x in department[i]]

    for i in range(len(department)):
        temp = department[i][0]
        dept.append(temp)

    for i in range(len(other)):
        length = len(other[i]) - 1
        count = 5
        for j in reversed(range(count, length)):
            other[i].pop(j)

    for i in range(len(other)):
        temp = other[i][1].replace(' ', '')
        fname.append(temp)

    for i in range(len(other)):
        temp = other[i][2].replace(' ', '')
        lname.append(temp)

    for i in other:
        macids.append(i[0])

    for i in range(len(other)):
        temp = other[i][4].replace(' ', '')
        gpalist.append(float(temp))

    for i in range(len(other)):
        temp = other[i][3].replace(' ', '')
        if temp == 'male':
            genderl.append(GenT.male)
        else:
            genderl.append(GenT.female)

    for i in range(len(other)):
        temp = other[i][-1].replace(' ', '')
        if temp == "True":
            freechoicel.append(True)
        else:
            freechoicel.append(False)

    for i in range(len(other)):
        length = len(other[i])
        for j in range(length):
            (other[i][j]).replace('', '')

    for i in range(len(other)):
        indexofdept = department[i]
        other[i].insert(4, indexofdept)

    for i in range(len(other)):
        for index, item in enumerate(dept[i]):
            if item == "civil":
                dept[i][index] = DeptT.civil
            if item == "chemical":
                dept[i][index] = DeptT.chemical
            if item == "electrical":
                dept[i][index] = DeptT.electrical
            if item == "mechanical":
                dept[i][index] = DeptT.mechanical
            if item == "software":
                dept[i][index] = DeptT.software
            if item == "engphys":
                dept[i][index] = DeptT.engphys
            if item == "materials":
                dept[i][index] = DeptT.materials

    SALst.init()

    for i in range(len(other)):
        sinfo = SInfoT(fname[i], lname[i], genderl[i],
            gpalist[i], SeqADT(dept[i]), freechoicel[i])
        SALst.add(macids[i], sinfo)


## @brief load_dcap_data reads in data from a file, storing it in DCapALst
#  @param s the name of the file to be read
def load_dcap_data(s):
    with open(s, 'r') as infile:
        contents = infile.readlines()
    other = [x.strip().split(', ') for x in contents]

    for i in range(len(other)):
        if other[i][0] == "civil":
            other[i][0] = DeptT.civil
        if other[i][0] == "chemical":
            other[i][0] = DeptT.chemical
        if other[i][0] == "electrical":
            other[i][0] = DeptT.electrical
        if other[i][0] == "mechanical":
            other[i][0] = DeptT.mechanical
        if other[i][0] == "software":
            other[i][0] = DeptT.software
        if other[i][0] == "engphys":
            other[i][0] = DeptT.engphys
        if other[i][0] == "materials":
            other[i][0] = DeptT.materials

    for i in range(len(other)):
        other[i].append(float(other[i][1]))
        other[i].pop(1)

    DCapALst.init()
    for i in range(len(other)):
        DCapALst.add(other[i][0], other[i][1])
