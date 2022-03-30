import numpy as np


a = np.array([[1, 1, 3, 10],
              [2, 4, -3, 1],
              [1, -1, 4, -8]])


def ReductionGauss(Aaug):
    for c in range(0, len(Aaug) + 1):
        for e in range(c + 1, len(Aaug)):
            g = Aaug[e][c] / Aaug[c][c]
            if g < 0:
                Aaug[e, :] = Aaug[e, :] + abs(g * Aaug[c, :])

            elif g > 0:
                Aaug[e, :] = Aaug[e, :] - g * Aaug[0, :]
    return Aaug

def ResolutionSystTripSup(Taug):

    r = []
    a = ReductionGauss(Taug)
    print(a)
    print(a[-1][-1])
    for e in range(len(a)):
        r.append()


    return r

print(ResolutionSystTripSup(a))



