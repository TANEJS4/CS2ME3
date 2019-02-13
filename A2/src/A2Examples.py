from StdntAllocTypes import *
from SeqADT import *
from DCapALst import *
from AALst import *
from SALst import *
SALst.init()
DCapALst.init()
DCapALst.add(DeptT.civil, 10)
DCapALst.add(DeptT.software, 10)
DCapALst.add(DeptT.mechanical, 10)
DCapALst.add(DeptT.engphys, 10)
DCapALst.add(DeptT.materials, 10)
DCapALst.add(DeptT.electrical, 10)
DCapALst.add(DeptT.chemical, 10)

sinfo2 = SInfoT("first2", "last2", GenT.male, 4.0, SeqADT([DeptT.materials, DeptT.civil]), True)
sinfo1 = SInfoT("first", "last", GenT.female, 2.0, SeqADT([DeptT.materials, DeptT.chemical]), True)
sinfo3 = SInfoT("first3", "last3", GenT.male, 3.9, SeqADT([DeptT.civil, DeptT.materials]), True)
sinfo4 = SInfoT("first4", "last4", GenT.male, 5.0, SeqADT([DeptT.materials, DeptT.engphys]), True)
sinfo5 = SInfoT("first5", "last5", GenT.male, 7.0, SeqADT([DeptT.engphys, DeptT.chemical]), True)

SALst.init()
SALst.add("stdnt1", sinfo1)
SALst.add("stdnt2", sinfo2)
SALst.add("stdnt3", sinfo3)
SALst.add("stdnt4", sinfo4)
SALst.add("stdnt5", sinfo5)


# print(SALst.elm("stdnt1"))
#
# print(SALst.sort(lambda t: t.gender == GenT.male ))
#
# print(SALst.average(lambda x: x.gender == GenT.male))

AALst.init()
SALst.allocate()
print(AALst.lst_alloc(DeptT.materials))
