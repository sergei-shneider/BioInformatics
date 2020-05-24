
    
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {'A':[0]*k, 'C': [0]*k, 'G':[0]*k, 'T':[0]*k}
    for i in range(t):
        for j in range(k):
            count[Motifs[i][j]][j]+=1/t

    return count
def Consensus(Motifs):
    consOut = ''
    count = Profile(Motifs)
    k = len(Motifs[0])
    for i in range(k):
        maxFreq = ['', 0]
        for item in count:
            if count[item][i]>0.5:
                consOut+=item
                maxFreq=['', 0]
                break
            else: 
                if count[item][i]>maxFreq[1]:
                    maxFreq[0]=item
                    maxFreq[1] = count[item][i]
        consOut+= maxFreq[0]
    return consOut   
def Score(Motifs):
    # Insert code here
    cons = Consensus(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    count = 0
    for i in range(t):
        for j in range(k):
            if Motifs[i][j]!=cons[j]:
                count+=1
    return count
    
def Pr(Text, Profile):
    output = 1
    for i, letter in enumerate(Text):
        output*=Profile[letter][i]
    return output
def ProfileMostProbableKmer(text, k, profile):
    t=len(text)
    candidate = [0, 0]
    for i in range(t-k+1):
        probable = Pr(text[i:i+k], profile)
        if probable>candidate[1]:
            candidate[1] = probable
            candidate[0] = i
    return text[candidate[0]:candidate[0]+k]
def GreedyMotifSearch(Dna, k, t):
    lenStr = len(Dna[0])
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    BestScore = 0
    for i in range(lenStr-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            print(Dna[j])
            p = Profile(Motifs)
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, p))
            print(Motifs)
        thisScore = Score(Motifs)
        print(thisScore)
        try:
            BestScore = Score(BestMotifs)
        except:
            BestScore = float("inf")
        if thisScore<BestScore:
            BestMotifs = Motifs
    return BestMotifs
