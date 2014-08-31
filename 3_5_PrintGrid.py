def do_four(f,s):
    f(s)
    f(s)
    f(s)
    f(s)

def print_sym(s):
    print(s,end="")

def print_hori_line():
    print_sym('+')
    do_four(print,'-')
    print_sym('+')
    do_four(print_sym,'-')
    print_sym('+')
    print()

def print_vert_line():
    do_four(print_sym,'|    |    |\n')

def print_grid():
    print_hori_line()
    print_vert_line()
    print_hori_line()
    print_vert_line()
    print_hori_line()
    

print_grid()
        
