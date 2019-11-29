from sys import argv
from copy import *
from BayesianNetwork import BayesianNetwork    

# Read arguments
B, E, A, J, M = None, None, None, None, None
for a in argv[1:]:
    if a[0]=='B' and a[1]=='f':
        B = False
    elif a[0]=='B' and a[1]=='t':
        B = True
    if a[0]=='E' and a[1]=='f':
        E = False
    elif a[0]=='E' and a[1]=='t':
        E = True
    if a[0]=='A' and a[1]=='f':
        A = False
    elif a[0]=='A' and a[1]=='t':
        A = True
    if a[0]=='J' and a[1]=='f':
        J = False
    elif a[0]=='J' and a[1]=='t':
        J = True
    if a[0]=='M' and a[1]=='f':
        M = False
    elif a[0]=='M' and a[1]=='t':
        M = True

# Deal with conditions
cond = []
if 'given' in argv:
    for g in range(argv.index('given')+1, len(argv)):
        cond.append(argv[g][0])

# Build a truth table via dfs
def buildTruth(truthTable,truth):
    if truth.count(None) == 0:
        truthTable.append(truth)
        return truthTable
    else:
        noneIdx = truth.index(None)
        t = deepcopy(truth)
        t[noneIdx] = True
        f = deepcopy(truth)
        f[noneIdx] = False
        buildTruth(truthTable, t)
        buildTruth(truthTable, f)
        return truthTable

truthTable = buildTruth([], [B, E, A, J, M])

# Instantiate class
bn = BayesianNetwork()
final_probability = 0.0
for t in truthTable:
    final_probability += bn.calculateProb(t[0], t[1], t[2], t[3], t[4], cond)

print 'The answer of probability is : {}'.format(final_probability)