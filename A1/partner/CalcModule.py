## @file CalcModule.py
#  @author Rohit Saily
#  @brief Module used to process student and department data.
#  @date 2019-01-18

from a1_constants import MIN_GPA, MAX_GPA, MIN_PASSING_GPA, GENDERS
from a1_utility import remove_duplicates

""" Helper Functions """
## @brief Allocates a student to their topmost available choice if they have a passing gpa, defined in a1_constants.py.
#  @details If a student cannot be allocated to any of their choices, they simply are not allocated. If their choice is not found in allocations or spots_available, it is ignored.
#  @param student The student to be allocated to a department, represented by a dictionary that maps data categories to data.
#  @param allocations A dictionary that maps a department to a list of student dictionaries already allocated.
#  @param spots_available A dictionary that maps a department to the number of students that can be allocated to it.
def allocate_topmost_available_choice(student, allocations, spots_available):
    if not (MIN_PASSING_GPA <= student['gpa'] <= MAX_GPA):
        return #Do not allocate the student, they are not passing or have an invalid GPA
    for choice in student['choices']:
        if 0 < spots_available[choice]:
            try:
                allocations[choice].append(student)
            except KeyError:
                continue #The choice is not allocateable, continue to try the next one
            else:
                try:
                    spots_available[choice] -= 1
                except KeyError:
                    allocations[choice].remove(student) #We cannot gurantee the department exists with space, so we cannot allocate the student without it being in the spots_available dictionary
                    continue
                else:
                    return

""" API """
## @brief Sorts students by descending GPA.
#  @details
#       Each student is represented by a dictionary that maps data categories to data.
#       This function does not mutate the original list.
#       Sorts using Tim Sort via Python's sorted function.
#  @param S The list of students represented by dictionaries that map data categories to corresponding data.
#  @return The list of dictionaries representing students organized by descending GPA.
def sort(S):
    if S == []:
        return S
    return sorted(S, key=lambda student: student['gpa'], reverse=True)

## @brief Averages the GPA of students, filtered by gender.
#  @details Any student found to have a gpa below the minimum or above the maximum, each defined in a1_constants.py, will be ignored in the computation.
#  @param L The list of students, each represented by dictionaries that map data categories to data.
#  @param g The gender to filter by, case insensitive.
#  @return None if no students were found to average otherwise it is the average computed.
def average(L, g):
    if not L:
        return None
    gpas = []
    for student in L:
        if not (MIN_GPA <= student['gpa'] <= MAX_GPA):
            continue
        try:
            if student['gender'] == g.lower():
                gpas.append(student['gpa'])
        except KeyError:
            continue
        else:
            pass
    try:
        average = sum(gpas) / len(gpas)
    except ZeroDivisionError:
        return None #There where no values to average hence there is no average
    else:
        return average

## @brief Allocates students to departments based on code defined allocation scheme.
#  @details
#       The code defined allocation scheme is as follows:
#           1. Free choice students are allocated before students without free choice.
#           2. Students with higher GPAs are allocated first.
#           3. Students with failing GPAs or GPAs above the maximum are not allocated.
#           4. Students who cannot fit into any of departments they chose are not allocated to any department.
#  @param S The list of students represented by dictionaries that map data categories to corresponding data.
#  @param F The list of mac ids of students who have free choice.
#  @param C A dictionary that maps department names to their capacity.
#  @return A dictionary mapping departments to a list of students allocated to that department.
def allocate(S, F, C):
    if not C:
        return {} #No allocations can be made without departments!
    allocations = {}
    spots_available = {department:capacity for department, capacity in C.items()}
    for department in spots_available:
        allocations[department] = []
    if not S:
        return allocations #No students to allocate
    students = []
    students.extend(sort(S))
    remove_duplicates(students) #To prevent accidentally allocating a student twice if they are defined multiple times in the list.
    free_choice_students = []
    for student in students:
        if student['macid'] in F:
            free_choice_students.append(student)
            students.remove(student)
    non_free_choice_students = students #Just to 'rename' the variable and increase code readability since students now holds only students without free choice.
    for student in free_choice_students:
        allocate_topmost_available_choice(student, allocations, spots_available)
    for student in non_free_choice_students:
        allocate_topmost_available_choice(student, allocations, spots_available)
    return allocations
