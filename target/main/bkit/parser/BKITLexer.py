# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01fc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\7")
        buf.write("\2\u0098\n\2\f\2\16\2\u009b\13\2\3\3\3\3\3\3\5\3\u00a0")
        buf.write("\n\3\3\4\3\4\3\4\7\4\u00a5\n\4\f\4\16\4\u00a8\13\4\5\4")
        buf.write("\u00aa\n\4\3\5\3\5\3\5\3\5\7\5\u00b0\n\5\f\5\16\5\u00b3")
        buf.write("\13\5\3\6\3\6\3\6\3\6\7\6\u00b9\n\6\f\6\16\6\u00bc\13")
        buf.write("\6\3\7\3\7\3\b\6\b\u00c1\n\b\r\b\16\b\u00c2\3\t\3\t\7")
        buf.write("\t\u00c7\n\t\f\t\16\t\u00ca\13\t\3\n\3\n\5\n\u00ce\n\n")
        buf.write("\3\n\6\n\u00d1\n\n\r\n\16\n\u00d2\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00db\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00e6\n\f\3\r\3\r\7\r\u00ea\n\r\f\r\16\r")
        buf.write("\u00ed\13\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u00f6")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\7\17\u00fd\n\17\f\17\16")
        buf.write("\17\u0100\13\17\5\17\u0102\n\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u010a\n\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*")
        buf.write("\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\39\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\6F\u01e2\n")
        buf.write("F\rF\16F\u01e3\3F\3F\3G\3G\3H\3H\7H\u01ec\nH\fH\16H\u01ef")
        buf.write("\13H\3I\3I\7I\u01f3\nI\fI\16I\u01f6\13I\3I\3I\3I\3J\3")
        buf.write("J\2\2K\3\3\5\4\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\5\27")
        buf.write("\6\31\7\33\2\35\b\37\2!\t#\n%\13\'\f)\r+\16-\17/\20\61")
        buf.write("\21\63\22\65\23\67\249\25;\26=\27?\30A\31C\32E\33G\34")
        buf.write("I\35K\36M\37O Q!S\"U#W$Y%[&]\'_(a)c*e+g,i-k.m/o\60q\61")
        buf.write("s\62u\63w\64y\65{\66}\67\1778\u00819\u0083:\u0085;\u0087")
        buf.write("<\u0089=\u008b>\u008d?\u008f@\u0091A\u0093B\3\2\21\3\2")
        buf.write("c|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2QQqq\3\2\639\3\2")
        buf.write("\629\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2GGgg\4\2--//\6\2\f")
        buf.write("\f$$))^^\t\2))^^ddhhppttvv\5\2\13\f\17\17\"\"\2\u020b")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u009f\3\2\2")
        buf.write("\2\7\u00a9\3\2\2\2\t\u00ab\3\2\2\2\13\u00b4\3\2\2\2\r")
        buf.write("\u00bd\3\2\2\2\17\u00c0\3\2\2\2\21\u00c4\3\2\2\2\23\u00cb")
        buf.write("\3\2\2\2\25\u00d4\3\2\2\2\27\u00e5\3\2\2\2\31\u00e7\3")
        buf.write("\2\2\2\33\u00f5\3\2\2\2\35\u00f7\3\2\2\2\37\u0109\3\2")
        buf.write("\2\2!\u010b\3\2\2\2#\u0110\3\2\2\2%\u0115\3\2\2\2\'\u011c")
        buf.write("\3\2\2\2)\u011f\3\2\2\2+\u0123\3\2\2\2-\u0129\3\2\2\2")
        buf.write("/\u012f\3\2\2\2\61\u0136\3\2\2\2\63\u013f\3\2\2\2\65\u0149")
        buf.write("\3\2\2\2\67\u014f\3\2\2\29\u0158\3\2\2\2;\u0160\3\2\2")
        buf.write("\2=\u0164\3\2\2\2?\u016b\3\2\2\2A\u0175\3\2\2\2C\u0178")
        buf.write("\3\2\2\2E\u017e\3\2\2\2G\u0187\3\2\2\2I\u018c\3\2\2\2")
        buf.write("K\u018e\3\2\2\2M\u0191\3\2\2\2O\u0193\3\2\2\2Q\u0196\3")
        buf.write("\2\2\2S\u0198\3\2\2\2U\u019b\3\2\2\2W\u019d\3\2\2\2Y\u01a0")
        buf.write("\3\2\2\2[\u01a2\3\2\2\2]\u01a4\3\2\2\2_\u01a7\3\2\2\2")
        buf.write("a\u01aa\3\2\2\2c\u01ad\3\2\2\2e\u01b0\3\2\2\2g\u01b2\3")
        buf.write("\2\2\2i\u01b4\3\2\2\2k\u01b7\3\2\2\2m\u01ba\3\2\2\2o\u01be")
        buf.write("\3\2\2\2q\u01c1\3\2\2\2s\u01c4\3\2\2\2u\u01c8\3\2\2\2")
        buf.write("w\u01cc\3\2\2\2y\u01ce\3\2\2\2{\u01d0\3\2\2\2}\u01d2\3")
        buf.write("\2\2\2\177\u01d4\3\2\2\2\u0081\u01d6\3\2\2\2\u0083\u01d8")
        buf.write("\3\2\2\2\u0085\u01da\3\2\2\2\u0087\u01dc\3\2\2\2\u0089")
        buf.write("\u01de\3\2\2\2\u008b\u01e1\3\2\2\2\u008d\u01e7\3\2\2\2")
        buf.write("\u008f\u01e9\3\2\2\2\u0091\u01f0\3\2\2\2\u0093\u01fa\3")
        buf.write("\2\2\2\u0095\u0099\t\2\2\2\u0096\u0098\t\3\2\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\4\3\2\2\2\u009b\u0099\3\2\2\2\u009c")
        buf.write("\u00a0\5\7\4\2\u009d\u00a0\5\13\6\2\u009e\u00a0\5\t\5")
        buf.write("\2\u009f\u009c\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e")
        buf.write("\3\2\2\2\u00a0\6\3\2\2\2\u00a1\u00aa\7\62\2\2\u00a2\u00a6")
        buf.write("\t\4\2\2\u00a3\u00a5\t\5\2\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00a1\3")
        buf.write("\2\2\2\u00a9\u00a2\3\2\2\2\u00aa\b\3\2\2\2\u00ab\u00ac")
        buf.write("\7\62\2\2\u00ac\u00ad\t\6\2\2\u00ad\u00b1\t\7\2\2\u00ae")
        buf.write("\u00b0\t\b\2\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\n\3\2\2")
        buf.write("\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7\62\2\2\u00b5\u00b6")
        buf.write("\t\t\2\2\u00b6\u00ba\t\n\2\2\u00b7\u00b9\t\13\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00bb\f\3\2\2\2\u00bc\u00ba\3\2\2")
        buf.write("\2\u00bd\u00be\t\5\2\2\u00be\16\3\2\2\2\u00bf\u00c1\5")
        buf.write("\r\7\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\20\3\2\2\2\u00c4\u00c8")
        buf.write("\5\u0089E\2\u00c5\u00c7\5\r\7\2\u00c6\u00c5\3\2\2\2\u00c7")
        buf.write("\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\22\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cd\t\f")
        buf.write("\2\2\u00cc\u00ce\t\r\2\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00d1\5\r\7\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\24\3\2\2\2\u00d4\u00da\5\17")
        buf.write("\b\2\u00d5\u00db\5\21\t\2\u00d6\u00db\5\23\n\2\u00d7\u00d8")
        buf.write("\5\21\t\2\u00d8\u00d9\5\23\n\2\u00d9\u00db\3\2\2\2\u00da")
        buf.write("\u00d5\3\2\2\2\u00da\u00d6\3\2\2\2\u00da\u00d7\3\2\2\2")
        buf.write("\u00db\26\3\2\2\2\u00dc\u00dd\7V\2\2\u00dd\u00de\7t\2")
        buf.write("\2\u00de\u00df\7w\2\2\u00df\u00e6\7g\2\2\u00e0\u00e1\7")
        buf.write("H\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write("\7u\2\2\u00e4\u00e6\7g\2\2\u00e5\u00dc\3\2\2\2\u00e5\u00e0")
        buf.write("\3\2\2\2\u00e6\30\3\2\2\2\u00e7\u00eb\7$\2\2\u00e8\u00ea")
        buf.write("\5\33\16\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ee\3\2\2\2")
        buf.write("\u00ed\u00eb\3\2\2\2\u00ee\u00ef\7$\2\2\u00ef\32\3\2\2")
        buf.write("\2\u00f0\u00f6\n\16\2\2\u00f1\u00f2\7^\2\2\u00f2\u00f6")
        buf.write("\t\17\2\2\u00f3\u00f4\7)\2\2\u00f4\u00f6\7$\2\2\u00f5")
        buf.write("\u00f0\3\2\2\2\u00f5\u00f1\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f6\34\3\2\2\2\u00f7\u0101\5\177@\2\u00f8\u00fe\5\37")
        buf.write("\20\2\u00f9\u00fa\5\u0087D\2\u00fa\u00fb\5\37\20\2\u00fb")
        buf.write("\u00fd\3\2\2\2\u00fc\u00f9\3\2\2\2\u00fd\u0100\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0102\3")
        buf.write("\2\2\2\u0100\u00fe\3\2\2\2\u0101\u00f8\3\2\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\5\u0081A\2\u0104")
        buf.write("\36\3\2\2\2\u0105\u010a\5\5\3\2\u0106\u010a\5\25\13\2")
        buf.write("\u0107\u010a\5\27\f\2\u0108\u010a\5\35\17\2\u0109\u0105")
        buf.write("\3\2\2\2\u0109\u0106\3\2\2\2\u0109\u0107\3\2\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a \3\2\2\2\u010b\u010c\7D\2\2\u010c")
        buf.write("\u010d\7q\2\2\u010d\u010e\7f\2\2\u010e\u010f\7{\2\2\u010f")
        buf.write("\"\3\2\2\2\u0110\u0111\7G\2\2\u0111\u0112\7n\2\2\u0112")
        buf.write("\u0113\7u\2\2\u0113\u0114\7g\2\2\u0114$\3\2\2\2\u0115")
        buf.write("\u0116\7G\2\2\u0116\u0117\7p\2\2\u0117\u0118\7f\2\2\u0118")
        buf.write("\u0119\7H\2\2\u0119\u011a\7q\2\2\u011a\u011b\7t\2\2\u011b")
        buf.write("&\3\2\2\2\u011c\u011d\7K\2\2\u011d\u011e\7h\2\2\u011e")
        buf.write("(\3\2\2\2\u011f\u0120\7X\2\2\u0120\u0121\7c\2\2\u0121")
        buf.write("\u0122\7t\2\2\u0122*\3\2\2\2\u0123\u0124\7G\2\2\u0124")
        buf.write("\u0125\7p\2\2\u0125\u0126\7f\2\2\u0126\u0127\7F\2\2\u0127")
        buf.write("\u0128\7q\2\2\u0128,\3\2\2\2\u0129\u012a\7D\2\2\u012a")
        buf.write("\u012b\7t\2\2\u012b\u012c\7g\2\2\u012c\u012d\7c\2\2\u012d")
        buf.write("\u012e\7m\2\2\u012e.\3\2\2\2\u012f\u0130\7G\2\2\u0130")
        buf.write("\u0131\7n\2\2\u0131\u0132\7u\2\2\u0132\u0133\7g\2\2\u0133")
        buf.write("\u0134\7K\2\2\u0134\u0135\7h\2\2\u0135\60\3\2\2\2\u0136")
        buf.write("\u0137\7G\2\2\u0137\u0138\7p\2\2\u0138\u0139\7f\2\2\u0139")
        buf.write("\u013a\7Y\2\2\u013a\u013b\7j\2\2\u013b\u013c\7k\2\2\u013c")
        buf.write("\u013d\7n\2\2\u013d\u013e\7g\2\2\u013e\62\3\2\2\2\u013f")
        buf.write("\u0140\7R\2\2\u0140\u0141\7c\2\2\u0141\u0142\7t\2\2\u0142")
        buf.write("\u0143\7c\2\2\u0143\u0144\7o\2\2\u0144\u0145\7g\2\2\u0145")
        buf.write("\u0146\7v\2\2\u0146\u0147\7g\2\2\u0147\u0148\7t\2\2\u0148")
        buf.write("\64\3\2\2\2\u0149\u014a\7Y\2\2\u014a\u014b\7j\2\2\u014b")
        buf.write("\u014c\7k\2\2\u014c\u014d\7n\2\2\u014d\u014e\7g\2\2\u014e")
        buf.write("\66\3\2\2\2\u014f\u0150\7E\2\2\u0150\u0151\7q\2\2\u0151")
        buf.write("\u0152\7p\2\2\u0152\u0153\7v\2\2\u0153\u0154\7k\2\2\u0154")
        buf.write("\u0155\7p\2\2\u0155\u0156\7w\2\2\u0156\u0157\7g\2\2\u0157")
        buf.write("8\3\2\2\2\u0158\u0159\7G\2\2\u0159\u015a\7p\2\2\u015a")
        buf.write("\u015b\7f\2\2\u015b\u015c\7D\2\2\u015c\u015d\7q\2\2\u015d")
        buf.write("\u015e\7f\2\2\u015e\u015f\7{\2\2\u015f:\3\2\2\2\u0160")
        buf.write("\u0161\7H\2\2\u0161\u0162\7q\2\2\u0162\u0163\7t\2\2\u0163")
        buf.write("<\3\2\2\2\u0164\u0165\7T\2\2\u0165\u0166\7g\2\2\u0166")
        buf.write("\u0167\7v\2\2\u0167\u0168\7w\2\2\u0168\u0169\7t\2\2\u0169")
        buf.write("\u016a\7p\2\2\u016a>\3\2\2\2\u016b\u016c\7Q\2\2\u016c")
        buf.write("\u016d\7r\2\2\u016d\u016e\7g\2\2\u016e\u016f\7t\2\2\u016f")
        buf.write("\u0170\7c\2\2\u0170\u0171\7v\2\2\u0171\u0172\7q\2\2\u0172")
        buf.write("\u0173\7t\2\2\u0173\u0174\7u\2\2\u0174@\3\2\2\2\u0175")
        buf.write("\u0176\7F\2\2\u0176\u0177\7q\2\2\u0177B\3\2\2\2\u0178")
        buf.write("\u0179\7G\2\2\u0179\u017a\7p\2\2\u017a\u017b\7f\2\2\u017b")
        buf.write("\u017c\7K\2\2\u017c\u017d\7h\2\2\u017dD\3\2\2\2\u017e")
        buf.write("\u017f\7H\2\2\u017f\u0180\7w\2\2\u0180\u0181\7p\2\2\u0181")
        buf.write("\u0182\7e\2\2\u0182\u0183\7v\2\2\u0183\u0184\7k\2\2\u0184")
        buf.write("\u0185\7q\2\2\u0185\u0186\7p\2\2\u0186F\3\2\2\2\u0187")
        buf.write("\u0188\7V\2\2\u0188\u0189\7j\2\2\u0189\u018a\7g\2\2\u018a")
        buf.write("\u018b\7p\2\2\u018bH\3\2\2\2\u018c\u018d\7/\2\2\u018d")
        buf.write("J\3\2\2\2\u018e\u018f\7/\2\2\u018f\u0190\7\60\2\2\u0190")
        buf.write("L\3\2\2\2\u0191\u0192\7-\2\2\u0192N\3\2\2\2\u0193\u0194")
        buf.write("\7-\2\2\u0194\u0195\7\60\2\2\u0195P\3\2\2\2\u0196\u0197")
        buf.write("\7,\2\2\u0197R\3\2\2\2\u0198\u0199\7,\2\2\u0199\u019a")
        buf.write("\7\60\2\2\u019aT\3\2\2\2\u019b\u019c\7^\2\2\u019cV\3\2")
        buf.write("\2\2\u019d\u019e\7^\2\2\u019e\u019f\7\60\2\2\u019fX\3")
        buf.write("\2\2\2\u01a0\u01a1\7\'\2\2\u01a1Z\3\2\2\2\u01a2\u01a3")
        buf.write("\7#\2\2\u01a3\\\3\2\2\2\u01a4\u01a5\7(\2\2\u01a5\u01a6")
        buf.write("\7(\2\2\u01a6^\3\2\2\2\u01a7\u01a8\7~\2\2\u01a8\u01a9")
        buf.write("\7~\2\2\u01a9`\3\2\2\2\u01aa\u01ab\7?\2\2\u01ab\u01ac")
        buf.write("\7?\2\2\u01acb\3\2\2\2\u01ad\u01ae\7#\2\2\u01ae\u01af")
        buf.write("\7?\2\2\u01afd\3\2\2\2\u01b0\u01b1\7>\2\2\u01b1f\3\2\2")
        buf.write("\2\u01b2\u01b3\7@\2\2\u01b3h\3\2\2\2\u01b4\u01b5\7>\2")
        buf.write("\2\u01b5\u01b6\7?\2\2\u01b6j\3\2\2\2\u01b7\u01b8\7@\2")
        buf.write("\2\u01b8\u01b9\7?\2\2\u01b9l\3\2\2\2\u01ba\u01bb\7?\2")
        buf.write("\2\u01bb\u01bc\7\61\2\2\u01bc\u01bd\7?\2\2\u01bdn\3\2")
        buf.write("\2\2\u01be\u01bf\7>\2\2\u01bf\u01c0\7\60\2\2\u01c0p\3")
        buf.write("\2\2\2\u01c1\u01c2\7@\2\2\u01c2\u01c3\7\60\2\2\u01c3r")
        buf.write("\3\2\2\2\u01c4\u01c5\7>\2\2\u01c5\u01c6\7?\2\2\u01c6\u01c7")
        buf.write("\7\60\2\2\u01c7t\3\2\2\2\u01c8\u01c9\7@\2\2\u01c9\u01ca")
        buf.write("\7?\2\2\u01ca\u01cb\7\60\2\2\u01cbv\3\2\2\2\u01cc\u01cd")
        buf.write("\7*\2\2\u01cdx\3\2\2\2\u01ce\u01cf\7+\2\2\u01cfz\3\2\2")
        buf.write("\2\u01d0\u01d1\7]\2\2\u01d1|\3\2\2\2\u01d2\u01d3\7_\2")
        buf.write("\2\u01d3~\3\2\2\2\u01d4\u01d5\7}\2\2\u01d5\u0080\3\2\2")
        buf.write("\2\u01d6\u01d7\7\177\2\2\u01d7\u0082\3\2\2\2\u01d8\u01d9")
        buf.write("\7<\2\2\u01d9\u0084\3\2\2\2\u01da\u01db\7=\2\2\u01db\u0086")
        buf.write("\3\2\2\2\u01dc\u01dd\7.\2\2\u01dd\u0088\3\2\2\2\u01de")
        buf.write("\u01df\7\60\2\2\u01df\u008a\3\2\2\2\u01e0\u01e2\t\20\2")
        buf.write("\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("\u01e6\bF\2\2\u01e6\u008c\3\2\2\2\u01e7\u01e8\13\2\2\2")
        buf.write("\u01e8\u008e\3\2\2\2\u01e9\u01ed\7$\2\2\u01ea\u01ec\5")
        buf.write("\33\16\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed")
        buf.write("\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u0090\3\2\2\2")
        buf.write("\u01ef\u01ed\3\2\2\2\u01f0\u01f4\7$\2\2\u01f1\u01f3\5")
        buf.write("\33\16\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f7\3\2\2\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f7\u01f8\7^\2\2\u01f8\u01f9\n")
        buf.write("\17\2\2\u01f9\u0092\3\2\2\2\u01fa\u01fb\13\2\2\2\u01fb")
        buf.write("\u0094\3\2\2\2\27\2\u0099\u009f\u00a6\u00a9\u00b1\u00ba")
        buf.write("\u00c2\u00c8\u00cd\u00d2\u00da\u00e5\u00eb\u00f5\u00fe")
        buf.write("\u0101\u0109\u01e3\u01ed\u01f4\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    INTLIT = 2
    FLOATLIT = 3
    BOOLEANLIT = 4
    STRINGLIT = 5
    ARRAYLIT = 6
    BODY = 7
    ELSE = 8
    END_FOR = 9
    IF = 10
    VAR = 11
    END_DO = 12
    BREAK = 13
    ELSE_IF = 14
    END_WHILE = 15
    PARAMETER = 16
    WHILE = 17
    CONTINUE = 18
    END_BODY = 19
    FOR = 20
    RETURN = 21
    OPERATORS = 22
    DO = 23
    END_IF = 24
    FUNCTION = 25
    THEN = 26
    INT_SUB_OP = 27
    FLOAT_SUB_OP = 28
    INT_ADD_OP = 29
    FLOAT_ADD_OP = 30
    INT_MUL_OP = 31
    FLOAT_MUL_OP = 32
    INT_DIV_OP = 33
    FLOAT_DIV_OP = 34
    INT_REMAINDER_OP = 35
    NEG_OP = 36
    CONJ_OP = 37
    DISJ_OP = 38
    EQ_OP = 39
    INT_NEQ_OP = 40
    INT_LT_OP = 41
    INT_GT_OP = 42
    INT_LTE_OP = 43
    INT_GTE_OP = 44
    FLOAT_NEQ_OP = 45
    FLOAT_LT_OP = 46
    FLOAT_GT_OP = 47
    FLOAT_LTE_OP = 48
    FLOAT_GTE_OP = 49
    LP = 50
    RP = 51
    LSB = 52
    RSB = 53
    LCB = 54
    RCB = 55
    COLON = 56
    SEMI = 57
    COMMA = 58
    DOT = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    UNTERMINATED_COMMENT = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'Operators'", 
            "'Do'", "'EndIf'", "'Function'", "'Then'", "'-'", "'-.'", "'+'", 
            "'+.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
            "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "':'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "ARRAYLIT", 
            "BODY", "ELSE", "END_FOR", "IF", "VAR", "END_DO", "BREAK", "ELSE_IF", 
            "END_WHILE", "PARAMETER", "WHILE", "CONTINUE", "END_BODY", "FOR", 
            "RETURN", "OPERATORS", "DO", "END_IF", "FUNCTION", "THEN", "INT_SUB_OP", 
            "FLOAT_SUB_OP", "INT_ADD_OP", "FLOAT_ADD_OP", "INT_MUL_OP", 
            "FLOAT_MUL_OP", "INT_DIV_OP", "FLOAT_DIV_OP", "INT_REMAINDER_OP", 
            "NEG_OP", "CONJ_OP", "DISJ_OP", "EQ_OP", "INT_NEQ_OP", "INT_LT_OP", 
            "INT_GT_OP", "INT_LTE_OP", "INT_GTE_OP", "FLOAT_NEQ_OP", "FLOAT_LT_OP", 
            "FLOAT_GT_OP", "FLOAT_LTE_OP", "FLOAT_GTE_OP", "LP", "RP", "LSB", 
            "RSB", "LCB", "RCB", "COLON", "SEMI", "COMMA", "DOT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "INTLIT", "BASE10", "BASE8", "BASE16", "DIGIT", 
                  "INT_PART", "DECIMAL_PART", "EXPONENT_PART", "FLOATLIT", 
                  "BOOLEANLIT", "STRINGLIT", "STR_CHAR", "ARRAYLIT", "LITERAL", 
                  "BODY", "ELSE", "END_FOR", "IF", "VAR", "END_DO", "BREAK", 
                  "ELSE_IF", "END_WHILE", "PARAMETER", "WHILE", "CONTINUE", 
                  "END_BODY", "FOR", "RETURN", "OPERATORS", "DO", "END_IF", 
                  "FUNCTION", "THEN", "INT_SUB_OP", "FLOAT_SUB_OP", "INT_ADD_OP", 
                  "FLOAT_ADD_OP", "INT_MUL_OP", "FLOAT_MUL_OP", "INT_DIV_OP", 
                  "FLOAT_DIV_OP", "INT_REMAINDER_OP", "NEG_OP", "CONJ_OP", 
                  "DISJ_OP", "EQ_OP", "INT_NEQ_OP", "INT_LT_OP", "INT_GT_OP", 
                  "INT_LTE_OP", "INT_GTE_OP", "FLOAT_NEQ_OP", "FLOAT_LT_OP", 
                  "FLOAT_GT_OP", "FLOAT_LTE_OP", "FLOAT_GTE_OP", "LP", "RP", 
                  "LSB", "RSB", "LCB", "RCB", "COLON", "SEMI", "COMMA", 
                  "DOT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


