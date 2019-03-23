## @file SeqADt.py
#  @author Shivam Taneja
#  @brief SeqADt
#  @date 01/02/2019

## @brief An abstract data type that represents a sequence (in the set)


class SeqADT:

    i = 0

    ## @brief SeqADT constructor
    #  @details takes a sequence and initializes index
    #  @param x Sequence to be used
    def __init__(self, x):
        self.s = list(x)
        self.i = 0
    ## @brief start initializes the variable i which represents index

    def start(self):
        SeqADT.i = 0
    ## @brief next moves the index to the next by just incrementing
    #  @return the value of the index
    #  @exception StopIteration - if the index goes above the length of the sequence

    def next(self):
        if(self.i >= len(self.s)):
            raise StopIteration
        res = (self.s)[self.i]
        self.i = self.i + 1
        return res
    ## @brief end ends the iteration
    #  @return true or false, if the index is the last or if the index is
    #           not the last of the sequence, respectively

    def end(self):
        return self.i >= len(self.s)
