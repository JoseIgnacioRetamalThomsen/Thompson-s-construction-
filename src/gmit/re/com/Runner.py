from src.gmit.re.com import ThomsonsMap
from src.gmit.re.com import Shunting
from src.gmit.re.com import Thomsons


class Runner:
    # main method, start of program
    if __name__ == '__main__':
        print("hello")

        ThomsonsMap.NFA.initStateCount(1)

        #a?nan
        #a?^n.a^n a^n a?.a?.a?.a.a.a a.a.a
        string = "/*.((a-z)|(0-9)|/.)*.@.((a-z)|(0-9))*./..(a-z)+"
        #s1 = "(0|(1.(0.1*(0.0)*.0)*.1)*)*"
        s1 = "a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a"
        p = Shunting.Converter().toPofix(s1)
        print(p)
        n = ThomsonsMap.compile(p)
       # n.tf.printF()
        print(n.run("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

        n = ThomsonsMap.NFA("z")
        n.plus()
        print(n.run(""))
        n.tf.printF()

        print("last")
        print(Thomsons.match("a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a?.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a.a","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
        print(Thomsons.match("a?", "aa"))
