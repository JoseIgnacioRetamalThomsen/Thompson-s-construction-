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
        runc = ThomsonsMap.RunChar("((a-z)|(A-Z)).((a-z)|\')*.s.(/.| |/?|!|\"|\')");
        runc = ThomsonsMap.RunChar("((a-z)|(A-Z)).((a-z)|\')*.(/.| |/?|!|\"|\')");
        print(runc.run('a'))
        print(runc.run('\''))
        print(runc.run('s'))
        print(runc.run('f'))
        print(runc.run('s'))
        print(runc.run('.'))
        print(runc.check())
        runc.clear()

        print(runc.run('a'))
        print(runc.run(' '))
        file = open("c:/textfiles/WarAndPeace-LeoTolstoy.txt",encoding="utf-8")
        matchs = list()
        linenum =0
        pos =0
        while True:
            line = file.readline()
            if(len(line) == 0): break;
           # for c in line:
            i = 0
            while i < len(line):
                c = line[i]
                runc.clear()
                start = i;
                stop =0
                for x in range(start,len(line)):
                   # print(x)
                    if(runc.run(line[x])):
                        stop = x
                        if(runc.check()):
                            # match
                            matchs.append((linenum,start))


                            i=stop
                            break
                    else:
                        break




                i  += 1
                pos =i

            #print(linenum)
            linenum += 1

        print(len(matchs))

