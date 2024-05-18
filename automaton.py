from state import State

class Automaton():
    # Constructor for the Automaton class.
    # state: the initial state
    def __init__(self, state: State):
        self.state = state
        # we will also need to create a buffer
        # to keep track of the tokens we are reading
        self.buffer = ""

# Match method will return a bool that says
# wether the string passed matched the automaton
# input: the string to be matched

    def match(self, input: str):
        # Clear the buffer every time we match
        # This helps mantain the buffer clean in
        # consecuent calls to match in the same
        # automaton
        self.buffer = ""

        currentState = self.state

        # if input is empty string, return
        # true if the automaton is in a final state,
        # false otherwise
        if len(input) == 0:
            return currentState.isFinal

# we know input len is not 0, so we
# iterate from 0 to len(input) - 1
        for i in range(0, len(input)):
            # we get the current char, nextState and onNavigate
            symbol = input[i]
            nextState = currentState.getNextState(symbol)
            onNavigate = currentState.onNavigates.get(symbol)

            # if the nextState is None, we short-circuit
            # and return false inmediatly. This helps us avoid
            # cases where we have a state that has no transitions
            if nextState is None:
                return False

# We check if a callback was provided
            if onNavigate is not None:
                # if a callback was provided, call it
                # with the current state as the argument
                # we strip the buffer to avoid extra spaces
                onNavigate(currentState, self.buffer.strip())
                # we clear the buffer after calling onNavigate
                self.buffer = ""

# we update the current state and add the symbol
# to the buffer
            self.buffer += symbol
            currentState = nextState

# Once we are done iterating through the input,
# we return True if the automaton is in a final state,
# false otherwise
        return currentState.isFinal


# This function creates automaton.png, a graphical representation
# of the current automaton.
# This function was mainly written by Github Copilot AI Assistant,
# as it is not in the assignments requirements but is useful for
# visualizing the automaton

    def graph(self):
        from visual_automata.fa.nfa import VisualNFA
        from forbiddenfruit import curse
        from frozendict import frozendict
        import copy

        def deepcopy(self: frozendict) -> frozendict:
            return copy.deepcopy(self)
        
        curse(frozendict, "deepcopy", deepcopy)

        def pop(self: str) -> str:
            last_char = self[-1]
            self = self[:-1]
            return last_char
        
        curse(str, "pop", pop)

        states: set[State] = set()
        def traverse(state: State):
            if state in states:
                return
            states.add(state)
            for _, nextState in state.transitions.items():
                for state in nextState:
                    traverse(state)

        traverse(self.state)

        all_symbols = set()
        for state in states:
            all_symbols.update(state.transitions.keys())

        transitions = {}
        for state in states:
            transitions[state.name] = {}
            for symbol in all_symbols:
                nextStates = state.getNextState(symbol)
                if nextStates is not None:
                    if len(nextStates) == 1:
                        transitions[state.name][symbol] = nextStates[0].name
                    else:
                        transitions[state.name][symbol] = [nextState.name for nextState in nextStates]

    

        final_states = set([state.name for state in states if state.isFinal])


        nfa = VisualNFA(
            states=set([state.name for state in states]),
            input_symbols=all_symbols,
            transitions=transitions,
            initial_state="S",
            final_states=final_states
        )

        
        return nfa.show_diagram(filename="automaton")
