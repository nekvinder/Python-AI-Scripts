from functools import reduce
tmpfactors = dict()
def factors(n):
    if str(n) in tmpfactors:
        return tmpfactors[str(n)]
    else:
        lst = set(reduce(list.__add__, ([i, n//i]
                                        for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        tmpfactors[str(n)] = list(lst.difference([n, 1]))
        return list(lst.difference([n, 1]))
for s in range(int(input())):
    aplhaArr = list(map(lambda x: chr(x), range(65, 65+26)))
    (N, L) = input().split(" ")
    cipherText = input().split(" ")
    primesUsed = list()
    words = list()
    for i in cipherText:
        fac = factors(int(i))
        words.append(fac)
        for x in fac:
            if x not in primesUsed:
                primesUsed.append(x)
    primesUsed.sort()
    sentence = ""
    for x in range(int(L)-1):
        sentence += (aplhaArr[primesUsed.index((set(words[x])-set(words[x+1])).pop())])
    sentence += (aplhaArr[primesUsed.index((set(words[len(words)-2]
                                                )-set(words[len(words)-3])).pop())])
    sentence += (aplhaArr[primesUsed.index((set(words[len(words)-1]
                                                )-set(words[len(words)-2])).pop())])
    print("Case #" + str(s+1) + ": " + sentence)
