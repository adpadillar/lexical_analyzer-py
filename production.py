from state import State
from automaton import Automaton

production_file = "production.txt"

def main():
  # read the file line by line
  with open(production_file, "r") as file:
    lines = file.readlines()

  state_names = set()
  states: dict[str, State] = dict()

  for line in lines:
    # split on left and right
    left, right = line.split("->")
    left = left.strip()
    right = right.strip()
    state_names.add(left)

  for state_name in state_names:
    state = State(state_name, state_names, False)
    states[state_name] = state


  for line in lines:
    left, right = line.split("->")
    left = left.strip()
    right = right.strip()

    if len(right) == 2:
      transition, target = right
      states[left].addTransition(transition, states[target])
    else:
      # we need to create a new final state
      new_state = State("z", "z", True)
      states[left].addTransition(right, new_state)

  initial_state = states["S"]
  automaton = Automaton(initial_state)
  automaton.graph()




  

if __name__ == "__main__":
  main()
