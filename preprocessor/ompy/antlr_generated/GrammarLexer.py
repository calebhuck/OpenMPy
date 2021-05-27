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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2x")
        buf.write("\u0476\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\4\u0092\t\u0092\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u01e5\n\26\3\27\3\27\5\27\u01e9\n")
        buf.write("\27\3\30\3\30\3\30\5\30\u01ee\n\30\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u01f4\n\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\38\38\39\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3")
        buf.write(":\3:\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\5=\u02b7")
        buf.write("\n=\3=\3=\5=\u02bb\n=\3=\5=\u02be\n=\5=\u02c0\n=\3=\3")
        buf.write("=\3>\3>\7>\u02c6\n>\f>\16>\u02c9\13>\3?\3?\3?\3?\3?\5")
        buf.write("?\u02d0\n?\3?\3?\5?\u02d4\n?\3@\3@\3@\3@\3@\5@\u02db\n")
        buf.write("@\3@\3@\5@\u02df\n@\3A\3A\7A\u02e3\nA\fA\16A\u02e6\13")
        buf.write("A\3A\6A\u02e9\nA\rA\16A\u02ea\5A\u02ed\nA\3B\3B\3B\6B")
        buf.write("\u02f2\nB\rB\16B\u02f3\3C\3C\3C\6C\u02f9\nC\rC\16C\u02fa")
        buf.write("\3D\3D\3D\6D\u0300\nD\rD\16D\u0301\3E\3E\5E\u0306\nE\3")
        buf.write("F\3F\5F\u030a\nF\3F\3F\3G\3G\3H\3H\3H\3H\3I\3I\3J\3J\3")
        buf.write("J\3K\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3O\3P\3P\3Q\3Q\3Q\3")
        buf.write("R\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3V\3W\3W\3W\3X\3X\3Y\3")
        buf.write("Y\3Z\3Z\3[\3[\3\\\3\\\3\\\3]\3]\3^\3^\3^\3_\3_\3_\3`\3")
        buf.write("`\3a\3a\3b\3b\3b\3c\3c\3c\3d\3d\3d\3e\3e\3e\3f\3f\3f\3")
        buf.write("g\3g\3h\3h\3h\3i\3i\3i\3j\3j\3j\3k\3k\3k\3l\3l\3l\3m\3")
        buf.write("m\3m\3n\3n\3n\3o\3o\3o\3p\3p\3p\3q\3q\3q\3r\3r\3r\3r\3")
        buf.write("s\3s\3s\3s\3t\3t\3t\3t\3u\3u\3u\3u\3v\3v\3v\5v\u0392\n")
        buf.write("v\3v\3v\3w\3w\3x\3x\3x\7x\u039b\nx\fx\16x\u039e\13x\3")
        buf.write("x\3x\3x\3x\7x\u03a4\nx\fx\16x\u03a7\13x\3x\5x\u03aa\n")
        buf.write("x\3y\3y\3y\3y\3y\7y\u03b1\ny\fy\16y\u03b4\13y\3y\3y\3")
        buf.write("y\3y\3y\3y\3y\3y\7y\u03be\ny\fy\16y\u03c1\13y\3y\3y\3")
        buf.write("y\5y\u03c6\ny\3z\3z\5z\u03ca\nz\3{\3{\3|\3|\3|\3|\5|\u03d2")
        buf.write("\n|\3}\3}\3~\3~\3\177\3\177\3\u0080\3\u0080\3\u0081\3")
        buf.write("\u0081\3\u0082\5\u0082\u03df\n\u0082\3\u0082\3\u0082\3")
        buf.write("\u0082\3\u0082\5\u0082\u03e5\n\u0082\3\u0083\3\u0083\5")
        buf.write("\u0083\u03e9\n\u0083\3\u0083\3\u0083\3\u0084\6\u0084\u03ee")
        buf.write("\n\u0084\r\u0084\16\u0084\u03ef\3\u0085\3\u0085\6\u0085")
        buf.write("\u03f4\n\u0085\r\u0085\16\u0085\u03f5\3\u0086\3\u0086")
        buf.write("\5\u0086\u03fa\n\u0086\3\u0086\6\u0086\u03fd\n\u0086\r")
        buf.write("\u0086\16\u0086\u03fe\3\u0087\3\u0087\3\u0087\7\u0087")
        buf.write("\u0404\n\u0087\f\u0087\16\u0087\u0407\13\u0087\3\u0087")
        buf.write("\3\u0087\3\u0087\3\u0087\7\u0087\u040d\n\u0087\f\u0087")
        buf.write("\16\u0087\u0410\13\u0087\3\u0087\5\u0087\u0413\n\u0087")
        buf.write("\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\7\u0088\u041a")
        buf.write("\n\u0088\f\u0088\16\u0088\u041d\13\u0088\3\u0088\3\u0088")
        buf.write("\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\7\u0088")
        buf.write("\u0427\n\u0088\f\u0088\16\u0088\u042a\13\u0088\3\u0088")
        buf.write("\3\u0088\3\u0088\5\u0088\u042f\n\u0088\3\u0089\3\u0089")
        buf.write("\5\u0089\u0433\n\u0089\3\u008a\5\u008a\u0436\n\u008a\3")
        buf.write("\u008b\5\u008b\u0439\n\u008b\3\u008c\5\u008c\u043c\n\u008c")
        buf.write("\3\u008d\3\u008d\3\u008d\3\u008e\6\u008e\u0442\n\u008e")
        buf.write("\r\u008e\16\u008e\u0443\3\u008f\3\u008f\3\u008f\7\u008f")
        buf.write("\u0449\n\u008f\f\u008f\16\u008f\u044c\13\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\7\u008f\u0453\n\u008f")
        buf.write("\f\u008f\16\u008f\u0456\13\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\7\u008f\u045e\n\u008f\f\u008f")
        buf.write("\16\u008f\u0461\13\u008f\5\u008f\u0463\n\u008f\3\u0090")
        buf.write("\3\u0090\5\u0090\u0467\n\u0090\3\u0090\5\u0090\u046a\n")
        buf.write("\u0090\3\u0090\3\u0090\5\u0090\u046e\n\u0090\3\u0091\5")
        buf.write("\u0091\u0471\n\u0091\3\u0092\3\u0092\5\u0092\u0475\n\u0092")
        buf.write("\6\u03b2\u03bf\u041b\u0428\2\u0093\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1")
        buf.write("R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00adX\u00afY\u00b1")
        buf.write("Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb_\u00bd`\u00bfa\u00c1")
        buf.write("b\u00c3c\u00c5d\u00c7e\u00c9f\u00cbg\u00cdh\u00cfi\u00d1")
        buf.write("j\u00d3k\u00d5l\u00d7m\u00d9n\u00dbo\u00ddp\u00dfq\u00e1")
        buf.write("r\u00e3s\u00e5t\u00e7u\u00e9v\u00ebw\u00edx\u00ef\2\u00f1")
        buf.write("\2\u00f3\2\u00f5\2\u00f7\2\u00f9\2\u00fb\2\u00fd\2\u00ff")
        buf.write("\2\u0101\2\u0103\2\u0105\2\u0107\2\u0109\2\u010b\2\u010d")
        buf.write("\2\u010f\2\u0111\2\u0113\2\u0115\2\u0117\2\u0119\2\u011b")
        buf.write("\2\u011d\2\u011f\2\u0121\2\u0123\2\3\2\36\b\2HHTTWWhh")
        buf.write("ttww\4\2HHhh\4\2TTtt\4\2DDdd\4\2QQqq\4\2ZZzz\4\2LLll\6")
        buf.write("\2\f\f\16\17))^^\6\2\f\f\16\17$$^^\3\2^^\3\2\63;\3\2\62")
        buf.write(";\3\2\629\5\2\62;CHch\3\2\62\63\4\2GGgg\4\2--//\7\2\2")
        buf.write("\13\r\16\20(*]_\u0081\7\2\2\13\r\16\20#%]_\u0081\4\2\2")
        buf.write("]_\u0081\3\2\2\u0081\4\2\13\13\"\"\3\2qq\4\2\f\f\16\17")
        buf.write("\3\2oo\3\2rr\u0129\2C\\aac|\u00ac\u00ac\u00b7\u00b7\u00bc")
        buf.write("\u00bc\u00c2\u00d8\u00da\u00f8\u00fa\u0243\u0252\u02c3")
        buf.write("\u02c8\u02d3\u02e2\u02e6\u02f0\u02f0\u037c\u037c\u0388")
        buf.write("\u0388\u038a\u038c\u038e\u038e\u0390\u03a3\u03a5\u03d0")
        buf.write("\u03d2\u03f7\u03f9\u0483\u048c\u04d0\u04d2\u04fb\u0502")
        buf.write("\u0511\u0533\u0558\u055b\u055b\u0563\u0589\u05d2\u05ec")
        buf.write("\u05f2\u05f4\u0623\u063c\u0642\u064c\u0670\u0671\u0673")
        buf.write("\u06d5\u06d7\u06d7\u06e7\u06e8\u06f0\u06f1\u06fc\u06fe")
        buf.write("\u0701\u0701\u0712\u0712\u0714\u0731\u074f\u076f\u0782")
        buf.write("\u07a7\u07b3\u07b3\u0906\u093b\u093f\u093f\u0952\u0952")
        buf.write("\u095a\u0963\u097f\u097f\u0987\u098e\u0991\u0992\u0995")
        buf.write("\u09aa\u09ac\u09b2\u09b4\u09b4\u09b8\u09bb\u09bf\u09bf")
        buf.write("\u09d0\u09d0\u09de\u09df\u09e1\u09e3\u09f2\u09f3\u0a07")
        buf.write("\u0a0c\u0a11\u0a12\u0a15\u0a2a\u0a2c\u0a32\u0a34\u0a35")
        buf.write("\u0a37\u0a38\u0a3a\u0a3b\u0a5b\u0a5e\u0a60\u0a60\u0a74")
        buf.write("\u0a76\u0a87\u0a8f\u0a91\u0a93\u0a95\u0aaa\u0aac\u0ab2")
        buf.write("\u0ab4\u0ab5\u0ab7\u0abb\u0abf\u0abf\u0ad2\u0ad2\u0ae2")
        buf.write("\u0ae3\u0b07\u0b0e\u0b11\u0b12\u0b15\u0b2a\u0b2c\u0b32")
        buf.write("\u0b34\u0b35\u0b37\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f\u0b61")
        buf.write("\u0b63\u0b73\u0b73\u0b85\u0b85\u0b87\u0b8c\u0b90\u0b92")
        buf.write("\u0b94\u0b97\u0b9b\u0b9c\u0b9e\u0b9e\u0ba0\u0ba1\u0ba5")
        buf.write("\u0ba6\u0baa\u0bac\u0bb0\u0bbb\u0c07\u0c0e\u0c10\u0c12")
        buf.write("\u0c14\u0c2a\u0c2c\u0c35\u0c37\u0c3b\u0c62\u0c63\u0c87")
        buf.write("\u0c8e\u0c90\u0c92\u0c94\u0caa\u0cac\u0cb5\u0cb7\u0cbb")
        buf.write("\u0cbf\u0cbf\u0ce0\u0ce0\u0ce2\u0ce3\u0d07\u0d0e\u0d10")
        buf.write("\u0d12\u0d14\u0d2a\u0d2c\u0d3b\u0d62\u0d63\u0d87\u0d98")
        buf.write("\u0d9c\u0db3\u0db5\u0dbd\u0dbf\u0dbf\u0dc2\u0dc8\u0e03")
        buf.write("\u0e32\u0e34\u0e35\u0e42\u0e48\u0e83\u0e84\u0e86\u0e86")
        buf.write("\u0e89\u0e8a\u0e8c\u0e8c\u0e8f\u0e8f\u0e96\u0e99\u0e9b")
        buf.write("\u0ea1\u0ea3\u0ea5\u0ea7\u0ea7\u0ea9\u0ea9\u0eac\u0ead")
        buf.write("\u0eaf\u0eb2\u0eb4\u0eb5\u0ebf\u0ebf\u0ec2\u0ec6\u0ec8")
        buf.write("\u0ec8\u0ede\u0edf\u0f02\u0f02\u0f42\u0f49\u0f4b\u0f6c")
        buf.write("\u0f8a\u0f8d\u1002\u1023\u1025\u1029\u102b\u102c\u1052")
        buf.write("\u1057\u10a2\u10c7\u10d2\u10fc\u10fe\u10fe\u1102\u115b")
        buf.write("\u1161\u11a4\u11aa\u11fb\u1202\u124a\u124c\u124f\u1252")
        buf.write("\u1258\u125a\u125a\u125c\u125f\u1262\u128a\u128c\u128f")
        buf.write("\u1292\u12b2\u12b4\u12b7\u12ba\u12c0\u12c2\u12c2\u12c4")
        buf.write("\u12c7\u12ca\u12d8\u12da\u1312\u1314\u1317\u131a\u135c")
        buf.write("\u1382\u1391\u13a2\u13f6\u1403\u166e\u1671\u1678\u1683")
        buf.write("\u169c\u16a2\u16ec\u16f0\u16f2\u1702\u170e\u1710\u1713")
        buf.write("\u1722\u1733\u1742\u1753\u1762\u176e\u1770\u1772\u1782")
        buf.write("\u17b5\u17d9\u17d9\u17de\u17de\u1822\u1879\u1882\u18aa")
        buf.write("\u1902\u191e\u1952\u196f\u1972\u1976\u1982\u19ab\u19c3")
        buf.write("\u19c9\u1a02\u1a18\u1d02\u1dc1\u1e02\u1e9d\u1ea2\u1efb")
        buf.write("\u1f02\u1f17\u1f1a\u1f1f\u1f22\u1f47\u1f4a\u1f4f\u1f52")
        buf.write("\u1f59\u1f5b\u1f5b\u1f5d\u1f5d\u1f5f\u1f5f\u1f61\u1f7f")
        buf.write("\u1f82\u1fb6\u1fb8\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8")
        buf.write("\u1fce\u1fd2\u1fd5\u1fd8\u1fdd\u1fe2\u1fee\u1ff4\u1ff6")
        buf.write("\u1ff8\u1ffe\u2073\u2073\u2081\u2081\u2092\u2096\u2104")
        buf.write("\u2104\u2109\u2109\u210c\u2115\u2117\u2117\u211a\u211f")
        buf.write("\u2126\u2126\u2128\u2128\u212a\u212a\u212c\u2133\u2135")
        buf.write("\u213b\u213e\u2141\u2147\u214b\u2162\u2185\u2c02\u2c30")
        buf.write("\u2c32\u2c60\u2c82\u2ce6\u2d02\u2d27\u2d32\u2d67\u2d71")
        buf.write("\u2d71\u2d82\u2d98\u2da2\u2da8\u2daa\u2db0\u2db2\u2db8")
        buf.write("\u2dba\u2dc0\u2dc2\u2dc8\u2dca\u2dd0\u2dd2\u2dd8\u2dda")
        buf.write("\u2de0\u3007\u3009\u3023\u302b\u3033\u3037\u303a\u303e")
        buf.write("\u3043\u3098\u309d\u30a1\u30a3\u30fc\u30fe\u3101\u3107")
        buf.write("\u312e\u3133\u3190\u31a2\u31b9\u31f2\u3201\u3402\u4db7")
        buf.write("\u4e02\u9fbd\ua002\ua48e\ua802\ua803\ua805\ua807\ua809")
        buf.write("\ua80c\ua80e\ua824\uac02\ud7a5\uf902\ufa2f\ufa32\ufa6c")
        buf.write("\ufa72\ufadb\ufb02\ufb08\ufb15\ufb19\ufb1f\ufb1f\ufb21")
        buf.write("\ufb2a\ufb2c\ufb38\ufb3a\ufb3e\ufb40\ufb40\ufb42\ufb43")
        buf.write("\ufb45\ufb46\ufb48\ufbb3\ufbd5\ufd3f\ufd52\ufd91\ufd94")
        buf.write("\ufdc9\ufdf2\ufdfd\ufe72\ufe76\ufe78\ufefe\uff23\uff3c")
        buf.write("\uff43\uff5c\uff68\uffc0\uffc4\uffc9\uffcc\uffd1\uffd4")
        buf.write("\uffd9\uffdc\uffde\u0096\2\62;\u0302\u0371\u0485\u0488")
        buf.write("\u0593\u05bb\u05bd\u05bf\u05c1\u05c1\u05c3\u05c4\u05c6")
        buf.write("\u05c7\u05c9\u05c9\u0612\u0617\u064d\u0660\u0662\u066b")
        buf.write("\u0672\u0672\u06d8\u06de\u06e1\u06e6\u06e9\u06ea\u06ec")
        buf.write("\u06ef\u06f2\u06fb\u0713\u0713\u0732\u074c\u07a8\u07b2")
        buf.write("\u0903\u0905\u093e\u093e\u0940\u094f\u0953\u0956\u0964")
        buf.write("\u0965\u0968\u0971\u0983\u0985\u09be\u09be\u09c0\u09c6")
        buf.write("\u09c9\u09ca\u09cd\u09cf\u09d9\u09d9\u09e4\u09e5\u09e8")
        buf.write("\u09f1\u0a03\u0a05\u0a3e\u0a3e\u0a40\u0a44\u0a49\u0a4a")
        buf.write("\u0a4d\u0a4f\u0a68\u0a73\u0a83\u0a85\u0abe\u0abe\u0ac0")
        buf.write("\u0ac7\u0ac9\u0acb\u0acd\u0acf\u0ae4\u0ae5\u0ae8\u0af1")
        buf.write("\u0b03\u0b05\u0b3e\u0b3e\u0b40\u0b45\u0b49\u0b4a\u0b4d")
        buf.write("\u0b4f\u0b58\u0b59\u0b68\u0b71\u0b84\u0b84\u0bc0\u0bc4")
        buf.write("\u0bc8\u0bca\u0bcc\u0bcf\u0bd9\u0bd9\u0be8\u0bf1\u0c03")
        buf.write("\u0c05\u0c40\u0c46\u0c48\u0c4a\u0c4c\u0c4f\u0c57\u0c58")
        buf.write("\u0c68\u0c71\u0c84\u0c85\u0cbe\u0cbe\u0cc0\u0cc6\u0cc8")
        buf.write("\u0cca\u0ccc\u0ccf\u0cd7\u0cd8\u0ce8\u0cf1\u0d04\u0d05")
        buf.write("\u0d40\u0d45\u0d48\u0d4a\u0d4c\u0d4f\u0d59\u0d59\u0d68")
        buf.write("\u0d71\u0d84\u0d85\u0dcc\u0dcc\u0dd1\u0dd6\u0dd8\u0dd8")
        buf.write("\u0dda\u0de1\u0df4\u0df5\u0e33\u0e33\u0e36\u0e3c\u0e49")
        buf.write("\u0e50\u0e52\u0e5b\u0eb3\u0eb3\u0eb6\u0ebb\u0ebd\u0ebe")
        buf.write("\u0eca\u0ecf\u0ed2\u0edb\u0f1a\u0f1b\u0f22\u0f2b\u0f37")
        buf.write("\u0f37\u0f39\u0f39\u0f3b\u0f3b\u0f40\u0f41\u0f73\u0f86")
        buf.write("\u0f88\u0f89\u0f92\u0f99\u0f9b\u0fbe\u0fc8\u0fc8\u102e")
        buf.write("\u1034\u1038\u103b\u1042\u104b\u1058\u105b\u1361\u1361")
        buf.write("\u136b\u1373\u1714\u1716\u1734\u1736\u1754\u1755\u1774")
        buf.write("\u1775\u17b8\u17d5\u17df\u17df\u17e2\u17eb\u180d\u180f")
        buf.write("\u1812\u181b\u18ab\u18ab\u1922\u192d\u1932\u193d\u1948")
        buf.write("\u1951\u19b2\u19c2\u19ca\u19cb\u19d2\u19db\u1a19\u1a1d")
        buf.write("\u1dc2\u1dc5\u2041\u2042\u2056\u2056\u20d2\u20de\u20e3")
        buf.write("\u20e3\u20e7\u20ed\u302c\u3031\u309b\u309c\ua804\ua804")
        buf.write("\ua808\ua808\ua80d\ua80d\ua825\ua829\ufb20\ufb20\ufe02")
        buf.write("\ufe11\ufe22\ufe25\ufe35\ufe36\ufe4f\ufe51\uff12\uff1b")
        buf.write("\uff41\uff41\2\u049e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2")
        buf.write("\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf")
        buf.write("\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2")
        buf.write("\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd")
        buf.write("\3\2\2\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2")
        buf.write("\2\2\u00d5\3\2\2\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2\2\2\u00db")
        buf.write("\3\2\2\2\2\u00dd\3\2\2\2\2\u00df\3\2\2\2\2\u00e1\3\2\2")
        buf.write("\2\2\u00e3\3\2\2\2\2\u00e5\3\2\2\2\2\u00e7\3\2\2\2\2\u00e9")
        buf.write("\3\2\2\2\2\u00eb\3\2\2\2\2\u00ed\3\2\2\2\3\u0125\3\2\2")
        buf.write("\2\5\u012a\3\2\2\2\7\u0133\3\2\2\2\t\u013c\3\2\2\2\13")
        buf.write("\u0144\3\2\2\2\r\u014b\3\2\2\2\17\u0152\3\2\2\2\21\u015b")
        buf.write("\3\2\2\2\23\u0163\3\2\2\2\25\u016a\3\2\2\2\27\u0177\3")
        buf.write("\2\2\2\31\u017f\3\2\2\2\33\u0188\3\2\2\2\35\u0196\3\2")
        buf.write("\2\2\37\u01a3\3\2\2\2!\u01ae\3\2\2\2#\u01b2\3\2\2\2%\u01b6")
        buf.write("\3\2\2\2\'\u01b9\3\2\2\2)\u01bc\3\2\2\2+\u01e4\3\2\2\2")
        buf.write("-\u01e8\3\2\2\2/\u01ed\3\2\2\2\61\u01f3\3\2\2\2\63\u01f5")
        buf.write("\3\2\2\2\65\u01f9\3\2\2\2\67\u0200\3\2\2\29\u0206\3\2")
        buf.write("\2\2;\u020b\3\2\2\2=\u0212\3\2\2\2?\u0215\3\2\2\2A\u021c")
        buf.write("\3\2\2\2C\u0225\3\2\2\2E\u022c\3\2\2\2G\u022f\3\2\2\2")
        buf.write("I\u0234\3\2\2\2K\u0239\3\2\2\2M\u023f\3\2\2\2O\u0243\3")
        buf.write("\2\2\2Q\u0246\3\2\2\2S\u024a\3\2\2\2U\u0252\3\2\2\2W\u0257")
        buf.write("\3\2\2\2Y\u025e\3\2\2\2[\u0265\3\2\2\2]\u0268\3\2\2\2")
        buf.write("_\u026c\3\2\2\2a\u0270\3\2\2\2c\u0273\3\2\2\2e\u0278\3")
        buf.write("\2\2\2g\u027d\3\2\2\2i\u0283\3\2\2\2k\u0289\3\2\2\2m\u028f")
        buf.write("\3\2\2\2o\u0293\3\2\2\2q\u0298\3\2\2\2s\u02a1\3\2\2\2")
        buf.write("u\u02a7\3\2\2\2w\u02ad\3\2\2\2y\u02bf\3\2\2\2{\u02c3\3")
        buf.write("\2\2\2}\u02cf\3\2\2\2\177\u02da\3\2\2\2\u0081\u02ec\3")
        buf.write("\2\2\2\u0083\u02ee\3\2\2\2\u0085\u02f5\3\2\2\2\u0087\u02fc")
        buf.write("\3\2\2\2\u0089\u0305\3\2\2\2\u008b\u0309\3\2\2\2\u008d")
        buf.write("\u030d\3\2\2\2\u008f\u030f\3\2\2\2\u0091\u0313\3\2\2\2")
        buf.write("\u0093\u0315\3\2\2\2\u0095\u0318\3\2\2\2\u0097\u031b\3")
        buf.write("\2\2\2\u0099\u031d\3\2\2\2\u009b\u031f\3\2\2\2\u009d\u0321")
        buf.write("\3\2\2\2\u009f\u0324\3\2\2\2\u00a1\u0326\3\2\2\2\u00a3")
        buf.write("\u0329\3\2\2\2\u00a5\u032c\3\2\2\2\u00a7\u032e\3\2\2\2")
        buf.write("\u00a9\u0330\3\2\2\2\u00ab\u0332\3\2\2\2\u00ad\u0335\3")
        buf.write("\2\2\2\u00af\u0338\3\2\2\2\u00b1\u033a\3\2\2\2\u00b3\u033c")
        buf.write("\3\2\2\2\u00b5\u033e\3\2\2\2\u00b7\u0340\3\2\2\2\u00b9")
        buf.write("\u0343\3\2\2\2\u00bb\u0345\3\2\2\2\u00bd\u0348\3\2\2\2")
        buf.write("\u00bf\u034b\3\2\2\2\u00c1\u034d\3\2\2\2\u00c3\u034f\3")
        buf.write("\2\2\2\u00c5\u0352\3\2\2\2\u00c7\u0355\3\2\2\2\u00c9\u0358")
        buf.write("\3\2\2\2\u00cb\u035b\3\2\2\2\u00cd\u035e\3\2\2\2\u00cf")
        buf.write("\u0360\3\2\2\2\u00d1\u0363\3\2\2\2\u00d3\u0366\3\2\2\2")
        buf.write("\u00d5\u0369\3\2\2\2\u00d7\u036c\3\2\2\2\u00d9\u036f\3")
        buf.write("\2\2\2\u00db\u0372\3\2\2\2\u00dd\u0375\3\2\2\2\u00df\u0378")
        buf.write("\3\2\2\2\u00e1\u037b\3\2\2\2\u00e3\u037e\3\2\2\2\u00e5")
        buf.write("\u0382\3\2\2\2\u00e7\u0386\3\2\2\2\u00e9\u038a\3\2\2\2")
        buf.write("\u00eb\u0391\3\2\2\2\u00ed\u0395\3\2\2\2\u00ef\u03a9\3")
        buf.write("\2\2\2\u00f1\u03c5\3\2\2\2\u00f3\u03c9\3\2\2\2\u00f5\u03cb")
        buf.write("\3\2\2\2\u00f7\u03d1\3\2\2\2\u00f9\u03d3\3\2\2\2\u00fb")
        buf.write("\u03d5\3\2\2\2\u00fd\u03d7\3\2\2\2\u00ff\u03d9\3\2\2\2")
        buf.write("\u0101\u03db\3\2\2\2\u0103\u03e4\3\2\2\2\u0105\u03e8\3")
        buf.write("\2\2\2\u0107\u03ed\3\2\2\2\u0109\u03f1\3\2\2\2\u010b\u03f7")
        buf.write("\3\2\2\2\u010d\u0412\3\2\2\2\u010f\u042e\3\2\2\2\u0111")
        buf.write("\u0432\3\2\2\2\u0113\u0435\3\2\2\2\u0115\u0438\3\2\2\2")
        buf.write("\u0117\u043b\3\2\2\2\u0119\u043d\3\2\2\2\u011b\u0441\3")
        buf.write("\2\2\2\u011d\u0462\3\2\2\2\u011f\u0464\3\2\2\2\u0121\u0470")
        buf.write("\3\2\2\2\u0123\u0474\3\2\2\2\u0125\u0126\7%\2\2\u0126")
        buf.write("\u0127\7q\2\2\u0127\u0128\7o\2\2\u0128\u0129\7r\2\2\u0129")
        buf.write("\4\3\2\2\2\u012a\u012b\7r\2\2\u012b\u012c\7c\2\2\u012c")
        buf.write("\u012d\7t\2\2\u012d\u012e\7c\2\2\u012e\u012f\7n\2\2\u012f")
        buf.write("\u0130\7n\2\2\u0130\u0131\7g\2\2\u0131\u0132\7n\2\2\u0132")
        buf.write("\6\3\2\2\2\u0133\u0134\7u\2\2\u0134\u0135\7g\2\2\u0135")
        buf.write("\u0136\7e\2\2\u0136\u0137\7v\2\2\u0137\u0138\7k\2\2\u0138")
        buf.write("\u0139\7q\2\2\u0139\u013a\7p\2\2\u013a\u013b\7u\2\2\u013b")
        buf.write("\b\3\2\2\2\u013c\u013d\7u\2\2\u013d\u013e\7g\2\2\u013e")
        buf.write("\u013f\7e\2\2\u013f\u0140\7v\2\2\u0140\u0141\7k\2\2\u0141")
        buf.write("\u0142\7q\2\2\u0142\u0143\7p\2\2\u0143\n\3\2\2\2\u0144")
        buf.write("\u0145\7o\2\2\u0145\u0146\7c\2\2\u0146\u0147\7u\2\2\u0147")
        buf.write("\u0148\7v\2\2\u0148\u0149\7g\2\2\u0149\u014a\7t\2\2\u014a")
        buf.write("\f\3\2\2\2\u014b\u014c\7u\2\2\u014c\u014d\7k\2\2\u014d")
        buf.write("\u014e\7p\2\2\u014e\u014f\7i\2\2\u014f\u0150\7n\2\2\u0150")
        buf.write("\u0151\7g\2\2\u0151\16\3\2\2\2\u0152\u0153\7e\2\2\u0153")
        buf.write("\u0154\7t\2\2\u0154\u0155\7k\2\2\u0155\u0156\7v\2\2\u0156")
        buf.write("\u0157\7k\2\2\u0157\u0158\7e\2\2\u0158\u0159\7c\2\2\u0159")
        buf.write("\u015a\7n\2\2\u015a\20\3\2\2\2\u015b\u015c\7d\2\2\u015c")
        buf.write("\u015d\7c\2\2\u015d\u015e\7t\2\2\u015e\u015f\7t\2\2\u015f")
        buf.write("\u0160\7k\2\2\u0160\u0161\7g\2\2\u0161\u0162\7t\2\2\u0162")
        buf.write("\22\3\2\2\2\u0163\u0164\7c\2\2\u0164\u0165\7v\2\2\u0165")
        buf.write("\u0166\7q\2\2\u0166\u0167\7o\2\2\u0167\u0168\7k\2\2\u0168")
        buf.write("\u0169\7e\2\2\u0169\24\3\2\2\2\u016a\u016b\7p\2\2\u016b")
        buf.write("\u016c\7w\2\2\u016c\u016d\7o\2\2\u016d\u016e\7a\2\2\u016e")
        buf.write("\u016f\7v\2\2\u016f\u0170\7j\2\2\u0170\u0171\7t\2\2\u0171")
        buf.write("\u0172\7g\2\2\u0172\u0173\7c\2\2\u0173\u0174\7f\2\2\u0174")
        buf.write("\u0175\7u\2\2\u0175\u0176\7*\2\2\u0176\26\3\2\2\2\u0177")
        buf.write("\u0178\7u\2\2\u0178\u0179\7j\2\2\u0179\u017a\7c\2\2\u017a")
        buf.write("\u017b\7t\2\2\u017b\u017c\7g\2\2\u017c\u017d\7f\2\2\u017d")
        buf.write("\u017e\7*\2\2\u017e\30\3\2\2\2\u017f\u0180\7r\2\2\u0180")
        buf.write("\u0181\7t\2\2\u0181\u0182\7k\2\2\u0182\u0183\7x\2\2\u0183")
        buf.write("\u0184\7c\2\2\u0184\u0185\7v\2\2\u0185\u0186\7g\2\2\u0186")
        buf.write("\u0187\7*\2\2\u0187\32\3\2\2\2\u0188\u0189\7h\2\2\u0189")
        buf.write("\u018a\7k\2\2\u018a\u018b\7t\2\2\u018b\u018c\7u\2\2\u018c")
        buf.write("\u018d\7v\2\2\u018d\u018e\7r\2\2\u018e\u018f\7t\2\2\u018f")
        buf.write("\u0190\7k\2\2\u0190\u0191\7x\2\2\u0191\u0192\7c\2\2\u0192")
        buf.write("\u0193\7v\2\2\u0193\u0194\7g\2\2\u0194\u0195\7*\2\2\u0195")
        buf.write("\34\3\2\2\2\u0196\u0197\7n\2\2\u0197\u0198\7c\2\2\u0198")
        buf.write("\u0199\7u\2\2\u0199\u019a\7v\2\2\u019a\u019b\7r\2\2\u019b")
        buf.write("\u019c\7t\2\2\u019c\u019d\7k\2\2\u019d\u019e\7x\2\2\u019e")
        buf.write("\u019f\7c\2\2\u019f\u01a0\7v\2\2\u01a0\u01a1\7g\2\2\u01a1")
        buf.write("\u01a2\7*\2\2\u01a2\36\3\2\2\2\u01a3\u01a4\7t\2\2\u01a4")
        buf.write("\u01a5\7g\2\2\u01a5\u01a6\7f\2\2\u01a6\u01a7\7w\2\2\u01a7")
        buf.write("\u01a8\7e\2\2\u01a8\u01a9\7v\2\2\u01a9\u01aa\7k\2\2\u01aa")
        buf.write("\u01ab\7q\2\2\u01ab\u01ac\7p\2\2\u01ac\u01ad\7*\2\2\u01ad")
        buf.write(" \3\2\2\2\u01ae\u01af\7o\2\2\u01af\u01b0\7k\2\2\u01b0")
        buf.write("\u01b1\7p\2\2\u01b1\"\3\2\2\2\u01b2\u01b3\7o\2\2\u01b3")
        buf.write("\u01b4\7c\2\2\u01b4\u01b5\7z\2\2\u01b5$\3\2\2\2\u01b6")
        buf.write("\u01b7\7(\2\2\u01b7\u01b8\7(\2\2\u01b8&\3\2\2\2\u01b9")
        buf.write("\u01ba\7~\2\2\u01ba\u01bb\7~\2\2\u01bb(\3\2\2\2\u01bc")
        buf.write("\u01bd\7u\2\2\u01bd\u01be\7e\2\2\u01be\u01bf\7j\2\2\u01bf")
        buf.write("\u01c0\7g\2\2\u01c0\u01c1\7f\2\2\u01c1\u01c2\7w\2\2\u01c2")
        buf.write("\u01c3\7n\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5\7*\2\2\u01c5")
        buf.write("*\3\2\2\2\u01c6\u01c7\7u\2\2\u01c7\u01c8\7v\2\2\u01c8")
        buf.write("\u01c9\7c\2\2\u01c9\u01ca\7v\2\2\u01ca\u01cb\7k\2\2\u01cb")
        buf.write("\u01e5\7e\2\2\u01cc\u01cd\7f\2\2\u01cd\u01ce\7{\2\2\u01ce")
        buf.write("\u01cf\7p\2\2\u01cf\u01d0\7c\2\2\u01d0\u01d1\7o\2\2\u01d1")
        buf.write("\u01d2\7k\2\2\u01d2\u01e5\7e\2\2\u01d3\u01d4\7i\2\2\u01d4")
        buf.write("\u01d5\7w\2\2\u01d5\u01d6\7k\2\2\u01d6\u01d7\7f\2\2\u01d7")
        buf.write("\u01d8\7g\2\2\u01d8\u01e5\7f\2\2\u01d9\u01da\7c\2\2\u01da")
        buf.write("\u01db\7w\2\2\u01db\u01dc\7v\2\2\u01dc\u01e5\7q\2\2\u01dd")
        buf.write("\u01de\7t\2\2\u01de\u01df\7w\2\2\u01df\u01e0\7p\2\2\u01e0")
        buf.write("\u01e1\7v\2\2\u01e1\u01e2\7k\2\2\u01e2\u01e3\7o\2\2\u01e3")
        buf.write("\u01e5\7g\2\2\u01e4\u01c6\3\2\2\2\u01e4\u01cc\3\2\2\2")
        buf.write("\u01e4\u01d3\3\2\2\2\u01e4\u01d9\3\2\2\2\u01e4\u01dd\3")
        buf.write("\2\2\2\u01e5,\3\2\2\2\u01e6\u01e9\5}?\2\u01e7\u01e9\5")
        buf.write("\177@\2\u01e8\u01e6\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9")
        buf.write(".\3\2\2\2\u01ea\u01ee\5\61\31\2\u01eb\u01ee\5\u0089E\2")
        buf.write("\u01ec\u01ee\5\u008bF\2\u01ed\u01ea\3\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ee\60\3\2\2\2\u01ef\u01f4")
        buf.write("\5\u0081A\2\u01f0\u01f4\5\u0083B\2\u01f1\u01f4\5\u0085")
        buf.write("C\2\u01f2\u01f4\5\u0087D\2\u01f3\u01ef\3\2\2\2\u01f3\u01f0")
        buf.write("\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4")
        buf.write("\62\3\2\2\2\u01f5\u01f6\7f\2\2\u01f6\u01f7\7g\2\2\u01f7")
        buf.write("\u01f8\7h\2\2\u01f8\64\3\2\2\2\u01f9\u01fa\7t\2\2\u01fa")
        buf.write("\u01fb\7g\2\2\u01fb\u01fc\7v\2\2\u01fc\u01fd\7w\2\2\u01fd")
        buf.write("\u01fe\7t\2\2\u01fe\u01ff\7p\2\2\u01ff\66\3\2\2\2\u0200")
        buf.write("\u0201\7t\2\2\u0201\u0202\7c\2\2\u0202\u0203\7k\2\2\u0203")
        buf.write("\u0204\7u\2\2\u0204\u0205\7g\2\2\u02058\3\2\2\2\u0206")
        buf.write("\u0207\7h\2\2\u0207\u0208\7t\2\2\u0208\u0209\7q\2\2\u0209")
        buf.write("\u020a\7o\2\2\u020a:\3\2\2\2\u020b\u020c\7k\2\2\u020c")
        buf.write("\u020d\7o\2\2\u020d\u020e\7r\2\2\u020e\u020f\7q\2\2\u020f")
        buf.write("\u0210\7t\2\2\u0210\u0211\7v\2\2\u0211<\3\2\2\2\u0212")
        buf.write("\u0213\7c\2\2\u0213\u0214\7u\2\2\u0214>\3\2\2\2\u0215")
        buf.write("\u0216\7i\2\2\u0216\u0217\7n\2\2\u0217\u0218\7q\2\2\u0218")
        buf.write("\u0219\7d\2\2\u0219\u021a\7c\2\2\u021a\u021b\7n\2\2\u021b")
        buf.write("@\3\2\2\2\u021c\u021d\7p\2\2\u021d\u021e\7q\2\2\u021e")
        buf.write("\u021f\7p\2\2\u021f\u0220\7n\2\2\u0220\u0221\7q\2\2\u0221")
        buf.write("\u0222\7e\2\2\u0222\u0223\7c\2\2\u0223\u0224\7n\2\2\u0224")
        buf.write("B\3\2\2\2\u0225\u0226\7c\2\2\u0226\u0227\7u\2\2\u0227")
        buf.write("\u0228\7u\2\2\u0228\u0229\7g\2\2\u0229\u022a\7t\2\2\u022a")
        buf.write("\u022b\7v\2\2\u022bD\3\2\2\2\u022c\u022d\7k\2\2\u022d")
        buf.write("\u022e\7h\2\2\u022eF\3\2\2\2\u022f\u0230\7g\2\2\u0230")
        buf.write("\u0231\7n\2\2\u0231\u0232\7k\2\2\u0232\u0233\7h\2\2\u0233")
        buf.write("H\3\2\2\2\u0234\u0235\7g\2\2\u0235\u0236\7n\2\2\u0236")
        buf.write("\u0237\7u\2\2\u0237\u0238\7g\2\2\u0238J\3\2\2\2\u0239")
        buf.write("\u023a\7y\2\2\u023a\u023b\7j\2\2\u023b\u023c\7k\2\2\u023c")
        buf.write("\u023d\7n\2\2\u023d\u023e\7g\2\2\u023eL\3\2\2\2\u023f")
        buf.write("\u0240\7h\2\2\u0240\u0241\7q\2\2\u0241\u0242\7t\2\2\u0242")
        buf.write("N\3\2\2\2\u0243\u0244\7k\2\2\u0244\u0245\7p\2\2\u0245")
        buf.write("P\3\2\2\2\u0246\u0247\7v\2\2\u0247\u0248\7t\2\2\u0248")
        buf.write("\u0249\7{\2\2\u0249R\3\2\2\2\u024a\u024b\7h\2\2\u024b")
        buf.write("\u024c\7k\2\2\u024c\u024d\7p\2\2\u024d\u024e\7c\2\2\u024e")
        buf.write("\u024f\7n\2\2\u024f\u0250\7n\2\2\u0250\u0251\7{\2\2\u0251")
        buf.write("T\3\2\2\2\u0252\u0253\7y\2\2\u0253\u0254\7k\2\2\u0254")
        buf.write("\u0255\7v\2\2\u0255\u0256\7j\2\2\u0256V\3\2\2\2\u0257")
        buf.write("\u0258\7g\2\2\u0258\u0259\7z\2\2\u0259\u025a\7e\2\2\u025a")
        buf.write("\u025b\7g\2\2\u025b\u025c\7r\2\2\u025c\u025d\7v\2\2\u025d")
        buf.write("X\3\2\2\2\u025e\u025f\7n\2\2\u025f\u0260\7c\2\2\u0260")
        buf.write("\u0261\7o\2\2\u0261\u0262\7d\2\2\u0262\u0263\7f\2\2\u0263")
        buf.write("\u0264\7c\2\2\u0264Z\3\2\2\2\u0265\u0266\7q\2\2\u0266")
        buf.write("\u0267\7t\2\2\u0267\\\3\2\2\2\u0268\u0269\7c\2\2\u0269")
        buf.write("\u026a\7p\2\2\u026a\u026b\7f\2\2\u026b^\3\2\2\2\u026c")
        buf.write("\u026d\7p\2\2\u026d\u026e\7q\2\2\u026e\u026f\7v\2\2\u026f")
        buf.write("`\3\2\2\2\u0270\u0271\7k\2\2\u0271\u0272\7u\2\2\u0272")
        buf.write("b\3\2\2\2\u0273\u0274\7P\2\2\u0274\u0275\7q\2\2\u0275")
        buf.write("\u0276\7p\2\2\u0276\u0277\7g\2\2\u0277d\3\2\2\2\u0278")
        buf.write("\u0279\7V\2\2\u0279\u027a\7t\2\2\u027a\u027b\7w\2\2\u027b")
        buf.write("\u027c\7g\2\2\u027cf\3\2\2\2\u027d\u027e\7H\2\2\u027e")
        buf.write("\u027f\7c\2\2\u027f\u0280\7n\2\2\u0280\u0281\7u\2\2\u0281")
        buf.write("\u0282\7g\2\2\u0282h\3\2\2\2\u0283\u0284\7e\2\2\u0284")
        buf.write("\u0285\7n\2\2\u0285\u0286\7c\2\2\u0286\u0287\7u\2\2\u0287")
        buf.write("\u0288\7u\2\2\u0288j\3\2\2\2\u0289\u028a\7{\2\2\u028a")
        buf.write("\u028b\7k\2\2\u028b\u028c\7g\2\2\u028c\u028d\7n\2\2\u028d")
        buf.write("\u028e\7f\2\2\u028el\3\2\2\2\u028f\u0290\7f\2\2\u0290")
        buf.write("\u0291\7g\2\2\u0291\u0292\7n\2\2\u0292n\3\2\2\2\u0293")
        buf.write("\u0294\7r\2\2\u0294\u0295\7c\2\2\u0295\u0296\7u\2\2\u0296")
        buf.write("\u0297\7u\2\2\u0297p\3\2\2\2\u0298\u0299\7e\2\2\u0299")
        buf.write("\u029a\7q\2\2\u029a\u029b\7p\2\2\u029b\u029c\7v\2\2\u029c")
        buf.write("\u029d\7k\2\2\u029d\u029e\7p\2\2\u029e\u029f\7w\2\2\u029f")
        buf.write("\u02a0\7g\2\2\u02a0r\3\2\2\2\u02a1\u02a2\7d\2\2\u02a2")
        buf.write("\u02a3\7t\2\2\u02a3\u02a4\7g\2\2\u02a4\u02a5\7c\2\2\u02a5")
        buf.write("\u02a6\7m\2\2\u02a6t\3\2\2\2\u02a7\u02a8\7c\2\2\u02a8")
        buf.write("\u02a9\7u\2\2\u02a9\u02aa\7{\2\2\u02aa\u02ab\7p\2\2\u02ab")
        buf.write("\u02ac\7e\2\2\u02acv\3\2\2\2\u02ad\u02ae\7c\2\2\u02ae")
        buf.write("\u02af\7y\2\2\u02af\u02b0\7c\2\2\u02b0\u02b1\7k\2\2\u02b1")
        buf.write("\u02b2\7v\2\2\u02b2x\3\2\2\2\u02b3\u02b4\6=\2\2\u02b4")
        buf.write("\u02c0\5\u011b\u008e\2\u02b5\u02b7\7\17\2\2\u02b6\u02b5")
        buf.write("\3\2\2\2\u02b6\u02b7\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8")
        buf.write("\u02bb\7\f\2\2\u02b9\u02bb\4\16\17\2\u02ba\u02b6\3\2\2")
        buf.write("\2\u02ba\u02b9\3\2\2\2\u02bb\u02bd\3\2\2\2\u02bc\u02be")
        buf.write("\5\u011b\u008e\2\u02bd\u02bc\3\2\2\2\u02bd\u02be\3\2\2")
        buf.write("\2\u02be\u02c0\3\2\2\2\u02bf\u02b3\3\2\2\2\u02bf\u02ba")
        buf.write("\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c2\b=\2\2\u02c2")
        buf.write("z\3\2\2\2\u02c3\u02c7\5\u0121\u0091\2\u02c4\u02c6\5\u0123")
        buf.write("\u0092\2\u02c5\u02c4\3\2\2\2\u02c6\u02c9\3\2\2\2\u02c7")
        buf.write("\u02c5\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8|\3\2\2\2\u02c9")
        buf.write("\u02c7\3\2\2\2\u02ca\u02d0\t\2\2\2\u02cb\u02cc\t\3\2\2")
        buf.write("\u02cc\u02d0\t\4\2\2\u02cd\u02ce\t\4\2\2\u02ce\u02d0\t")
        buf.write("\3\2\2\u02cf\u02ca\3\2\2\2\u02cf\u02cb\3\2\2\2\u02cf\u02cd")
        buf.write("\3\2\2\2\u02cf\u02d0\3\2\2\2\u02d0\u02d3\3\2\2\2\u02d1")
        buf.write("\u02d4\5\u00efx\2\u02d2\u02d4\5\u00f1y\2\u02d3\u02d1\3")
        buf.write("\2\2\2\u02d3\u02d2\3\2\2\2\u02d4~\3\2\2\2\u02d5\u02db")
        buf.write("\t\5\2\2\u02d6\u02d7\t\5\2\2\u02d7\u02db\t\4\2\2\u02d8")
        buf.write("\u02d9\t\4\2\2\u02d9\u02db\t\5\2\2\u02da\u02d5\3\2\2\2")
        buf.write("\u02da\u02d6\3\2\2\2\u02da\u02d8\3\2\2\2\u02db\u02de\3")
        buf.write("\2\2\2\u02dc\u02df\5\u010d\u0087\2\u02dd\u02df\5\u010f")
        buf.write("\u0088\2\u02de\u02dc\3\2\2\2\u02de\u02dd\3\2\2\2\u02df")
        buf.write("\u0080\3\2\2\2\u02e0\u02e4\5\u00f9}\2\u02e1\u02e3\5\u00fb")
        buf.write("~\2\u02e2\u02e1\3\2\2\2\u02e3\u02e6\3\2\2\2\u02e4\u02e2")
        buf.write("\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5\u02ed\3\2\2\2\u02e6")
        buf.write("\u02e4\3\2\2\2\u02e7\u02e9\7\62\2\2\u02e8\u02e7\3\2\2")
        buf.write("\2\u02e9\u02ea\3\2\2\2\u02ea\u02e8\3\2\2\2\u02ea\u02eb")
        buf.write("\3\2\2\2\u02eb\u02ed\3\2\2\2\u02ec\u02e0\3\2\2\2\u02ec")
        buf.write("\u02e8\3\2\2\2\u02ed\u0082\3\2\2\2\u02ee\u02ef\7\62\2")
        buf.write("\2\u02ef\u02f1\t\6\2\2\u02f0\u02f2\5\u00fd\177\2\u02f1")
        buf.write("\u02f0\3\2\2\2\u02f2\u02f3\3\2\2\2\u02f3\u02f1\3\2\2\2")
        buf.write("\u02f3\u02f4\3\2\2\2\u02f4\u0084\3\2\2\2\u02f5\u02f6\7")
        buf.write("\62\2\2\u02f6\u02f8\t\7\2\2\u02f7\u02f9\5\u00ff\u0080")
        buf.write("\2\u02f8\u02f7\3\2\2\2\u02f9\u02fa\3\2\2\2\u02fa\u02f8")
        buf.write("\3\2\2\2\u02fa\u02fb\3\2\2\2\u02fb\u0086\3\2\2\2\u02fc")
        buf.write("\u02fd\7\62\2\2\u02fd\u02ff\t\5\2\2\u02fe\u0300\5\u0101")
        buf.write("\u0081\2\u02ff\u02fe\3\2\2\2\u0300\u0301\3\2\2\2\u0301")
        buf.write("\u02ff\3\2\2\2\u0301\u0302\3\2\2\2\u0302\u0088\3\2\2\2")
        buf.write("\u0303\u0306\5\u0103\u0082\2\u0304\u0306\5\u0105\u0083")
        buf.write("\2\u0305\u0303\3\2\2\2\u0305\u0304\3\2\2\2\u0306\u008a")
        buf.write("\3\2\2\2\u0307\u030a\5\u0089E\2\u0308\u030a\5\u0107\u0084")
        buf.write("\2\u0309\u0307\3\2\2\2\u0309\u0308\3\2\2\2\u030a\u030b")
        buf.write("\3\2\2\2\u030b\u030c\t\b\2\2\u030c\u008c\3\2\2\2\u030d")
        buf.write("\u030e\7\60\2\2\u030e\u008e\3\2\2\2\u030f\u0310\7\60\2")
        buf.write("\2\u0310\u0311\7\60\2\2\u0311\u0312\7\60\2\2\u0312\u0090")
        buf.write("\3\2\2\2\u0313\u0314\7,\2\2\u0314\u0092\3\2\2\2\u0315")
        buf.write("\u0316\7*\2\2\u0316\u0317\bJ\3\2\u0317\u0094\3\2\2\2\u0318")
        buf.write("\u0319\7+\2\2\u0319\u031a\bK\4\2\u031a\u0096\3\2\2\2\u031b")
        buf.write("\u031c\7.\2\2\u031c\u0098\3\2\2\2\u031d\u031e\7<\2\2\u031e")
        buf.write("\u009a\3\2\2\2\u031f\u0320\7=\2\2\u0320\u009c\3\2\2\2")
        buf.write("\u0321\u0322\7,\2\2\u0322\u0323\7,\2\2\u0323\u009e\3\2")
        buf.write("\2\2\u0324\u0325\7?\2\2\u0325\u00a0\3\2\2\2\u0326\u0327")
        buf.write("\7]\2\2\u0327\u0328\bQ\5\2\u0328\u00a2\3\2\2\2\u0329\u032a")
        buf.write("\7_\2\2\u032a\u032b\bR\6\2\u032b\u00a4\3\2\2\2\u032c\u032d")
        buf.write("\7~\2\2\u032d\u00a6\3\2\2\2\u032e\u032f\7`\2\2\u032f\u00a8")
        buf.write("\3\2\2\2\u0330\u0331\7(\2\2\u0331\u00aa\3\2\2\2\u0332")
        buf.write("\u0333\7>\2\2\u0333\u0334\7>\2\2\u0334\u00ac\3\2\2\2\u0335")
        buf.write("\u0336\7@\2\2\u0336\u0337\7@\2\2\u0337\u00ae\3\2\2\2\u0338")
        buf.write("\u0339\7-\2\2\u0339\u00b0\3\2\2\2\u033a\u033b\7/\2\2\u033b")
        buf.write("\u00b2\3\2\2\2\u033c\u033d\7\61\2\2\u033d\u00b4\3\2\2")
        buf.write("\2\u033e\u033f\7\'\2\2\u033f\u00b6\3\2\2\2\u0340\u0341")
        buf.write("\7\61\2\2\u0341\u0342\7\61\2\2\u0342\u00b8\3\2\2\2\u0343")
        buf.write("\u0344\7\u0080\2\2\u0344\u00ba\3\2\2\2\u0345\u0346\7}")
        buf.write("\2\2\u0346\u0347\b^\7\2\u0347\u00bc\3\2\2\2\u0348\u0349")
        buf.write("\7\177\2\2\u0349\u034a\b_\b\2\u034a\u00be\3\2\2\2\u034b")
        buf.write("\u034c\7>\2\2\u034c\u00c0\3\2\2\2\u034d\u034e\7@\2\2\u034e")
        buf.write("\u00c2\3\2\2\2\u034f\u0350\7?\2\2\u0350\u0351\7?\2\2\u0351")
        buf.write("\u00c4\3\2\2\2\u0352\u0353\7@\2\2\u0353\u0354\7?\2\2\u0354")
        buf.write("\u00c6\3\2\2\2\u0355\u0356\7>\2\2\u0356\u0357\7?\2\2\u0357")
        buf.write("\u00c8\3\2\2\2\u0358\u0359\7>\2\2\u0359\u035a\7@\2\2\u035a")
        buf.write("\u00ca\3\2\2\2\u035b\u035c\7#\2\2\u035c\u035d\7?\2\2\u035d")
        buf.write("\u00cc\3\2\2\2\u035e\u035f\7B\2\2\u035f\u00ce\3\2\2\2")
        buf.write("\u0360\u0361\7/\2\2\u0361\u0362\7@\2\2\u0362\u00d0\3\2")
        buf.write("\2\2\u0363\u0364\7-\2\2\u0364\u0365\7?\2\2\u0365\u00d2")
        buf.write("\3\2\2\2\u0366\u0367\7/\2\2\u0367\u0368\7?\2\2\u0368\u00d4")
        buf.write("\3\2\2\2\u0369\u036a\7,\2\2\u036a\u036b\7?\2\2\u036b\u00d6")
        buf.write("\3\2\2\2\u036c\u036d\7B\2\2\u036d\u036e\7?\2\2\u036e\u00d8")
        buf.write("\3\2\2\2\u036f\u0370\7\61\2\2\u0370\u0371\7?\2\2\u0371")
        buf.write("\u00da\3\2\2\2\u0372\u0373\7\'\2\2\u0373\u0374\7?\2\2")
        buf.write("\u0374\u00dc\3\2\2\2\u0375\u0376\7(\2\2\u0376\u0377\7")
        buf.write("?\2\2\u0377\u00de\3\2\2\2\u0378\u0379\7~\2\2\u0379\u037a")
        buf.write("\7?\2\2\u037a\u00e0\3\2\2\2\u037b\u037c\7`\2\2\u037c\u037d")
        buf.write("\7?\2\2\u037d\u00e2\3\2\2\2\u037e\u037f\7>\2\2\u037f\u0380")
        buf.write("\7>\2\2\u0380\u0381\7?\2\2\u0381\u00e4\3\2\2\2\u0382\u0383")
        buf.write("\7@\2\2\u0383\u0384\7@\2\2\u0384\u0385\7?\2\2\u0385\u00e6")
        buf.write("\3\2\2\2\u0386\u0387\7,\2\2\u0387\u0388\7,\2\2\u0388\u0389")
        buf.write("\7?\2\2\u0389\u00e8\3\2\2\2\u038a\u038b\7\61\2\2\u038b")
        buf.write("\u038c\7\61\2\2\u038c\u038d\7?\2\2\u038d\u00ea\3\2\2\2")
        buf.write("\u038e\u0392\5\u011b\u008e\2\u038f\u0392\5\u011d\u008f")
        buf.write("\2\u0390\u0392\5\u011f\u0090\2\u0391\u038e\3\2\2\2\u0391")
        buf.write("\u038f\3\2\2\2\u0391\u0390\3\2\2\2\u0392\u0393\3\2\2\2")
        buf.write("\u0393\u0394\bv\t\2\u0394\u00ec\3\2\2\2\u0395\u0396\13")
        buf.write("\2\2\2\u0396\u00ee\3\2\2\2\u0397\u039c\7)\2\2\u0398\u039b")
        buf.write("\5\u00f7|\2\u0399\u039b\n\t\2\2\u039a\u0398\3\2\2\2\u039a")
        buf.write("\u0399\3\2\2\2\u039b\u039e\3\2\2\2\u039c\u039a\3\2\2\2")
        buf.write("\u039c\u039d\3\2\2\2\u039d\u039f\3\2\2\2\u039e\u039c\3")
        buf.write("\2\2\2\u039f\u03aa\7)\2\2\u03a0\u03a5\7$\2\2\u03a1\u03a4")
        buf.write("\5\u00f7|\2\u03a2\u03a4\n\n\2\2\u03a3\u03a1\3\2\2\2\u03a3")
        buf.write("\u03a2\3\2\2\2\u03a4\u03a7\3\2\2\2\u03a5\u03a3\3\2\2\2")
        buf.write("\u03a5\u03a6\3\2\2\2\u03a6\u03a8\3\2\2\2\u03a7\u03a5\3")
        buf.write("\2\2\2\u03a8\u03aa\7$\2\2\u03a9\u0397\3\2\2\2\u03a9\u03a0")
        buf.write("\3\2\2\2\u03aa\u00f0\3\2\2\2\u03ab\u03ac\7)\2\2\u03ac")
        buf.write("\u03ad\7)\2\2\u03ad\u03ae\7)\2\2\u03ae\u03b2\3\2\2\2\u03af")
        buf.write("\u03b1\5\u00f3z\2\u03b0\u03af\3\2\2\2\u03b1\u03b4\3\2")
        buf.write("\2\2\u03b2\u03b3\3\2\2\2\u03b2\u03b0\3\2\2\2\u03b3\u03b5")
        buf.write("\3\2\2\2\u03b4\u03b2\3\2\2\2\u03b5\u03b6\7)\2\2\u03b6")
        buf.write("\u03b7\7)\2\2\u03b7\u03c6\7)\2\2\u03b8\u03b9\7$\2\2\u03b9")
        buf.write("\u03ba\7$\2\2\u03ba\u03bb\7$\2\2\u03bb\u03bf\3\2\2\2\u03bc")
        buf.write("\u03be\5\u00f3z\2\u03bd\u03bc\3\2\2\2\u03be\u03c1\3\2")
        buf.write("\2\2\u03bf\u03c0\3\2\2\2\u03bf\u03bd\3\2\2\2\u03c0\u03c2")
        buf.write("\3\2\2\2\u03c1\u03bf\3\2\2\2\u03c2\u03c3\7$\2\2\u03c3")
        buf.write("\u03c4\7$\2\2\u03c4\u03c6\7$\2\2\u03c5\u03ab\3\2\2\2\u03c5")
        buf.write("\u03b8\3\2\2\2\u03c6\u00f2\3\2\2\2\u03c7\u03ca\5\u00f5")
        buf.write("{\2\u03c8\u03ca\5\u00f7|\2\u03c9\u03c7\3\2\2\2\u03c9\u03c8")
        buf.write("\3\2\2\2\u03ca\u00f4\3\2\2\2\u03cb\u03cc\n\13\2\2\u03cc")
        buf.write("\u00f6\3\2\2\2\u03cd\u03ce\7^\2\2\u03ce\u03d2\13\2\2\2")
        buf.write("\u03cf\u03d0\7^\2\2\u03d0\u03d2\5y=\2\u03d1\u03cd\3\2")
        buf.write("\2\2\u03d1\u03cf\3\2\2\2\u03d2\u00f8\3\2\2\2\u03d3\u03d4")
        buf.write("\t\f\2\2\u03d4\u00fa\3\2\2\2\u03d5\u03d6\t\r\2\2\u03d6")
        buf.write("\u00fc\3\2\2\2\u03d7\u03d8\t\16\2\2\u03d8\u00fe\3\2\2")
        buf.write("\2\u03d9\u03da\t\17\2\2\u03da\u0100\3\2\2\2\u03db\u03dc")
        buf.write("\t\20\2\2\u03dc\u0102\3\2\2\2\u03dd\u03df\5\u0107\u0084")
        buf.write("\2\u03de\u03dd\3\2\2\2\u03de\u03df\3\2\2\2\u03df\u03e0")
        buf.write("\3\2\2\2\u03e0\u03e5\5\u0109\u0085\2\u03e1\u03e2\5\u0107")
        buf.write("\u0084\2\u03e2\u03e3\7\60\2\2\u03e3\u03e5\3\2\2\2\u03e4")
        buf.write("\u03de\3\2\2\2\u03e4\u03e1\3\2\2\2\u03e5\u0104\3\2\2\2")
        buf.write("\u03e6\u03e9\5\u0107\u0084\2\u03e7\u03e9\5\u0103\u0082")
        buf.write("\2\u03e8\u03e6\3\2\2\2\u03e8\u03e7\3\2\2\2\u03e9\u03ea")
        buf.write("\3\2\2\2\u03ea\u03eb\5\u010b\u0086\2\u03eb\u0106\3\2\2")
        buf.write("\2\u03ec\u03ee\5\u00fb~\2\u03ed\u03ec\3\2\2\2\u03ee\u03ef")
        buf.write("\3\2\2\2\u03ef\u03ed\3\2\2\2\u03ef\u03f0\3\2\2\2\u03f0")
        buf.write("\u0108\3\2\2\2\u03f1\u03f3\7\60\2\2\u03f2\u03f4\5\u00fb")
        buf.write("~\2\u03f3\u03f2\3\2\2\2\u03f4\u03f5\3\2\2\2\u03f5\u03f3")
        buf.write("\3\2\2\2\u03f5\u03f6\3\2\2\2\u03f6\u010a\3\2\2\2\u03f7")
        buf.write("\u03f9\t\21\2\2\u03f8\u03fa\t\22\2\2\u03f9\u03f8\3\2\2")
        buf.write("\2\u03f9\u03fa\3\2\2\2\u03fa\u03fc\3\2\2\2\u03fb\u03fd")
        buf.write("\5\u00fb~\2\u03fc\u03fb\3\2\2\2\u03fd\u03fe\3\2\2\2\u03fe")
        buf.write("\u03fc\3\2\2\2\u03fe\u03ff\3\2\2\2\u03ff\u010c\3\2\2\2")
        buf.write("\u0400\u0405\7)\2\2\u0401\u0404\5\u0113\u008a\2\u0402")
        buf.write("\u0404\5\u0119\u008d\2\u0403\u0401\3\2\2\2\u0403\u0402")
        buf.write("\3\2\2\2\u0404\u0407\3\2\2\2\u0405\u0403\3\2\2\2\u0405")
        buf.write("\u0406\3\2\2\2\u0406\u0408\3\2\2\2\u0407\u0405\3\2\2\2")
        buf.write("\u0408\u0413\7)\2\2\u0409\u040e\7$\2\2\u040a\u040d\5\u0115")
        buf.write("\u008b\2\u040b\u040d\5\u0119\u008d\2\u040c\u040a\3\2\2")
        buf.write("\2\u040c\u040b\3\2\2\2\u040d\u0410\3\2\2\2\u040e\u040c")
        buf.write("\3\2\2\2\u040e\u040f\3\2\2\2\u040f\u0411\3\2\2\2\u0410")
        buf.write("\u040e\3\2\2\2\u0411\u0413\7$\2\2\u0412\u0400\3\2\2\2")
        buf.write("\u0412\u0409\3\2\2\2\u0413\u010e\3\2\2\2\u0414\u0415\7")
        buf.write(")\2\2\u0415\u0416\7)\2\2\u0416\u0417\7)\2\2\u0417\u041b")
        buf.write("\3\2\2\2\u0418\u041a\5\u0111\u0089\2\u0419\u0418\3\2\2")
        buf.write("\2\u041a\u041d\3\2\2\2\u041b\u041c\3\2\2\2\u041b\u0419")
        buf.write("\3\2\2\2\u041c\u041e\3\2\2\2\u041d\u041b\3\2\2\2\u041e")
        buf.write("\u041f\7)\2\2\u041f\u0420\7)\2\2\u0420\u042f\7)\2\2\u0421")
        buf.write("\u0422\7$\2\2\u0422\u0423\7$\2\2\u0423\u0424\7$\2\2\u0424")
        buf.write("\u0428\3\2\2\2\u0425\u0427\5\u0111\u0089\2\u0426\u0425")
        buf.write("\3\2\2\2\u0427\u042a\3\2\2\2\u0428\u0429\3\2\2\2\u0428")
        buf.write("\u0426\3\2\2\2\u0429\u042b\3\2\2\2\u042a\u0428\3\2\2\2")
        buf.write("\u042b\u042c\7$\2\2\u042c\u042d\7$\2\2\u042d\u042f\7$")
        buf.write("\2\2\u042e\u0414\3\2\2\2\u042e\u0421\3\2\2\2\u042f\u0110")
        buf.write("\3\2\2\2\u0430\u0433\5\u0117\u008c\2\u0431\u0433\5\u0119")
        buf.write("\u008d\2\u0432\u0430\3\2\2\2\u0432\u0431\3\2\2\2\u0433")
        buf.write("\u0112\3\2\2\2\u0434\u0436\t\23\2\2\u0435\u0434\3\2\2")
        buf.write("\2\u0436\u0114\3\2\2\2\u0437\u0439\t\24\2\2\u0438\u0437")
        buf.write("\3\2\2\2\u0439\u0116\3\2\2\2\u043a\u043c\t\25\2\2\u043b")
        buf.write("\u043a\3\2\2\2\u043c\u0118\3\2\2\2\u043d\u043e\7^\2\2")
        buf.write("\u043e\u043f\t\26\2\2\u043f\u011a\3\2\2\2\u0440\u0442")
        buf.write("\t\27\2\2\u0441\u0440\3\2\2\2\u0442\u0443\3\2\2\2\u0443")
        buf.write("\u0441\3\2\2\2\u0443\u0444\3\2\2\2\u0444\u011c\3\2\2\2")
        buf.write("\u0445\u0446\7%\2\2\u0446\u044a\n\30\2\2\u0447\u0449\n")
        buf.write("\31\2\2\u0448\u0447\3\2\2\2\u0449\u044c\3\2\2\2\u044a")
        buf.write("\u0448\3\2\2\2\u044a\u044b\3\2\2\2\u044b\u0463\3\2\2\2")
        buf.write("\u044c\u044a\3\2\2\2\u044d\u044e\7%\2\2\u044e\u044f\7")
        buf.write("q\2\2\u044f\u0450\3\2\2\2\u0450\u0454\n\32\2\2\u0451\u0453")
        buf.write("\n\31\2\2\u0452\u0451\3\2\2\2\u0453\u0456\3\2\2\2\u0454")
        buf.write("\u0452\3\2\2\2\u0454\u0455\3\2\2\2\u0455\u0463\3\2\2\2")
        buf.write("\u0456\u0454\3\2\2\2\u0457\u0458\7%\2\2\u0458\u0459\7")
        buf.write("q\2\2\u0459\u045a\7o\2\2\u045a\u045b\3\2\2\2\u045b\u045f")
        buf.write("\n\33\2\2\u045c\u045e\n\31\2\2\u045d\u045c\3\2\2\2\u045e")
        buf.write("\u0461\3\2\2\2\u045f\u045d\3\2\2\2\u045f\u0460\3\2\2\2")
        buf.write("\u0460\u0463\3\2\2\2\u0461\u045f\3\2\2\2\u0462\u0445\3")
        buf.write("\2\2\2\u0462\u044d\3\2\2\2\u0462\u0457\3\2\2\2\u0463\u011e")
        buf.write("\3\2\2\2\u0464\u0466\7^\2\2\u0465\u0467\5\u011b\u008e")
        buf.write("\2\u0466\u0465\3\2\2\2\u0466\u0467\3\2\2\2\u0467\u046d")
        buf.write("\3\2\2\2\u0468\u046a\7\17\2\2\u0469\u0468\3\2\2\2\u0469")
        buf.write("\u046a\3\2\2\2\u046a\u046b\3\2\2\2\u046b\u046e\7\f\2\2")
        buf.write("\u046c\u046e\4\16\17\2\u046d\u0469\3\2\2\2\u046d\u046c")
        buf.write("\3\2\2\2\u046e\u0120\3\2\2\2\u046f\u0471\t\34\2\2\u0470")
        buf.write("\u046f\3\2\2\2\u0471\u0122\3\2\2\2\u0472\u0475\5\u0121")
        buf.write("\u0091\2\u0473\u0475\t\35\2\2\u0474\u0472\3\2\2\2\u0474")
        buf.write("\u0473\3\2\2\2\u0475\u0124\3\2\2\2@\2\u01e4\u01e8\u01ed")
        buf.write("\u01f3\u02b6\u02ba\u02bd\u02bf\u02c7\u02cf\u02d3\u02da")
        buf.write("\u02de\u02e4\u02ea\u02ec\u02f3\u02fa\u0301\u0305\u0309")
        buf.write("\u0391\u039a\u039c\u03a3\u03a5\u03a9\u03b2\u03bf\u03c5")
        buf.write("\u03c9\u03d1\u03de\u03e4\u03e8\u03ef\u03f5\u03f9\u03fe")
        buf.write("\u0403\u0405\u040c\u040e\u0412\u041b\u0428\u042e\u0432")
        buf.write("\u0435\u0438\u043b\u0443\u044a\u0454\u045f\u0462\u0466")
        buf.write("\u0469\u046d\u0470\u0474\n\3=\2\3J\3\3K\4\3Q\5\3R\6\3")
        buf.write("^\7\3_\b\b\2\2")
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
    T__19 = 20
    SCHEDULE = 21
    STRING = 22
    NUMBER = 23
    INTEGER = 24
    DEF = 25
    RETURN = 26
    RAISE = 27
    FROM = 28
    IMPORT = 29
    AS = 30
    GLOBAL = 31
    NONLOCAL = 32
    ASSERT = 33
    IF = 34
    ELIF = 35
    ELSE = 36
    WHILE = 37
    FOR = 38
    IN = 39
    TRY = 40
    FINALLY = 41
    WITH = 42
    EXCEPT = 43
    LAMBDA = 44
    OR = 45
    AND = 46
    NOT = 47
    IS = 48
    NONE = 49
    TRUE = 50
    FALSE = 51
    CLASS = 52
    YIELD = 53
    DEL = 54
    PASS = 55
    CONTINUE = 56
    BREAK = 57
    ASYNC = 58
    AWAIT = 59
    NEWLINE = 60
    NAME = 61
    STRING_LITERAL = 62
    BYTES_LITERAL = 63
    DECIMAL_INTEGER = 64
    OCT_INTEGER = 65
    HEX_INTEGER = 66
    BIN_INTEGER = 67
    FLOAT_NUMBER = 68
    IMAG_NUMBER = 69
    DOT = 70
    ELLIPSIS = 71
    STAR = 72
    OPEN_PAREN = 73
    CLOSE_PAREN = 74
    COMMA = 75
    COLON = 76
    SEMI_COLON = 77
    POWER = 78
    ASSIGN = 79
    OPEN_BRACK = 80
    CLOSE_BRACK = 81
    OR_OP = 82
    XOR = 83
    AND_OP = 84
    LEFT_SHIFT = 85
    RIGHT_SHIFT = 86
    ADD = 87
    MINUS = 88
    DIV = 89
    MOD = 90
    IDIV = 91
    NOT_OP = 92
    OPEN_BRACE = 93
    CLOSE_BRACE = 94
    LESS_THAN = 95
    GREATER_THAN = 96
    EQUALS = 97
    GT_EQ = 98
    LT_EQ = 99
    NOT_EQ_1 = 100
    NOT_EQ_2 = 101
    AT = 102
    ARROW = 103
    ADD_ASSIGN = 104
    SUB_ASSIGN = 105
    MULT_ASSIGN = 106
    AT_ASSIGN = 107
    DIV_ASSIGN = 108
    MOD_ASSIGN = 109
    AND_ASSIGN = 110
    OR_ASSIGN = 111
    XOR_ASSIGN = 112
    LEFT_SHIFT_ASSIGN = 113
    RIGHT_SHIFT_ASSIGN = 114
    POWER_ASSIGN = 115
    IDIV_ASSIGN = 116
    SKIP_ = 117
    UNKNOWN_CHAR = 118

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#omp'", "'parallel'", "'sections'", "'section'", "'master'", 
            "'single'", "'critical'", "'barrier'", "'atomic'", "'num_threads('", 
            "'shared('", "'private('", "'firstprivate('", "'lastprivate('", 
            "'reduction('", "'min'", "'max'", "'&&'", "'||'", "'schedule('", 
            "'def'", "'return'", "'raise'", "'from'", "'import'", "'as'", 
            "'global'", "'nonlocal'", "'assert'", "'if'", "'elif'", "'else'", 
            "'while'", "'for'", "'in'", "'try'", "'finally'", "'with'", 
            "'except'", "'lambda'", "'or'", "'and'", "'not'", "'is'", "'None'", 
            "'True'", "'False'", "'class'", "'yield'", "'del'", "'pass'", 
            "'continue'", "'break'", "'async'", "'await'", "'.'", "'...'", 
            "'*'", "'('", "')'", "','", "':'", "';'", "'**'", "'='", "'['", 
            "']'", "'|'", "'^'", "'&'", "'<<'", "'>>'", "'+'", "'-'", "'/'", 
            "'%'", "'//'", "'~'", "'{'", "'}'", "'<'", "'>'", "'=='", "'>='", 
            "'<='", "'<>'", "'!='", "'@'", "'->'", "'+='", "'-='", "'*='", 
            "'@='", "'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", 
            "'**='", "'//='" ]

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
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "SCHEDULE", "STRING", "NUMBER", "INTEGER", "DEF", "RETURN", 
                  "RAISE", "FROM", "IMPORT", "AS", "GLOBAL", "NONLOCAL", 
                  "ASSERT", "IF", "ELIF", "ELSE", "WHILE", "FOR", "IN", 
                  "TRY", "FINALLY", "WITH", "EXCEPT", "LAMBDA", "OR", "AND", 
                  "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", "YIELD", 
                  "DEL", "PASS", "CONTINUE", "BREAK", "ASYNC", "AWAIT", 
                  "NEWLINE", "NAME", "STRING_LITERAL", "BYTES_LITERAL", 
                  "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
                  "FLOAT_NUMBER", "IMAG_NUMBER", "DOT", "ELLIPSIS", "STAR", 
                  "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
                  "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", 
                  "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
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
            actions[59] = self.NEWLINE_action 
            actions[72] = self.OPEN_PAREN_action 
            actions[73] = self.CLOSE_PAREN_action 
            actions[79] = self.OPEN_BRACK_action 
            actions[80] = self.CLOSE_BRACK_action 
            actions[92] = self.OPEN_BRACE_action 
            actions[93] = self.CLOSE_BRACE_action 
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
            preds[59] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


