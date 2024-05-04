from sm import stateMachine


def lexer(filepath: str) -> None:
    with open(filepath, "r") as f:
        contents = f.read()
        lines = contents.split("\n")

    automaton = stateMachine()
    automaton.graph()

    print("Token\tType")
    for line in lines:
        line += " "  # this is hacky but it ensures that the last character is a space
        automaton.match(line)


lexer("input.xa")
