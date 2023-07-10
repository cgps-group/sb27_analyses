import pandas as pd

# Load data from pathogen.watch results provided by Corin Yeats
df = pd.read_csv("../Escherichia coli__cgmlst.csv")
df = df.sample(frac=0.1, random_state=42)
df = df.reset_index()


# Extract allele information from cgmlst results
temp_list =[]
for index, row in df.iterrows():
    temp_list.append( [row['Genome Name']] + row['code'].split("_") )
df = pd.DataFrame(temp_list)


# Parse data in columns to treat loci with multiple alleles found,
# loci with unreported alleles 
for column in df:
    if column ==0:
        continue

    tl = list(df[column])
    tl = list(dict.fromkeys(tl))
    
    num = []
    new = []
    com = []
    new_d = dict()

    # Organize values accprding to which ones are numbers and which ones arent
    for a in tl:
        if a.isdigit():
            num.append(a)
        else:
            if "," in a:
                com.append(a)
            else:
                new.append(a)


    # Create dictionary with alleles as keys and identities as the value
    # If it is a number then the allele and the identity is the same
    for nu in num:
        new_d[nu] = nu

    # If it is not a number then the allele is the hash and the identity is a artificial number
    for n in new:
        new_d[n] = n

    # If the allele has a comma,
    for c in com:
        first = c.split(",")[0]
        new_d[c] = first


    # Remap new data
    df = df.replace({column:new_d})

# Save to pickle
df.to_pickle("subset0.pkl")
