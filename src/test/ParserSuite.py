import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # Predefined testcases
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    # Test program
    def test_simple_program_1(self):
        input = """Var: x;
Function: fact
    Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody.
Function: main
    Body:
        x = 10;
        fact (x);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_simple_program_2(self):
        input = """Var: x[5] = {1,2,3,4,5};
Function: sum
    Parameter: x[5]
        Body:
            Var: sum = 0;
            For (i = 0 , i < 5, 1) Do
                sum = sum + i;
            EndFor.
            Return sum;
        EndBody.
Function: main
    Body:
        sum(x);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_simple_program_3(self):
        input = """
Function: radius
    Parameter: x,       y
        Body:
            Var: radius;
            radius = sqrt(x*x + y*y);
            Return radius;
        EndBody.
Function: main
    Body:
        Var : x = 3, y = 4;
        radius(x,   y);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_simple_program_4(self):
        input = """
Function: radius
    Parameter: x,       y
        Body:
            Var: radius;
            radius = sqrt(x*.x +. y*.y);
            Return radius;
        EndBody.
Function: main
    Body:
        Var : x = 3.5e0, y = 4.6e-0;
        radius(x,   y);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_simple_program_5(self):
        input = """Var: string_list[4] = {"","","","",""};
Function: get_string_list
    Parameter: list[4]
        Body:
            Var : str_input = "";
            For (i = 0 , i < 4, 1) Do
                str_input = read();
                list[i] = str_input;
            EndFor.
            Return list;
        EndBody.
Function: print_string_list
    Parameter: list[4]
        Body:
            For (i = 0 , i < 4, 1) Do
                printStrLn(list[i]);
            EndFor.
        EndBody.
Function: main
    Body:
        print_string_list(string_list);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

#     def test_simple_program_2(self):
#         input = """Var: x[5] = {1,2,3,4,5};
# Function: sum
#     Parameter: x[5]
#         Body:
#             Var: sum = 0;
#             For (i = 0 , i < 5, 1) Do
#                 sum = sum + i;
#             EndFor.
#             Return sum;
#         EndBody.
# Function: main
#     Body:
#         sum(x);
#     EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,204))

#     def test_simple_program_2(self):
#         input = """Var: x[5] = {1,2,3,4,5};
# Function: sum
#     Parameter: x[5]
#         Body:
#             Var: sum = 0;
#             For (i = 0 , i < 5, 1) Do
#                 sum = sum + i;
#             EndFor.
#             Return sum;
#         EndBody.
# Function: main
#     Body:
#         sum(x);
#     EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,204))

#     def test_simple_program_2(self):
#         input = """Var: x[5] = {1,2,3,4,5};
# Function: sum
#     Parameter: x[5]
#         Body:
#             Var: sum = 0;
#             For (i = 0 , i < 5, 1) Do
#                 sum = sum + i;
#             EndFor.
#             Return sum;
#         EndBody.
# Function: main
#     Body:
#         sum(x);
#     EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,204))

#     def test_simple_program_2(self):
#         input = """Var: x[5] = {1,2,3,4,5};
# Function: sum
#     Parameter: x[5]
#         Body:
#             Var: sum = 0;
#             For (i = 0 , i < 5, 1) Do
#                 sum = sum + i;
#             EndFor.
#             Return sum;
#         EndBody.
# Function: main
#     Body:
#         sum(x);
#     EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,204))

#     def test_simple_program_2(self):
#         input = """Var: x[5] = {1,2,3,4,5};
# Function: sum
#     Parameter: x[5]
#         Body:
#             Var: sum = 0;
#             For (i = 0 , i < 5, 1) Do
#                 sum = sum + i;
#             EndFor.
#             Return sum;
#         EndBody.
# Function: main
#     Body:
#         sum(x);
#     EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,204))

