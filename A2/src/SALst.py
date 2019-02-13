## @file SALst.py
#  @author Shivam Taneja
#  @brief SALst
#  @date 01/02/2019

from StdntAllocTypes import *
from AALst import *
from DCapALst import *

## @brief An abstract data type that stores student information


class SALst:

    s = set()
    ## @brief init initial data structure

    def init():
        SALst.s = set()

    ## @brief add adds the tuple of macid and student info in the set
    #  @param m MacId of the student (string)
    #  @param i information of the student(SInfoT)
    #  @exception throws KeyError if input i is not of the SInfoT type

    @staticmethod
    def add(m, i):
        if isinstance(i, SInfoT):
            SALst.s.add(tuple((m, i)))
        else:
            raise KeyError

    ## @brief remove deletes the tuple of macid and student info from the set
    #  @param m MacId of the student (string)
    #  @exception throws KeyError if input m is not found in the set
    @staticmethod
    def remove(m):
        mac = None
        for i in SALst.s:
            if i[0] == m:
                mac = i
        if not mac:
            raise KeyError
        else:
            SALst.s.remove(mac)

    ## @brief elm checks if the input string is in the data structure
    #  @param m MacId of the student (string)
    #  @return true if MacId is found else False
    @staticmethod
    def elm(m):
        for i in SALst.s:
            if i[0] == m:
                return True
        return False

    ## @brief info gives information about input from the data structure
    #  @param m MacId of the student (string)
    #  @return information of the student (SInfoT)
    @staticmethod
    def info(m):
        for i in SALst.s:
            if m == i[0]:
                return i[1]
        raise KeyError

    ## @brief sort sorts the data structure
    #  @details it uses inbuilt sorted function to sort Data structure
    #            based on their gpa and the lambda function
    #  @param f lambda function expresssion
    #  @return the data structure sorted according to the parameter
    @staticmethod
    def sort(f):
        pre = []
        res = []
        for i in SALst.s:
            if f(i[1]):
                pre.append(i)
        sort = sorted(pre, key=lambda x: x[1].gpa)
        for i in sort:
            res.append(i[0])
        return list(reversed(res))

    ## @brief average gives the requested average
    #  @param f lambda function expresssion
    #  @details Gets the average of GPA only of those sets who matches
    #           with the lambda expresssion
    #  @return average of the gpa (Numeric)
    @staticmethod
    def average(f):
        try:
            count = 0
            add = 0
            if SALst.s is None:
                raise ValueError
            for i in SALst.s:
                if f(i[1]):
                    count += 1
                    add += i[1].gpa
            res = add / count
            return res
        except:
            raise ValueError

    ## @brief allocate allot students based on the provided conditions
    #  @details Sorts the data structure (condtion->gpa more than or equal to the 4)
    #           starts alloting students with free choice as priority then
    #           students without freechoice. The limit of alloting is decided by
    #            the department capacity
    #  @exception Throws RuntimeError
    @staticmethod
    def allocate():
        AALst.init()
        f = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in f:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)
        s = SALst.sort(lambda t: not (t.freechoice) and t.gpa >= 4.0)
        for m in s:
            ch = SALst.info(m).choices
            alloc = False
            while not alloc and not ch.end():
                d = ch.next()
                if (AALst.num_alloc(d) < DCapALst.capacity(d)):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not alloc:
                raise RuntimeError

    @staticmethod
    def get_gpa(m, s):
        for i in s:
            if m == i[0]:
                # print(i.gpa)
                return i.gpa
