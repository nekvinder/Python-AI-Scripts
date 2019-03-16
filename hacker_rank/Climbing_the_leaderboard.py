# Todo : make optimization,large dataset takes too much time
def helpingFn(scores, aliceval):
    scores.append(aliceval)
    scores.sort(reverse=True)
    rnk = list()
    rank = 1
    for i in range(len(scores)):
        rnk.append(rank)
        if i + 1 == len(scores):
            break;
        if not scores[i + 1] == scores[i]:
            rank += 1
    print(rnk[scores.index(aliceval)], end='')


def climbingLeaderboard(scores, alice):
    for e in alice:
        helpingFn(scores, e)


climbingLeaderboard(list(map(int, "100 90 90 80 75 60".split(" "))), list(map(int, "50 65 77 90 102".split(" "))))
