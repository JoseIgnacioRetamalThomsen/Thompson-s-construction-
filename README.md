# How to run
  From root folder:
  
     python src/gmit/re/com/app.py



# Introduction


I start by deciding environment for develop the program. After doing some search online and ask some class mates about IDE for python, PyCharm was the most recommended one so i use it. 



First challenge was learn how to code in python, what was a bit confusing because I'm use to fully object oriented programing languages with string types. So I think there is a over use of classes and the coding style is not so consistent.

Then I went to understand Thomson's constructions, I first look into Wikipedia but couldn't really understand it, was the book that help me more. 

Then I think at 2 ways for implementing : create a data structure using sets and maps for represent the transition function and the other use  nodes for the NFA graph. So I decide to implement boot for them compare the performance.
Luckily I did first the one that use a data structure (I will call that map implementation), and then following the class videos I implement the nodes method.



The test show's that the Map algorithm perform much better than the node algorithm, but of them escalate linear on relation to the string input size. I did not test how they escalate in relation of the regex size. Also the time for compile the regex was not tested.

# Thomson's Constructions

Thomson’s construction/ algorithm is the method we have us in this project to transform a regular expression into a non deterministic finite automaton (NFA). Then we use that NFA to match strings.

The algorithm consists in 5 basic rules for empty(ε), symbol, concatenation, union and Kleene star expressions.

Example:

* Empty expression ε is represented as:

![Expression  ε ](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsons_e.png)

* The symbol a:

![Expression a](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsons_a.png)

* Concatenation of a and b: 

![Concatenation](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsons_acb.png)

* Union of a and b:

![Union](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsons_aub.png)

* Kleene star of a:

![Kleene star](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsons_k.png)


The examples are for only one symbol, but the same method is valid if a and b are initial and accept state of bigger automatons.

Therefore, we will start from the simplest automaton (symbol) and create a more complex using the methods shows in the example. Using this method, we are warranty that there will be always only one accept state.


# Thomson's Construction using maps and sets

I have implements  Thomson’s construction  using maps and list for represent the transition functions, using a python dictionary that maps to another dictionary that maps to a set :

    { Q : { Symbols :  {P(Q)}  }  }  

Q are the finite states.

Symbols are the alphabet.

P(Q) is the set of possible next states. 

States Q are defined by positives numbers, 0 represent the state before initial. 

Alphabet (symbols) are also defined by positives numbers, characters are use using they integer representation, -1 represent the empty string, which it will be used only at the start because the transition function will be created in the way that all ε transitions from a state will be.

image here


The transition from q1 with the symbol a will be:
     {q1 : {a : {a1, a} } 




For example, the start of a automata that the initial state is 1 is represented as:

     { 0 : { -1 , {1} }}

The most simple automata that accept only the symbol 1, with accept state = 2:

     { 0 : { -1 , {1} ,   1  : { 1 , {2} } }

A NFA and a transition function class are use, NFA class has a transition function. NFA are created with one parameter wich is the symbol that it will accept, then they can be mixed for create more complex NFA's.


## The NFA class 


  Is Define using a transition function and a accept state, which is guaranteed to be only one because we are using Thomson’s construction. States are always increasing, there is a static variable and function that give the new states and keep the count.

  The constructor take a single symbol as argument and create the most simple NFA that accept that symbol. Then that NFA will grow using the concatenation, union and star operations.

## Implementigs Thomson's constructions rules:

*  Empty expression ε :
   Creating a new NFA object with no parameter will create it .

         nfa = NFA()

    It will have only one transition :

        {0: {-1: {2 } }} -> 2 is accept state

   The initial state will be given by the static method.
 
 ### The symbol a:

       nfa = NFA('a')

  It transition function is :

        { 0: {-1: { 2 } },  2: { 97 : { 3 } } } 

   2 is initial state, a is store as character integer: 97, 3 is the accept state.



### Concatenation of a and b:

  a:

        { 0: {-1: { 2 } },  2: { 97: { 3 } } } 


  ![a](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsonsmap_a.png)

  b: 

        { 0: {-1: { 4 } },  4: { 98: { 5 } } }

  ![b](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsonsmap_b.png)

  a . b :

        { 0: {-1: { 2 } },  -> keep start state of a

          2: { 97: { 4 } },  -> add transition from accept of a to initial b

          4: { 98: { 5 } }}  -> Keep last transition of b

                             -> Keep initial state, set accept state to 5

  The transition above has been optimized, first look like:

  ![a.b 1](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsonsmap_acb1.png)

  We can see that state 4 is useless so it can be removed:

 ![a.b final](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsonsmap_acb2.png)

General rules :

-	Keep start state of a.
-	Add transition to start state of b to all states that get to accept state of a.
-	Remove start transition of b.
-	Add all remain transition of b to a.
-	Set accept state to accept state of b.  



 ###  a U b :

           { 0: {-1: { 2, 4 } }, -> add initial state of a and b to new initial state

             2: {97: { 6 } },    -> add new accept state to a transition, we can remove the old (3)

             4: {98: { 6 } } }   -> add new accept state to b transition, we can remove the old (5)

                                  -> new initial state is 5, this state is not needed and have been removed.
                                     New accept state is 6.

Before:

![a U b before](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsonsmap_aub1.png)

After optimization :

![a U b after](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsonsmap_aub2.png)

General rules :

-	Create new start and accept state.
-	Add the new initial state and initial state of b to a.
-	Remove start transition of b.
-	Add all remaining transitions on b to a.
-	All transitions that get to accept state of a and b goes also to the new accept state.


  
### Kleene star a:

   a*:

              { 0: { -1: { 2, 4, 5 } },  -> add 3 and 4 states to start

                2: { 97: { 2, 3, 5} } }   -> add transition from 2 to 3 and 2 to 5 

                                           -> new initial state is 4, new accept state is 5.

![Kleene star](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsonsmap_k.png)

This can be optimized, I think  state 3 and 4 can be removed.   

General rules :

-	Create new initial and start state.
-	Add new initial and accept state to a accept state.
-	All transition that go to old accept state, now also go to old initial state and new accept state.



### One or zero

  This is done using union() between 'a' NFA and ε NFA.

           { 0: {-1:  { 2, 5} },
             2: { 97: { 5   } } } 
              }

  ![? after](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomsonsmap_q2.png)

### Range (a-Z)


For the range I just did multiple union. 



Please check the wiki https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project.wiki.git
