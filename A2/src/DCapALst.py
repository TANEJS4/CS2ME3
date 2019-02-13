## @file DCapALst.py
#  @author Shivam Taneja
#  @brief DCapALst
#  @date 01/02/2019
from StdntAllocTypes import *

## @brief An abstract data type that stores departments and it's capacity


class DCapALst:
    s = set()

    ## @brief init initial data structure
    def init():
        DCapALst.s = set()

    ## @brief add adds element to the set data structure
    #  @param d department name of DeptT
    #  @param n capacity of the corresponding department
    #  @exception throws KeyError if datatypes of n doesn't matches
    @staticmethod
    def add(d, n):
        for i in DCapALst.s:
            if d == i[0]:
                raise KeyError

        DCapALst.s.add((d, n))


    ## @brief remove deletes element from the set data structure
    #  @param d department name of DeptT
    #  @exception throws KeyError if department is not found
    @staticmethod
    def remove(d):
        flag = None
        for i in DCapALst.s:
            if i[0] == d:
                flag = i
        if not flag:
            raise KeyError
        else:
            DCapALst.s.remove(flag)

    ## @brief elm checks if the department exists in the set
    #  @param d department name of DeptT
    #  @return True if department exists else False
    @staticmethod
    def elm(d):
        for i in DCapALst.s:
            if i[0] == d:
                return True
        return False

    ## @brief capacity checks the department size
    #  @param d department name of DeptT
    #  @return number of seats available in department
    #  @exception throws KeyError if department is not found
    @staticmethod
    def capacity(d):
        try:
            for i in DCapALst.s:
                if d == i[0]:
                    return i[1]
        except:
            raise KeyError
