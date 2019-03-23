## @file ReadAllocationData.py
#  @author Shivam Taneja
#  @brief reads data from json files and return required results
#  @date 17/01/2019

import json

## @brief A function to return list of dictionaries
# @details uses the package "json" to output list of dictionaries from the json file
# @param s The filepath of concerned json file
# @return The list of dictionaries with students information
def readStdnts(s):
    with open(s,'r') as fh:
        x = json.load(fh)

    return x

## @brief A function to return list of students macid
# @details uses the package "json" to output list of strings(macid) from the json file
# @param s The filepath of concerned json file
# @return The list of strings with students with free choices
def readFreeChoice(s):
    with open(s,'r') as fh:
        x = json.load(fh)

    fh.close()
    return x

        # for everyDic in x:
        #     curValue = everyDic.get("gpa")
        #     print(type(curValue))
        #     if (curValue >= 4.0 and curValue <= 12.0):
        #         lst.append(everyDic['macid'])

## @brief A function to return dictionary of dept with the number of seats available
# @details uses the package "json" to output dictionary from the json file
# @param s The filepath of concerned json file
# @return The dictionary with department names as keys and number of available
def readDeptCapacity(s):
    # choice = { 'civil' : 0 , 'chemical' : 0 , 'electrical' : 0, 'mechanical' :0 , 'software' : 0, 'materials' : 0, 'engphys' :0 }
    with open(s,'r') as fh:
        x = json.load(fh)
        # for i in x:
        #     which3 = i['dept']
        #     for x in choice:
        #         for j in range(3):
        #             if (x == which3[j]):
        #                 choice[x] = choice[x] + 1
    fh.close()
    return x
