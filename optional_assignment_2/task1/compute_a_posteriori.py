from sys import argv

class env:
    def __init__(self):
        self.h1 = [0.1, 1, 0]
        self.h2 = [0.2, 0.75, 0.25]
        self.h3 = [0.4, 0.5, 0.5]
        self.h4 = [0.2, 0.25, 0.75]
        self.h5 = [0.1, 0, 1]
        self.bags = [self.h1, self.h2, self.h3, self.h4, self.h5]
        self.obs = 0.5
    
    def posterior(self, cand):
        for b in self.bags:
            if cand=='C':
                b[0] = b[1]*b[0]/self.obs
            else:
                b[0] = b[2]*b[0]/self.obs

    def observation(self, cand):
        self.obs = 0
        for b in self.bags:
            if cand=="C":
                self.obs += b[0] * b[1]
            else:
                self.obs += b[0] * b[2]
        return self.obs

if __name__ == "__main__":
    Q = argv[1]+'C'
    E = env()
    f = open('result.txt', 'w')
    f.write("Observation sequence Q: {}\n".format(Q))
    f.write("Length of Q: {}\n".format(len(Q)))
    E.observation(Q[0])
    for i in range(len(Q)-1):
        f.write("\nAfter Observation {}: {}\n\n".format(i+1, Q[i]))   
        E.posterior(Q[i])
        curr = E.observation(Q[i+1])
        for j in range(len(E.bags)):
            f.write("P(h{} | Q) = {}\n".format(j+1, E.bags[j][0]))
        if Q[i+1]=='C':
            f.write("\nProbability that the next candy we pick will be C, given Q: {}".format(curr))
            f.write("\nProbability that the next candy we pick will be L, given Q: {}\n".format(1-curr))
        else:
            f.write("\nProbability that the next candy we pick will be C, given Q: {}".format(1-curr))
            f.write("\nProbability that the next candy we pick will be L, given Q: {}\n".format(curr))

