## @file DCapALst.py
#  @author Orlando Ortega 
#  @brief Controls Departments and their Capacities
#  @date  2/11/19

from StdntAllocTypes import *

## @brief An abstract data type that represents a Department and their Capacity, List
class DCapALst:

  s = {}
## @brief Constructs DCapALst object
#  @details takes in no arguments, and initiates an empty dictionary
  @staticmethod
  def init():
    DCapALst.s = {}

## @brief Adds departments and their capacities to the dictionary
#  @details Adds departments as keys, and their capacities as their values to the dictionary
#  @param d Department of type DeptT
#  @param n Current department capacity
#  @exception KeyError Throws error when department is already in the dictionary
  @staticmethod
  def add(d: DeptT, n: int):
    if(d in DCapALst.s):
      raise KeyError

    DCapALst.s[d] = n

## @brief Removes departments and their capacities from the dictionary
#  @details Removes departments and their capacities from the dictionary
#  @param d Department of type DeptT
#  @exception KeyError Throws error when department is not in the dictionary
  @staticmethod
  def remove(d: DeptT):
    if(d not in DCapALst.s):
      raise KeyError
    
    del DCapALst.s[d]

## @brief Checks to see if department is in the dictionary
#  @details Checks for department in dictionary and returns a boolean value
#  @param d Department of type DeptT
#  @return Returns boolean depending on whether the department is in the dictionary
  @staticmethod
  def elm(d: DeptT):
    return d in DCapALst.s

## @brief Displays Capacity
#  @details Receives department and returns it's capacity
#  @param d Department of type DeptT
#  @exception KeyError Throws error when department is not in the dictionary
  @staticmethod
  def capacity(d: DeptT):
    if(d not in DCapALst.s):
      raise KeyError
    
    return DCapALst.s[d]
      

