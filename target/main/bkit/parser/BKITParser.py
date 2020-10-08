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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0152\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\7\2.\n\2\f\2\16\2\61")
        buf.write("\13\2\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\7\3@\n\3\f\3\16\3C\13\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\5\4J\n\4\3\5\3\5\3\5\3\5\7\5P\n\5\f\5\16\5S\13\5\3")
        buf.write("\6\3\6\3\6\3\6\5\6Y\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7")
        buf.write("\7b\n\7\f\7\16\7e\13\7\3\b\3\b\3\b\3\b\7\bk\n\b\f\b\16")
        buf.write("\bn\13\b\3\t\3\t\3\t\7\ts\n\t\f\t\16\tv\13\t\3\t\7\ty")
        buf.write("\n\t\f\t\16\t|\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u008a\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\7\f\u0096\n\f\f\f\16\f\u0099\13\f")
        buf.write("\3\r\3\r\3\r\3\r\7\r\u009f\n\r\f\r\16\r\u00a2\13\r\3\r")
        buf.write("\7\r\u00a5\n\r\f\r\16\r\u00a8\13\r\3\r\3\r\3\r\3\r\7\r")
        buf.write("\u00ae\n\r\f\r\16\r\u00b1\13\r\3\r\7\r\u00b4\n\r\f\r\16")
        buf.write("\r\u00b7\13\r\7\r\u00b9\n\r\f\r\16\r\u00bc\13\r\3\r\3")
        buf.write("\r\7\r\u00c0\n\r\f\r\16\r\u00c3\13\r\3\r\7\r\u00c6\n\r")
        buf.write("\f\r\16\r\u00c9\13\r\5\r\u00cb\n\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\7\16\u00dc\n\16\f\16\16\16\u00df\13\16\3\16\7\16\u00e2")
        buf.write("\n\16\f\16\16\16\u00e5\13\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00ee\n\17\f\17\16\17\u00f1\13\17\3\17")
        buf.write("\7\17\u00f4\n\17\f\17\16\17\u00f7\13\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\7\20\u00fe\n\20\f\20\16\20\u0101\13\20\3\20")
        buf.write("\7\20\u0104\n\20\f\20\16\20\u0107\13\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\7\24\u011c\n\24\f\24\16\24\u011f")
        buf.write("\13\24\5\24\u0121\n\24\3\24\3\24\3\25\3\25\5\25\u0127")
        buf.write("\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\6\26\u0136\n\26\r\26\16\26\u0137\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u013f\n\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u014d")
        buf.write("\n\26\f\26\16\26\u0150\13\26\3\26\2\3*\27\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*\2\t\3\2\4\b\3\2\35")
        buf.write("\36\3\2\3\b\3\2!%\3\2\35 \3\2\'(\3\2)\63\2\u016a\2/\3")
        buf.write("\2\2\2\4:\3\2\2\2\6F\3\2\2\2\bK\3\2\2\2\nT\3\2\2\2\f\\")
        buf.write("\3\2\2\2\16f\3\2\2\2\20o\3\2\2\2\22\u0089\3\2\2\2\24\u008b")
        buf.write("\3\2\2\2\26\u0090\3\2\2\2\30\u009a\3\2\2\2\32\u00cf\3")
        buf.write("\2\2\2\34\u00e9\3\2\2\2\36\u00fb\3\2\2\2 \u010d\3\2\2")
        buf.write("\2\"\u0110\3\2\2\2$\u0113\3\2\2\2&\u0116\3\2\2\2(\u0124")
        buf.write("\3\2\2\2*\u013e\3\2\2\2,.\5\4\3\2-,\3\2\2\2.\61\3\2\2")
        buf.write("\2/-\3\2\2\2/\60\3\2\2\2\60\65\3\2\2\2\61/\3\2\2\2\62")
        buf.write("\64\5\n\6\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2")
        buf.write("\65\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289\7\2\2\39\3")
        buf.write("\3\2\2\2:;\7\r\2\2;<\7;\2\2<A\5\6\4\2=>\7=\2\2>@\5\6\4")
        buf.write("\2?=\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2\2C")
        buf.write("A\3\2\2\2DE\7<\2\2E\5\3\2\2\2FI\5\b\5\2GH\7\64\2\2HJ\t")
        buf.write("\2\2\2IG\3\2\2\2IJ\3\2\2\2J\7\3\2\2\2KQ\7\3\2\2LM\7\67")
        buf.write("\2\2MN\7\4\2\2NP\78\2\2OL\3\2\2\2PS\3\2\2\2QO\3\2\2\2")
        buf.write("QR\3\2\2\2R\t\3\2\2\2SQ\3\2\2\2TU\7\33\2\2UV\7;\2\2VX")
        buf.write("\7\3\2\2WY\5\f\7\2XW\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\5\20")
        buf.write("\t\2[\13\3\2\2\2\\]\7\22\2\2]^\7;\2\2^c\5\16\b\2_`\7=")
        buf.write("\2\2`b\5\16\b\2a_\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2")
        buf.write("\2d\r\3\2\2\2ec\3\2\2\2fl\7\3\2\2gh\7\67\2\2hi\7\4\2\2")
        buf.write("ik\78\2\2jg\3\2\2\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2m\17")
        buf.write("\3\2\2\2nl\3\2\2\2op\7\t\2\2pt\7;\2\2qs\5\4\3\2rq\3\2")
        buf.write("\2\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2uz\3\2\2\2vt\3\2\2\2")
        buf.write("wy\5\22\n\2xw\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{}")
        buf.write("\3\2\2\2|z\3\2\2\2}~\7\25\2\2~\177\7>\2\2\177\21\3\2\2")
        buf.write("\2\u0080\u008a\5\24\13\2\u0081\u008a\5\30\r\2\u0082\u008a")
        buf.write("\5\32\16\2\u0083\u008a\5\34\17\2\u0084\u008a\5\36\20\2")
        buf.write("\u0085\u008a\5$\23\2\u0086\u008a\5(\25\2\u0087\u008a\5")
        buf.write(" \21\2\u0088\u008a\5\"\22\2\u0089\u0080\3\2\2\2\u0089")
        buf.write("\u0081\3\2\2\2\u0089\u0082\3\2\2\2\u0089\u0083\3\2\2\2")
        buf.write("\u0089\u0084\3\2\2\2\u0089\u0085\3\2\2\2\u0089\u0086\3")
        buf.write("\2\2\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\23")
        buf.write("\3\2\2\2\u008b\u008c\5\26\f\2\u008c\u008d\7\64\2\2\u008d")
        buf.write("\u008e\5*\26\2\u008e\u008f\7<\2\2\u008f\25\3\2\2\2\u0090")
        buf.write("\u0097\7\3\2\2\u0091\u0092\7\67\2\2\u0092\u0093\5*\26")
        buf.write("\2\u0093\u0094\78\2\2\u0094\u0096\3\2\2\2\u0095\u0091")
        buf.write("\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\27\3\2\2\2\u0099\u0097\3\2\2\2\u009a")
        buf.write("\u009b\7\f\2\2\u009b\u009c\5*\26\2\u009c\u00a0\7\34\2")
        buf.write("\2\u009d\u009f\5\4\3\2\u009e\u009d\3\2\2\2\u009f\u00a2")
        buf.write("\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u00a6\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a5\5\22\n")
        buf.write("\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00ba\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a9\u00aa\7\20\2\2\u00aa\u00ab\5*\26")
        buf.write("\2\u00ab\u00af\7\34\2\2\u00ac\u00ae\5\4\3\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b5\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b2\u00b4\5\22\n\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00a9\3\2\2\2")
        buf.write("\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3")
        buf.write("\2\2\2\u00bb\u00ca\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00c1")
        buf.write("\7\n\2\2\u00be\u00c0\5\4\3\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write("\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\u00c7\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c6\5")
        buf.write("\22\n\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00cb\3\2\2\2")
        buf.write("\u00c9\u00c7\3\2\2\2\u00ca\u00bd\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\7\32\2\2\u00cd")
        buf.write("\u00ce\7>\2\2\u00ce\31\3\2\2\2\u00cf\u00d0\7\26\2\2\u00d0")
        buf.write("\u00d1\7\65\2\2\u00d1\u00d2\7\3\2\2\u00d2\u00d3\7\64\2")
        buf.write("\2\u00d3\u00d4\5*\26\2\u00d4\u00d5\7=\2\2\u00d5\u00d6")
        buf.write("\5*\26\2\u00d6\u00d7\7=\2\2\u00d7\u00d8\5*\26\2\u00d8")
        buf.write("\u00d9\7\66\2\2\u00d9\u00dd\7\31\2\2\u00da\u00dc\5\4\3")
        buf.write("\2\u00db\u00da\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e3\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00e0\u00e2\5\22\n\2\u00e1\u00e0\3\2\2")
        buf.write("\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4")
        buf.write("\3\2\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6")
        buf.write("\u00e7\7\13\2\2\u00e7\u00e8\7>\2\2\u00e8\33\3\2\2\2\u00e9")
        buf.write("\u00ea\7\23\2\2\u00ea\u00eb\5*\26\2\u00eb\u00ef\7\31\2")
        buf.write("\2\u00ec\u00ee\5\4\3\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1")
        buf.write("\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f5\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f4\5\22\n")
        buf.write("\2\u00f3\u00f2\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3")
        buf.write("\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7")
        buf.write("\u00f5\3\2\2\2\u00f8\u00f9\7\21\2\2\u00f9\u00fa\7>\2\2")
        buf.write("\u00fa\35\3\2\2\2\u00fb\u00ff\7\31\2\2\u00fc\u00fe\5\4")
        buf.write("\3\2\u00fd\u00fc\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0105\3\2\2\2\u0101")
        buf.write("\u00ff\3\2\2\2\u0102\u0104\5\22\n\2\u0103\u0102\3\2\2")
        buf.write("\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106")
        buf.write("\3\2\2\2\u0106\u0108\3\2\2\2\u0107\u0105\3\2\2\2\u0108")
        buf.write("\u0109\7\23\2\2\u0109\u010a\5*\26\2\u010a\u010b\7\16\2")
        buf.write("\2\u010b\u010c\7>\2\2\u010c\37\3\2\2\2\u010d\u010e\7\17")
        buf.write("\2\2\u010e\u010f\7<\2\2\u010f!\3\2\2\2\u0110\u0111\7\24")
        buf.write("\2\2\u0111\u0112\7<\2\2\u0112#\3\2\2\2\u0113\u0114\5&")
        buf.write("\24\2\u0114\u0115\7<\2\2\u0115%\3\2\2\2\u0116\u0117\7")
        buf.write("\3\2\2\u0117\u0120\7\65\2\2\u0118\u011d\5*\26\2\u0119")
        buf.write("\u011a\7=\2\2\u011a\u011c\5*\26\2\u011b\u0119\3\2\2\2")
        buf.write("\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3")
        buf.write("\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0118")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2\u0122")
        buf.write("\u0123\7\66\2\2\u0123\'\3\2\2\2\u0124\u0126\7\27\2\2\u0125")
        buf.write("\u0127\5*\26\2\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128\u0129\7<\2\2\u0129)\3\2\2\2")
        buf.write("\u012a\u012b\b\26\1\2\u012b\u012c\7\65\2\2\u012c\u012d")
        buf.write("\5*\26\2\u012d\u012e\7\66\2\2\u012e\u013f\3\2\2\2\u012f")
        buf.write("\u013f\5&\24\2\u0130\u0135\7\3\2\2\u0131\u0132\7\67\2")
        buf.write("\2\u0132\u0133\5*\26\2\u0133\u0134\78\2\2\u0134\u0136")
        buf.write("\3\2\2\2\u0135\u0131\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013f\3\2\2\2")
        buf.write("\u0139\u013a\t\3\2\2\u013a\u013f\5*\26\t\u013b\u013c\7")
        buf.write("&\2\2\u013c\u013f\5*\26\b\u013d\u013f\t\4\2\2\u013e\u012a")
        buf.write("\3\2\2\2\u013e\u012f\3\2\2\2\u013e\u0130\3\2\2\2\u013e")
        buf.write("\u0139\3\2\2\2\u013e\u013b\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f\u014e\3\2\2\2\u0140\u0141\f\7\2\2\u0141\u0142\t")
        buf.write("\5\2\2\u0142\u014d\5*\26\b\u0143\u0144\f\6\2\2\u0144\u0145")
        buf.write("\t\6\2\2\u0145\u014d\5*\26\7\u0146\u0147\f\5\2\2\u0147")
        buf.write("\u0148\t\7\2\2\u0148\u014d\5*\26\6\u0149\u014a\f\4\2\2")
        buf.write("\u014a\u014b\t\b\2\2\u014b\u014d\5*\26\5\u014c\u0140\3")
        buf.write("\2\2\2\u014c\u0143\3\2\2\2\u014c\u0146\3\2\2\2\u014c\u0149")
        buf.write("\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f+\3\2\2\2\u0150\u014e\3\2\2\2#/\65")
        buf.write("AIQXcltz\u0089\u0097\u00a0\u00a6\u00af\u00b5\u00ba\u00c1")
        buf.write("\u00c7\u00ca\u00dd\u00e3\u00ef\u00f5\u00ff\u0105\u011d")
        buf.write("\u0120\u0126\u0137\u013e\u014c\u014e")
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
                     "'='", "'('", "')'", "'['", "']'", "'{'", "'}'", "':'", 
                     "';'", "','", "'.'" ]

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
                      "FLOAT_GT_OP", "FLOAT_LTE_OP", "FLOAT_GTE_OP", "ASSIGN_OP", 
                      "LP", "RP", "LSB", "RSB", "LCB", "RCB", "COLON", "SEMI", 
                      "COMMA", "DOT", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_var_dcl = 1
    RULE_var_init = 2
    RULE_var = 3
    RULE_func_dcl = 4
    RULE_param_list = 5
    RULE_param = 6
    RULE_body = 7
    RULE_statement = 8
    RULE_assign_stmt = 9
    RULE_variable = 10
    RULE_if_stmt = 11
    RULE_for_stmt = 12
    RULE_while_stmt = 13
    RULE_do_while_stmt = 14
    RULE_break_stmt = 15
    RULE_continue_stmt = 16
    RULE_call_stmt = 17
    RULE_func_call = 18
    RULE_return_stmt = 19
    RULE_expression = 20

    ruleNames =  [ "program", "var_dcl", "var_init", "var", "func_dcl", 
                   "param_list", "param", "body", "statement", "assign_stmt", 
                   "variable", "if_stmt", "for_stmt", "while_stmt", "do_while_stmt", 
                   "break_stmt", "continue_stmt", "call_stmt", "func_call", 
                   "return_stmt", "expression" ]

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
    ASSIGN_OP=50
    LP=51
    RP=52
    LSB=53
    RSB=54
    LCB=55
    RCB=56
    COLON=57
    SEMI=58
    COMMA=59
    DOT=60
    COMMENT=61
    WS=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    UNTERMINATED_COMMENT=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def var_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_dclContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_dclContext,i)


        def func_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Func_dclContext)
            else:
                return self.getTypedRuleContext(BKITParser.Func_dclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 42
                self.var_dcl()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 48
                self.func_dcl()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_initContext,i)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dcl" ):
                return visitor.visitVar_dcl(self)
            else:
                return visitor.visitChildren(self)




    def var_dcl(self):

        localctx = BKITParser.Var_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(BKITParser.VAR)
            self.state = 57
            self.match(BKITParser.COLON)
            self.state = 58
            self.var_init()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 59
                self.match(BKITParser.COMMA)
                self.state = 60
                self.var_init()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(BKITParser.VarContext,0)


        def ASSIGN_OP(self):
            return self.getToken(BKITParser.ASSIGN_OP, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(BKITParser.BOOLEANLIT, 0)

        def ARRAYLIT(self):
            return self.getToken(BKITParser.ARRAYLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init" ):
                return visitor.visitVar_init(self)
            else:
                return visitor.visitChildren(self)




    def var_init(self):

        localctx = BKITParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.var()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN_OP:
                self.state = 69
                self.match(BKITParser.ASSIGN_OP)
                self.state = 70
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLEANLIT) | (1 << BKITParser.STRINGLIT) | (1 << BKITParser.ARRAYLIT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTLIT)
            else:
                return self.getToken(BKITParser.INTLIT, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = BKITParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(BKITParser.ID)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 74
                self.match(BKITParser.LSB)
                self.state = 75
                self.match(BKITParser.INTLIT)
                self.state = 76
                self.match(BKITParser.RSB)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_dclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_dcl" ):
                return visitor.visitFunc_dcl(self)
            else:
                return visitor.visitChildren(self)




    def func_dcl(self):

        localctx = BKITParser.Func_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(BKITParser.FUNCTION)
            self.state = 83
            self.match(BKITParser.COLON)
            self.state = 84
            self.match(BKITParser.ID)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 85
                self.param_list()


            self.state = 88
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ParamContext)
            else:
                return self.getTypedRuleContext(BKITParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(BKITParser.PARAMETER)
            self.state = 91
            self.match(BKITParser.COLON)
            self.state = 92
            self.param()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 93
                self.match(BKITParser.COMMA)
                self.state = 94
                self.param()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTLIT)
            else:
                return self.getToken(BKITParser.INTLIT, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKITParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(BKITParser.ID)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 101
                self.match(BKITParser.LSB)
                self.state = 102
                self.match(BKITParser.INTLIT)
                self.state = 103
                self.match(BKITParser.RSB)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def END_BODY(self):
            return self.getToken(BKITParser.END_BODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_dclContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_dclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(BKITParser.BODY)
            self.state = 110
            self.match(BKITParser.COLON)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 111
                self.var_dcl()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                self.state = 117
                self.statement()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(BKITParser.END_BODY)
            self.state = 124
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 131
                self.call_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 132
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 133
                self.break_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 134
                self.continue_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def ASSIGN_OP(self):
            return self.getToken(BKITParser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.variable()
            self.state = 138
            self.match(BKITParser.ASSIGN_OP)
            self.state = 139
            self.expression(0)
            self.state = 140
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(BKITParser.ID)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 143
                self.match(BKITParser.LSB)
                self.state = 144
                self.expression(0)
                self.state = 145
                self.match(BKITParser.RSB)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def END_IF(self):
            return self.getToken(BKITParser.END_IF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_dclContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_dclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def ELSE_IF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSE_IF)
            else:
                return self.getToken(BKITParser.ELSE_IF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(BKITParser.IF)
            self.state = 153
            self.expression(0)
            self.state = 154
            self.match(BKITParser.THEN)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 155
                self.var_dcl()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                self.state = 161
                self.statement()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSE_IF:
                self.state = 167
                self.match(BKITParser.ELSE_IF)
                self.state = 168
                self.expression(0)
                self.state = 169
                self.match(BKITParser.THEN)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.VAR:
                    self.state = 170
                    self.var_dcl()
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                    self.state = 176
                    self.statement()
                    self.state = 181
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 187
                self.match(BKITParser.ELSE)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.VAR:
                    self.state = 188
                    self.var_dcl()
                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                    self.state = 194
                    self.statement()
                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 202
            self.match(BKITParser.END_IF)
            self.state = 203
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(BKITParser.ASSIGN_OP, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def END_FOR(self):
            return self.getToken(BKITParser.END_FOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_dclContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_dclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(BKITParser.FOR)
            self.state = 206
            self.match(BKITParser.LP)
            self.state = 207
            self.match(BKITParser.ID)
            self.state = 208
            self.match(BKITParser.ASSIGN_OP)
            self.state = 209
            self.expression(0)
            self.state = 210
            self.match(BKITParser.COMMA)
            self.state = 211
            self.expression(0)
            self.state = 212
            self.match(BKITParser.COMMA)
            self.state = 213
            self.expression(0)
            self.state = 214
            self.match(BKITParser.RP)
            self.state = 215
            self.match(BKITParser.DO)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 216
                self.var_dcl()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                self.state = 222
                self.statement()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self.match(BKITParser.END_FOR)
            self.state = 229
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def END_WHILE(self):
            return self.getToken(BKITParser.END_WHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_dclContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_dclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(BKITParser.WHILE)
            self.state = 232
            self.expression(0)
            self.state = 233
            self.match(BKITParser.DO)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 234
                self.var_dcl()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.IF) | (1 << BKITParser.BREAK) | (1 << BKITParser.WHILE) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.FOR) | (1 << BKITParser.RETURN) | (1 << BKITParser.DO))) != 0):
                self.state = 240
                self.statement()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
            self.match(BKITParser.END_WHILE)
            self.state = 247
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def END_DO(self):
            return self.getToken(BKITParser.END_DO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_dclContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_dclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_do_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(BKITParser.DO)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 250
                self.var_dcl()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 256
                    self.statement() 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 262
            self.match(BKITParser.WHILE)
            self.state = 263
            self.expression(0)
            self.state = 264
            self.match(BKITParser.END_DO)
            self.state = 265
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKITParser.BREAK)
            self.state = 268
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(BKITParser.CONTINUE)
            self.state = 271
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.func_call()
            self.state = 274
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = BKITParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(BKITParser.ID)
            self.state = 277
            self.match(BKITParser.LP)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLEANLIT) | (1 << BKITParser.STRINGLIT) | (1 << BKITParser.ARRAYLIT) | (1 << BKITParser.INT_SUB_OP) | (1 << BKITParser.FLOAT_SUB_OP) | (1 << BKITParser.NEG_OP) | (1 << BKITParser.LP))) != 0):
                self.state = 278
                self.expression(0)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 279
                    self.match(BKITParser.COMMA)
                    self.state = 280
                    self.expression(0)
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 288
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(BKITParser.RETURN)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLEANLIT) | (1 << BKITParser.STRINGLIT) | (1 << BKITParser.ARRAYLIT) | (1 << BKITParser.INT_SUB_OP) | (1 << BKITParser.FLOAT_SUB_OP) | (1 << BKITParser.NEG_OP) | (1 << BKITParser.LP))) != 0):
                self.state = 291
                self.expression(0)


            self.state = 294
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def INT_SUB_OP(self):
            return self.getToken(BKITParser.INT_SUB_OP, 0)

        def FLOAT_SUB_OP(self):
            return self.getToken(BKITParser.FLOAT_SUB_OP, 0)

        def NEG_OP(self):
            return self.getToken(BKITParser.NEG_OP, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(BKITParser.BOOLEANLIT, 0)

        def ARRAYLIT(self):
            return self.getToken(BKITParser.ARRAYLIT, 0)

        def INT_MUL_OP(self):
            return self.getToken(BKITParser.INT_MUL_OP, 0)

        def FLOAT_MUL_OP(self):
            return self.getToken(BKITParser.FLOAT_MUL_OP, 0)

        def INT_DIV_OP(self):
            return self.getToken(BKITParser.INT_DIV_OP, 0)

        def FLOAT_DIV_OP(self):
            return self.getToken(BKITParser.FLOAT_DIV_OP, 0)

        def INT_REMAINDER_OP(self):
            return self.getToken(BKITParser.INT_REMAINDER_OP, 0)

        def INT_ADD_OP(self):
            return self.getToken(BKITParser.INT_ADD_OP, 0)

        def FLOAT_ADD_OP(self):
            return self.getToken(BKITParser.FLOAT_ADD_OP, 0)

        def CONJ_OP(self):
            return self.getToken(BKITParser.CONJ_OP, 0)

        def DISJ_OP(self):
            return self.getToken(BKITParser.DISJ_OP, 0)

        def EQ_OP(self):
            return self.getToken(BKITParser.EQ_OP, 0)

        def INT_NEQ_OP(self):
            return self.getToken(BKITParser.INT_NEQ_OP, 0)

        def FLOAT_NEQ_OP(self):
            return self.getToken(BKITParser.FLOAT_NEQ_OP, 0)

        def INT_LT_OP(self):
            return self.getToken(BKITParser.INT_LT_OP, 0)

        def FLOAT_LT_OP(self):
            return self.getToken(BKITParser.FLOAT_LT_OP, 0)

        def INT_GT_OP(self):
            return self.getToken(BKITParser.INT_GT_OP, 0)

        def FLOAT_GT_OP(self):
            return self.getToken(BKITParser.FLOAT_GT_OP, 0)

        def INT_LTE_OP(self):
            return self.getToken(BKITParser.INT_LTE_OP, 0)

        def FLOAT_LTE_OP(self):
            return self.getToken(BKITParser.FLOAT_LTE_OP, 0)

        def INT_GTE_OP(self):
            return self.getToken(BKITParser.INT_GTE_OP, 0)

        def FLOAT_GTE_OP(self):
            return self.getToken(BKITParser.FLOAT_GTE_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 297
                self.match(BKITParser.LP)
                self.state = 298
                self.expression(0)
                self.state = 299
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.state = 301
                self.func_call()
                pass

            elif la_ == 3:
                self.state = 302
                self.match(BKITParser.ID)
                self.state = 307 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 303
                        self.match(BKITParser.LSB)
                        self.state = 304
                        self.expression(0)
                        self.state = 305
                        self.match(BKITParser.RSB)

                    else:
                        raise NoViableAltException(self)
                    self.state = 309 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 4:
                self.state = 311
                _la = self._input.LA(1)
                if not(_la==BKITParser.INT_SUB_OP or _la==BKITParser.FLOAT_SUB_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 312
                self.expression(7)
                pass

            elif la_ == 5:
                self.state = 313
                self.match(BKITParser.NEG_OP)
                self.state = 314
                self.expression(6)
                pass

            elif la_ == 6:
                self.state = 315
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLEANLIT) | (1 << BKITParser.STRINGLIT) | (1 << BKITParser.ARRAYLIT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 330
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 318
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 319
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT_MUL_OP) | (1 << BKITParser.FLOAT_MUL_OP) | (1 << BKITParser.INT_DIV_OP) | (1 << BKITParser.FLOAT_DIV_OP) | (1 << BKITParser.INT_REMAINDER_OP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 320
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 321
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 322
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT_SUB_OP) | (1 << BKITParser.FLOAT_SUB_OP) | (1 << BKITParser.INT_ADD_OP) | (1 << BKITParser.FLOAT_ADD_OP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 323
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 324
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 325
                        _la = self._input.LA(1)
                        if not(_la==BKITParser.CONJ_OP or _la==BKITParser.DISJ_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 326
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 327
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 328
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQ_OP) | (1 << BKITParser.INT_NEQ_OP) | (1 << BKITParser.INT_LT_OP) | (1 << BKITParser.INT_GT_OP) | (1 << BKITParser.INT_LTE_OP) | (1 << BKITParser.INT_GTE_OP) | (1 << BKITParser.FLOAT_NEQ_OP) | (1 << BKITParser.FLOAT_LT_OP) | (1 << BKITParser.FLOAT_GT_OP) | (1 << BKITParser.FLOAT_LTE_OP) | (1 << BKITParser.FLOAT_GTE_OP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 329
                        self.expression(3)
                        pass

             
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




