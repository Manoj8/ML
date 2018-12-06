import csv
with open('trainingexamples.csv') as csvFile:
        data = [tuple(line) for line in csv.reader(csvFile)]

def domain():
        D=[]
        for i in range(len(data[0])):
                D.append(list(set(ele[i] for ele in data)))
        return D
D = domain()

def consistant(h1,h2):
        for x,y in zip(h1,h2):
                if not(x=='?' or (x!='Փ' and (x==y or y=='Փ'))):
                        return False
        return True

def candidateAlgorithm():
        G = {('?',) * (len(data[0]) - 1),}
        S = ['Փ'] * (len(data[0]) - 1)
        no=0
        print("G[{0}]".format(no),G)
        print("S[{0}]".format(no),S)
        for item in data:
                no += 1
                inp,res = item[:-1],item[-1]
                if res in "Yy":
                        i=0        
                        G = {g for g in G if  (consistant(g,inp))}
                        for s,x in zip(S,inp):
                                if not s == x:
                                        S[i]='?' if s!='Փ' else x
                                i+=1
                else:
                        S=S
                        gprev = G.copy()
                        for g in gprev:
                                if g not in G:
                                        continue
                                
                                for i in range(len(g)):
                                        if g[i]=='?':
                                                for val in D[i]:
                                                        if inp!=val and val==S[i]:
                                                                g_new=g[:i]+ (val,) + g[i:]
                                                                G.add(g_new)
                                        else:
                                                G.add(g)
                                                G.difference_update([h for h in G if any([consistant(h,g1) for g1 in G if h!=g1])])
        print("G[{0}]".format(no),G)
        print("S[{0}]".format(no),S)
candidateAlgorithm()
