## @file test_All.py
#  @author Shivam taneja
#  @brief Provides cases for the SeqADT.py, DCapALst.py and SALst.py
#  @date 11/02/2019

from StdntAllocTypes import *
from SeqADT import *
from DCapALst import *
from SALst import *
from pytest import *


## @brief A class required by "pytest" package to test cases
class TestSeqADt:

    def test_seq_next(self):
        val1 = SeqADT([10, 1])
        x = val1.next()
        assert x == 10

    def test_raises_stopiteration_seq_next(self):
        val2 = SeqADT([])
        with raises(StopIteration):
            val2.next()

    def test_seq_end_true(self):
        val1 = SeqADT([])
        x = val1.end()
        assert x == True

    def test_seq_end_false(self):
        val1 = SeqADT([10, 1239123, 9])
        x = val1.end()
        assert x == False


class TestDCapAlst:

    def test_dcapadd_none(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 20)
        x = DCapALst.capacity(DeptT.civil)
        assert x == 20

    def test_dcapadd_something(self):
        DCapALst.init()
        AALst.init()
        SALst.init()
        DCapALst.add(DeptT.civil, 10)

        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        SALst.add("stdnt2", sinfo2)

        SALst.allocate()

        x = DCapALst.capacity(DeptT.civil)

        assert x == 10

    def test_dcapadd_error(self):
        DCapALst.init()
        AALst.init()
        SALst.init()
        DCapALst.add(DeptT.civil, 20)
        DCapALst.add(DeptT.mechanical, 20)

        with raises(KeyError):
            DCapALst.add(DeptT.civil, 30)

    def test_dcapremove(self):
        DCapALst.init()
        AALst.init()
        SALst.init()
        DCapALst.add(DeptT.civil, 30)
        DCapALst.add(DeptT.engphys, 10)
        DCapALst.remove(DeptT.civil)
        with raises(KeyError):
            DCapALst.remove(DeptT.mechanical)

    def test_dcapeelm(self):
        DCapALst.init()
        AALst.init()
        SALst.init()
        DCapALst.add(DeptT.civil, 20)
        DCapALst.add(DeptT.mechanical, 20)
        assert DCapALst.elm(DeptT.civil)
    def test_dcapeelm1(self):
        DCapALst.init()
        AALst.init()
        SALst.init()
        DCapALst.add(DeptT.civil, 20)
        assert not DCapALst.elm(DeptT.engphys)

    def test_dcapcapacity(self):
        DCapALst.init()
        AALst.init()
        SALst.init()
        DCapALst.add(DeptT.civil, 1)
        DCapALst.add(DeptT.mechanical, 230)
        assert DCapALst.capacity(DeptT.mechanical) == 230

    def test_dcapcapacity1(self):
        DCapALst.init()
        AALst.init()
        SALst.init()
        DCapALst.add(DeptT.civil, 1)
        assert not DCapALst.capacity(DeptT.engphys)


class TestSALst:

    def test_saladd_empty1(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 1)
        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)

        SALst.add("stdnt2", sinfo2)
        AALst.init()
        SALst.allocate()
        x = (AALst.lst_alloc(DeptT.engphys))

        assert x == []

    def test_saladd_empty2(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 1)
        sinfo2 = SInfoT("first2", "last2", GenT.male, 3.0, SeqADT([DeptT.civil]), True)

        SALst.add("stdnt2", sinfo2)
        AALst.init()
        SALst.allocate()
        x = (AALst.lst_alloc(DeptT.civil))

        assert x == []

    def test_saladd(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)
        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)

        SALst.add("stdnt2", sinfo2)
        AALst.init()
        SALst.allocate()
        x = (AALst.lst_alloc(DeptT.civil))

        assert x == ["stdnt2"]

    def test_salremoveempty(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)
        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)

        SALst.add("stdnt2", sinfo2)
        SALst.remove("stdnt2")
        AALst.init()
        SALst.allocate()
        x = (AALst.lst_alloc(DeptT.civil))
        assert x == []

    def test_salremove1(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)
        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        sinfo1 = SInfoT("first1", "last1", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        SALst.add("stdnt2", sinfo2)
        SALst.add("stdnt1", sinfo1)

        SALst.remove("stdnt2")
        AALst.init()
        SALst.allocate()

        x = (AALst.lst_alloc(DeptT.civil))
        assert x == ["stdnt1"]

    def test_salremove_error(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)

        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        SALst.add("stdnt2", sinfo2)

        with raises(KeyError):
            SALst.remove("stdnt1")

    def test_salelm_true1(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)

        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        SALst.add("stdnt2", sinfo2)

        x = SALst.elm("stdnt2")
        assert x == True

    def test_salelm_true2(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)

        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        sinfo1 = SInfoT("first1", "last1", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)

        x = SALst.elm("stdnt2")
        assert x == True

    def test_salelm_false1(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)

        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        sinfo1 = SInfoT("first1", "last1", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)

        x = SALst.elm("stdnt3")
        assert x == False

    def test_salelm_false2(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)

        x = SALst.elm("stdnt1")
        assert x == False

    def test_salelm_false3(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)
        sinfo1 = SInfoT("first1", "last1", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        SALst.add("stdnt2", sinfo1)

        x = SALst.elm("stdnt1")
        assert x == False


    def test_salinfo1(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)

        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        sinfo1 = SInfoT("first1", "last1", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)

        x = SALst.info("stdnt2")
        #SeqADT creates an object with different pointer address on each run
        assert x is not None

    def test_salinfoerror1(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)

        sinfo2 = SInfoT("first2", "last2", GenT.male, 8.0, SeqADT([DeptT.civil]), True)
        SALst.add("stdnt2", sinfo2)
        with raises(KeyError):
            SALst.info("stdnt1")

    def test_salinfoError2(self):
        SALst.init()
        DCapALst.init()

        DCapALst.add(DeptT.civil, 20)

        with raises(KeyError):
            SALst.info("stdnt1")


    def test_salsort1(self):
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

        res = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        assert res == ['stdnt5', 'stdnt4', 'stdnt2']

    def test_salsort2(self):
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
        sinfo3 = SInfoT("first3", "last3", GenT.male, 3.9, SeqADT([DeptT.civil, DeptT.materials]), False)
        sinfo4 = SInfoT("first4", "last4", GenT.male, 5.0, SeqADT([DeptT.materials, DeptT.engphys]), True)
        sinfo5 = SInfoT("first5", "last5", GenT.male, 7.0, SeqADT([DeptT.engphys, DeptT.chemical]), True)

        SALst.init()
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        SALst.add("stdnt3", sinfo3)
        SALst.add("stdnt4", sinfo4)
        SALst.add("stdnt5", sinfo5)

        res = SALst.sort(lambda t: t.gender == GenT.male )
        assert res == ['stdnt5', 'stdnt4', 'stdnt2', 'stdnt3']

    def test_salaverage(self):
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
        sinfo3 = SInfoT("first3", "last3", GenT.male, 3.9, SeqADT([DeptT.civil, DeptT.materials]), False)
        sinfo4 = SInfoT("first4", "last4", GenT.male, 5.0, SeqADT([DeptT.materials, DeptT.engphys]), True)
        sinfo5 = SInfoT("first5", "last5", GenT.male, 7.0, SeqADT([DeptT.engphys, DeptT.chemical]), True)

        SALst.init()
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        SALst.add("stdnt3", sinfo3)
        SALst.add("stdnt4", sinfo4)
        SALst.add("stdnt5", sinfo5)

        res = SALst.average(lambda x: x.gender == GenT.male)
        assert res == 4.975


    def test_salaverage_error(self):
        SALst.init()
        DCapALst.init()
        DCapALst.add(DeptT.civil, 10)
        DCapALst.add(DeptT.software, 10)
        DCapALst.add(DeptT.mechanical, 10)
        DCapALst.add(DeptT.engphys, 10)
        DCapALst.add(DeptT.materials, 10)
        DCapALst.add(DeptT.electrical, 10)
        DCapALst.add(DeptT.chemical, 10)
        SALst.init()

        with raises(ValueError):
            SALst.average(lambda x: x.gpa > 6 and x.gender == GenT.male)


    def test_salallocate(self):
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
        sinfo3 = SInfoT("first3", "last3", GenT.male, 5.9, SeqADT([DeptT.civil, DeptT.materials]), True)
        sinfo4 = SInfoT("first4", "last4", GenT.male, 5.0, SeqADT([DeptT.materials, DeptT.engphys]), True)
        sinfo5 = SInfoT("first5", "last5", GenT.male, 7.0, SeqADT([DeptT.engphys, DeptT.chemical]), True)

        SALst.init()
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        SALst.add("stdnt3", sinfo3)
        SALst.add("stdnt4", sinfo4)
        SALst.add("stdnt5", sinfo5)
        SALst.allocate()
        assert AALst.lst_alloc(DeptT.civil) == ['stdnt3']

    def test_salallocate1(self):
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
        SALst.allocate()
        assert AALst.lst_alloc(DeptT.materials) == ['stdnt4', 'stdnt2']
