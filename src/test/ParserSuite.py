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

    # Test valid variable declaration
    def test_var_dcl_1(self):
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_var_dcl_2(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_var_dcl_3(self):
        input = """Var: c, d = 6, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_var_dcl_4(self):
        input = """Var: c, d = 6.5e-3, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_var_dcl_5(self):
        input = """Var: c, d = False, e = True, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_var_dcl_6(self):
        input = """Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_var_dcl_7(self):
        input = """Var: m = "This is a \\t string", n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_var_dcl_8(self):
        input = """Var: a = 5;
        Var     : b=0.e3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_var_dcl_9(self):
        input = """Var: a = 5, b, c = 6;
        Var     : d=0.e3,   e = "string";
        Var : f = {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_var_dcl_10(self):
        input = """Var: a,b,c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    # Test invalid variable declaration
    def test_invalid_var_dcl_1(self):
        input = """: a = 5;"""
        expect = "Error on line 1 col 0: :"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_invalid_var_dcl_2(self):   # ???
        input = """b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = "Error on line 1 col 0: b"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_invalid_var_dcl_3(self):   # ???
        input = """Var: c, d = 6, e, f,"""
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_invalid_var_dcl_4(self):
        input = """Var: c, d = 6.5e-3; e, f;"""
        expect = "Error on line 1 col 20: e"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_invalid_var_dcl_5(self):
        input = """Var c, d = False, e = True, f;"""
        expect = "Error on line 1 col 4: c"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    # Test valid function declaration
    def test_valid_func_dcl_1(self):
        input = """
Function: main
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_valid_func_dcl_2(self):
        input = """
Function: main
    Parameter: n
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_valid_func_dcl_3(self):
        input = """
Function: main
    Parameter: a,b[5],  c[2][3][4]
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_valid_func_dcl_4(self):
        input = """
Function: main
    Body:
        Var : a = 1, b = 2;
        c = a + b;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_valid_func_dcl_5(self):
        input = """
Function: sum
    Body:
        Var : a = 1, b = 2;
        Var : c = 3;
        c = a + c;
        c = b + c;
        Return c;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    # Test invalid function declaration
    def test_invalid_func_dcl_1(self):  # ???
        input = """Function: main"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_invalid_func_dcl_2(self):
        input = """
Function: main
    Parameter:
    Body:
    EndBody."""
        expect = "Error on line 4 col 4: Body"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_invalid_func_dcl_3(self):
        input = """
Function: main
    Parameter: n = 5
    Body:
    EndBody."""
        expect = "Error on line 3 col 17: ="
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_invalid_func_dcl_4(self):
        input = """
Function: main
    Parameter: a, b; c
    Body:
    EndBody."""
        expect = "Error on line 3 col 19: ;"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_invalid_func_dcl_5(self):
        input = """
Function: sum
    Parameter: n
    Body:
        c = a + b;
        Var : d = 5;
        d = d + c;
    EndBody."""
        expect = "Error on line 6 col 8: Var"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    # Test valid assignment statement
    def test_valid_assign_stmt_1(self):
        input = """
Function: sum
    Body:
        a = b + c + 5;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_valid_assign_stmt_2(self):
        input = """
Function: sum
    Body:
        a = {{1,2}, {3,4}, {5,6}};
        a[1] = {4,3};
        a[0][1] = 1;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    
    def test_valid_assign_stmt_3(self):
        input = """
Function: sum
    Parameter: n
    Body:
        a = {{1,2}, {3,4}, {5,6}};
        a[x] = {4,3};
        a[x+y][x-y] = {1,2};
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    # Test invalid assignment statement
    def test_invalid_assign_stmt_1(self):
        input = """
Function: sum
    Parameter: n
    Body:
        a = {{1,2}, {3,4}, {5,6}};
        a[0,1] = 1;
    EndBody."""
        expect = "Error on line 6 col 11: ,"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_invalid_assign_stmt_2(self):
        input = """
Function: sum
    Parameter: n
    Body:
        a = {{1,2}, {3,4}, {5,6}};
        a[0] = a[1] = {1,2};
    EndBody."""
        expect = "Error on line 6 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,239))


    # Test full program
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

