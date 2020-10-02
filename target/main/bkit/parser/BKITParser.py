# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\13\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2")
        buf.write("\t\2\4\3\2\2\2\4\5\7\r\2\2\5\6\7:\2\2\6\7\7\3\2\2\7\b")
        buf.write("\7;\2\2\b\t\7\2\2\3\t\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Body'", "'Else'", 
                     "'EndFor'", "'If'", "'Var'", "'EndDo'", "'Break'", 
                     "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
                     "'Continue'", "'EndBody'", "'For'", "'Return'", "'Operators'", 
                     "'Do'", "'EndIf'", "'Function'", "'Then'", "'-'", "'-.'", 
                     "'+'", "'+.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "':'", "';'", 
                     "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "ID", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                      "STRINGLIT", "ARRAYLIT", "BODY", "ELSE", "END_FOR", 
                      "IF", "VAR", "END_DO", "BREAK", "ELSE_IF", "END_WHILE", 
                      "PARAMETER", "WHILE", "CONTINUE", "END_BODY", "FOR", 
                      "RETURN", "OPERATORS", "DO", "END_IF", "FUNCTION", 
                      "THEN", "INT_SUB_OP", "FLOAT_SUB_OP", "INT_ADD_OP", 
                      "FLOAT_ADD_OP", "INT_MUL_OP", "FLOAT_MUL_OP", "INT_DIV_OP", 
                      "FLOAT_DIV_OP", "INT_REMAINDER_OP", "NEG_OP", "CONJ_OP", 
                      "DISJ_OP", "EQ_OP", "INT_NEQ_OP", "INT_LT_OP", "INT_GT_OP", 
                      "INT_LTE_OP", "INT_GTE_OP", "FLOAT_NEQ_OP", "FLOAT_LT_OP", 
                      "FLOAT_GT_OP", "FLOAT_LTE_OP", "FLOAT_GTE_OP", "LP", 
                      "RP", "LSB", "RSB", "LCB", "RCB", "COLON", "SEMI", 
                      "COMMA", "DOT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    INTLIT=2
    FLOATLIT=3
    BOOLEANLIT=4
    STRINGLIT=5
    ARRAYLIT=6
    BODY=7
    ELSE=8
    END_FOR=9
    IF=10
    VAR=11
    END_DO=12
    BREAK=13
    ELSE_IF=14
    END_WHILE=15
    PARAMETER=16
    WHILE=17
    CONTINUE=18
    END_BODY=19
    FOR=20
    RETURN=21
    OPERATORS=22
    DO=23
    END_IF=24
    FUNCTION=25
    THEN=26
    INT_SUB_OP=27
    FLOAT_SUB_OP=28
    INT_ADD_OP=29
    FLOAT_ADD_OP=30
    INT_MUL_OP=31
    FLOAT_MUL_OP=32
    INT_DIV_OP=33
    FLOAT_DIV_OP=34
    INT_REMAINDER_OP=35
    NEG_OP=36
    CONJ_OP=37
    DISJ_OP=38
    EQ_OP=39
    INT_NEQ_OP=40
    INT_LT_OP=41
    INT_GT_OP=42
    INT_LTE_OP=43
    INT_GTE_OP=44
    FLOAT_NEQ_OP=45
    FLOAT_LT_OP=46
    FLOAT_GT_OP=47
    FLOAT_LTE_OP=48
    FLOAT_GTE_OP=49
    LP=50
    RP=51
    LSB=52
    RSB=53
    LCB=54
    RCB=55
    COLON=56
    SEMI=57
    COMMA=58
    DOT=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    UNTERMINATED_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.ID)
            self.state = 5
            self.match(BKITParser.SEMI)
            self.state = 6
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





