import re

keywords = {"if", "else", "while", "int", "return"}

def lexical_analyzer(code):
    tokens = re.findall(r'[a-zA-Z_]\w*|\d+|[+\-*/=]', code

    for token in tokens:
        if token in keywords:
            print(token, "-> KEYWORD")
        elif token.isdigit():
            print(token, "-> NUMBER")
        elif re.match(r'[a-zA-Z_]\w*', token):
            print(token, "-> IDENTIFIER")
        else:
            print(token, "-> OPERATOR")

code = "int a = 5 + b"
lexical_analyzer(code)
