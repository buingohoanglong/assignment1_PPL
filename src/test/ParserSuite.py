import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program_1(self):
        input = """Var: x;
Function: fact
    Parameter: n,  m
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1) *    m;
            EndIf.
        EndBody.
Function: main
    Body:
        x = 10;
        fact (x,   5);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    # no function declaration ???????????????
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """Var: x;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))