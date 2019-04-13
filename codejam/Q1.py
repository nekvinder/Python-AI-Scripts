# codejam
def fourcheck(n):
    return (str(n).__contains__("4"))


def fourpos(n):
    indices = [str(n).__len__() - i for i, x in enumerate(str(n)) if x == "4"]
    return(indices)


for i in range(int(input())):
    cinput = int(input())
    tmpSecondNum = 0
    if(fourcheck(cinput) == False):
        print("Case #"+str(i+1)+": "+str(cinput)+" "+str(tmpSecondNum))
    else:
        while(True):
            val = 0
            for s in fourpos(cinput):
                val += 10**(s-1)
            # print(val)
            tmpSecondNum += val
            if(fourcheck(cinput-tmpSecondNum) == False and fourcheck(tmpSecondNum) == False):
                print("Case #"+str(i+1)+": "+str(cinput -
                                                 tmpSecondNum)+" "+str(tmpSecondNum))
                break
