from src.gmit.re.com import Shunting

# Thomson's construction from class video

# Represent a state with two arrosws labelled by label
# use None for label representing "e" arrows
class state:
    label = None
    edge1 = None
    edge2 = None


# An NFA is represented by its initial and accept state
class NFA:
    intial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept


def compile(pofix):

    nfastack = []

    for c in pofix:
        if c == '.':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()

            # join them,a accept state of nfa1 equals to initial statci of nfa2
            nfa1.accept.edge1 = nfa2.initial

            # push new nfa to the stack
            nfastack.append(NFA(nfa1.initial, nfa2.accept))

        elif c == '|':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()

            # new states
            initial = state()
            accept = state()

            # initial state edges point to nfa1 and nf2 initial state
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            # accept state of nfa1 and nfa2 points to new accept state
            nfa1.accept = accept
            nfa2.accept = accept

            # push nfa to the stack
            nfastack.append(NFA(initial, accept))
        elif c == '*':
            # Pop single NFA for stack
            nfa1 = nfastack.pop()
            # Create new initial and accept state
            initial = state()
            accept = state()
            # join new initial state to nfa1's initial state and the new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # joint the old accept state to the new accept stte and nfa1's initial statte
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept

            # Push the new NFA to the stac
            nfastack.append(NFA(initial, accept))
        elif c == "+":

            # Pop single NFA for stack
            nfa1 = nfastack.pop()
            # Create new initial and accept state
            initial = state()
            accept = state()
            # join new initial state to nfa1's initial state and the new accept state
            initial.edge1 = nfa1.initial

            # joint the old accept state to the new accept stte and nfa1's initial statte
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept

            # Push the new NFA to the stac
            nfastack.append(NFA(initial, accept))

        else:
            # Create new initial and accept state
            accept = state()
            initial = state()
            # Join the new initial state to the accept state using an arrow label c
            initial.label = c
            initial.edge1 = accept
            # Push new NFA to the stack
            nfastack.append(NFA(initial, accept))

    # nfa stack should have only one single element
    return nfastack.pop()

def followes(state):
    """Return the set of states that can be reached from state following e arrows and his state."""

    # Create a new set with state as it's only member.
    states = set()
    states.add(state)

    # Check if state has arrows labelled e from it.
    if state.label is None:
        # check if edge1 is a state
        if state.edge1 is not None:
            # If there's and edge1, follow it.
            states |= followes(state.edge1)
        # Check if edge2 is a state
        if state.edge2 is not None:
            # If there's and edge2, follow it.
            states |= followes(state.edge2)

    # Return the set of states.
    return states


def match(infix,string):
    """Matches string to the infix regular expression."""

    # shunt and compile the regular expresion
    postfix = Shunting.Converter().toPofix(infix);
    nfa = compile(postfix)

    # The current set of states and the next set of states;
    current = set()
    next = set()

    # Add the initial state to the current set.
    current |= followes(nfa.initial)

    # loop through each character in the string.
    for s in string:
        # Loop through the current set of states.
        for c in current:
            # Check if that state is labelled s.
            if c.label == s:
                # Add the edge1 state to the next set.
                next |= followes(c.edge1)
        # set current to next, and clear out next.
        current = next
        next = set()

    # Check if the accept stare is in the set of current states.
    return(nfa.accept in current)



