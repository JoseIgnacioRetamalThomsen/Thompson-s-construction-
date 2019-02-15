
# Represent a transition function for a NDA
# alphabet is represent with positive integers (0,1,...)
# -1 represent the empty string
# -1 represent the state before initial state
# 0 intitial state
class MapTransitionFuncion:


  #  m ={"q":{-1,"q0"}}
    m={}
    def __init__(self):

        self.addTransition(-1,-1,0)





    #add states to the map
    def addTransition(self,initialState,path,finalStates={}):

       #check if there is any transition in the inputed states and simbol
       #if the is a transition it will apend the new final states
       if initialState in self.m:
           if path in self.m[initialState]:
                self.m[initialState][path]= self.m[initialState][path].union(finalStates)
       else:
           self.m[initialState] = {path: finalStates}


    def getState(self,actualState,path):

        if actualState in self.m:
            if path in self.m[actualState]:
               return self.m[actualState][path]
