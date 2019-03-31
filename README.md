# How to run
  From root folder:
  
     python src/gmit/re/com/app.py

# How to use 


* Concatenation : . 

 a followed by a b

      a.b

* Union : |

a or b


      a|b
* Kleene start , zero or many : *

 Zero or many a



      a*
* One or many :  +

 One or many a

       a+

* Zero or one : ?

 Zero or one a

       a?

* Range: -

 All lower case letter on English alphabet:

    (a-z)


* Escape : /


 a followed by a dot.

     a./.

### Examples 

*  Any English letter lower or upper case:

        ((a-z)|(A-Z))
*  The word hello followed by a question mark, followed by a space, with one or many number at the end
      
         h.e.l.l.o./?. .(0-9)+

## Features

### Single string match
 
 Run a regex against a single string. 

### Single string match from file

  Run regex against a single string from a file. Can be use for run regex against long string.

### Search on file

  Search occurrences of regex on a string from a file. 
* Match the smallest string that is accepted by the regex.
* If show output is selected shows the line, start and end of the string that is accepted.

### Match on file line by line

  Run regex against each line of the file, every line is run as a different string.
  

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


# Thomson's using nodes

This is the method's that have been show in the video class. It implement Thomson's construction using nodes and connecting them by to edges.

A state is represented by a node as:
 
      class state:
            label = None
            edge1 = None
            edge2 = None

![state](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomson_state.png)

A NFA will be define with a initial and a accept state:

      class NFA:
            state initial = None
            state accept = None
### Rules :
* When the label of a state is None, any edge connected will be a ε transition.
* When the label is assigned the edge will be the transition for the symbol on the label. This works because Thomson's construction warranty that we will have only one transition from a labeled state.


### Symbol a:

  The basic automaton that accept only the symbol 'a' will looks like:

![a](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomson_a.png)

  Rules followed for create the automaton:
* Create 2 states initial and accept
* Set label of initial state to 'a'
* Connect edge1 of initial state to accept state



### a.b 

* Connect edge1 of accept state of a to initial state of b
* a initial state is the new initial state.
* b accept state is new accept state

![a.b](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomson_acb.png)


### a or b 

* Create a new accept and initial state.
* Connected edge1 of new accept state to a initial state.
* Connected edge2 of new accept state to b initial state.
* Connect a accept state to new accept state.
* Connect b accept state to new accept state.

![a U b](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomson_aob.png)


### a*

* Create new initial and accept state
* Connect new initial to a initial and new accept states.
* connect a accept to a state and new initial

![Kleene star](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomson_k.png)


### a+
 
 Same than a* but we just don't connect new initial state to new accept state:

![One or many](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomson_q.png)

### a?(One or zero)

* Create new initial and accept state.
* Create a new empty state.
* Connect new initial to a initial and to the new empty state.
* Connect a accept state to new accept state.
* Connect new empty label to new accept state.

![?](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/thomson_qm.png)

# Shunting Yard Algorithm

 We will useShunting Yard algorithm for convert infix expressions(most common way of writing mathematical expressions, ex: a+b) into post fix expressions (a+b in post fix is ab+). With the expression in post fix notation it would be possible to create the NFA using Thomson's construction.
It use a stack for operators and the following rules [1]:

1. If the incoming symbols is an operand, print it..

2. If the incoming symbol is a left parenthesis, push it on the stack.

3. If the incoming symbol is a right parenthesis: discard the right parenthesis, pop and print the stack symbols until you see a left parenthesis. Pop the left parenthesis and discard it.

4. If the incoming symbol is an operator and the stack is empty or contains a left parenthesis on top, push the incoming operator onto the stack.

5. If the incoming symbol is an operator and has either higher precedence than the operator on the top of the stack, 
or has the same precedence as the operator on the top of the stack and is right associative -- push it on the stack.

6. If the incoming symbol is an operator and has either lower precedence than the operator on the top of the stack, or has the same precedence as the operator on the top of the stack and is left associative -- continue to pop the stack until this is not true. Then, push the incoming operator.

7. At the end of the expression, pop and print all operators on the stack. (No parentheses should remain.)
 

***
[Shunting Yard Algorithm](http://www.oxfordmathcenter.com/drupal7/node/628)


# Testing and comparing algorithms

## Odd number of 1 regex

 Test regex again string of 0 and 1 of different length.

     0*.1.0*.(0*.1.0*.1.0*)* 
    
 [regex from this website.](https://t4tutorials.com/regular-expression-for-the-language-of-an-odd-number-of-1s/#RE_01001010)

   The regex was run against files with string of 0 and 1, each line contains 1000 characters (0 or 1), starting with 10 lines and doubling the size each time.

The time in seconds for each algorithm is in the table below:

![table](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/odd_table.png)

Graph Size/ seconds:

![Normal](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/odd_graph_normal.png)


Log scale graph

![Log](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/odd_graph_log.png)

### Conclusion

We can see that bot algorithms escalate linearly in relation to the size of the string.  

## Email validation regex

On this test the regex was use to validate email string, the regex was compiled and then run it against the strings(only compiled once for each test). This test don't really show's how the alorithm's grows because they are test against strings of the (more or less) same size. But still contrast the 2 algorithms.

      ((a-z)|(A-Z)|(0-9)).((a-z)|(A-Z)|(0-9)|_|/.|/-|/+)*.((a-z)|(A-Z)|(0-9)).@.((a-z)|(A-Z)|(0-9)).((a-z)|(A-Z)|(0-9)|/.)*./..(((a-z)|(A-Z)).((a-z)|(A-Z)).((a-z)|(A-Z))|((a-z)|(A-Z)).((a-z)|(A-Z)))


* start with letter or number: 

      ((a-z)|(A-Z)|(0-9))
* followed by zero or more any letter number or _.-+ special character : 

      ((a-z)|(A-Z)|(0-9)|_|/.|/-|/+)*
* followed by a letter or a number :  

       ((a-z)|(A-Z)|(0-9))
* followed by @: 
 
       @
* followed by a  letter or number after the @ : 


       ((a-z)|(A-Z)|(0-9))
* followed by zero or more letter, number or . : 


       ((a-z)|(A-Z)|(0-9)|/.)*
* end with a dot followed by 2 or 3 letter : 


       /..(((a-z)|(A-Z)).((a-z)|(A-Z)).((a-z)|(A-Z))|((a-z)|(A-Z)).((a-z)|(A-Z)))



![Email table](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/email_table.png)

![Email normal](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/odd_graph_normal.png)

![email log](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/email_log.png)


# Search for words finishing on s in a text file:


      ((a-z)|(A-Z)).((a-z)|'|/-)*.s.(/.| |/?|!|"|')

* start with a lower or upper case letter : 


      ((a-z)|(A-Z))
* followed by a combination of letter ' or - : 


      ((a-z)|'|/-)*
* followed by a s : 


      s
* finish with a withe space or ?!"' after the s:  



      (/.| |/?|!|"|')



![search table](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/search_end_s.png)


![search normal](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/search_normal.png)

![search log](https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project/blob/master/imgs/search_log.png)


# Conclusion

  I got a better understanding of how automatons  can be use for solve programing problems, while learning a new programing language. The develop of the project help me to understand how NFA works and know more about they limits.
 
 The most challenging part of the project was to fully understand Thomson's construction for then implement it on the map and node algorithm. Python was challenging on the start but then I got use to it. 

I'm Happy with the result of the project because I was able to implement both algorithms as I wanted from the start, still I think I did not calculate well the time it would take me to write the final report.

Some future enchantments that can be done are : 
* Catch errors when wrong formatted regex are input.
* Remove dot for concatenation.
* UI more informative .
* Map algorithm can be optimized.
* Fix node algorithm followes() method that goes in infinite loop with double Kleene star(I had planned to test the algorithms using the regex that tell if a binary number is 3 multiple but node algorithm throws stack over flow exception ((0|((1.(0.1*.(0.0)*.0)*.1))*)*) ).


# References

### Shunting yard algorithm

[Shunting Yard Algorithm](http://www.oxfordmathcenter.com/drupal7/node/628)

[Wikipedia](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)

### Thomson's construction

 [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction)

[Converting a regular expression to a NFA - Thompson's Algorithm](http://www.cs.may.ie/staff/jpower/Courses/Previous/parsing/node5.html)

 Michael Sipser. Introduction to the Theory of Computation. International Thomson Publishing, 3rd edition, 1996. (Page 68)

[How are finite automata implemented in code?](https://stackoverflow.com/questions/35272592/how-are-finite-automata-implemented-in-code/35279645)

### Python

 [Understanding the main method of python](https://stackoverflow.com/questions/22492162/understanding-the-main-method-of-python)

[Scroll bar](https://stackoverflow.com/questions/13832720/how-to-attach-a-scrollbar-to-a-text-widget)

[UI](https://www.python-course.eu/tkinter_layout_management.php)

[Unit Test](https://docs.python.org/3/library/unittest.html)

[Time](https://docs.python.org/3/library/time.html)

[Tkinter](https://docs.python.org/3/library/tkinter.html)

 




