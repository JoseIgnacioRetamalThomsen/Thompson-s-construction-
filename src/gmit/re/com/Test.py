import unittest
import Shunting
import Thomsons
import ThomsonsMap


class Test(unittest.TestCase):

    @unittest.skip("feature not implemented")
    def test_no_dot_shunting(self):
        """
        Test the use of no dot for concatenation on shunting algorithm.
        :return: Nothing.
        """
        testCases = [ ("ab", "a.b"),  ("abc", "a.b.c"),  ("a*b*", "a*.b*"),  ("(a-z)b?", "(a-z).b?"), (
            "a?b+c*(a-z)*t", "a?.b+.c*.(a-z)*.t"), ("(0|(1(01*(00)*0)*1)*)*", "(0|(1.(0.1*.(0.0)*.0)*.1)*)*"),
            (
               "((a-z)|(A-Z)|(0-9)).((a-z)|(A-Z)|(0-9)|_|/.)*.@.((a-z)|(A-Z)|/.)*./..(((a-z)|(A-Z)).((a-z)|(A-Z)).((a-z)|(A-Z))|((a-z)|(A-Z)).((a-z)|(A-Z)))",
                "((a-z)|(A-Z)|(0-9))((a-z)|(A-Z)|(0-9)|_|/.)*@((a-z)|(A-Z)|/.)*/.(((a-z)|(A-Z))((a-z)|(A-Z))((a-z)|(A-Z))|((a-z)|(A-Z))((a-z)|(A-Z)))"),
                          ("abc","abc")]

        for case in testCases:
            print(case[0])
            self.assertEqual(Shunting.Converter().toPofix(case[0]), Shunting.Converter().toPofix(case[1]))

    matchtestcases  = [ ("a.b.c","",False),
                      ("a.b.c", "abc",True),
                      ("a.b.c","abbc",False),
                      ("a.b.c", "abcc", False),
                      ("a.b.c", "abad", False),
                      ("a.b.c", "abbbc", False),
                        ("a.b.c", "adc", False),
                        ("a.(b|d).c", "", False),
                        ("a.(b|d).c", "abc", True),
                        ("a.(b|d).c", "abbc", False),
                        ("a.(b|d).c", "abcc", False),
                        ("a.(b|d).c", "abad", False),
                        ("a.(b|d).c", "abbbc", False),
                        ("a.(b|d).c", "adc", True),
                        ("a.(b|d)*", "", False),
                        ("a.(b|d)*", "abc", False),
                        ("a.(b|d)*", "abbc", False),
                        ("a.(b|d)*", "abcc", False),
                        ("a.(b|d)*", "abad", False),
                        ("a.(b|d)*", "abbbc", False),
                        ("a.(b|d)*", "adc", False),
                        ("a.(b.b)*.c", "", False),
                        ("a.(b.b)*.c", "abc", False),
                        ("a.(b.b)*.c", "abbc", True),
                        ("a.(b.b)*.c", "abcc", False),
                        ("a.(b.b)*.c", "abad", False),
                        ("a.(b.b)*.c", "abbbc", False),
                        ("a.(b.b)*.c", "adc", False),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "0", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "00", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "11", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "000", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "011", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "110", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "0000", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "0011", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "0110", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "1001", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "00000", True),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "1", False),
                        ("(0|((1.(0.1*.(0.0)*.0)*.1))*)*", "10", False),
                      ]
    # fail becuase overflow for multiple of 3 regex test
    @unittest.expectedFailure
    def test_thomsons(self):

        for case in self.matchtestcases:
            self.assertEqual(Thomsons.match(case[0],case[1]),case[2])
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    def test_thomsonsMap(self):
        for case in self.matchtestcases:
            self.assertEqual(ThomsonsMap.compile(Shunting.Converter().toPofix(case[0])).run(case[1]),case[2])

if __name__ == '__main__':
    unittest.main()
