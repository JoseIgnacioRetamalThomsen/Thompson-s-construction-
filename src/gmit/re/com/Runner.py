from src.gmit.re.MapTransitionFunction import  MapTransitionFuncion

class Runner:

    #main method, start of program
    if __name__ == '__main__':
        print("Working");


        ##trnaasition function for most simple automata
        # automate accept only string 1, accept state is q1

        tf = MapTransitionFuncion()
        tf.addTransition(0, 1, 1);
        ##start wiht -1
        aState = set()
        aState = aState.union({tf.getState(-1,-1)});
        print("first state:")
        print( aState)
        #go with one
        print("final state")
        aState1 = set()

        for x in aState:
            aState1 = aState1.union({tf.getState(x,1)})

        print(aState1)
        # try another 1 so would have no state
        aState = set()

        for x in aState1:
            aState = aState.union({tf.getState(x,1)})
            
        print(aState)





