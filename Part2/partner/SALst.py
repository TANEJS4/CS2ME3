## @file SALst.py
#  @author Orlando Ortega 
#  @brief SALst
#  @date  2/11/19
from StdntAllocTypes import *
from AALst import *
from DCapALst import *
from typing import NamedTuple

## @brief An abstract data type for students
#  @details Stores a tuple with first index being the macid of a student, and the second being the
#  information of the student of type SInfoT
class StudentT(NamedTuple):
  macid: str
  info: SInfoT

## @brief Local Method for GPA
#  @details Returns the GPA of a given student
#  @param m Student's macid
#  @param s Student's info of type SInfoT
#  @return The student's gpa
def get_gpa(m,s: SInfoT):
  return s.gpa

## @brief An abstract data type for associating students
#  @details Associates student's macid with their student info, it is also able to sort, find the average and allocate these students
#  into their programs of choice
class SALst:

  s = []

## @brief Constructor for SALst
#  @details Initializes an empty list
  @staticmethod
  def init():
    SALst.s = []  

## @brief Adds students to a list
#  @details Takes in the macid and information of a student and appends them to a list in the form of a tuple of type
#  StudentT
#  @param m Student's macid
#  @param i Student's info of type SInfoT
#  @exception Throws KeyError if the student is already in the list
  @staticmethod
  def add(m: str, i: SInfoT):
    for item in SALst.s:
      if m == item.macid:
        raise KeyError


    SALst.s.append(StudentT(m, i))

## @brief Removes students from the list
#  @details Takes in the macid of a student and removes them from the list
#  @param m Student's macid
#  @exception Throws KeyError if the student is not already in the list
  @staticmethod
  def remove(m: str):
    #keeps track of elements that have been iterated
    counter = len(SALst.s)

    #iterate through list
    for item in SALst.s:
      #if student was found remove them
      if m == item.macid:
        SALst.s.remove(item)
      else:
        counter -= 1
    
    #if the counter = 0, it means that all elements of the list have been viewed, therefore the student is not on the list
    if counter == 0:
      raise KeyError

## @brief Checks if the student is in the list
#  @details Takes in the macid of a student and checks if they are in the student list
#  @param m Student's macid
#  @return Boolean value of whether the student is in the list
  @staticmethod
  def elm(m: str):
    for item in SALst.s:
      if m == item.macid:
        return True
      
    return False

## @brief Returns a student's information
#  @details Takes in the macid of a student and returns their information
#  @param m Student's macid
#  @exception Throws KeyError if student is not in the list
#  @return Student information
  @staticmethod
  def info(m: str):
  #keeps track of elements that have been iterated
   counter = len(SALst.s)

  #iterate through list
   for item in SALst.s:
     #if student was found remove them
     if m == item.macid:
       return item.info
     else:
       counter -= 1

   #if the counter = 0, it means that all elements of the list have been viewed, therefore the student is not on the list
   if counter == 0:
     raise KeyError

## @brief Returns a sorted list of students
#  @details Takes in a function and finds the students that satisfy it, once those students are found it returns a list
#  of those students in descending gpa order. Furthermore, the algorithm used to sort is insertion sort, of which geeksforgeeks
#  and the textbook Algorithms were consulted for advice
#  @param f Function that takes in as a parameter SInfoT and returns a boolean
#  @return Sorted student list
  @staticmethod
  def sort(f):
    sorted_studentT_list = []
    finished_list = []

    #appends students that satisfy the function condition into a temporary list
    for item in SALst.s:
      if (f(item.info)):
        sorted_studentT_list.append(item)
    
    # Iterate through every element on the list starting from the second position
    for i in range(1, len(sorted_studentT_list)): 
  
      key = sorted_studentT_list[i] 

      # Move those students with a higher gpa closer to the start of the array to achieve a descending GPA order
      j = i-1
      while j >= 0 and get_gpa(key.macid,key.info) > get_gpa(sorted_studentT_list[j].macid,sorted_studentT_list[j].info) : 
        #exchanges both elements if the gpa if the gpa of the second element is higher than that of the first element
        sorted_studentT_list[j+1] = sorted_studentT_list[j] 
        j -= 1

      sorted_studentT_list[j+1] = key 

    #appends the macid's of the sorted students, into a temporary list(this list is therefore sorted)
    for item in sorted_studentT_list:
      finished_list.append(item.macid)

    return finished_list

## @brief Returns the average gpa of students
#  @details Takes in a function and finds the students that satisfy it, once those students are found it returns the
#  average GPA of those students
#  @exception Throws ValueError if there are no students that satisfy the function requirement
#  @param f Function that takes in as a parameter SInfoT and returns a boolean
#  @return Students' average gpa
  @staticmethod
  def average(f):
    counter = 0
    total = 0
    average = 0

    #counts and adds each of the student's gpa that satisfy the function
    for item in SALst.s:
      if(f(item.info)):
        total += item.info.gpa
        counter += 1
    
    #if there were students that satisfied the requirement return their average gpa
    if(counter == 0):
      raise ValueError
    else:
      average = total/counter
      return average

## @brief Allocates students into their respective choices
#  @details First sorts students that are in the freechoice list and proceeds to allocate those first 
#  (in order of GPA, highest to lowest), it then proceeds to those students that aren't and conducts
#  the exact same procedure
#  @exception Throws RuntimeError if a student could not be placed into any program of their choice
  @staticmethod
  def allocate():

    AALst.init()

    #allocates students that are in the freechoice list and have a gpa higher than 4 into their program choices
    F = SALst.sort((lambda t: t.freechoice and t.gpa >= 4.0))
    for m in F:
      ch = SALst.info(m).choices
      AALst.add_stdnt(ch.next(), m)
    
    #allocates students that are not in the freechoice list and have a gpa higher than 4 into their program choices
    S = SALst.sort(lambda t: not(t.freechoice) and t.gpa >= 4.0)
    for m in S:
      ch = SALst.info(m).choices

      #checks for the next choice if their top choice is out of capacity in order to priority
      alloc = False
      while(not(alloc) and not(ch.end())):
        d = ch.next()
        if(AALst.num_alloc(d) < DCapALst.capacity(d)):
          AALst.add_stdnt(d, m)
          alloc = True
      
      #if a student could not be allocated an error is raised
      if(not(alloc)):
        raise RuntimeError

  
      



  