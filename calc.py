import ply.lex as lex
tokens = (
    "NUMBER_FLOAT",
    "IDENTIFIER",
    "LEFT_BRACE",
    "RIGHT_BRACE",
    "SEMICOLON",
    "ASSIGNMENT",
    "NUMBER_INT",
    "COMMA",
    "X",
    "Y",
    "LEFT_PAREN",
    "RIGHT_PAREN",
    "INCREMENT",
    "DECREMENT" 
)

t_ignore  = ' \t'
def t_error1(t):
    r"-?\d+ [a-zA-Z_][a-zA-Z_0-9]* "
    print ("Unknown text '%s'" % (t.value,))
    
def t_error2(t):
    r"-?(\d+\.\d*)[a-zA-Z_][a-zA-Z_0-9]*|(\.\d+)[a-zA-Z_][a-zA-Z_0-9]*  "
    print ("Unknown text '%s'" % (t.value,))

   
def t_NUMBER_FLOAT(t):
    r"-?(\d+\.\d*)|(\.\d+)"
    t.value = float(t.value)
    return t

def t_NUMBER_INT(t):
    r"-?\d+"
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.value = str(t.value)
    return t

def t_LEFT_BRACE(t):
    r"{"
    return t

def t_ASSIGNMENT(t):
    r"="
    return t

def t_RIGHT_BRACE(t):
    r"}"
    return t

def t_SEMICOLON(t):
    r";"
    return t

def t_COMMA(t):
    r","
    return t

def t_X(t):
    r"[X]"
    return t

def t_Y(t):
    r"[Y]"
    return t

def t_LEFT_PAREN(t):
    r"\("
    return t

def t_RIGHT_PAREN(t):
    r"\)"
    return t

def t_INCREMENT(t):
    r"\++"
    return t

def t_DECREMENT(t):
    r"\--"
    return t

def t_error3(t):
    r'. [a-zA-Z_][a-zA-Z_0-9]* | .-?(\d+\.\d*)|.(\.\d+) | .-?\d+ '
    print("Unknown text '%s'" % (t.value,))

    
def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))


lex.lex()

num = input ("")
while (num!=""):
        lex.input(num)
        for tok in iter(lex.token, None):
            print (tok.type , tok.value)
        num = input ("")




