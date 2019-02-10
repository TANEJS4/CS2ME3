## @file CalcModule.py
#  @author Shivam Taneja
#  @brief Calculates and provide required results based on the output from ReadAllocationData
#  @date 17/01/2019


## @brief a function to sort list
# @details The function sorts in descending order on "gpa"
# @param S The unordered list of dictionaries
# @return sorted list of dictionaries using 2 inbuilt functions
def sort(S):
    newS = sorted(S, key=lambda k: k['gpa'])
    newS.reverse()
    return newS

## @brief a function to get the average of male/female 's GPA
# @details The function uses the for loop to check if the string matches
#           and adds the gpa and increment variable "tot" so as to perform
#           average algorithm correctly
# @param L The list of dictionaries
# @param g The string input -> "male" or "female"
# @return average of gender's gpa
def average(L,g):
    tot = 0
    avgB = 0
    for i in L:
        if(i['gender'] == g):
            avgB +=i['gpa']
            tot +=1
    average = avgB/tot
    return average

## @brief a function to allocate student to a dept
# @details The function allocate student to a dept based on their gpa
#           and their preferenece
#           function also gives preferenece to students with free choice
#           The function also makes sure dept in not over filled
# @param S The list of dictionaries
# @param F The list of "macid" of students with free choice
# @param C The dictionary of each dept and their seats available
# @return list of dictionaries where key is the dept and values
#           are the dictionaries of students alloted the dept
def allocate(S,F,C):
    newS = sorted(S, key=lambda k: k['gpa'])
    newS.reverse()

    resDict = { 'civil' : [] , 'chemical' : [] , 'electrical' : [], 'mechanical' :[] , 'software' : [], 'materials' : [], 'engphys' :[] }
    for everyDic in newS: #newS is the list of dic and i in every dic
        if everyDic['macid'] in F:
            stream = everyDic['dept'][0]
            for allStreams in resDict:
                if (stream == allStreams):
                    resDict[stream].append(everyDic) #all free choice
                    C[stream] -=1

        elif everyDic['macid'] not in F and everyDic['gpa'] > 4.0:
            for checkLength in resDict:
                for iterate in range(3):
                    stream = everyDic['dept'][iterate]
                    if (len(resDict[checkLength]) < C[checkLength]):
                        resDict[stream].append(everyDic)
                        C[stream] -=1
                        break
    return resDict
