import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    # Test normal identifier
    def test_normal_identifier1(self):
        self.assertTrue(TestLexer.checkLexeme("aBc", "aBc,<EOF>",1))

    def test_normal_identifier2(self):
        self.assertTrue(TestLexer.checkLexeme("a1c", "a1c,<EOF>",2))

    def test_normal_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("a_c", "a_c,<EOF>",3))

    def test_normal_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("a", "a,<EOF>",4))

    def test_normal_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>",5))

    # Test invalid identifier   ?????????
    def test_invalid_identifier1(self):
        self.assertTrue(TestLexer.checkLexeme("Abc", "Error Token A",6))

    def test_invalid_identifier2(self):
        self.assertTrue(TestLexer.checkLexeme("_bc", "Error Token _",7))     

    def test_invalid_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("9bc", "9,bc,<EOF>",8))     

    def test_invalid_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("a:bc", "a,:,bc,<EOF>",9))     

    def test_invalid_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("ABC", "Error Token A",10))    

    # Test normal integer literal
    def test_normal_int_literal1(self):
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>",11))  

    def test_normal_int_literal2(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>",12))  

    def test_normal_int_literal3(self):
        self.assertTrue(TestLexer.checkLexeme("0x123", "0x123,<EOF>",13))  

    def test_normal_int_literal4(self):
        self.assertTrue(TestLexer.checkLexeme("0xDEF", "0xDEF,<EOF>",14))  

    def test_normal_int_literal5(self):
        self.assertTrue(TestLexer.checkLexeme("0X123", "0X123,<EOF>",15))  

    def test_normal_int_literal6(self):
        self.assertTrue(TestLexer.checkLexeme("0XDEF", "0XDEF,<EOF>",16))  

    def test_normal_int_literal7(self):
        self.assertTrue(TestLexer.checkLexeme("0o123", "0o123,<EOF>",17))  

    def test_normal_int_literal8(self):
        self.assertTrue(TestLexer.checkLexeme("0o567", "0o567,<EOF>",18))  

    def test_normal_int_literal9(self):
        self.assertTrue(TestLexer.checkLexeme("0O123", "0O123,<EOF>",19))  

    def test_normal_int_literal10(self):
        self.assertTrue(TestLexer.checkLexeme("0O567", "0O567,<EOF>",20))  

    # Test invalid integer literal
    def test_invalid_int_literal1(self):
        self.assertTrue(TestLexer.checkLexeme("0123", "0,123,<EOF>",21))  

    def test_invalid_int_literal2(self):
        self.assertTrue(TestLexer.checkLexeme("00123", "0,0,123,<EOF>",22))  

    def test_invalid_int_literal3(self):
        self.assertTrue(TestLexer.checkLexeme("1A2", "1,Error Token A",23))  

    def test_invalid_int_literal4(self):
        self.assertTrue(TestLexer.checkLexeme("12A", "12,Error Token A",24))  

    def test_invalid_int_literal5(self):
        self.assertTrue(TestLexer.checkLexeme("0x0123", "0,x0123,<EOF>",25))  

    def test_invalid_int_literal6(self):
        self.assertTrue(TestLexer.checkLexeme("0XAGB", "0XA,Error Token G",26))  

    def test_invalid_int_literal7(self):
        self.assertTrue(TestLexer.checkLexeme("0XABG", "0XAB,Error Token G",27))  

    def test_invalid_int_literal8(self):
        self.assertTrue(TestLexer.checkLexeme("0o0123", "0,o0123,<EOF>",28))  

    def test_invalid_int_literal9(self):
        self.assertTrue(TestLexer.checkLexeme("0O182", "0O1,82,<EOF>",29))  

    def test_invalid_int_literal10(self):
        self.assertTrue(TestLexer.checkLexeme("0O128", "0O12,8,<EOF>",30))  

    # Predefined testcases
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

