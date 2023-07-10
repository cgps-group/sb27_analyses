import pandas as pd

df = pd.read_csv("Escherichia coli__cgmlst.csv")
df = df.sample(frac=0.1, random_state=42)
df = df.reset_index()

l =[]
for index, row in df.iterrows():
    l.append( [row['Genome Name']] + row['code'].split("_") )

df = pd.DataFrame(l)


for column in df:
    if column ==0:
        continue

    #print(list(df[column]))
    #print("before")
    
    tl = list(df[column])
    tl = list(dict.fromkeys(tl))
    
    num = []
    new = []
    com = []
    new_d = dict()

    #organize values accprding to which ones are numbers and which ones arent
    for a in tl:
        if a.isdigit():
            num.append(int(a))
        else:
            if "," in a:
                com.append(a)
            else:
                new.append(a)


    # Create dictionary with alleles as keys and identities as the value

    # If it is a number then the allele and the identity is the same
    for nu in num:
        new_d[nu] = int(nu)

    # If it is not a number then the allele is the hash and the identity is a artificial number
    start = max(num)
    for n in new:
        start = start+1
        new_d[n] = int(start)

    # If the allele has a comma,
    for c in com:
        first = c.split(",")[0]
        if first.isdigit():
            new_d[c] = int(first)
        else:
            start = start+1
            new_d[c] = int(start)


    #remappear new datos
    df = df.replace({column:new_d})

    #print(new_d)
    #print(list(df[column]))
    #exit()


print(df)


df.to_pickle("subset.pkl") 
#np.save("subset.npy",X)
