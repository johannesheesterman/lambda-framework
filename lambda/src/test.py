from sys import stdin,argv
from antlr4 import *
from LambdaParser.LambdaLexer import LambdaLexer
from LambdaParser.LambdaParser import LambdaParser
from LambdaInterpeter.LambdaInterpeter import LambdaInterpeter

input_script_path = argv[1]
#input_script = ''.join(stdin.readlines())
input_script = ''.join(open(input_script_path).readlines())
input_stream = InputStream(input_script)
lexer = LambdaLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = LambdaParser(tokens)

tree = parser.prog()

LambdaInterpeter().visit(tree)