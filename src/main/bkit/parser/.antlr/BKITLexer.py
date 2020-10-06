# Generated from /home/longbui/Documents/PPL/ass1/assignment1/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0232\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\7\2\u009c\n\2\f\2\16\2\u009f\13\2\3\3\3\3\3")
        buf.write("\3\5\3\u00a4\n\3\3\4\3\4\3\4\7\4\u00a9\n\4\f\4\16\4\u00ac")
        buf.write("\13\4\5\4\u00ae\n\4\3\5\3\5\3\5\3\5\7\5\u00b4\n\5\f\5")
        buf.write("\16\5\u00b7\13\5\3\6\3\6\3\6\3\6\7\6\u00bd\n\6\f\6\16")
        buf.write("\6\u00c0\13\6\3\7\3\7\3\b\6\b\u00c5\n\b\r\b\16\b\u00c6")
        buf.write("\3\t\3\t\7\t\u00cb\n\t\f\t\16\t\u00ce\13\t\3\n\3\n\5\n")
        buf.write("\u00d2\n\n\3\n\6\n\u00d5\n\n\r\n\16\n\u00d6\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00df\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u00ea\n\f\3\r\3\r\7\r\u00ee\n\r")
        buf.write("\f\r\16\r\u00f1\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00fb\n\16\3\17\3\17\7\17\u00ff\n\17\f\17\16")
        buf.write("\17\u0102\13\17\3\17\3\17\7\17\u0106\n\17\f\17\16\17\u0109")
        buf.write("\13\17\3\17\3\17\7\17\u010d\n\17\f\17\16\17\u0110\13\17")
        buf.write("\3\17\3\17\7\17\u0114\n\17\f\17\16\17\u0117\13\17\7\17")
        buf.write("\u0119\n\17\f\17\16\17\u011c\13\17\5\17\u011e\n\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\5\20\u0126\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3:\3;\3;\3;\3;\3")
        buf.write("<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3")
        buf.write("E\3E\3F\3F\3G\3G\3G\3G\7G\u0203\nG\fG\16G\u0206\13G\3")
        buf.write("G\3G\3G\3G\3G\3H\6H\u020e\nH\rH\16H\u020f\3H\3H\3I\3I")
        buf.write("\3J\3J\7J\u0218\nJ\fJ\16J\u021b\13J\3J\3J\3K\3K\7K\u0221")
        buf.write("\nK\fK\16K\u0224\13K\3K\3K\3K\3K\3L\3L\3L\3L\7L\u022e")
        buf.write("\nL\fL\16L\u0231\13L\4\u0204\u022f\2M\3\3\5\4\7\2\t\2")
        buf.write("\13\2\r\2\17\2\21\2\23\2\25\5\27\6\31\7\33\2\35\b\37\2")
        buf.write("!\t#\n%\13\'\f)\r+\16-\17/\20\61\21\63\22\65\23\67\24")
        buf.write("9\25;\26=\27?\30A\31C\32E\33G\34I\35K\36M\37O Q!S\"U#")
        buf.write("W$Y%[&]\'_(a)c*e+g,i-k.m/o\60q\61s\62u\63w\64y\65{\66")
        buf.write("}\67\1778\u00819\u0083:\u0085;\u0087<\u0089=\u008b>\u008d")
        buf.write("?\u008f@\u0091A\u0093B\u0095C\u0097D\3\2\21\3\2c|\6\2")
        buf.write("\62;C\\aac|\3\2\63;\3\2\62;\4\2QQqq\3\2\639\3\2\629\4")
        buf.write("\2ZZzz\4\2\63;CH\4\2\62;CH\4\2GGgg\4\2--//\6\2\f\f$$)")
        buf.write(")^^\t\2))^^ddhhppttvv\5\2\13\f\17\17\"\"\2\u0247\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099")
        buf.write("\3\2\2\2\5\u00a3\3\2\2\2\7\u00ad\3\2\2\2\t\u00af\3\2\2")
        buf.write("\2\13\u00b8\3\2\2\2\r\u00c1\3\2\2\2\17\u00c4\3\2\2\2\21")
        buf.write("\u00c8\3\2\2\2\23\u00cf\3\2\2\2\25\u00d8\3\2\2\2\27\u00e9")
        buf.write("\3\2\2\2\31\u00eb\3\2\2\2\33\u00fa\3\2\2\2\35\u00fc\3")
        buf.write("\2\2\2\37\u0125\3\2\2\2!\u0127\3\2\2\2#\u012c\3\2\2\2")
        buf.write("%\u0131\3\2\2\2\'\u0138\3\2\2\2)\u013b\3\2\2\2+\u013f")
        buf.write("\3\2\2\2-\u0145\3\2\2\2/\u014b\3\2\2\2\61\u0152\3\2\2")
        buf.write("\2\63\u015b\3\2\2\2\65\u0165\3\2\2\2\67\u016b\3\2\2\2")
        buf.write("9\u0174\3\2\2\2;\u017c\3\2\2\2=\u0180\3\2\2\2?\u0187\3")
        buf.write("\2\2\2A\u0191\3\2\2\2C\u0194\3\2\2\2E\u019a\3\2\2\2G\u01a3")
        buf.write("\3\2\2\2I\u01a8\3\2\2\2K\u01aa\3\2\2\2M\u01ad\3\2\2\2")
        buf.write("O\u01af\3\2\2\2Q\u01b2\3\2\2\2S\u01b4\3\2\2\2U\u01b7\3")
        buf.write("\2\2\2W\u01b9\3\2\2\2Y\u01bc\3\2\2\2[\u01be\3\2\2\2]\u01c0")
        buf.write("\3\2\2\2_\u01c3\3\2\2\2a\u01c6\3\2\2\2c\u01c9\3\2\2\2")
        buf.write("e\u01cc\3\2\2\2g\u01ce\3\2\2\2i\u01d0\3\2\2\2k\u01d3\3")
        buf.write("\2\2\2m\u01d6\3\2\2\2o\u01da\3\2\2\2q\u01dd\3\2\2\2s\u01e0")
        buf.write("\3\2\2\2u\u01e4\3\2\2\2w\u01e8\3\2\2\2y\u01ea\3\2\2\2")
        buf.write("{\u01ec\3\2\2\2}\u01ee\3\2\2\2\177\u01f0\3\2\2\2\u0081")
        buf.write("\u01f2\3\2\2\2\u0083\u01f4\3\2\2\2\u0085\u01f6\3\2\2\2")
        buf.write("\u0087\u01f8\3\2\2\2\u0089\u01fa\3\2\2\2\u008b\u01fc\3")
        buf.write("\2\2\2\u008d\u01fe\3\2\2\2\u008f\u020d\3\2\2\2\u0091\u0213")
        buf.write("\3\2\2\2\u0093\u0215\3\2\2\2\u0095\u021e\3\2\2\2\u0097")
        buf.write("\u0229\3\2\2\2\u0099\u009d\t\2\2\2\u009a\u009c\t\3\2\2")
        buf.write("\u009b\u009a\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009d\u009e\3\2\2\2\u009e\4\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u00a0\u00a4\5\7\4\2\u00a1\u00a4\5\13\6\2\u00a2")
        buf.write("\u00a4\5\t\5\2\u00a3\u00a0\3\2\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a2\3\2\2\2\u00a4\6\3\2\2\2\u00a5\u00ae\7\62")
        buf.write("\2\2\u00a6\u00aa\t\4\2\2\u00a7\u00a9\t\5\2\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa")
        buf.write("\u00ab\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ad\u00a5\3\2\2\2\u00ad\u00a6\3\2\2\2\u00ae\b\3\2\2")
        buf.write("\2\u00af\u00b0\7\62\2\2\u00b0\u00b1\t\6\2\2\u00b1\u00b5")
        buf.write("\t\7\2\2\u00b2\u00b4\t\b\2\2\u00b3\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\n\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\7\62")
        buf.write("\2\2\u00b9\u00ba\t\t\2\2\u00ba\u00be\t\n\2\2\u00bb\u00bd")
        buf.write("\t\13\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\f\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c1\u00c2\t\5\2\2\u00c2\16\3\2\2\2\u00c3")
        buf.write("\u00c5\5\r\7\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\20\3\2")
        buf.write("\2\2\u00c8\u00cc\5\u008bF\2\u00c9\u00cb\5\r\7\2\u00ca")
        buf.write("\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cd\3\2\2\2\u00cd\22\3\2\2\2\u00ce\u00cc\3\2")
        buf.write("\2\2\u00cf\u00d1\t\f\2\2\u00d0\u00d2\t\r\2\2\u00d1\u00d0")
        buf.write("\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3")
        buf.write("\u00d5\5\r\7\2\u00d4\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\24\3\2")
        buf.write("\2\2\u00d8\u00de\5\17\b\2\u00d9\u00df\5\21\t\2\u00da\u00df")
        buf.write("\5\23\n\2\u00db\u00dc\5\21\t\2\u00dc\u00dd\5\23\n\2\u00dd")
        buf.write("\u00df\3\2\2\2\u00de\u00d9\3\2\2\2\u00de\u00da\3\2\2\2")
        buf.write("\u00de\u00db\3\2\2\2\u00df\26\3\2\2\2\u00e0\u00e1\7V\2")
        buf.write("\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7w\2\2\u00e3\u00ea\7")
        buf.write("g\2\2\u00e4\u00e5\7H\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7u\2\2\u00e8\u00ea\7g\2\2\u00e9\u00e0")
        buf.write("\3\2\2\2\u00e9\u00e4\3\2\2\2\u00ea\30\3\2\2\2\u00eb\u00ef")
        buf.write("\7$\2\2\u00ec\u00ee\5\33\16\2\u00ed\u00ec\3\2\2\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f2\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7")
        buf.write("$\2\2\u00f3\u00f4\b\r\2\2\u00f4\32\3\2\2\2\u00f5\u00fb")
        buf.write("\n\16\2\2\u00f6\u00f7\7^\2\2\u00f7\u00fb\t\17\2\2\u00f8")
        buf.write("\u00f9\7)\2\2\u00f9\u00fb\7$\2\2\u00fa\u00f5\3\2\2\2\u00fa")
        buf.write("\u00f6\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\34\3\2\2\2\u00fc")
        buf.write("\u0100\5\u0081A\2\u00fd\u00ff\5\u008fH\2\u00fe\u00fd\3")
        buf.write("\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101")
        buf.write("\3\2\2\2\u0101\u011d\3\2\2\2\u0102\u0100\3\2\2\2\u0103")
        buf.write("\u0107\5\37\20\2\u0104\u0106\5\u008fH\2\u0105\u0104\3")
        buf.write("\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u011a\3\2\2\2\u0109\u0107\3\2\2\2\u010a")
        buf.write("\u010e\5\u0089E\2\u010b\u010d\5\u008fH\2\u010c\u010b\3")
        buf.write("\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e\3\2\2\2\u0111")
        buf.write("\u0115\5\37\20\2\u0112\u0114\5\u008fH\2\u0113\u0112\3")
        buf.write("\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0118")
        buf.write("\u010a\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3")
        buf.write("\2\2\2\u011d\u0103\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f")
        buf.write("\3\2\2\2\u011f\u0120\5\u0083B\2\u0120\36\3\2\2\2\u0121")
        buf.write("\u0126\5\5\3\2\u0122\u0126\5\25\13\2\u0123\u0126\5\27")
        buf.write("\f\2\u0124\u0126\5\35\17\2\u0125\u0121\3\2\2\2\u0125\u0122")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126")
        buf.write(" \3\2\2\2\u0127\u0128\7D\2\2\u0128\u0129\7q\2\2\u0129")
        buf.write("\u012a\7f\2\2\u012a\u012b\7{\2\2\u012b\"\3\2\2\2\u012c")
        buf.write("\u012d\7G\2\2\u012d\u012e\7n\2\2\u012e\u012f\7u\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130$\3\2\2\2\u0131\u0132\7G\2\2\u0132")
        buf.write("\u0133\7p\2\2\u0133\u0134\7f\2\2\u0134\u0135\7H\2\2\u0135")
        buf.write("\u0136\7q\2\2\u0136\u0137\7t\2\2\u0137&\3\2\2\2\u0138")
        buf.write("\u0139\7K\2\2\u0139\u013a\7h\2\2\u013a(\3\2\2\2\u013b")
        buf.write("\u013c\7X\2\2\u013c\u013d\7c\2\2\u013d\u013e\7t\2\2\u013e")
        buf.write("*\3\2\2\2\u013f\u0140\7G\2\2\u0140\u0141\7p\2\2\u0141")
        buf.write("\u0142\7f\2\2\u0142\u0143\7F\2\2\u0143\u0144\7q\2\2\u0144")
        buf.write(",\3\2\2\2\u0145\u0146\7D\2\2\u0146\u0147\7t\2\2\u0147")
        buf.write("\u0148\7g\2\2\u0148\u0149\7c\2\2\u0149\u014a\7m\2\2\u014a")
        buf.write(".\3\2\2\2\u014b\u014c\7G\2\2\u014c\u014d\7n\2\2\u014d")
        buf.write("\u014e\7u\2\2\u014e\u014f\7g\2\2\u014f\u0150\7K\2\2\u0150")
        buf.write("\u0151\7h\2\2\u0151\60\3\2\2\2\u0152\u0153\7G\2\2\u0153")
        buf.write("\u0154\7p\2\2\u0154\u0155\7f\2\2\u0155\u0156\7Y\2\2\u0156")
        buf.write("\u0157\7j\2\2\u0157\u0158\7k\2\2\u0158\u0159\7n\2\2\u0159")
        buf.write("\u015a\7g\2\2\u015a\62\3\2\2\2\u015b\u015c\7R\2\2\u015c")
        buf.write("\u015d\7c\2\2\u015d\u015e\7t\2\2\u015e\u015f\7c\2\2\u015f")
        buf.write("\u0160\7o\2\2\u0160\u0161\7g\2\2\u0161\u0162\7v\2\2\u0162")
        buf.write("\u0163\7g\2\2\u0163\u0164\7t\2\2\u0164\64\3\2\2\2\u0165")
        buf.write("\u0166\7Y\2\2\u0166\u0167\7j\2\2\u0167\u0168\7k\2\2\u0168")
        buf.write("\u0169\7n\2\2\u0169\u016a\7g\2\2\u016a\66\3\2\2\2\u016b")
        buf.write("\u016c\7E\2\2\u016c\u016d\7q\2\2\u016d\u016e\7p\2\2\u016e")
        buf.write("\u016f\7v\2\2\u016f\u0170\7k\2\2\u0170\u0171\7p\2\2\u0171")
        buf.write("\u0172\7w\2\2\u0172\u0173\7g\2\2\u01738\3\2\2\2\u0174")
        buf.write("\u0175\7G\2\2\u0175\u0176\7p\2\2\u0176\u0177\7f\2\2\u0177")
        buf.write("\u0178\7D\2\2\u0178\u0179\7q\2\2\u0179\u017a\7f\2\2\u017a")
        buf.write("\u017b\7{\2\2\u017b:\3\2\2\2\u017c\u017d\7H\2\2\u017d")
        buf.write("\u017e\7q\2\2\u017e\u017f\7t\2\2\u017f<\3\2\2\2\u0180")
        buf.write("\u0181\7T\2\2\u0181\u0182\7g\2\2\u0182\u0183\7v\2\2\u0183")
        buf.write("\u0184\7w\2\2\u0184\u0185\7t\2\2\u0185\u0186\7p\2\2\u0186")
        buf.write(">\3\2\2\2\u0187\u0188\7Q\2\2\u0188\u0189\7r\2\2\u0189")
        buf.write("\u018a\7g\2\2\u018a\u018b\7t\2\2\u018b\u018c\7c\2\2\u018c")
        buf.write("\u018d\7v\2\2\u018d\u018e\7q\2\2\u018e\u018f\7t\2\2\u018f")
        buf.write("\u0190\7u\2\2\u0190@\3\2\2\2\u0191\u0192\7F\2\2\u0192")
        buf.write("\u0193\7q\2\2\u0193B\3\2\2\2\u0194\u0195\7G\2\2\u0195")
        buf.write("\u0196\7p\2\2\u0196\u0197\7f\2\2\u0197\u0198\7K\2\2\u0198")
        buf.write("\u0199\7h\2\2\u0199D\3\2\2\2\u019a\u019b\7H\2\2\u019b")
        buf.write("\u019c\7w\2\2\u019c\u019d\7p\2\2\u019d\u019e\7e\2\2\u019e")
        buf.write("\u019f\7v\2\2\u019f\u01a0\7k\2\2\u01a0\u01a1\7q\2\2\u01a1")
        buf.write("\u01a2\7p\2\2\u01a2F\3\2\2\2\u01a3\u01a4\7V\2\2\u01a4")
        buf.write("\u01a5\7j\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7\7p\2\2\u01a7")
        buf.write("H\3\2\2\2\u01a8\u01a9\7/\2\2\u01a9J\3\2\2\2\u01aa\u01ab")
        buf.write("\7/\2\2\u01ab\u01ac\7\60\2\2\u01acL\3\2\2\2\u01ad\u01ae")
        buf.write("\7-\2\2\u01aeN\3\2\2\2\u01af\u01b0\7-\2\2\u01b0\u01b1")
        buf.write("\7\60\2\2\u01b1P\3\2\2\2\u01b2\u01b3\7,\2\2\u01b3R\3\2")
        buf.write("\2\2\u01b4\u01b5\7,\2\2\u01b5\u01b6\7\60\2\2\u01b6T\3")
        buf.write("\2\2\2\u01b7\u01b8\7^\2\2\u01b8V\3\2\2\2\u01b9\u01ba\7")
        buf.write("^\2\2\u01ba\u01bb\7\60\2\2\u01bbX\3\2\2\2\u01bc\u01bd")
        buf.write("\7\'\2\2\u01bdZ\3\2\2\2\u01be\u01bf\7#\2\2\u01bf\\\3\2")
        buf.write("\2\2\u01c0\u01c1\7(\2\2\u01c1\u01c2\7(\2\2\u01c2^\3\2")
        buf.write("\2\2\u01c3\u01c4\7~\2\2\u01c4\u01c5\7~\2\2\u01c5`\3\2")
        buf.write("\2\2\u01c6\u01c7\7?\2\2\u01c7\u01c8\7?\2\2\u01c8b\3\2")
        buf.write("\2\2\u01c9\u01ca\7#\2\2\u01ca\u01cb\7?\2\2\u01cbd\3\2")
        buf.write("\2\2\u01cc\u01cd\7>\2\2\u01cdf\3\2\2\2\u01ce\u01cf\7@")
        buf.write("\2\2\u01cfh\3\2\2\2\u01d0\u01d1\7>\2\2\u01d1\u01d2\7?")
        buf.write("\2\2\u01d2j\3\2\2\2\u01d3\u01d4\7@\2\2\u01d4\u01d5\7?")
        buf.write("\2\2\u01d5l\3\2\2\2\u01d6\u01d7\7?\2\2\u01d7\u01d8\7\61")
        buf.write("\2\2\u01d8\u01d9\7?\2\2\u01d9n\3\2\2\2\u01da\u01db\7>")
        buf.write("\2\2\u01db\u01dc\7\60\2\2\u01dcp\3\2\2\2\u01dd\u01de\7")
        buf.write("@\2\2\u01de\u01df\7\60\2\2\u01dfr\3\2\2\2\u01e0\u01e1")
        buf.write("\7>\2\2\u01e1\u01e2\7?\2\2\u01e2\u01e3\7\60\2\2\u01e3")
        buf.write("t\3\2\2\2\u01e4\u01e5\7@\2\2\u01e5\u01e6\7?\2\2\u01e6")
        buf.write("\u01e7\7\60\2\2\u01e7v\3\2\2\2\u01e8\u01e9\7?\2\2\u01e9")
        buf.write("x\3\2\2\2\u01ea\u01eb\7*\2\2\u01ebz\3\2\2\2\u01ec\u01ed")
        buf.write("\7+\2\2\u01ed|\3\2\2\2\u01ee\u01ef\7]\2\2\u01ef~\3\2\2")
        buf.write("\2\u01f0\u01f1\7_\2\2\u01f1\u0080\3\2\2\2\u01f2\u01f3")
        buf.write("\7}\2\2\u01f3\u0082\3\2\2\2\u01f4\u01f5\7\177\2\2\u01f5")
        buf.write("\u0084\3\2\2\2\u01f6\u01f7\7<\2\2\u01f7\u0086\3\2\2\2")
        buf.write("\u01f8\u01f9\7=\2\2\u01f9\u0088\3\2\2\2\u01fa\u01fb\7")
        buf.write(".\2\2\u01fb\u008a\3\2\2\2\u01fc\u01fd\7\60\2\2\u01fd\u008c")
        buf.write("\3\2\2\2\u01fe\u01ff\7,\2\2\u01ff\u0200\7,\2\2\u0200\u0204")
        buf.write("\3\2\2\2\u0201\u0203\13\2\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0206\3\2\2\2\u0204\u0205\3\2\2\2\u0204\u0202\3\2\2\2")
        buf.write("\u0205\u0207\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0208\7")
        buf.write(",\2\2\u0208\u0209\7,\2\2\u0209\u020a\3\2\2\2\u020a\u020b")
        buf.write("\bG\3\2\u020b\u008e\3\2\2\2\u020c\u020e\t\20\2\2\u020d")
        buf.write("\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u020d\3\2\2\2")
        buf.write("\u020f\u0210\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212\b")
        buf.write("H\3\2\u0212\u0090\3\2\2\2\u0213\u0214\13\2\2\2\u0214\u0092")
        buf.write("\3\2\2\2\u0215\u0219\7$\2\2\u0216\u0218\5\33\16\2\u0217")
        buf.write("\u0216\3\2\2\2\u0218\u021b\3\2\2\2\u0219\u0217\3\2\2\2")
        buf.write("\u0219\u021a\3\2\2\2\u021a\u021c\3\2\2\2\u021b\u0219\3")
        buf.write("\2\2\2\u021c\u021d\bJ\4\2\u021d\u0094\3\2\2\2\u021e\u0222")
        buf.write("\7$\2\2\u021f\u0221\5\33\16\2\u0220\u021f\3\2\2\2\u0221")
        buf.write("\u0224\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2")
        buf.write("\u0223\u0225\3\2\2\2\u0224\u0222\3\2\2\2\u0225\u0226\7")
        buf.write("^\2\2\u0226\u0227\n\17\2\2\u0227\u0228\bK\5\2\u0228\u0096")
        buf.write("\3\2\2\2\u0229\u022a\7,\2\2\u022a\u022b\7,\2\2\u022b\u022f")
        buf.write("\3\2\2\2\u022c\u022e\13\2\2\2\u022d\u022c\3\2\2\2\u022e")
        buf.write("\u0231\3\2\2\2\u022f\u0230\3\2\2\2\u022f\u022d\3\2\2\2")
        buf.write("\u0230\u0098\3\2\2\2\u0231\u022f\3\2\2\2\35\2\u009d\u00a3")
        buf.write("\u00aa\u00ad\u00b5\u00be\u00c6\u00cc\u00d1\u00d6\u00de")
        buf.write("\u00e9\u00ef\u00fa\u0100\u0107\u010e\u0115\u011a\u011d")
        buf.write("\u0125\u0204\u020f\u0219\u0222\u022f\6\3\r\2\b\2\2\3J")
        buf.write("\3\3K\4")
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
    ASSIGN_OP = 50
    LP = 51
    RP = 52
    LSB = 53
    RSB = 54
    LCB = 55
    RCB = 56
    COLON = 57
    SEMI = 58
    COMMA = 59
    DOT = 60
    COMMENT = 61
    WS = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    UNTERMINATED_COMMENT = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'Operators'", 
            "'Do'", "'EndIf'", "'Function'", "'Then'", "'-'", "'-.'", "'+'", 
            "'+.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
            "'<.'", "'>.'", "'<=.'", "'>=.'", "'='", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "':'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "ARRAYLIT", 
            "BODY", "ELSE", "END_FOR", "IF", "VAR", "END_DO", "BREAK", "ELSE_IF", 
            "END_WHILE", "PARAMETER", "WHILE", "CONTINUE", "END_BODY", "FOR", 
            "RETURN", "OPERATORS", "DO", "END_IF", "FUNCTION", "THEN", "INT_SUB_OP", 
            "FLOAT_SUB_OP", "INT_ADD_OP", "FLOAT_ADD_OP", "INT_MUL_OP", 
            "FLOAT_MUL_OP", "INT_DIV_OP", "FLOAT_DIV_OP", "INT_REMAINDER_OP", 
            "NEG_OP", "CONJ_OP", "DISJ_OP", "EQ_OP", "INT_NEQ_OP", "INT_LT_OP", 
            "INT_GT_OP", "INT_LTE_OP", "INT_GTE_OP", "FLOAT_NEQ_OP", "FLOAT_LT_OP", 
            "FLOAT_GT_OP", "FLOAT_LTE_OP", "FLOAT_GTE_OP", "ASSIGN_OP", 
            "LP", "RP", "LSB", "RSB", "LCB", "RCB", "COLON", "SEMI", "COMMA", 
            "DOT", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

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
                  "FLOAT_GT_OP", "FLOAT_LTE_OP", "FLOAT_GTE_OP", "ASSIGN_OP", 
                  "LP", "RP", "LSB", "RSB", "LCB", "RCB", "COLON", "SEMI", 
                  "COMMA", "DOT", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
            return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[11] = self.STRINGLIT_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    value = str(self.text);
                    self.text = value[1:-1]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    value = str(self.text)
                    self.text = value[1:]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    value = str(self.text)
                    self.text = value[1:]
                
     


