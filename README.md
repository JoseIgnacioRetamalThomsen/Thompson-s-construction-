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




Please check the wiki https://github.com/JoseIgnacioRetamalThomsen/graph-theory-project.wiki.git
