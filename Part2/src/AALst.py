## @file AALst.py
#  @author Shivam Taneja
#  @brief AALst
#  @date 01/02/2019

from StdntAllocTypes import *

## @brief An abstract data type that stores the allocated departments and students


class AALst:
    s = list()

    ## @brief init initial data structure
    @staticmethod
    def init():
        AALst.s = [(DeptT.materials, []), (DeptT.civil, []),
         (DeptT.chemical, []), (DeptT.electrical, []), (DeptT.mechanical, []),
          (DeptT.engphys, []), (DeptT.software, []), (DeptT.electrical, [])]


    ## @brief add_stdnt adds elements in the form of tuple to the set data structure
    #  @param dep department name of DeptT
    #  @param m list of all the macids in that department (string)
    @staticmethod
    def add_stdnt(dep, m):
        for i in AALst.s:
            if i[0] == dep:
                i[1].append(m)

    ## @brief lst_alloc provides with the list of macids in the department
    #  @param d department name of DeptT
    #  @return List of macids (string)
    @staticmethod
    def lst_alloc(d):
        for i in AALst.s:
            if i[0] == d:
                return i[1]

    ## @brief num_alloc provides with the number of allocated macids in the department
    #  @param d department name of DeptT
    #  @return  Number of allocated students (Natural number)
    @staticmethod
    def num_alloc(d):
        for i in AALst.s:
            if i[0] == d:
                return len(i[1])
