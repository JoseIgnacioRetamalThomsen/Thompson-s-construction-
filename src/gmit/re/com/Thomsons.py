# Thomson's construction base on class video
# Jose Retamal
# Graph theory project GMIT 2019

# Base on:
# https://swtch.com/~rsc/regexp/regexp1.html
# https://web.microsoftstream.com/video/946a7826-e536-4295-b050-857975162e6c
# https://web.microsoftstream.com/video/5e2a482a-b1c9-48a3-b183-19eb8362abc9

from src.gmit.re.com import Shunting


# Represent a state with two arrosws labelled by label
# use None for label representing "e" arrows
class state:
    """
    Represent a state with 2 transitions
    Non label represent the "E" arrow
    """
    label = None
    edge1 = None
    edge2 = None


# An NFA is represented by its initial and accept state
class NFA:
    """
    NFA with inital and accpet state
    """
    intial = None
    accept = None

    def __init__(self, initial, accept):
        """
        Create NFA
        :param initial: Points to initial state
        :param accept:  Points to accept state
        """
        self.initial = initial
        self.accept = accept


def compile(pofix):
    """
    Compile a postfix expression into a NFA
    :param pofix: Postfix expression to compile.
    :return: The new created NFA.
    """

    # Used for create the NFA using Thomson's constructions,
    # will have a single NFA at the end.
    nfastack = []

    # For escape character.
    isEscape = False;

    for c in pofix:
        if isEscape:
            # If is escape, add new simple NFA to stack.
            # Create new initial and accept state
            accept = state()
            initial = state()
            # Join the new initial state to the accept state using an arrow label c
            initial.label = c
            initial.edge1 = accept
            # Push new NFA to the stack
            nfastack.append(NFA(initial, accept))

            # Next character will be not escaped.
            isEscape = False
        else:
            if c == '/':
                # Escape for next character
                isEscape = True

            elif c == '.':
                # Pop NFA 1 and 2 from stack
                nfa2 = nfastack.pop()
                nfa1 = nfastack.pop()

                # join them,a accept state of nfa1 equals to initial statci of nfa2
                nfa1.accept.edge1 = nfa2.initial

                # push new nfa to the stack
                nfastack.append(NFA(nfa1.initial, nfa2.accept))

            elif c == '|':
                # Pop NFA 1 and 2 from stack
                nfa2 = nfastack.pop()
                nfa1 = nfastack.pop()

                # Create new initial and accept states
                initial = state()
                accept = state()

                # initial state edges point to nfa1 and nf2 initial state
                initial.edge1 = nfa1.initial
                initial.edge2 = nfa2.initial

                # accept state of nfa1 and nfa2 points to new accept state
                nfa1.accept.edge1 = accept
                nfa2.accept.edge1 = accept

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
                # Join new initial state to nfa1's initial state
                initial.edge1 = nfa1.initial

                # Join the old accept state to the new accept state and nfa1's initial state.
                nfa1.accept.edge1 = nfa1.initial
                nfa1.accept.edge2 = accept

                # Push the new NFA to the stac
                nfastack.append(NFA(initial, accept))

            elif c == "?":
                # Pop single NFA for stack
                nfa1 = nfastack.pop()
                # Create new initial and accept state
                initial = state()
                accept = state()

                # Single state for accept zero occurrence.
                non = state()
                # New inital points to nfa1 initial(old initial)
                # and to the new state created.
                initial.edge1 = nfa1.initial
                initial.edge2 = non
                # nfa1 points to new accept state so does
                # new created state.
                nfa1.accept.edge1 = accept
                non.edge1 = accept
                # Push the  created NFA to stack
                nfastack.append(NFA(initial, accept))

            elif c == "-":
                # Pop 2 most recent.
                nfa2 = nfastack.pop()
                # We will grow this nfa
                nfa1 = nfastack.pop()

                # Get symbol of the nfa1 and 2,
                # this two are the boundaries of the range : c1-c2.
                c1 = nfa1.initial.label
                c2 = nfa2.initial.label

                nfa = None;

                for x in range(ord(c1) + 1, ord(c2)):
                    # Loop through each character in the range of c1-c2,
                    # creating a union between them: c1|c1.1|c1.2|...

                    # create a new NFA that accept x
                    accept0 = state()
                    initial0 = state()
                    initial0.label = chr(x)
                    initial0.edge1 = accept0
                    nfa0 = NFA(initial0, accept0)

                    # Union of the new created nfa to the growing nfa.
                    initial2 = state()
                    accept2 = state()
                    initial2.edge1 = nfa1.initial
                    initial2.edge2 = nfa0.initial
                    nfa1.accept.edge1 = accept2
                    nfa0.accept.edge1 = accept2
                    nfa1 = NFA(initial2, accept2)

                # We have only do c1-c(2-1)
                # So we do union of nfa2 to the growing NFA
                initial = state()
                accept = state()
                # join new initial state to nfa1's initial state and the new accept state
                initial.edge1 = nfa1.initial
                initial.edge2 = nfa2.initial
                # joint the old accept state to the new accept stte and nfa1's initial statte
                nfa1.accept.edge1 = accept
                nfa2.accept.edge1 = accept

                # Push new NFA to stack
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
    """
    Return the set of states that can be reached from state following e arrows and his state.
    :param state: starting state from where e arrows will follow
    :return: The set of states that can be reached from param state following e arrows.
    """

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


def match(infix, string):
    """
    Matches string to the infix regular expression.
    :param infix: Infix regex.
    :param string: String for match the regex.
    :return: True if the regex match on the string.
    """

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
    return (nfa.accept in current)


class Runner:
    """
    For run several string on the same NFA.
    """

    # Compiled NFA/
    nfa = None

    # The current set of states and the next set of states;
    current = set()
    next = set()

    def __init__(self, infix):
        """
        Create object with a infix regex, compile the nfa with it.
        :param infix: The infix regex
        """
        # Convert infix string into postfix and then compile the NFA.
        self.nfa = compile(Shunting.Converter().toPofix(infix))

        # Add the initial state to the current set.
        self.current |= followes(self.nfa.initial)

    def runNext(self, string):
        """
        Run a string on the NFA
        :param string: String to run
        :return: No return.
        """
        # loop through each character in the string.
        for s in string:
            # Loop through the current set of states.
            for c in self.current:
                # Check if that state is labelled s.
                if c.label == s:
                    # Add the edge1 state to the next set.
                    self.next |= followes(c.edge1)
            # set current to next, and clear out next.
            self.current = self.next
            self.next = set()

    def finish(self):
        """
        Finish the run on the automaton
        :return: True if the string match on the automaton
        """
        # Check if any of the current state is accept.
        return (self.nfa.accept in self.current)