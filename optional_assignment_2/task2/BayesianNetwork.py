class BayesianNetwork:
    def __init__(self):
        self.B = .001
        self.E = .002
        self.A_BE = .95
        self.A_BnE = .94
        self.A_nBE = .29
        self.A_nBnE = .001
        self.J_A = .90
        self.J_nA = .05
        self.M_A = .70
        self.M_nA = .01

    def calculateProb(self, B, E, A, J, M, cond):
        dummyJ, dummyM, dummyA, dummyB, dummyE = 0.0, 0.0, 0.0, 0.0, 0.0
        # check given conditions
        if not B:
            dummyB = 1 - self.B
        else:
            dummyB = self.B
        if not E:
            dummyE = 1 - self.E
        else:
            dummyE = self.E
        if not A:
            if J:
                dummyJ = self.J_nA
            else:
                dummyJ = 1 - self.J_nA
            if M:
                dummyM = self.M_nA
            else:
                dummyM = 1 - self.M_nA
        else:
            if J:
                dummyJ = self.J_A
            else:
                dummyJ = 1 - self.J_A
            if M:
                dummyM = self.M_A
            else:
                dummyM = 1 - self.M_A
        if B and E:
            if A:
                dummyA = self.A_BE
            else:
                dummyA = 1 - self.A_BE
        if not B and E:
            if A:
                dummyA = self.A_nBE
            else:
                dummyA = 1 - self.A_nBE
        if B and not E:
            if A:
                dummyA = self.A_BnE
            else:
                dummyA = 1 - self.A_BnE
        if not B and not E:
            if A:
                dummyA = self.A_nBnE
            else:
                dummyA = 1 - self.A_nBnE
        # calculate denominator
        denom = 1.
        for c in cond:
            if c=='B':
                denom *= dummyB
            if c=='E':
                denom *= dummyE
            if c=='A':
                denom *= dummyA
            if c=='J':
                denom *= dummyJ
            if c=='M':
                denom *= dummyM
        return dummyB*dummyE*dummyA*dummyJ*dummyM/denom