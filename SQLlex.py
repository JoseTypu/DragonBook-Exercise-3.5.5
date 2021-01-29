from ply import lex

tokens = (
    'select',
    'where',
    'from',
)

palabra = input ("Inserte: ")
def t_select(t):
    r"""(S|s)(E|e)(L|l)(E|e)(C|c)(T|t)"""
    t.value = "SELECT"
    return t

def t_where(t):
    r"""(W|w)(H|h)(E|e)(R|r)(E|e)"""
    t.value = "WHERE"
    return t

def t_from(t):
    r"""(F|f)(R|r)(O|o)(M|m)"""
    t.value = "FROM"
    return t

t_ignore = " \t\n"

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Caracter no valido '%s' en linea %d" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(palabra)

for token in lexer:
    print(token)