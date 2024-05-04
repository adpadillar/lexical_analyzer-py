from state import State
import networkx as nx
import matplotlib.pyplot as plt
import sys


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
        graphLabels = {" ": "ε", "z": "a-z", "9": "0-9", ".": "<dot>"}

        # graph the automaton using networkx and matplotlib
        G = nx.DiGraph()

        initialState = self.state

        # add the initial state
        G.add_node(initialState.name)

        def addEdges(state: State):
            for symbol, nextState in state.transitions.items():
                G.add_edge(state.name,
                           nextState.name,
                           label=graphLabels.get(symbol, symbol),
                           final=nextState.isFinal)

        def traverse(state: State, visited: set):
            if state in visited:
                return
            visited.add(state)
            addEdges(state)
            for _, nextState in state.transitions.items():
                traverse(nextState, visited)

        sys.setrecursionlimit(10000)  # Increase recursion limit
        traverse(initialState, set())

        # show the graph
        pos = nx.spring_layout(G, k=10)  # Increase k value for more spacing
        nx.draw(G,
                pos,
                with_labels=True,
                node_size=330,
                node_color="skyblue",
                font_size=6,
                font_color="black",
                arrowsize=5)
        edge_labels = nx.get_edge_attributes(G, 'label')

        # this will be a dict[(node1, node2)] = bool denoting if the edge is final
        final_edges = nx.get_edge_attributes(G, 'final')
        final_nodes = set()
        nonfinal_nodes = set()
        for edge, is_final in final_edges.items():
            if is_final:
                final_nodes.add(edge[0])
            else:
                nonfinal_nodes.add(edge[0])

        print("Final Nodes:", final_nodes)
        print("Nonfinal Nodes:", nonfinal_nodes)

        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels, font_size=6,
            label_pos=0.3)  # Adjust label_pos to change the position of the labels
        plt.savefig("automaton.png", dpi=300)
        plt.clf()  # Clear the current figure
