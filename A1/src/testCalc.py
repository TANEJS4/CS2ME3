## @file testCalc.py
#  @author Shivam taneja
#  @brief Provides cases for the CalcModule and ReadAllocationData
#  @date 17/01/2019

# @details for more documentation with package i used
#           https://docs.python-guide.org/writing/tests/

import unittest

import json
import CalcModule
import ReadAllocationData



## @brief A class required by "unittest" package to test cases

class testCase(unittest.TestCase):
## @brief ReadAllocationData - test

  ## @brief tests readStdnts function from ReadAllocationData.py

  #  @details uses provided json file to use get its own answer and checks for the output
  #           provided by readStdnts
  #  @exception is the outputs doesnt match, one error is added and whole test file fails
    def test_readStdnts(self):
        file = 'allstud.json'
        fh = open(file ,'r')

        res1 = json.load(fh)
        res2 = ReadAllocationData.readStdnts(file)
        self.assertEqual(res1, res2)

        fh.close()

 ## @brief tests readFreeChoice function from ReadAllocationData.py

 #  @details uses provided json file to use get its own answer and checks for the output
 #           provided by readFreeChoice
 #  @exception is the outputs doesnt match, one error is added and whole test file fails
    def test_readFreeChoice(self):
        file = 'freechoice.json'

        res1 = ['dog1', 'via1', 'gav', 'diiv', 'taneja', 'bdsfds']
        res2 = ReadAllocationData.readFreeChoice(file)
        self.assertEqual(res1, res2)

 ## @brief tests readDeptCapacity function from ReadAllocationData.py

 #  @details uses provided json file to use get its own answer and checks for the output
 #           provided by readDeptCapacity
 #  @exception is the outputs doesnt match, one error is added and whole test file fails
    def test_readDeptCapacity(self):
        file = 'department.json'

        res1 = {"civil": 20,"chemical": 30, "electrical": 40, "mechanical": 100, "software": 10, "materials": 100,"engphys": 40}

        res2 = ReadAllocationData.readDeptCapacity(file)

        self.assertEqual(res1, res2)

## @brief CalcModule - test

 ## @brief tests sort function from CalcModule.py

 #  @details uses provided json file to use get its own answer and checks for the output
 #           provided by CalcModule
 #  @exception is the outputs doesnt match, one error is added and whole test file fails

    def test_sort(self):
        requestedFile = [{'macid': 'via1', 'fname': 'cols', 'lname': 'Gas', 'gender': 'female', 'gpa': 9, 'dept': ['mechanical', 'engphys', 'software']}, {'macid': 'diiv', 'fname': 'dovija', 'lname': 'gupt', 'gender': 'female', 'gpa': 9, 'dept': ['software', 'mechanical', 'materials']}, {'macid': 'taneja', 'fname': 'shiva', 'lname': 'helloworld', 'gender': 'female', 'gpa': 9, 'dept': ['chemical', 'civil', 'electrical']}, {'macid': 'bdsfds', 'fname': 'hnfdgb', 'lname': 'vdsffs', 'gender': 'female', 'gpa': 9, 'dept': ['software', 'engphys', 'electrical']}, {'macid': 'gav', 'fname': 'ry', 'lname': 'chuk', 'gender': 'male', 'gpa': 6, 'dept': ['chemical', 'electrical', 'software']}, {'macid': 'dog1', 'fname': 'gie', 'lname': 'ge', 'gender': 'male', 'gpa': 5, 'dept': ['engphys', 'software', 'mechanical']}]

        res1 = CalcModule.sort(ReadAllocationData.readStdnts('allstud.json'))
        res2 = [{'macid': 'bdsfds', 'fname': 'hnfdgb', 'lname': 'vdsffs', 'gender': 'female', 'gpa': 9, 'dept': ['software', 'engphys', 'electrical']}, {'macid': 'taneja', 'fname': 'shiva', 'lname': 'helloworld', 'gender': 'female', 'gpa': 9, 'dept': ['chemical', 'civil', 'electrical']}, {'macid': 'diiv', 'fname': 'dovija', 'lname': 'gupt', 'gender': 'female', 'gpa': 9, 'dept': ['software', 'mechanical', 'materials']}, {'macid': 'via1', 'fname': 'cols', 'lname': 'Gas', 'gender': 'female', 'gpa': 9, 'dept': ['mechanical', 'engphys', 'software']}, {'macid': 'gav', 'fname': 'ry', 'lname': 'chuk', 'gender': 'male', 'gpa': 6, 'dept': ['chemical', 'electrical', 'software']}, {'macid': 'dog1', 'fname': 'gie', 'lname': 'ge', 'gender': 'male', 'gpa': 5, 'dept': ['engphys', 'software', 'mechanical']}]

        self.assertEqual(res1,res2)
 ## @brief tests average function from CalcModule.py

 #  @details uses provided json file to use get its own answer and checks for the output
 #           provided by CalcModule
 #  @exception is the outputs doesnt match, one error is added and whole test file fails

    def test_average(self):
        requestedFile = [{'macid': 'dog1', 'fname': 'gie', 'lname': 'ge', 'gender': 'male', 'gpa': 5, 'dept': [ 'engphys','software', 'mechanical']}, {'macid': 'via1', 'fname': 'cols', 'lname': 'Gas', 'gender': 'female', 'gpa': 9, 'dept': [ 'mechanical', 'engphys','software']}, {'macid': 'gav', 'fname': 'ry', 'lname': 'chuk', 'gender': 'male', 'gpa': 6, 'dept': [ 'chemical', 'electrical','software']}, {'macid': 'diiv', 'fname': 'dovija', 'lname': 'gupt', 'gender': 'female', 'gpa': 9, 'dept': [ 'software','mechanical', 'materials']}, {'macid': 'taneja', 'fname': 'shiva', 'lname': 'helloworld', 'gender': 'female', 'gpa': 9, 'dept': ['chemical','civil', 'electrical']}, {'macid': 'bdsfds', 'fname': 'hnfdgb', 'lname': 'vdsffs', 'gender': 'female', 'gpa': 9, 'dept': ['software', 'engphys', 'electrical']}]

        res1M = CalcModule.average(requestedFile,'male')
        res1F = CalcModule.average(requestedFile,'female')

        self.assertEqual(res1M,5.5)
        self.assertEqual(res1F,9)
 ## @brief tests allocate function from CalcModule.py

 #  @details uses provided json file to use get its own answer and checks for the output
 #           provided by CalcModule
 #  @exception is the outputs doesnt match, one error is added and whole test file fails

    def test_allocate(self):
        file1 = ReadAllocationData.readStdnts("allstud.json")
        file2 = ReadAllocationData.readFreeChoice("freechoice.json")
        file3 = ReadAllocationData.readDeptCapacity("department.json")

        res1 = {'civil': [], 'chemical': [{'macid': 'taneja', 'fname': 'shiva', 'lname': 'helloworld', 'gender': 'female', 'gpa': 9, 'dept': ['chemical', 'civil', 'electrical']}, {'macid': 'gav', 'fname': 'ry', 'lname': 'chuk', 'gender': 'male', 'gpa': 6, 'dept': ['chemical', 'electrical', 'software']}], 'electrical': [], 'mechanical': [{'macid': 'via1', 'fname': 'cols', 'lname': 'Gas', 'gender': 'female', 'gpa': 9, 'dept': ['mechanical', 'engphys', 'software']}], 'software': [{'macid': 'bdsfds', 'fname': 'hnfdgb', 'lname': 'vdsffs', 'gender': 'female', 'gpa': 9, 'dept': ['software', 'engphys', 'electrical']}, {'macid': 'diiv', 'fname': 'dovija', 'lname': 'gupt', 'gender': 'female', 'gpa': 9, 'dept': ['software', 'mechanical', 'materials']}], 'materials': [], 'engphys': [{'macid': 'dog1', 'fname': 'gie', 'lname': 'ge', 'gender': 'male', 'gpa': 5, 'dept': ['engphys', 'software', 'mechanical']}]}


        res2 = CalcModule.allocate(file1,file2,file3)

        self.assertEqual(res1,res2)

## @brief runs all the test cases
if __name__ == '__main__':
    unittest.main()
