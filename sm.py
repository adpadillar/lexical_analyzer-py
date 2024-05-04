from state import State
from automaton import Automaton

alphabet = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
operators = "+-*/="
symbols = "()"
space = " "


def printRow(state: State, symbol: str):
    print(f"{symbol}\t{state.value}")


def stateMachine():
    # STARTING STATE > s0
    s0 = State("s0", "s0", True)

    # NUMBER STATES
    int_state = State("int", "integer", True)
    s1 = State("s1", "s1", False)
    float_state = State("float", "float", True)

    # OPERATOR STATES
    eq_state = State("eq", "assignment", True)
    add_state = State("add", "sum", True)
    sub_state = State("sub", "subtract", True)
    mul_state = State("mul", "product", True)
    div_state = State("div", "division", True)

    # SYMBOL STATES
    lparen_state = State("lpar", "left parentheses", True)
    rparen_state = State("rpar", "right parentheses", True)

    # IDENTIFIER STATE
    id_state = State("id", "variable", True)

    s0.addTransition(space, s0)  # ignore spaces

    # LOGIC NUMBER TRANSITIONS
    for d in digits:
        s0.addTransition(d, int_state)
        int_state.addTransition(d, int_state)
        s1.addTransition(d, float_state)
        float_state.addTransition(d, float_state)

    # move from int to float when we see a dot
    int_state.addTransition(".", s1)

    # INGOING NUMBER TRANSITIONS
    # we want to run code every time we gracefully transition to a new state

    # going from number to space, we go back to s0
    int_state.addTransition(space, s0, printRow)
    float_state.addTransition(space, s0, printRow)

    # going from number to operator, we go to the operator state
    int_state.addTransition("=", eq_state, printRow)
    float_state.addTransition("=", eq_state, printRow)
    int_state.addTransition("+", add_state, printRow)
    float_state.addTransition("+", add_state, printRow)
    int_state.addTransition("-", sub_state, printRow)
    float_state.addTransition("-", sub_state, printRow)
    int_state.addTransition("*", mul_state, printRow)
    float_state.addTransition("*", mul_state, printRow)
    int_state.addTransition("/", div_state, printRow)
    float_state.addTransition("/", div_state, printRow)

    # going from number to symbol, we go to the symbol state
    int_state.addTransition("(", lparen_state, printRow)
    float_state.addTransition("(", lparen_state, printRow)
    int_state.addTransition(")", rparen_state, printRow)
    float_state.addTransition(")", rparen_state, printRow)

    # going from number to identifier, we go to the identifier state
    for c in alphabet:
        int_state.addTransition(c, id_state, printRow)
        float_state.addTransition(c, id_state, printRow)

    # INGOING OPERATOR TRANTISIONS
    s0.addTransition("=", eq_state)
    s0.addTransition("+", add_state)
    s0.addTransition("-", sub_state)
    s0.addTransition("*", mul_state)
    s0.addTransition("/", div_state)

    # OUTGOING OPERATOR TRANSITIONS
    # going from operator to another operator, we go to the operator state
    # equals:
    eq_state.addTransition("=", eq_state, printRow)
    eq_state.addTransition("+", add_state, printRow)
    eq_state.addTransition("-", sub_state, printRow)
    eq_state.addTransition("*", mul_state, printRow)
    eq_state.addTransition("/", div_state, printRow)
    # addition:
    add_state.addTransition("=", eq_state, printRow)
    add_state.addTransition("+", add_state, printRow)
    add_state.addTransition("-", sub_state, printRow)
    add_state.addTransition("*", mul_state, printRow)
    add_state.addTransition("/", div_state, printRow)

    # subtraction:
    sub_state.addTransition("=", eq_state, printRow)
    sub_state.addTransition("+", add_state, printRow)
    sub_state.addTransition("-", sub_state, printRow)
    sub_state.addTransition("*", mul_state, printRow)
    sub_state.addTransition("/", div_state, printRow)

    # multiplication:
    mul_state.addTransition("=", eq_state, printRow)
    mul_state.addTransition("+", add_state, printRow)
    mul_state.addTransition("-", sub_state, printRow)
    mul_state.addTransition("*", mul_state, printRow)
    mul_state.addTransition("/", div_state, printRow)

    # division:
    div_state.addTransition("=", eq_state, printRow)
    div_state.addTransition("+", add_state, printRow)
    div_state.addTransition("-", sub_state, printRow)
    div_state.addTransition("*", mul_state, printRow)
    div_state.addTransition("/", div_state, printRow)

    # going from operator to space, we go back to s0
    eq_state.addTransition(space, s0, printRow)
    add_state.addTransition(space, s0, printRow)
    sub_state.addTransition(space, s0, printRow)
    mul_state.addTransition(space, s0, printRow)
    div_state.addTransition(space, s0, printRow)

    # going from operator to number, we go to the number state
    for d in digits:
        eq_state.addTransition(d, int_state, printRow)
        add_state.addTransition(d, int_state, printRow)
        sub_state.addTransition(d, int_state, printRow)
        mul_state.addTransition(d, int_state, printRow)
        div_state.addTransition(d, int_state, printRow)

    # going from operator to identifier, we go to the identifier state
    for c in alphabet:
        eq_state.addTransition(c, id_state, printRow)
        add_state.addTransition(c, id_state, printRow)
        sub_state.addTransition(c, id_state, printRow)
        mul_state.addTransition(c, id_state, printRow)
        div_state.addTransition(c, id_state, printRow)

    # going from operator to symbol, we go to the symbol state
    eq_state.addTransition("(", lparen_state, printRow)
    add_state.addTransition("(", lparen_state, printRow)
    sub_state.addTransition("(", lparen_state, printRow)
    mul_state.addTransition("(", lparen_state, printRow)
    div_state.addTransition("(", lparen_state, printRow)
    eq_state.addTransition(")", rparen_state, printRow)
    add_state.addTransition(")", rparen_state, printRow)
    sub_state.addTransition(")", rparen_state, printRow)
    mul_state.addTransition(")", rparen_state, printRow)
    div_state.addTransition(")", rparen_state, printRow)

    # INGOING IDENTIFIER TRANSITIONS
    for c in alphabet:
        s0.addTransition(c, id_state)
        id_state.addTransition(c, id_state)

    # OUTGOING IDENTIFIER TRANSITIONS
    # going from identifier to space, we go back to s0
    id_state.addTransition(space, s0, printRow)

    # going from identifier to operator, we go to the operator state
    id_state.addTransition("=", eq_state, printRow)
    id_state.addTransition("+", add_state, printRow)
    id_state.addTransition("-", sub_state, printRow)
    id_state.addTransition("*", mul_state, printRow)
    id_state.addTransition("/", div_state, printRow)

    # going from identifier to symbol, we go to the symbol state
    id_state.addTransition("(", lparen_state, printRow)
    id_state.addTransition(")", rparen_state, printRow)

    # go from identifier to number, we go to the number state
    for d in digits:
        id_state.addTransition(d, int_state, printRow)

    # LOGIC SYMBOL TRANSITIONS
    s0.addTransition("(", lparen_state)
    s0.addTransition(")", rparen_state)

    # OUTGOING SYMBOL TRANSITIONS
    # going from symbol to space, we go back to s0
    lparen_state.addTransition(space, s0, printRow)
    rparen_state.addTransition(space, s0, printRow)

    # going from symbol to number, we go to the number state
    for d in digits:
        lparen_state.addTransition(d, int_state, printRow)
        rparen_state.addTransition(d, int_state, printRow)

    # going from symbol to operator, we go to the operator state
    lparen_state.addTransition("=", eq_state, printRow)
    rparen_state.addTransition("=", eq_state, printRow)
    lparen_state.addTransition("+", add_state, printRow)
    rparen_state.addTransition("+", add_state, printRow)
    lparen_state.addTransition("-", sub_state, printRow)
    rparen_state.addTransition("-", sub_state, printRow)
    lparen_state.addTransition("*", mul_state, printRow)
    rparen_state.addTransition("*", mul_state, printRow)
    lparen_state.addTransition("/", div_state, printRow)
    rparen_state.addTransition("/", div_state, printRow)

    # going from symbol to identifier, we go to the identifier state
    for c in alphabet:
        lparen_state.addTransition(c, id_state, printRow)
        rparen_state.addTransition(c, id_state, printRow)

    automaton = Automaton(s0)

    return automaton
