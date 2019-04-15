## @file SeqADT.py
#  @author Orlando Ortega 
#  @brief A program takes in a sequence, and its able to iterate through it
#  @date  2/11/19

## @brief SeqADT Abstract Data type which is able to iterate through a sequence
class SeqADT:

  s = []
  i = 0

## @brief Constructs SeqADT
#  @details Assigns the array into variable s, which in this case is a sequence of T, furthermore it also initializes
#  i which acts as the index of the sequence
#  @param self The instance of the object itself
#  @param s The sequence to be iterated over
  def __init__(self, x):
    self.s = x
    self.i = 0

## @brief Restarts index
#  @details Assigns i the value of 0, in order to restart the iteration of the sequence back to the first element
#  @param self The instance of the object itself

  def start(self):
    self.i = 0
  
## @brief Iterates to the next element of the sequence
#  @details It returns the current element of the sequence while also increasing the index to get ready for the next element
#  @exception Throws a StopITeration error if index is outside the range of the sequence
#  @param self The instance of the object itself
#  @return The value at the current index of i in the Object's sequence
  def next(self):
    if (self.i >= len(self.s)):
      raise StopIteration
    currentIndex = self.i
    self.i += 1
    return self.s[currentIndex]

## @brief Checks for end of sequence
#  @details Checks the current index of the sequence to see if it is out of range, therefore concluding that the iteration has
#  ended
#  @param self The instance of the object itself
#  @return true if the current index is outside the length of the sequence, otherwise false.
  def end(self):
    return self.i >= len(self.s)

