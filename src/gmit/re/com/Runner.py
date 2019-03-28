#from src.gmit.re.com import ThomsonsMap
#from src.gmit.re.com import Shunting
#from src.gmit.re.com import Thomsons
import ThomsonsMap
import Shunting
import Thomsons

class Runner:
    # main method, start of program
    if __name__ == '__main__':
        print("hello")

        ThomsonsMap.NFA.initStateCount(1)

        # word that finish with s
        #runc = ThomsonsMap.RunChar("((a-z)|(A-Z)).((a-z)|\')*.s.(/.| |/?|!|\"|\')");
        runc = Thomsons.RunChar("((a-z)|(A-Z)).((a-z)|\')*.s.(/.| |/?|!|\"|\')");
        print(runc.run('a'))
        print(runc.run('\''))
        print(runc.run('s'))
        print(runc.run(' '))
        print(runc.check())


