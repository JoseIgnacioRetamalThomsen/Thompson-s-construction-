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

    def __init__(self,initial,accept):
        self.initial = initial
        self.accept = accept

def compile(pofix):
    nfastack=[]

    for c in pofix:
        if c =='.':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()

            # join them,a accept state of nfa1 equals to initial statci of nfa2
            nfa1.accept.edge1 = nfa2.initial

            # push new nfa to the stack
            nfastack.append(NFA(nfa1.initial,nfa2.accept))

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

            #push nfa to the stack
            nfastack.append(NFA(initial,accept))
        elif c=='*':
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
            nfastack.append(NFA(initial,accept))

        else:
            # Create new initial and accept state
            accept = state()
            initial = state()
            # Join the new initial state to the accept state using an arrow label c
            initial.label = c
            initial.edge1 = accept
            # Push new NFA to the stack
            nfastack.append(NFA(initial,accept))

    # nfastack showuld have only one single element
    return nfastack.pop()