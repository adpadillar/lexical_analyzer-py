from shiny.express import input, render, ui

def plot(string: str):
  from state import State
  from automaton import Automaton

  state_names = set()
  states: dict[str, State] = dict()

  lines = string.split("\n")

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
  return automaton.graph()

ui.input_text_area(
    "caption_regular",
    "Caption:",
    "S -> aA\nS -> bB\nA -> bB\nA -> c\nB -> ε",
)

@render.image
def image():
  try:
    plot(input.caption_regular())
  except:
    # if it fails, its fine, just render the default image
    pass
  img = {"src": "./automaton.png", "width": "400px"}
  return img

