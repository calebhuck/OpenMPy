# Generated from /Users/calebhuck/PycharmProjects/OpenMPy/preprocessor/Grammar.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
import re
import importlib
# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2w")
        buf.write("\u046d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080")
        buf.write("\t\u0080\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083")
        buf.write("\4\u0084\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087")
        buf.write("\t\u0087\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a")
        buf.write("\4\u008b\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e")
        buf.write("\t\u008e\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\5\25\u01dc\n\25\3\26\3\26\5\26\u01e0\n\26\3\27\3")
        buf.write("\27\3\27\5\27\u01e5\n\27\3\30\3\30\3\30\3\30\5\30\u01eb")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*")
        buf.write("\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\38\38\38\38\39\39\39\39\39\3")
        buf.write("9\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3<\3<\3<\5<\u02ae")
        buf.write("\n<\3<\3<\5<\u02b2\n<\3<\5<\u02b5\n<\5<\u02b7\n<\3<\3")
        buf.write("<\3=\3=\7=\u02bd\n=\f=\16=\u02c0\13=\3>\3>\3>\3>\3>\5")
        buf.write(">\u02c7\n>\3>\3>\5>\u02cb\n>\3?\3?\3?\3?\3?\5?\u02d2\n")
        buf.write("?\3?\3?\5?\u02d6\n?\3@\3@\7@\u02da\n@\f@\16@\u02dd\13")
        buf.write("@\3@\6@\u02e0\n@\r@\16@\u02e1\5@\u02e4\n@\3A\3A\3A\6A")
        buf.write("\u02e9\nA\rA\16A\u02ea\3B\3B\3B\6B\u02f0\nB\rB\16B\u02f1")
        buf.write("\3C\3C\3C\6C\u02f7\nC\rC\16C\u02f8\3D\3D\5D\u02fd\nD\3")
        buf.write("E\3E\5E\u0301\nE\3E\3E\3F\3F\3G\3G\3G\3G\3H\3H\3I\3I\3")
        buf.write("I\3J\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3N\3O\3O\3P\3P\3P\3")
        buf.write("Q\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3U\3V\3V\3V\3W\3W\3X\3")
        buf.write("X\3Y\3Y\3Z\3Z\3[\3[\3[\3\\\3\\\3]\3]\3]\3^\3^\3^\3_\3")
        buf.write("_\3`\3`\3a\3a\3a\3b\3b\3b\3c\3c\3c\3d\3d\3d\3e\3e\3e\3")
        buf.write("f\3f\3g\3g\3g\3h\3h\3h\3i\3i\3i\3j\3j\3j\3k\3k\3k\3l\3")
        buf.write("l\3l\3m\3m\3m\3n\3n\3n\3o\3o\3o\3p\3p\3p\3q\3q\3q\3q\3")
        buf.write("r\3r\3r\3r\3s\3s\3s\3s\3t\3t\3t\3t\3u\3u\3u\5u\u0389\n")
        buf.write("u\3u\3u\3v\3v\3w\3w\3w\7w\u0392\nw\fw\16w\u0395\13w\3")
        buf.write("w\3w\3w\3w\7w\u039b\nw\fw\16w\u039e\13w\3w\5w\u03a1\n")
        buf.write("w\3x\3x\3x\3x\3x\7x\u03a8\nx\fx\16x\u03ab\13x\3x\3x\3")
        buf.write("x\3x\3x\3x\3x\3x\7x\u03b5\nx\fx\16x\u03b8\13x\3x\3x\3")
        buf.write("x\5x\u03bd\nx\3y\3y\5y\u03c1\ny\3z\3z\3{\3{\3{\3{\5{\u03c9")
        buf.write("\n{\3|\3|\3}\3}\3~\3~\3\177\3\177\3\u0080\3\u0080\3\u0081")
        buf.write("\5\u0081\u03d6\n\u0081\3\u0081\3\u0081\3\u0081\3\u0081")
        buf.write("\5\u0081\u03dc\n\u0081\3\u0082\3\u0082\5\u0082\u03e0\n")
        buf.write("\u0082\3\u0082\3\u0082\3\u0083\6\u0083\u03e5\n\u0083\r")
        buf.write("\u0083\16\u0083\u03e6\3\u0084\3\u0084\6\u0084\u03eb\n")
        buf.write("\u0084\r\u0084\16\u0084\u03ec\3\u0085\3\u0085\5\u0085")
        buf.write("\u03f1\n\u0085\3\u0085\6\u0085\u03f4\n\u0085\r\u0085\16")
        buf.write("\u0085\u03f5\3\u0086\3\u0086\3\u0086\7\u0086\u03fb\n\u0086")
        buf.write("\f\u0086\16\u0086\u03fe\13\u0086\3\u0086\3\u0086\3\u0086")
        buf.write("\3\u0086\7\u0086\u0404\n\u0086\f\u0086\16\u0086\u0407")
        buf.write("\13\u0086\3\u0086\5\u0086\u040a\n\u0086\3\u0087\3\u0087")
        buf.write("\3\u0087\3\u0087\3\u0087\7\u0087\u0411\n\u0087\f\u0087")
        buf.write("\16\u0087\u0414\13\u0087\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write("\3\u0087\3\u0087\3\u0087\3\u0087\7\u0087\u041e\n\u0087")
        buf.write("\f\u0087\16\u0087\u0421\13\u0087\3\u0087\3\u0087\3\u0087")
        buf.write("\5\u0087\u0426\n\u0087\3\u0088\3\u0088\5\u0088\u042a\n")
        buf.write("\u0088\3\u0089\5\u0089\u042d\n\u0089\3\u008a\5\u008a\u0430")
        buf.write("\n\u008a\3\u008b\5\u008b\u0433\n\u008b\3\u008c\3\u008c")
        buf.write("\3\u008c\3\u008d\6\u008d\u0439\n\u008d\r\u008d\16\u008d")
        buf.write("\u043a\3\u008e\3\u008e\3\u008e\7\u008e\u0440\n\u008e\f")
        buf.write("\u008e\16\u008e\u0443\13\u008e\3\u008e\3\u008e\3\u008e")
        buf.write("\3\u008e\3\u008e\7\u008e\u044a\n\u008e\f\u008e\16\u008e")
        buf.write("\u044d\13\u008e\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e")
        buf.write("\3\u008e\7\u008e\u0455\n\u008e\f\u008e\16\u008e\u0458")
        buf.write("\13\u008e\5\u008e\u045a\n\u008e\3\u008f\3\u008f\5\u008f")
        buf.write("\u045e\n\u008f\3\u008f\5\u008f\u0461\n\u008f\3\u008f\3")
        buf.write("\u008f\5\u008f\u0465\n\u008f\3\u0090\5\u0090\u0468\n\u0090")
        buf.write("\3\u0091\3\u0091\5\u0091\u046c\n\u0091\6\u03a9\u03b6\u0412")
        buf.write("\u041f\2\u0092\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097")
        buf.write("M\u0099N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7")
        buf.write("U\u00a9V\u00abW\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7")
        buf.write("]\u00b9^\u00bb_\u00bd`\u00bfa\u00c1b\u00c3c\u00c5d\u00c7")
        buf.write("e\u00c9f\u00cbg\u00cdh\u00cfi\u00d1j\u00d3k\u00d5l\u00d7")
        buf.write("m\u00d9n\u00dbo\u00ddp\u00dfq\u00e1r\u00e3s\u00e5t\u00e7")
        buf.write("u\u00e9v\u00ebw\u00ed\2\u00ef\2\u00f1\2\u00f3\2\u00f5")
        buf.write("\2\u00f7\2\u00f9\2\u00fb\2\u00fd\2\u00ff\2\u0101\2\u0103")
        buf.write("\2\u0105\2\u0107\2\u0109\2\u010b\2\u010d\2\u010f\2\u0111")
        buf.write("\2\u0113\2\u0115\2\u0117\2\u0119\2\u011b\2\u011d\2\u011f")
        buf.write("\2\u0121\2\3\2\36\b\2HHTTWWhhttww\4\2HHhh\4\2TTtt\4\2")
        buf.write("DDdd\4\2QQqq\4\2ZZzz\4\2LLll\6\2\f\f\16\17))^^\6\2\f\f")
        buf.write("\16\17$$^^\3\2^^\3\2\63;\3\2\62;\3\2\629\5\2\62;CHch\3")
        buf.write("\2\62\63\4\2GGgg\4\2--//\7\2\2\13\r\16\20(*]_\u0081\7")
        buf.write("\2\2\13\r\16\20#%]_\u0081\4\2\2]_\u0081\3\2\2\u0081\4")
        buf.write("\2\13\13\"\"\3\2qq\4\2\f\f\16\17\3\2oo\3\2rr\u0129\2C")
        buf.write("\\aac|\u00ac\u00ac\u00b7\u00b7\u00bc\u00bc\u00c2\u00d8")
        buf.write("\u00da\u00f8\u00fa\u0243\u0252\u02c3\u02c8\u02d3\u02e2")
        buf.write("\u02e6\u02f0\u02f0\u037c\u037c\u0388\u0388\u038a\u038c")
        buf.write("\u038e\u038e\u0390\u03a3\u03a5\u03d0\u03d2\u03f7\u03f9")
        buf.write("\u0483\u048c\u04d0\u04d2\u04fb\u0502\u0511\u0533\u0558")
        buf.write("\u055b\u055b\u0563\u0589\u05d2\u05ec\u05f2\u05f4\u0623")
        buf.write("\u063c\u0642\u064c\u0670\u0671\u0673\u06d5\u06d7\u06d7")
        buf.write("\u06e7\u06e8\u06f0\u06f1\u06fc\u06fe\u0701\u0701\u0712")
        buf.write("\u0712\u0714\u0731\u074f\u076f\u0782\u07a7\u07b3\u07b3")
        buf.write("\u0906\u093b\u093f\u093f\u0952\u0952\u095a\u0963\u097f")
        buf.write("\u097f\u0987\u098e\u0991\u0992\u0995\u09aa\u09ac\u09b2")
        buf.write("\u09b4\u09b4\u09b8\u09bb\u09bf\u09bf\u09d0\u09d0\u09de")
        buf.write("\u09df\u09e1\u09e3\u09f2\u09f3\u0a07\u0a0c\u0a11\u0a12")
        buf.write("\u0a15\u0a2a\u0a2c\u0a32\u0a34\u0a35\u0a37\u0a38\u0a3a")
        buf.write("\u0a3b\u0a5b\u0a5e\u0a60\u0a60\u0a74\u0a76\u0a87\u0a8f")
        buf.write("\u0a91\u0a93\u0a95\u0aaa\u0aac\u0ab2\u0ab4\u0ab5\u0ab7")
        buf.write("\u0abb\u0abf\u0abf\u0ad2\u0ad2\u0ae2\u0ae3\u0b07\u0b0e")
        buf.write("\u0b11\u0b12\u0b15\u0b2a\u0b2c\u0b32\u0b34\u0b35\u0b37")
        buf.write("\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f\u0b61\u0b63\u0b73\u0b73")
        buf.write("\u0b85\u0b85\u0b87\u0b8c\u0b90\u0b92\u0b94\u0b97\u0b9b")
        buf.write("\u0b9c\u0b9e\u0b9e\u0ba0\u0ba1\u0ba5\u0ba6\u0baa\u0bac")
        buf.write("\u0bb0\u0bbb\u0c07\u0c0e\u0c10\u0c12\u0c14\u0c2a\u0c2c")
        buf.write("\u0c35\u0c37\u0c3b\u0c62\u0c63\u0c87\u0c8e\u0c90\u0c92")
        buf.write("\u0c94\u0caa\u0cac\u0cb5\u0cb7\u0cbb\u0cbf\u0cbf\u0ce0")
        buf.write("\u0ce0\u0ce2\u0ce3\u0d07\u0d0e\u0d10\u0d12\u0d14\u0d2a")
        buf.write("\u0d2c\u0d3b\u0d62\u0d63\u0d87\u0d98\u0d9c\u0db3\u0db5")
        buf.write("\u0dbd\u0dbf\u0dbf\u0dc2\u0dc8\u0e03\u0e32\u0e34\u0e35")
        buf.write("\u0e42\u0e48\u0e83\u0e84\u0e86\u0e86\u0e89\u0e8a\u0e8c")
        buf.write("\u0e8c\u0e8f\u0e8f\u0e96\u0e99\u0e9b\u0ea1\u0ea3\u0ea5")
        buf.write("\u0ea7\u0ea7\u0ea9\u0ea9\u0eac\u0ead\u0eaf\u0eb2\u0eb4")
        buf.write("\u0eb5\u0ebf\u0ebf\u0ec2\u0ec6\u0ec8\u0ec8\u0ede\u0edf")
        buf.write("\u0f02\u0f02\u0f42\u0f49\u0f4b\u0f6c\u0f8a\u0f8d\u1002")
        buf.write("\u1023\u1025\u1029\u102b\u102c\u1052\u1057\u10a2\u10c7")
        buf.write("\u10d2\u10fc\u10fe\u10fe\u1102\u115b\u1161\u11a4\u11aa")
        buf.write("\u11fb\u1202\u124a\u124c\u124f\u1252\u1258\u125a\u125a")
        buf.write("\u125c\u125f\u1262\u128a\u128c\u128f\u1292\u12b2\u12b4")
        buf.write("\u12b7\u12ba\u12c0\u12c2\u12c2\u12c4\u12c7\u12ca\u12d8")
        buf.write("\u12da\u1312\u1314\u1317\u131a\u135c\u1382\u1391\u13a2")
        buf.write("\u13f6\u1403\u166e\u1671\u1678\u1683\u169c\u16a2\u16ec")
        buf.write("\u16f0\u16f2\u1702\u170e\u1710\u1713\u1722\u1733\u1742")
        buf.write("\u1753\u1762\u176e\u1770\u1772\u1782\u17b5\u17d9\u17d9")
        buf.write("\u17de\u17de\u1822\u1879\u1882\u18aa\u1902\u191e\u1952")
        buf.write("\u196f\u1972\u1976\u1982\u19ab\u19c3\u19c9\u1a02\u1a18")
        buf.write("\u1d02\u1dc1\u1e02\u1e9d\u1ea2\u1efb\u1f02\u1f17\u1f1a")
        buf.write("\u1f1f\u1f22\u1f47\u1f4a\u1f4f\u1f52\u1f59\u1f5b\u1f5b")
        buf.write("\u1f5d\u1f5d\u1f5f\u1f5f\u1f61\u1f7f\u1f82\u1fb6\u1fb8")
        buf.write("\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8\u1fce\u1fd2\u1fd5")
        buf.write("\u1fd8\u1fdd\u1fe2\u1fee\u1ff4\u1ff6\u1ff8\u1ffe\u2073")
        buf.write("\u2073\u2081\u2081\u2092\u2096\u2104\u2104\u2109\u2109")
        buf.write("\u210c\u2115\u2117\u2117\u211a\u211f\u2126\u2126\u2128")
        buf.write("\u2128\u212a\u212a\u212c\u2133\u2135\u213b\u213e\u2141")
        buf.write("\u2147\u214b\u2162\u2185\u2c02\u2c30\u2c32\u2c60\u2c82")
        buf.write("\u2ce6\u2d02\u2d27\u2d32\u2d67\u2d71\u2d71\u2d82\u2d98")
        buf.write("\u2da2\u2da8\u2daa\u2db0\u2db2\u2db8\u2dba\u2dc0\u2dc2")
        buf.write("\u2dc8\u2dca\u2dd0\u2dd2\u2dd8\u2dda\u2de0\u3007\u3009")
        buf.write("\u3023\u302b\u3033\u3037\u303a\u303e\u3043\u3098\u309d")
        buf.write("\u30a1\u30a3\u30fc\u30fe\u3101\u3107\u312e\u3133\u3190")
        buf.write("\u31a2\u31b9\u31f2\u3201\u3402\u4db7\u4e02\u9fbd\ua002")
        buf.write("\ua48e\ua802\ua803\ua805\ua807\ua809\ua80c\ua80e\ua824")
        buf.write("\uac02\ud7a5\uf902\ufa2f\ufa32\ufa6c\ufa72\ufadb\ufb02")
        buf.write("\ufb08\ufb15\ufb19\ufb1f\ufb1f\ufb21\ufb2a\ufb2c\ufb38")
        buf.write("\ufb3a\ufb3e\ufb40\ufb40\ufb42\ufb43\ufb45\ufb46\ufb48")
        buf.write("\ufbb3\ufbd5\ufd3f\ufd52\ufd91\ufd94\ufdc9\ufdf2\ufdfd")
        buf.write("\ufe72\ufe76\ufe78\ufefe\uff23\uff3c\uff43\uff5c\uff68")
        buf.write("\uffc0\uffc4\uffc9\uffcc\uffd1\uffd4\uffd9\uffdc\uffde")
        buf.write("\u0096\2\62;\u0302\u0371\u0485\u0488\u0593\u05bb\u05bd")
        buf.write("\u05bf\u05c1\u05c1\u05c3\u05c4\u05c6\u05c7\u05c9\u05c9")
        buf.write("\u0612\u0617\u064d\u0660\u0662\u066b\u0672\u0672\u06d8")
        buf.write("\u06de\u06e1\u06e6\u06e9\u06ea\u06ec\u06ef\u06f2\u06fb")
        buf.write("\u0713\u0713\u0732\u074c\u07a8\u07b2\u0903\u0905\u093e")
        buf.write("\u093e\u0940\u094f\u0953\u0956\u0964\u0965\u0968\u0971")
        buf.write("\u0983\u0985\u09be\u09be\u09c0\u09c6\u09c9\u09ca\u09cd")
        buf.write("\u09cf\u09d9\u09d9\u09e4\u09e5\u09e8\u09f1\u0a03\u0a05")
        buf.write("\u0a3e\u0a3e\u0a40\u0a44\u0a49\u0a4a\u0a4d\u0a4f\u0a68")
        buf.write("\u0a73\u0a83\u0a85\u0abe\u0abe\u0ac0\u0ac7\u0ac9\u0acb")
        buf.write("\u0acd\u0acf\u0ae4\u0ae5\u0ae8\u0af1\u0b03\u0b05\u0b3e")
        buf.write("\u0b3e\u0b40\u0b45\u0b49\u0b4a\u0b4d\u0b4f\u0b58\u0b59")
        buf.write("\u0b68\u0b71\u0b84\u0b84\u0bc0\u0bc4\u0bc8\u0bca\u0bcc")
        buf.write("\u0bcf\u0bd9\u0bd9\u0be8\u0bf1\u0c03\u0c05\u0c40\u0c46")
        buf.write("\u0c48\u0c4a\u0c4c\u0c4f\u0c57\u0c58\u0c68\u0c71\u0c84")
        buf.write("\u0c85\u0cbe\u0cbe\u0cc0\u0cc6\u0cc8\u0cca\u0ccc\u0ccf")
        buf.write("\u0cd7\u0cd8\u0ce8\u0cf1\u0d04\u0d05\u0d40\u0d45\u0d48")
        buf.write("\u0d4a\u0d4c\u0d4f\u0d59\u0d59\u0d68\u0d71\u0d84\u0d85")
        buf.write("\u0dcc\u0dcc\u0dd1\u0dd6\u0dd8\u0dd8\u0dda\u0de1\u0df4")
        buf.write("\u0df5\u0e33\u0e33\u0e36\u0e3c\u0e49\u0e50\u0e52\u0e5b")
        buf.write("\u0eb3\u0eb3\u0eb6\u0ebb\u0ebd\u0ebe\u0eca\u0ecf\u0ed2")
        buf.write("\u0edb\u0f1a\u0f1b\u0f22\u0f2b\u0f37\u0f37\u0f39\u0f39")
        buf.write("\u0f3b\u0f3b\u0f40\u0f41\u0f73\u0f86\u0f88\u0f89\u0f92")
        buf.write("\u0f99\u0f9b\u0fbe\u0fc8\u0fc8\u102e\u1034\u1038\u103b")
        buf.write("\u1042\u104b\u1058\u105b\u1361\u1361\u136b\u1373\u1714")
        buf.write("\u1716\u1734\u1736\u1754\u1755\u1774\u1775\u17b8\u17d5")
        buf.write("\u17df\u17df\u17e2\u17eb\u180d\u180f\u1812\u181b\u18ab")
        buf.write("\u18ab\u1922\u192d\u1932\u193d\u1948\u1951\u19b2\u19c2")
        buf.write("\u19ca\u19cb\u19d2\u19db\u1a19\u1a1d\u1dc2\u1dc5\u2041")
        buf.write("\u2042\u2056\u2056\u20d2\u20de\u20e3\u20e3\u20e7\u20ed")
        buf.write("\u302c\u3031\u309b\u309c\ua804\ua804\ua808\ua808\ua80d")
        buf.write("\ua80d\ua825\ua829\ufb20\ufb20\ufe02\ufe11\ufe22\ufe25")
        buf.write("\ufe35\ufe36\ufe4f\ufe51\uff12\uff1b\uff41\uff41\2\u0495")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2")
        buf.write("\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9")
        buf.write("\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2")
        buf.write("\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2\2\2\u00d7")
        buf.write("\3\2\2\2\2\u00d9\3\2\2\2\2\u00db\3\2\2\2\2\u00dd\3\2\2")
        buf.write("\2\2\u00df\3\2\2\2\2\u00e1\3\2\2\2\2\u00e3\3\2\2\2\2\u00e5")
        buf.write("\3\2\2\2\2\u00e7\3\2\2\2\2\u00e9\3\2\2\2\2\u00eb\3\2\2")
        buf.write("\2\3\u0123\3\2\2\2\5\u0128\3\2\2\2\7\u0131\3\2\2\2\t\u013a")
        buf.write("\3\2\2\2\13\u0142\3\2\2\2\r\u0149\3\2\2\2\17\u0150\3\2")
        buf.write("\2\2\21\u0159\3\2\2\2\23\u0161\3\2\2\2\25\u016e\3\2\2")
        buf.write("\2\27\u0176\3\2\2\2\31\u017f\3\2\2\2\33\u018d\3\2\2\2")
        buf.write("\35\u019a\3\2\2\2\37\u01a5\3\2\2\2!\u01a9\3\2\2\2#\u01ad")
        buf.write("\3\2\2\2%\u01b0\3\2\2\2\'\u01b3\3\2\2\2)\u01db\3\2\2\2")
        buf.write("+\u01df\3\2\2\2-\u01e4\3\2\2\2/\u01ea\3\2\2\2\61\u01ec")
        buf.write("\3\2\2\2\63\u01f0\3\2\2\2\65\u01f7\3\2\2\2\67\u01fd\3")
        buf.write("\2\2\29\u0202\3\2\2\2;\u0209\3\2\2\2=\u020c\3\2\2\2?\u0213")
        buf.write("\3\2\2\2A\u021c\3\2\2\2C\u0223\3\2\2\2E\u0226\3\2\2\2")
        buf.write("G\u022b\3\2\2\2I\u0230\3\2\2\2K\u0236\3\2\2\2M\u023a\3")
        buf.write("\2\2\2O\u023d\3\2\2\2Q\u0241\3\2\2\2S\u0249\3\2\2\2U\u024e")
        buf.write("\3\2\2\2W\u0255\3\2\2\2Y\u025c\3\2\2\2[\u025f\3\2\2\2")
        buf.write("]\u0263\3\2\2\2_\u0267\3\2\2\2a\u026a\3\2\2\2c\u026f\3")
        buf.write("\2\2\2e\u0274\3\2\2\2g\u027a\3\2\2\2i\u0280\3\2\2\2k\u0286")
        buf.write("\3\2\2\2m\u028a\3\2\2\2o\u028f\3\2\2\2q\u0298\3\2\2\2")
        buf.write("s\u029e\3\2\2\2u\u02a4\3\2\2\2w\u02b6\3\2\2\2y\u02ba\3")
        buf.write("\2\2\2{\u02c6\3\2\2\2}\u02d1\3\2\2\2\177\u02e3\3\2\2\2")
        buf.write("\u0081\u02e5\3\2\2\2\u0083\u02ec\3\2\2\2\u0085\u02f3\3")
        buf.write("\2\2\2\u0087\u02fc\3\2\2\2\u0089\u0300\3\2\2\2\u008b\u0304")
        buf.write("\3\2\2\2\u008d\u0306\3\2\2\2\u008f\u030a\3\2\2\2\u0091")
        buf.write("\u030c\3\2\2\2\u0093\u030f\3\2\2\2\u0095\u0312\3\2\2\2")
        buf.write("\u0097\u0314\3\2\2\2\u0099\u0316\3\2\2\2\u009b\u0318\3")
        buf.write("\2\2\2\u009d\u031b\3\2\2\2\u009f\u031d\3\2\2\2\u00a1\u0320")
        buf.write("\3\2\2\2\u00a3\u0323\3\2\2\2\u00a5\u0325\3\2\2\2\u00a7")
        buf.write("\u0327\3\2\2\2\u00a9\u0329\3\2\2\2\u00ab\u032c\3\2\2\2")
        buf.write("\u00ad\u032f\3\2\2\2\u00af\u0331\3\2\2\2\u00b1\u0333\3")
        buf.write("\2\2\2\u00b3\u0335\3\2\2\2\u00b5\u0337\3\2\2\2\u00b7\u033a")
        buf.write("\3\2\2\2\u00b9\u033c\3\2\2\2\u00bb\u033f\3\2\2\2\u00bd")
        buf.write("\u0342\3\2\2\2\u00bf\u0344\3\2\2\2\u00c1\u0346\3\2\2\2")
        buf.write("\u00c3\u0349\3\2\2\2\u00c5\u034c\3\2\2\2\u00c7\u034f\3")
        buf.write("\2\2\2\u00c9\u0352\3\2\2\2\u00cb\u0355\3\2\2\2\u00cd\u0357")
        buf.write("\3\2\2\2\u00cf\u035a\3\2\2\2\u00d1\u035d\3\2\2\2\u00d3")
        buf.write("\u0360\3\2\2\2\u00d5\u0363\3\2\2\2\u00d7\u0366\3\2\2\2")
        buf.write("\u00d9\u0369\3\2\2\2\u00db\u036c\3\2\2\2\u00dd\u036f\3")
        buf.write("\2\2\2\u00df\u0372\3\2\2\2\u00e1\u0375\3\2\2\2\u00e3\u0379")
        buf.write("\3\2\2\2\u00e5\u037d\3\2\2\2\u00e7\u0381\3\2\2\2\u00e9")
        buf.write("\u0388\3\2\2\2\u00eb\u038c\3\2\2\2\u00ed\u03a0\3\2\2\2")
        buf.write("\u00ef\u03bc\3\2\2\2\u00f1\u03c0\3\2\2\2\u00f3\u03c2\3")
        buf.write("\2\2\2\u00f5\u03c8\3\2\2\2\u00f7\u03ca\3\2\2\2\u00f9\u03cc")
        buf.write("\3\2\2\2\u00fb\u03ce\3\2\2\2\u00fd\u03d0\3\2\2\2\u00ff")
        buf.write("\u03d2\3\2\2\2\u0101\u03db\3\2\2\2\u0103\u03df\3\2\2\2")
        buf.write("\u0105\u03e4\3\2\2\2\u0107\u03e8\3\2\2\2\u0109\u03ee\3")
        buf.write("\2\2\2\u010b\u0409\3\2\2\2\u010d\u0425\3\2\2\2\u010f\u0429")
        buf.write("\3\2\2\2\u0111\u042c\3\2\2\2\u0113\u042f\3\2\2\2\u0115")
        buf.write("\u0432\3\2\2\2\u0117\u0434\3\2\2\2\u0119\u0438\3\2\2\2")
        buf.write("\u011b\u0459\3\2\2\2\u011d\u045b\3\2\2\2\u011f\u0467\3")
        buf.write("\2\2\2\u0121\u046b\3\2\2\2\u0123\u0124\7%\2\2\u0124\u0125")
        buf.write("\7q\2\2\u0125\u0126\7o\2\2\u0126\u0127\7r\2\2\u0127\4")
        buf.write("\3\2\2\2\u0128\u0129\7r\2\2\u0129\u012a\7c\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b\u012c\7c\2\2\u012c\u012d\7n\2\2\u012d\u012e")
        buf.write("\7n\2\2\u012e\u012f\7g\2\2\u012f\u0130\7n\2\2\u0130\6")
        buf.write("\3\2\2\2\u0131\u0132\7u\2\2\u0132\u0133\7g\2\2\u0133\u0134")
        buf.write("\7e\2\2\u0134\u0135\7v\2\2\u0135\u0136\7k\2\2\u0136\u0137")
        buf.write("\7q\2\2\u0137\u0138\7p\2\2\u0138\u0139\7u\2\2\u0139\b")
        buf.write("\3\2\2\2\u013a\u013b\7u\2\2\u013b\u013c\7g\2\2\u013c\u013d")
        buf.write("\7e\2\2\u013d\u013e\7v\2\2\u013e\u013f\7k\2\2\u013f\u0140")
        buf.write("\7q\2\2\u0140\u0141\7p\2\2\u0141\n\3\2\2\2\u0142\u0143")
        buf.write("\7o\2\2\u0143\u0144\7c\2\2\u0144\u0145\7u\2\2\u0145\u0146")
        buf.write("\7v\2\2\u0146\u0147\7g\2\2\u0147\u0148\7t\2\2\u0148\f")
        buf.write("\3\2\2\2\u0149\u014a\7u\2\2\u014a\u014b\7k\2\2\u014b\u014c")
        buf.write("\7p\2\2\u014c\u014d\7i\2\2\u014d\u014e\7n\2\2\u014e\u014f")
        buf.write("\7g\2\2\u014f\16\3\2\2\2\u0150\u0151\7e\2\2\u0151\u0152")
        buf.write("\7t\2\2\u0152\u0153\7k\2\2\u0153\u0154\7v\2\2\u0154\u0155")
        buf.write("\7k\2\2\u0155\u0156\7e\2\2\u0156\u0157\7c\2\2\u0157\u0158")
        buf.write("\7n\2\2\u0158\20\3\2\2\2\u0159\u015a\7d\2\2\u015a\u015b")
        buf.write("\7c\2\2\u015b\u015c\7t\2\2\u015c\u015d\7t\2\2\u015d\u015e")
        buf.write("\7k\2\2\u015e\u015f\7g\2\2\u015f\u0160\7t\2\2\u0160\22")
        buf.write("\3\2\2\2\u0161\u0162\7p\2\2\u0162\u0163\7w\2\2\u0163\u0164")
        buf.write("\7o\2\2\u0164\u0165\7a\2\2\u0165\u0166\7v\2\2\u0166\u0167")
        buf.write("\7j\2\2\u0167\u0168\7t\2\2\u0168\u0169\7g\2\2\u0169\u016a")
        buf.write("\7c\2\2\u016a\u016b\7f\2\2\u016b\u016c\7u\2\2\u016c\u016d")
        buf.write("\7*\2\2\u016d\24\3\2\2\2\u016e\u016f\7u\2\2\u016f\u0170")
        buf.write("\7j\2\2\u0170\u0171\7c\2\2\u0171\u0172\7t\2\2\u0172\u0173")
        buf.write("\7g\2\2\u0173\u0174\7f\2\2\u0174\u0175\7*\2\2\u0175\26")
        buf.write("\3\2\2\2\u0176\u0177\7r\2\2\u0177\u0178\7t\2\2\u0178\u0179")
        buf.write("\7k\2\2\u0179\u017a\7x\2\2\u017a\u017b\7c\2\2\u017b\u017c")
        buf.write("\7v\2\2\u017c\u017d\7g\2\2\u017d\u017e\7*\2\2\u017e\30")
        buf.write("\3\2\2\2\u017f\u0180\7h\2\2\u0180\u0181\7k\2\2\u0181\u0182")
        buf.write("\7t\2\2\u0182\u0183\7u\2\2\u0183\u0184\7v\2\2\u0184\u0185")
        buf.write("\7r\2\2\u0185\u0186\7t\2\2\u0186\u0187\7k\2\2\u0187\u0188")
        buf.write("\7x\2\2\u0188\u0189\7c\2\2\u0189\u018a\7v\2\2\u018a\u018b")
        buf.write("\7g\2\2\u018b\u018c\7*\2\2\u018c\32\3\2\2\2\u018d\u018e")
        buf.write("\7n\2\2\u018e\u018f\7c\2\2\u018f\u0190\7u\2\2\u0190\u0191")
        buf.write("\7v\2\2\u0191\u0192\7r\2\2\u0192\u0193\7t\2\2\u0193\u0194")
        buf.write("\7k\2\2\u0194\u0195\7x\2\2\u0195\u0196\7c\2\2\u0196\u0197")
        buf.write("\7v\2\2\u0197\u0198\7g\2\2\u0198\u0199\7*\2\2\u0199\34")
        buf.write("\3\2\2\2\u019a\u019b\7t\2\2\u019b\u019c\7g\2\2\u019c\u019d")
        buf.write("\7f\2\2\u019d\u019e\7w\2\2\u019e\u019f\7e\2\2\u019f\u01a0")
        buf.write("\7v\2\2\u01a0\u01a1\7k\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3")
        buf.write("\7p\2\2\u01a3\u01a4\7*\2\2\u01a4\36\3\2\2\2\u01a5\u01a6")
        buf.write("\7o\2\2\u01a6\u01a7\7k\2\2\u01a7\u01a8\7p\2\2\u01a8 \3")
        buf.write("\2\2\2\u01a9\u01aa\7o\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac")
        buf.write("\7z\2\2\u01ac\"\3\2\2\2\u01ad\u01ae\7(\2\2\u01ae\u01af")
        buf.write("\7(\2\2\u01af$\3\2\2\2\u01b0\u01b1\7~\2\2\u01b1\u01b2")
        buf.write("\7~\2\2\u01b2&\3\2\2\2\u01b3\u01b4\7u\2\2\u01b4\u01b5")
        buf.write("\7e\2\2\u01b5\u01b6\7j\2\2\u01b6\u01b7\7g\2\2\u01b7\u01b8")
        buf.write("\7f\2\2\u01b8\u01b9\7w\2\2\u01b9\u01ba\7n\2\2\u01ba\u01bb")
        buf.write("\7g\2\2\u01bb\u01bc\7*\2\2\u01bc(\3\2\2\2\u01bd\u01be")
        buf.write("\7u\2\2\u01be\u01bf\7v\2\2\u01bf\u01c0\7c\2\2\u01c0\u01c1")
        buf.write("\7v\2\2\u01c1\u01c2\7k\2\2\u01c2\u01dc\7e\2\2\u01c3\u01c4")
        buf.write("\7f\2\2\u01c4\u01c5\7{\2\2\u01c5\u01c6\7p\2\2\u01c6\u01c7")
        buf.write("\7c\2\2\u01c7\u01c8\7o\2\2\u01c8\u01c9\7k\2\2\u01c9\u01dc")
        buf.write("\7e\2\2\u01ca\u01cb\7i\2\2\u01cb\u01cc\7w\2\2\u01cc\u01cd")
        buf.write("\7k\2\2\u01cd\u01ce\7f\2\2\u01ce\u01cf\7g\2\2\u01cf\u01dc")
        buf.write("\7f\2\2\u01d0\u01d1\7c\2\2\u01d1\u01d2\7w\2\2\u01d2\u01d3")
        buf.write("\7v\2\2\u01d3\u01dc\7q\2\2\u01d4\u01d5\7t\2\2\u01d5\u01d6")
        buf.write("\7w\2\2\u01d6\u01d7\7p\2\2\u01d7\u01d8\7v\2\2\u01d8\u01d9")
        buf.write("\7k\2\2\u01d9\u01da\7o\2\2\u01da\u01dc\7g\2\2\u01db\u01bd")
        buf.write("\3\2\2\2\u01db\u01c3\3\2\2\2\u01db\u01ca\3\2\2\2\u01db")
        buf.write("\u01d0\3\2\2\2\u01db\u01d4\3\2\2\2\u01dc*\3\2\2\2\u01dd")
        buf.write("\u01e0\5{>\2\u01de\u01e0\5}?\2\u01df\u01dd\3\2\2\2\u01df")
        buf.write("\u01de\3\2\2\2\u01e0,\3\2\2\2\u01e1\u01e5\5/\30\2\u01e2")
        buf.write("\u01e5\5\u0087D\2\u01e3\u01e5\5\u0089E\2\u01e4\u01e1\3")
        buf.write("\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5.")
        buf.write("\3\2\2\2\u01e6\u01eb\5\177@\2\u01e7\u01eb\5\u0081A\2\u01e8")
        buf.write("\u01eb\5\u0083B\2\u01e9\u01eb\5\u0085C\2\u01ea\u01e6\3")
        buf.write("\2\2\2\u01ea\u01e7\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01e9")
        buf.write("\3\2\2\2\u01eb\60\3\2\2\2\u01ec\u01ed\7f\2\2\u01ed\u01ee")
        buf.write("\7g\2\2\u01ee\u01ef\7h\2\2\u01ef\62\3\2\2\2\u01f0\u01f1")
        buf.write("\7t\2\2\u01f1\u01f2\7g\2\2\u01f2\u01f3\7v\2\2\u01f3\u01f4")
        buf.write("\7w\2\2\u01f4\u01f5\7t\2\2\u01f5\u01f6\7p\2\2\u01f6\64")
        buf.write("\3\2\2\2\u01f7\u01f8\7t\2\2\u01f8\u01f9\7c\2\2\u01f9\u01fa")
        buf.write("\7k\2\2\u01fa\u01fb\7u\2\2\u01fb\u01fc\7g\2\2\u01fc\66")
        buf.write("\3\2\2\2\u01fd\u01fe\7h\2\2\u01fe\u01ff\7t\2\2\u01ff\u0200")
        buf.write("\7q\2\2\u0200\u0201\7o\2\2\u02018\3\2\2\2\u0202\u0203")
        buf.write("\7k\2\2\u0203\u0204\7o\2\2\u0204\u0205\7r\2\2\u0205\u0206")
        buf.write("\7q\2\2\u0206\u0207\7t\2\2\u0207\u0208\7v\2\2\u0208:\3")
        buf.write("\2\2\2\u0209\u020a\7c\2\2\u020a\u020b\7u\2\2\u020b<\3")
        buf.write("\2\2\2\u020c\u020d\7i\2\2\u020d\u020e\7n\2\2\u020e\u020f")
        buf.write("\7q\2\2\u020f\u0210\7d\2\2\u0210\u0211\7c\2\2\u0211\u0212")
        buf.write("\7n\2\2\u0212>\3\2\2\2\u0213\u0214\7p\2\2\u0214\u0215")
        buf.write("\7q\2\2\u0215\u0216\7p\2\2\u0216\u0217\7n\2\2\u0217\u0218")
        buf.write("\7q\2\2\u0218\u0219\7e\2\2\u0219\u021a\7c\2\2\u021a\u021b")
        buf.write("\7n\2\2\u021b@\3\2\2\2\u021c\u021d\7c\2\2\u021d\u021e")
        buf.write("\7u\2\2\u021e\u021f\7u\2\2\u021f\u0220\7g\2\2\u0220\u0221")
        buf.write("\7t\2\2\u0221\u0222\7v\2\2\u0222B\3\2\2\2\u0223\u0224")
        buf.write("\7k\2\2\u0224\u0225\7h\2\2\u0225D\3\2\2\2\u0226\u0227")
        buf.write("\7g\2\2\u0227\u0228\7n\2\2\u0228\u0229\7k\2\2\u0229\u022a")
        buf.write("\7h\2\2\u022aF\3\2\2\2\u022b\u022c\7g\2\2\u022c\u022d")
        buf.write("\7n\2\2\u022d\u022e\7u\2\2\u022e\u022f\7g\2\2\u022fH\3")
        buf.write("\2\2\2\u0230\u0231\7y\2\2\u0231\u0232\7j\2\2\u0232\u0233")
        buf.write("\7k\2\2\u0233\u0234\7n\2\2\u0234\u0235\7g\2\2\u0235J\3")
        buf.write("\2\2\2\u0236\u0237\7h\2\2\u0237\u0238\7q\2\2\u0238\u0239")
        buf.write("\7t\2\2\u0239L\3\2\2\2\u023a\u023b\7k\2\2\u023b\u023c")
        buf.write("\7p\2\2\u023cN\3\2\2\2\u023d\u023e\7v\2\2\u023e\u023f")
        buf.write("\7t\2\2\u023f\u0240\7{\2\2\u0240P\3\2\2\2\u0241\u0242")
        buf.write("\7h\2\2\u0242\u0243\7k\2\2\u0243\u0244\7p\2\2\u0244\u0245")
        buf.write("\7c\2\2\u0245\u0246\7n\2\2\u0246\u0247\7n\2\2\u0247\u0248")
        buf.write("\7{\2\2\u0248R\3\2\2\2\u0249\u024a\7y\2\2\u024a\u024b")
        buf.write("\7k\2\2\u024b\u024c\7v\2\2\u024c\u024d\7j\2\2\u024dT\3")
        buf.write("\2\2\2\u024e\u024f\7g\2\2\u024f\u0250\7z\2\2\u0250\u0251")
        buf.write("\7e\2\2\u0251\u0252\7g\2\2\u0252\u0253\7r\2\2\u0253\u0254")
        buf.write("\7v\2\2\u0254V\3\2\2\2\u0255\u0256\7n\2\2\u0256\u0257")
        buf.write("\7c\2\2\u0257\u0258\7o\2\2\u0258\u0259\7d\2\2\u0259\u025a")
        buf.write("\7f\2\2\u025a\u025b\7c\2\2\u025bX\3\2\2\2\u025c\u025d")
        buf.write("\7q\2\2\u025d\u025e\7t\2\2\u025eZ\3\2\2\2\u025f\u0260")
        buf.write("\7c\2\2\u0260\u0261\7p\2\2\u0261\u0262\7f\2\2\u0262\\")
        buf.write("\3\2\2\2\u0263\u0264\7p\2\2\u0264\u0265\7q\2\2\u0265\u0266")
        buf.write("\7v\2\2\u0266^\3\2\2\2\u0267\u0268\7k\2\2\u0268\u0269")
        buf.write("\7u\2\2\u0269`\3\2\2\2\u026a\u026b\7P\2\2\u026b\u026c")
        buf.write("\7q\2\2\u026c\u026d\7p\2\2\u026d\u026e\7g\2\2\u026eb\3")
        buf.write("\2\2\2\u026f\u0270\7V\2\2\u0270\u0271\7t\2\2\u0271\u0272")
        buf.write("\7w\2\2\u0272\u0273\7g\2\2\u0273d\3\2\2\2\u0274\u0275")
        buf.write("\7H\2\2\u0275\u0276\7c\2\2\u0276\u0277\7n\2\2\u0277\u0278")
        buf.write("\7u\2\2\u0278\u0279\7g\2\2\u0279f\3\2\2\2\u027a\u027b")
        buf.write("\7e\2\2\u027b\u027c\7n\2\2\u027c\u027d\7c\2\2\u027d\u027e")
        buf.write("\7u\2\2\u027e\u027f\7u\2\2\u027fh\3\2\2\2\u0280\u0281")
        buf.write("\7{\2\2\u0281\u0282\7k\2\2\u0282\u0283\7g\2\2\u0283\u0284")
        buf.write("\7n\2\2\u0284\u0285\7f\2\2\u0285j\3\2\2\2\u0286\u0287")
        buf.write("\7f\2\2\u0287\u0288\7g\2\2\u0288\u0289\7n\2\2\u0289l\3")
        buf.write("\2\2\2\u028a\u028b\7r\2\2\u028b\u028c\7c\2\2\u028c\u028d")
        buf.write("\7u\2\2\u028d\u028e\7u\2\2\u028en\3\2\2\2\u028f\u0290")
        buf.write("\7e\2\2\u0290\u0291\7q\2\2\u0291\u0292\7p\2\2\u0292\u0293")
        buf.write("\7v\2\2\u0293\u0294\7k\2\2\u0294\u0295\7p\2\2\u0295\u0296")
        buf.write("\7w\2\2\u0296\u0297\7g\2\2\u0297p\3\2\2\2\u0298\u0299")
        buf.write("\7d\2\2\u0299\u029a\7t\2\2\u029a\u029b\7g\2\2\u029b\u029c")
        buf.write("\7c\2\2\u029c\u029d\7m\2\2\u029dr\3\2\2\2\u029e\u029f")
        buf.write("\7c\2\2\u029f\u02a0\7u\2\2\u02a0\u02a1\7{\2\2\u02a1\u02a2")
        buf.write("\7p\2\2\u02a2\u02a3\7e\2\2\u02a3t\3\2\2\2\u02a4\u02a5")
        buf.write("\7c\2\2\u02a5\u02a6\7y\2\2\u02a6\u02a7\7c\2\2\u02a7\u02a8")
        buf.write("\7k\2\2\u02a8\u02a9\7v\2\2\u02a9v\3\2\2\2\u02aa\u02ab")
        buf.write("\6<\2\2\u02ab\u02b7\5\u0119\u008d\2\u02ac\u02ae\7\17\2")
        buf.write("\2\u02ad\u02ac\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u02af")
        buf.write("\3\2\2\2\u02af\u02b2\7\f\2\2\u02b0\u02b2\4\16\17\2\u02b1")
        buf.write("\u02ad\3\2\2\2\u02b1\u02b0\3\2\2\2\u02b2\u02b4\3\2\2\2")
        buf.write("\u02b3\u02b5\5\u0119\u008d\2\u02b4\u02b3\3\2\2\2\u02b4")
        buf.write("\u02b5\3\2\2\2\u02b5\u02b7\3\2\2\2\u02b6\u02aa\3\2\2\2")
        buf.write("\u02b6\u02b1\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02b9\b")
        buf.write("<\2\2\u02b9x\3\2\2\2\u02ba\u02be\5\u011f\u0090\2\u02bb")
        buf.write("\u02bd\5\u0121\u0091\2\u02bc\u02bb\3\2\2\2\u02bd\u02c0")
        buf.write("\3\2\2\2\u02be\u02bc\3\2\2\2\u02be\u02bf\3\2\2\2\u02bf")
        buf.write("z\3\2\2\2\u02c0\u02be\3\2\2\2\u02c1\u02c7\t\2\2\2\u02c2")
        buf.write("\u02c3\t\3\2\2\u02c3\u02c7\t\4\2\2\u02c4\u02c5\t\4\2\2")
        buf.write("\u02c5\u02c7\t\3\2\2\u02c6\u02c1\3\2\2\2\u02c6\u02c2\3")
        buf.write("\2\2\2\u02c6\u02c4\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c7\u02ca")
        buf.write("\3\2\2\2\u02c8\u02cb\5\u00edw\2\u02c9\u02cb\5\u00efx\2")
        buf.write("\u02ca\u02c8\3\2\2\2\u02ca\u02c9\3\2\2\2\u02cb|\3\2\2")
        buf.write("\2\u02cc\u02d2\t\5\2\2\u02cd\u02ce\t\5\2\2\u02ce\u02d2")
        buf.write("\t\4\2\2\u02cf\u02d0\t\4\2\2\u02d0\u02d2\t\5\2\2\u02d1")
        buf.write("\u02cc\3\2\2\2\u02d1\u02cd\3\2\2\2\u02d1\u02cf\3\2\2\2")
        buf.write("\u02d2\u02d5\3\2\2\2\u02d3\u02d6\5\u010b\u0086\2\u02d4")
        buf.write("\u02d6\5\u010d\u0087\2\u02d5\u02d3\3\2\2\2\u02d5\u02d4")
        buf.write("\3\2\2\2\u02d6~\3\2\2\2\u02d7\u02db\5\u00f7|\2\u02d8\u02da")
        buf.write("\5\u00f9}\2\u02d9\u02d8\3\2\2\2\u02da\u02dd\3\2\2\2\u02db")
        buf.write("\u02d9\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc\u02e4\3\2\2\2")
        buf.write("\u02dd\u02db\3\2\2\2\u02de\u02e0\7\62\2\2\u02df\u02de")
        buf.write("\3\2\2\2\u02e0\u02e1\3\2\2\2\u02e1\u02df\3\2\2\2\u02e1")
        buf.write("\u02e2\3\2\2\2\u02e2\u02e4\3\2\2\2\u02e3\u02d7\3\2\2\2")
        buf.write("\u02e3\u02df\3\2\2\2\u02e4\u0080\3\2\2\2\u02e5\u02e6\7")
        buf.write("\62\2\2\u02e6\u02e8\t\6\2\2\u02e7\u02e9\5\u00fb~\2\u02e8")
        buf.write("\u02e7\3\2\2\2\u02e9\u02ea\3\2\2\2\u02ea\u02e8\3\2\2\2")
        buf.write("\u02ea\u02eb\3\2\2\2\u02eb\u0082\3\2\2\2\u02ec\u02ed\7")
        buf.write("\62\2\2\u02ed\u02ef\t\7\2\2\u02ee\u02f0\5\u00fd\177\2")
        buf.write("\u02ef\u02ee\3\2\2\2\u02f0\u02f1\3\2\2\2\u02f1\u02ef\3")
        buf.write("\2\2\2\u02f1\u02f2\3\2\2\2\u02f2\u0084\3\2\2\2\u02f3\u02f4")
        buf.write("\7\62\2\2\u02f4\u02f6\t\5\2\2\u02f5\u02f7\5\u00ff\u0080")
        buf.write("\2\u02f6\u02f5\3\2\2\2\u02f7\u02f8\3\2\2\2\u02f8\u02f6")
        buf.write("\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9\u0086\3\2\2\2\u02fa")
        buf.write("\u02fd\5\u0101\u0081\2\u02fb\u02fd\5\u0103\u0082\2\u02fc")
        buf.write("\u02fa\3\2\2\2\u02fc\u02fb\3\2\2\2\u02fd\u0088\3\2\2\2")
        buf.write("\u02fe\u0301\5\u0087D\2\u02ff\u0301\5\u0105\u0083\2\u0300")
        buf.write("\u02fe\3\2\2\2\u0300\u02ff\3\2\2\2\u0301\u0302\3\2\2\2")
        buf.write("\u0302\u0303\t\b\2\2\u0303\u008a\3\2\2\2\u0304\u0305\7")
        buf.write("\60\2\2\u0305\u008c\3\2\2\2\u0306\u0307\7\60\2\2\u0307")
        buf.write("\u0308\7\60\2\2\u0308\u0309\7\60\2\2\u0309\u008e\3\2\2")
        buf.write("\2\u030a\u030b\7,\2\2\u030b\u0090\3\2\2\2\u030c\u030d")
        buf.write("\7*\2\2\u030d\u030e\bI\3\2\u030e\u0092\3\2\2\2\u030f\u0310")
        buf.write("\7+\2\2\u0310\u0311\bJ\4\2\u0311\u0094\3\2\2\2\u0312\u0313")
        buf.write("\7.\2\2\u0313\u0096\3\2\2\2\u0314\u0315\7<\2\2\u0315\u0098")
        buf.write("\3\2\2\2\u0316\u0317\7=\2\2\u0317\u009a\3\2\2\2\u0318")
        buf.write("\u0319\7,\2\2\u0319\u031a\7,\2\2\u031a\u009c\3\2\2\2\u031b")
        buf.write("\u031c\7?\2\2\u031c\u009e\3\2\2\2\u031d\u031e\7]\2\2\u031e")
        buf.write("\u031f\bP\5\2\u031f\u00a0\3\2\2\2\u0320\u0321\7_\2\2\u0321")
        buf.write("\u0322\bQ\6\2\u0322\u00a2\3\2\2\2\u0323\u0324\7~\2\2\u0324")
        buf.write("\u00a4\3\2\2\2\u0325\u0326\7`\2\2\u0326\u00a6\3\2\2\2")
        buf.write("\u0327\u0328\7(\2\2\u0328\u00a8\3\2\2\2\u0329\u032a\7")
        buf.write(">\2\2\u032a\u032b\7>\2\2\u032b\u00aa\3\2\2\2\u032c\u032d")
        buf.write("\7@\2\2\u032d\u032e\7@\2\2\u032e\u00ac\3\2\2\2\u032f\u0330")
        buf.write("\7-\2\2\u0330\u00ae\3\2\2\2\u0331\u0332\7/\2\2\u0332\u00b0")
        buf.write("\3\2\2\2\u0333\u0334\7\61\2\2\u0334\u00b2\3\2\2\2\u0335")
        buf.write("\u0336\7\'\2\2\u0336\u00b4\3\2\2\2\u0337\u0338\7\61\2")
        buf.write("\2\u0338\u0339\7\61\2\2\u0339\u00b6\3\2\2\2\u033a\u033b")
        buf.write("\7\u0080\2\2\u033b\u00b8\3\2\2\2\u033c\u033d\7}\2\2\u033d")
        buf.write("\u033e\b]\7\2\u033e\u00ba\3\2\2\2\u033f\u0340\7\177\2")
        buf.write("\2\u0340\u0341\b^\b\2\u0341\u00bc\3\2\2\2\u0342\u0343")
        buf.write("\7>\2\2\u0343\u00be\3\2\2\2\u0344\u0345\7@\2\2\u0345\u00c0")
        buf.write("\3\2\2\2\u0346\u0347\7?\2\2\u0347\u0348\7?\2\2\u0348\u00c2")
        buf.write("\3\2\2\2\u0349\u034a\7@\2\2\u034a\u034b\7?\2\2\u034b\u00c4")
        buf.write("\3\2\2\2\u034c\u034d\7>\2\2\u034d\u034e\7?\2\2\u034e\u00c6")
        buf.write("\3\2\2\2\u034f\u0350\7>\2\2\u0350\u0351\7@\2\2\u0351\u00c8")
        buf.write("\3\2\2\2\u0352\u0353\7#\2\2\u0353\u0354\7?\2\2\u0354\u00ca")
        buf.write("\3\2\2\2\u0355\u0356\7B\2\2\u0356\u00cc\3\2\2\2\u0357")
        buf.write("\u0358\7/\2\2\u0358\u0359\7@\2\2\u0359\u00ce\3\2\2\2\u035a")
        buf.write("\u035b\7-\2\2\u035b\u035c\7?\2\2\u035c\u00d0\3\2\2\2\u035d")
        buf.write("\u035e\7/\2\2\u035e\u035f\7?\2\2\u035f\u00d2\3\2\2\2\u0360")
        buf.write("\u0361\7,\2\2\u0361\u0362\7?\2\2\u0362\u00d4\3\2\2\2\u0363")
        buf.write("\u0364\7B\2\2\u0364\u0365\7?\2\2\u0365\u00d6\3\2\2\2\u0366")
        buf.write("\u0367\7\61\2\2\u0367\u0368\7?\2\2\u0368\u00d8\3\2\2\2")
        buf.write("\u0369\u036a\7\'\2\2\u036a\u036b\7?\2\2\u036b\u00da\3")
        buf.write("\2\2\2\u036c\u036d\7(\2\2\u036d\u036e\7?\2\2\u036e\u00dc")
        buf.write("\3\2\2\2\u036f\u0370\7~\2\2\u0370\u0371\7?\2\2\u0371\u00de")
        buf.write("\3\2\2\2\u0372\u0373\7`\2\2\u0373\u0374\7?\2\2\u0374\u00e0")
        buf.write("\3\2\2\2\u0375\u0376\7>\2\2\u0376\u0377\7>\2\2\u0377\u0378")
        buf.write("\7?\2\2\u0378\u00e2\3\2\2\2\u0379\u037a\7@\2\2\u037a\u037b")
        buf.write("\7@\2\2\u037b\u037c\7?\2\2\u037c\u00e4\3\2\2\2\u037d\u037e")
        buf.write("\7,\2\2\u037e\u037f\7,\2\2\u037f\u0380\7?\2\2\u0380\u00e6")
        buf.write("\3\2\2\2\u0381\u0382\7\61\2\2\u0382\u0383\7\61\2\2\u0383")
        buf.write("\u0384\7?\2\2\u0384\u00e8\3\2\2\2\u0385\u0389\5\u0119")
        buf.write("\u008d\2\u0386\u0389\5\u011b\u008e\2\u0387\u0389\5\u011d")
        buf.write("\u008f\2\u0388\u0385\3\2\2\2\u0388\u0386\3\2\2\2\u0388")
        buf.write("\u0387\3\2\2\2\u0389\u038a\3\2\2\2\u038a\u038b\bu\t\2")
        buf.write("\u038b\u00ea\3\2\2\2\u038c\u038d\13\2\2\2\u038d\u00ec")
        buf.write("\3\2\2\2\u038e\u0393\7)\2\2\u038f\u0392\5\u00f5{\2\u0390")
        buf.write("\u0392\n\t\2\2\u0391\u038f\3\2\2\2\u0391\u0390\3\2\2\2")
        buf.write("\u0392\u0395\3\2\2\2\u0393\u0391\3\2\2\2\u0393\u0394\3")
        buf.write("\2\2\2\u0394\u0396\3\2\2\2\u0395\u0393\3\2\2\2\u0396\u03a1")
        buf.write("\7)\2\2\u0397\u039c\7$\2\2\u0398\u039b\5\u00f5{\2\u0399")
        buf.write("\u039b\n\n\2\2\u039a\u0398\3\2\2\2\u039a\u0399\3\2\2\2")
        buf.write("\u039b\u039e\3\2\2\2\u039c\u039a\3\2\2\2\u039c\u039d\3")
        buf.write("\2\2\2\u039d\u039f\3\2\2\2\u039e\u039c\3\2\2\2\u039f\u03a1")
        buf.write("\7$\2\2\u03a0\u038e\3\2\2\2\u03a0\u0397\3\2\2\2\u03a1")
        buf.write("\u00ee\3\2\2\2\u03a2\u03a3\7)\2\2\u03a3\u03a4\7)\2\2\u03a4")
        buf.write("\u03a5\7)\2\2\u03a5\u03a9\3\2\2\2\u03a6\u03a8\5\u00f1")
        buf.write("y\2\u03a7\u03a6\3\2\2\2\u03a8\u03ab\3\2\2\2\u03a9\u03aa")
        buf.write("\3\2\2\2\u03a9\u03a7\3\2\2\2\u03aa\u03ac\3\2\2\2\u03ab")
        buf.write("\u03a9\3\2\2\2\u03ac\u03ad\7)\2\2\u03ad\u03ae\7)\2\2\u03ae")
        buf.write("\u03bd\7)\2\2\u03af\u03b0\7$\2\2\u03b0\u03b1\7$\2\2\u03b1")
        buf.write("\u03b2\7$\2\2\u03b2\u03b6\3\2\2\2\u03b3\u03b5\5\u00f1")
        buf.write("y\2\u03b4\u03b3\3\2\2\2\u03b5\u03b8\3\2\2\2\u03b6\u03b7")
        buf.write("\3\2\2\2\u03b6\u03b4\3\2\2\2\u03b7\u03b9\3\2\2\2\u03b8")
        buf.write("\u03b6\3\2\2\2\u03b9\u03ba\7$\2\2\u03ba\u03bb\7$\2\2\u03bb")
        buf.write("\u03bd\7$\2\2\u03bc\u03a2\3\2\2\2\u03bc\u03af\3\2\2\2")
        buf.write("\u03bd\u00f0\3\2\2\2\u03be\u03c1\5\u00f3z\2\u03bf\u03c1")
        buf.write("\5\u00f5{\2\u03c0\u03be\3\2\2\2\u03c0\u03bf\3\2\2\2\u03c1")
        buf.write("\u00f2\3\2\2\2\u03c2\u03c3\n\13\2\2\u03c3\u00f4\3\2\2")
        buf.write("\2\u03c4\u03c5\7^\2\2\u03c5\u03c9\13\2\2\2\u03c6\u03c7")
        buf.write("\7^\2\2\u03c7\u03c9\5w<\2\u03c8\u03c4\3\2\2\2\u03c8\u03c6")
        buf.write("\3\2\2\2\u03c9\u00f6\3\2\2\2\u03ca\u03cb\t\f\2\2\u03cb")
        buf.write("\u00f8\3\2\2\2\u03cc\u03cd\t\r\2\2\u03cd\u00fa\3\2\2\2")
        buf.write("\u03ce\u03cf\t\16\2\2\u03cf\u00fc\3\2\2\2\u03d0\u03d1")
        buf.write("\t\17\2\2\u03d1\u00fe\3\2\2\2\u03d2\u03d3\t\20\2\2\u03d3")
        buf.write("\u0100\3\2\2\2\u03d4\u03d6\5\u0105\u0083\2\u03d5\u03d4")
        buf.write("\3\2\2\2\u03d5\u03d6\3\2\2\2\u03d6\u03d7\3\2\2\2\u03d7")
        buf.write("\u03dc\5\u0107\u0084\2\u03d8\u03d9\5\u0105\u0083\2\u03d9")
        buf.write("\u03da\7\60\2\2\u03da\u03dc\3\2\2\2\u03db\u03d5\3\2\2")
        buf.write("\2\u03db\u03d8\3\2\2\2\u03dc\u0102\3\2\2\2\u03dd\u03e0")
        buf.write("\5\u0105\u0083\2\u03de\u03e0\5\u0101\u0081\2\u03df\u03dd")
        buf.write("\3\2\2\2\u03df\u03de\3\2\2\2\u03e0\u03e1\3\2\2\2\u03e1")
        buf.write("\u03e2\5\u0109\u0085\2\u03e2\u0104\3\2\2\2\u03e3\u03e5")
        buf.write("\5\u00f9}\2\u03e4\u03e3\3\2\2\2\u03e5\u03e6\3\2\2\2\u03e6")
        buf.write("\u03e4\3\2\2\2\u03e6\u03e7\3\2\2\2\u03e7\u0106\3\2\2\2")
        buf.write("\u03e8\u03ea\7\60\2\2\u03e9\u03eb\5\u00f9}\2\u03ea\u03e9")
        buf.write("\3\2\2\2\u03eb\u03ec\3\2\2\2\u03ec\u03ea\3\2\2\2\u03ec")
        buf.write("\u03ed\3\2\2\2\u03ed\u0108\3\2\2\2\u03ee\u03f0\t\21\2")
        buf.write("\2\u03ef\u03f1\t\22\2\2\u03f0\u03ef\3\2\2\2\u03f0\u03f1")
        buf.write("\3\2\2\2\u03f1\u03f3\3\2\2\2\u03f2\u03f4\5\u00f9}\2\u03f3")
        buf.write("\u03f2\3\2\2\2\u03f4\u03f5\3\2\2\2\u03f5\u03f3\3\2\2\2")
        buf.write("\u03f5\u03f6\3\2\2\2\u03f6\u010a\3\2\2\2\u03f7\u03fc\7")
        buf.write(")\2\2\u03f8\u03fb\5\u0111\u0089\2\u03f9\u03fb\5\u0117")
        buf.write("\u008c\2\u03fa\u03f8\3\2\2\2\u03fa\u03f9\3\2\2\2\u03fb")
        buf.write("\u03fe\3\2\2\2\u03fc\u03fa\3\2\2\2\u03fc\u03fd\3\2\2\2")
        buf.write("\u03fd\u03ff\3\2\2\2\u03fe\u03fc\3\2\2\2\u03ff\u040a\7")
        buf.write(")\2\2\u0400\u0405\7$\2\2\u0401\u0404\5\u0113\u008a\2\u0402")
        buf.write("\u0404\5\u0117\u008c\2\u0403\u0401\3\2\2\2\u0403\u0402")
        buf.write("\3\2\2\2\u0404\u0407\3\2\2\2\u0405\u0403\3\2\2\2\u0405")
        buf.write("\u0406\3\2\2\2\u0406\u0408\3\2\2\2\u0407\u0405\3\2\2\2")
        buf.write("\u0408\u040a\7$\2\2\u0409\u03f7\3\2\2\2\u0409\u0400\3")
        buf.write("\2\2\2\u040a\u010c\3\2\2\2\u040b\u040c\7)\2\2\u040c\u040d")
        buf.write("\7)\2\2\u040d\u040e\7)\2\2\u040e\u0412\3\2\2\2\u040f\u0411")
        buf.write("\5\u010f\u0088\2\u0410\u040f\3\2\2\2\u0411\u0414\3\2\2")
        buf.write("\2\u0412\u0413\3\2\2\2\u0412\u0410\3\2\2\2\u0413\u0415")
        buf.write("\3\2\2\2\u0414\u0412\3\2\2\2\u0415\u0416\7)\2\2\u0416")
        buf.write("\u0417\7)\2\2\u0417\u0426\7)\2\2\u0418\u0419\7$\2\2\u0419")
        buf.write("\u041a\7$\2\2\u041a\u041b\7$\2\2\u041b\u041f\3\2\2\2\u041c")
        buf.write("\u041e\5\u010f\u0088\2\u041d\u041c\3\2\2\2\u041e\u0421")
        buf.write("\3\2\2\2\u041f\u0420\3\2\2\2\u041f\u041d\3\2\2\2\u0420")
        buf.write("\u0422\3\2\2\2\u0421\u041f\3\2\2\2\u0422\u0423\7$\2\2")
        buf.write("\u0423\u0424\7$\2\2\u0424\u0426\7$\2\2\u0425\u040b\3\2")
        buf.write("\2\2\u0425\u0418\3\2\2\2\u0426\u010e\3\2\2\2\u0427\u042a")
        buf.write("\5\u0115\u008b\2\u0428\u042a\5\u0117\u008c\2\u0429\u0427")
        buf.write("\3\2\2\2\u0429\u0428\3\2\2\2\u042a\u0110\3\2\2\2\u042b")
        buf.write("\u042d\t\23\2\2\u042c\u042b\3\2\2\2\u042d\u0112\3\2\2")
        buf.write("\2\u042e\u0430\t\24\2\2\u042f\u042e\3\2\2\2\u0430\u0114")
        buf.write("\3\2\2\2\u0431\u0433\t\25\2\2\u0432\u0431\3\2\2\2\u0433")
        buf.write("\u0116\3\2\2\2\u0434\u0435\7^\2\2\u0435\u0436\t\26\2\2")
        buf.write("\u0436\u0118\3\2\2\2\u0437\u0439\t\27\2\2\u0438\u0437")
        buf.write("\3\2\2\2\u0439\u043a\3\2\2\2\u043a\u0438\3\2\2\2\u043a")
        buf.write("\u043b\3\2\2\2\u043b\u011a\3\2\2\2\u043c\u043d\7%\2\2")
        buf.write("\u043d\u0441\n\30\2\2\u043e\u0440\n\31\2\2\u043f\u043e")
        buf.write("\3\2\2\2\u0440\u0443\3\2\2\2\u0441\u043f\3\2\2\2\u0441")
        buf.write("\u0442\3\2\2\2\u0442\u045a\3\2\2\2\u0443\u0441\3\2\2\2")
        buf.write("\u0444\u0445\7%\2\2\u0445\u0446\7q\2\2\u0446\u0447\3\2")
        buf.write("\2\2\u0447\u044b\n\32\2\2\u0448\u044a\n\31\2\2\u0449\u0448")
        buf.write("\3\2\2\2\u044a\u044d\3\2\2\2\u044b\u0449\3\2\2\2\u044b")
        buf.write("\u044c\3\2\2\2\u044c\u045a\3\2\2\2\u044d\u044b\3\2\2\2")
        buf.write("\u044e\u044f\7%\2\2\u044f\u0450\7q\2\2\u0450\u0451\7o")
        buf.write("\2\2\u0451\u0452\3\2\2\2\u0452\u0456\n\33\2\2\u0453\u0455")
        buf.write("\n\31\2\2\u0454\u0453\3\2\2\2\u0455\u0458\3\2\2\2\u0456")
        buf.write("\u0454\3\2\2\2\u0456\u0457\3\2\2\2\u0457\u045a\3\2\2\2")
        buf.write("\u0458\u0456\3\2\2\2\u0459\u043c\3\2\2\2\u0459\u0444\3")
        buf.write("\2\2\2\u0459\u044e\3\2\2\2\u045a\u011c\3\2\2\2\u045b\u045d")
        buf.write("\7^\2\2\u045c\u045e\5\u0119\u008d\2\u045d\u045c\3\2\2")
        buf.write("\2\u045d\u045e\3\2\2\2\u045e\u0464\3\2\2\2\u045f\u0461")
        buf.write("\7\17\2\2\u0460\u045f\3\2\2\2\u0460\u0461\3\2\2\2\u0461")
        buf.write("\u0462\3\2\2\2\u0462\u0465\7\f\2\2\u0463\u0465\4\16\17")
        buf.write("\2\u0464\u0460\3\2\2\2\u0464\u0463\3\2\2\2\u0465\u011e")
        buf.write("\3\2\2\2\u0466\u0468\t\34\2\2\u0467\u0466\3\2\2\2\u0468")
        buf.write("\u0120\3\2\2\2\u0469\u046c\5\u011f\u0090\2\u046a\u046c")
        buf.write("\t\35\2\2\u046b\u0469\3\2\2\2\u046b\u046a\3\2\2\2\u046c")
        buf.write("\u0122\3\2\2\2@\2\u01db\u01df\u01e4\u01ea\u02ad\u02b1")
        buf.write("\u02b4\u02b6\u02be\u02c6\u02ca\u02d1\u02d5\u02db\u02e1")
        buf.write("\u02e3\u02ea\u02f1\u02f8\u02fc\u0300\u0388\u0391\u0393")
        buf.write("\u039a\u039c\u03a0\u03a9\u03b6\u03bc\u03c0\u03c8\u03d5")
        buf.write("\u03db\u03df\u03e6\u03ec\u03f0\u03f5\u03fa\u03fc\u0403")
        buf.write("\u0405\u0409\u0412\u041f\u0425\u0429\u042c\u042f\u0432")
        buf.write("\u043a\u0441\u044b\u0456\u0459\u045d\u0460\u0464\u0467")
        buf.write("\u046b\n\3<\2\3I\3\3J\4\3P\5\3Q\6\3]\7\3^\b\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    SCHEDULE = 20
    STRING = 21
    NUMBER = 22
    INTEGER = 23
    DEF = 24
    RETURN = 25
    RAISE = 26
    FROM = 27
    IMPORT = 28
    AS = 29
    GLOBAL = 30
    NONLOCAL = 31
    ASSERT = 32
    IF = 33
    ELIF = 34
    ELSE = 35
    WHILE = 36
    FOR = 37
    IN = 38
    TRY = 39
    FINALLY = 40
    WITH = 41
    EXCEPT = 42
    LAMBDA = 43
    OR = 44
    AND = 45
    NOT = 46
    IS = 47
    NONE = 48
    TRUE = 49
    FALSE = 50
    CLASS = 51
    YIELD = 52
    DEL = 53
    PASS = 54
    CONTINUE = 55
    BREAK = 56
    ASYNC = 57
    AWAIT = 58
    NEWLINE = 59
    NAME = 60
    STRING_LITERAL = 61
    BYTES_LITERAL = 62
    DECIMAL_INTEGER = 63
    OCT_INTEGER = 64
    HEX_INTEGER = 65
    BIN_INTEGER = 66
    FLOAT_NUMBER = 67
    IMAG_NUMBER = 68
    DOT = 69
    ELLIPSIS = 70
    STAR = 71
    OPEN_PAREN = 72
    CLOSE_PAREN = 73
    COMMA = 74
    COLON = 75
    SEMI_COLON = 76
    POWER = 77
    ASSIGN = 78
    OPEN_BRACK = 79
    CLOSE_BRACK = 80
    OR_OP = 81
    XOR = 82
    AND_OP = 83
    LEFT_SHIFT = 84
    RIGHT_SHIFT = 85
    ADD = 86
    MINUS = 87
    DIV = 88
    MOD = 89
    IDIV = 90
    NOT_OP = 91
    OPEN_BRACE = 92
    CLOSE_BRACE = 93
    LESS_THAN = 94
    GREATER_THAN = 95
    EQUALS = 96
    GT_EQ = 97
    LT_EQ = 98
    NOT_EQ_1 = 99
    NOT_EQ_2 = 100
    AT = 101
    ARROW = 102
    ADD_ASSIGN = 103
    SUB_ASSIGN = 104
    MULT_ASSIGN = 105
    AT_ASSIGN = 106
    DIV_ASSIGN = 107
    MOD_ASSIGN = 108
    AND_ASSIGN = 109
    OR_ASSIGN = 110
    XOR_ASSIGN = 111
    LEFT_SHIFT_ASSIGN = 112
    RIGHT_SHIFT_ASSIGN = 113
    POWER_ASSIGN = 114
    IDIV_ASSIGN = 115
    SKIP_ = 116
    UNKNOWN_CHAR = 117

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#omp'", "'parallel'", "'sections'", "'section'", "'master'", 
            "'single'", "'critical'", "'barrier'", "'num_threads('", "'shared('", 
            "'private('", "'firstprivate('", "'lastprivate('", "'reduction('", 
            "'min'", "'max'", "'&&'", "'||'", "'schedule('", "'def'", "'return'", 
            "'raise'", "'from'", "'import'", "'as'", "'global'", "'nonlocal'", 
            "'assert'", "'if'", "'elif'", "'else'", "'while'", "'for'", 
            "'in'", "'try'", "'finally'", "'with'", "'except'", "'lambda'", 
            "'or'", "'and'", "'not'", "'is'", "'None'", "'True'", "'False'", 
            "'class'", "'yield'", "'del'", "'pass'", "'continue'", "'break'", 
            "'async'", "'await'", "'.'", "'...'", "'*'", "'('", "')'", "','", 
            "':'", "';'", "'**'", "'='", "'['", "']'", "'|'", "'^'", "'&'", 
            "'<<'", "'>>'", "'+'", "'-'", "'/'", "'%'", "'//'", "'~'", "'{'", 
            "'}'", "'<'", "'>'", "'=='", "'>='", "'<='", "'<>'", "'!='", 
            "'@'", "'->'", "'+='", "'-='", "'*='", "'@='", "'/='", "'%='", 
            "'&='", "'|='", "'^='", "'<<='", "'>>='", "'**='", "'//='" ]

    symbolicNames = [ "<INVALID>",
            "SCHEDULE", "STRING", "NUMBER", "INTEGER", "DEF", "RETURN", 
            "RAISE", "FROM", "IMPORT", "AS", "GLOBAL", "NONLOCAL", "ASSERT", 
            "IF", "ELIF", "ELSE", "WHILE", "FOR", "IN", "TRY", "FINALLY", 
            "WITH", "EXCEPT", "LAMBDA", "OR", "AND", "NOT", "IS", "NONE", 
            "TRUE", "FALSE", "CLASS", "YIELD", "DEL", "PASS", "CONTINUE", 
            "BREAK", "ASYNC", "AWAIT", "NEWLINE", "NAME", "STRING_LITERAL", 
            "BYTES_LITERAL", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
            "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER", "DOT", "ELLIPSIS", 
            "STAR", "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
            "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", 
            "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "DIV", 
            "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", "LESS_THAN", 
            "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", 
            "AT", "ARROW", "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", 
            "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", 
            "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", 
            "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "SCHEDULE", 
                  "STRING", "NUMBER", "INTEGER", "DEF", "RETURN", "RAISE", 
                  "FROM", "IMPORT", "AS", "GLOBAL", "NONLOCAL", "ASSERT", 
                  "IF", "ELIF", "ELSE", "WHILE", "FOR", "IN", "TRY", "FINALLY", 
                  "WITH", "EXCEPT", "LAMBDA", "OR", "AND", "NOT", "IS", 
                  "NONE", "TRUE", "FALSE", "CLASS", "YIELD", "DEL", "PASS", 
                  "CONTINUE", "BREAK", "ASYNC", "AWAIT", "NEWLINE", "NAME", 
                  "STRING_LITERAL", "BYTES_LITERAL", "DECIMAL_INTEGER", 
                  "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
                  "IMAG_NUMBER", "DOT", "ELLIPSIS", "STAR", "OPEN_PAREN", 
                  "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", "POWER", 
                  "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", 
                  "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
                  "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", 
                  "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", 
                  "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
                  "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", 
                  "UNKNOWN_CHAR", "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM", 
                  "LONG_STRING_CHAR", "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", 
                  "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", 
                  "EXPONENT_FLOAT", "INT_PART", "FRACTION", "EXPONENT", 
                  "SHORT_BYTES", "LONG_BYTES", "LONG_BYTES_ITEM", "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", 
                  "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", "LONG_BYTES_CHAR", 
                  "BYTES_ESCAPE_SEQ", "SPACES", "COMMENT", "LINE_JOINING", 
                  "ID_START", "ID_CONTINUE" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens
    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents
    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened
    @opened.setter
    def opened(self, value):
        self._opened = value
    @property
    def lastToken(self):
        try:
            return self._lastToken
        except AttributeError:
            self._lastToken = None
            return self._lastToken
    @lastToken.setter
    def lastToken(self, value):
        self._lastToken = value
    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.lastToken = None
    def emitToken(self, t):
        super().emitToken(t)
        self.tokens.append(t)
    def nextToken(self):
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)
            self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()
            self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next
        return next if not self.tokens else self.tokens.pop(0)
    def createDedent(self):
        dedent = self.commonToken(LanguageParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent
    def commonToken(self, type, text, indent=0):
        stop = self.getCharIndex()-1-indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)
    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count
    def atStartOfInput(self):
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.NEWLINE_action 
            actions[71] = self.OPEN_PAREN_action 
            actions[72] = self.CLOSE_PAREN_action 
            actions[78] = self.OPEN_BRACK_action 
            actions[79] = self.CLOSE_BRACK_action 
            actions[91] = self.OPEN_BRACE_action 
            actions[92] = self.CLOSE_BRACE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            tempt = Lexer.text.fget(self)
            newLine = re.sub("[^\r\n\f]+", "", tempt)
            spaces = re.sub("[\r\n\f]+", "", tempt)
            la_char = ""
            try:
                la = self._input.LA(1)
                la_char = chr(la)       # Python does not compare char to ints directly
            except ValueError:          # End of file
                pass
            # Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
            # satisfy the final newline needed by the single_put rule used by the REPL.
            try:
                nextnext_la = self._input.LA(2)
                nextnext_la_char = chr(nextnext_la)
                la_o = nextnext_la_char
            except ValueError:
                nextnext_eof = True
            else:
                nextnext_eof = False
            '''
            try:
                la_m = chr(self._input.LA(3))
                la_p = chr(self._input.LA(4))
            except ValueError:
                omp_la_failed = True
            else:
                omp_la_failed = False'''


            try:
                la_o = chr(self._input.LA(2))
                la_m = chr(self._input.LA(3))
                la_p = chr(self._input.LA(4))
            except ValueError:
                omp_comment = False
            else:
                if la_o == 'o' and la_m == 'm' and la_p == 'p':
                    omp_comment = True
                else:
                    omp_comment = False


            if self.opened > 0 or nextnext_eof is False and (la_char == '\r' or la_char == '\n' or la_char == '\f' or (la_char == '#' and not omp_comment)): #(omp_la_failed or (la_o != 'o' or la_m != 'm' or la_p != 'p')))):
                self.skip()
            else:
                indent = self.getIndentationCount(spaces)
                previous = self.indents[-1] if self.indents else 0
                self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.createDedent())
                        self.indents.pop()
                
     

    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.opened += 1
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.opened -= 1
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.opened += 1
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.opened -= 1
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.opened += 1
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.opened -= 1
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[58] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


