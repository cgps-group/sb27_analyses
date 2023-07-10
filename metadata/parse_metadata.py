import pandas as pd

df = pd.read_csv("SB27_sample_master_list - sb27_master_list_06_07_2023.csv")

print(df)
df = df[df["Contamination"]=="Non contaminated"]
print(df)
df = df[df["species"]=="Escherichia coli"]
print(df)
df = df[df['sample'].str.startswith('SB27')]
print(df)


location_map = {
    "Arkansas":"Arkansas",
    "AZ":"Arizona",
    "CA":"California",
    "California":"California",
    "CO":"Colorado",
    "Delaware":"Delaware",
    "IL":"Illinois",
    "Indiana":"Indiana",
    "Iowa":"Iowa",
    "KS":"Kansas",
    "MI":"Michigan",
    "Minnesota":"Minnesota",
    "Mississippi":"Mississippi",
    "Missouri":"Missouri",
    "MN":"Minnesota",
    "MO":"Missouri",
    "NC":"North Carolina",
    "NE":"Nebraska",
    "Nebraska":"Nebraska",
    "NJ":"New Jersey",
    "OR":"Oregon",
    "PA":"Pennsylvania",
    "Pennsylvania":"Pennsylvania",
    "Texas":"Texas",
    "Typo?":"",
    "UT":"Utah",
    "Utah":"Utah",
    "TN":"Tennessee",
    "Washington":"Washington",
    "WI":"Wisconsin",
    "Wisconsin":"Wisconsin",
    "":""
}

df = df.replace({"State":location_map})


lat_dict = {
    "Arkansas":"35.2048883",
    "Arizona":"34.395342",
    "California":"36.7014631",
    "Colorado":"38.7251776",
    "Delaware":"38.6920451",
    "Illinois":"40.0796606",
    "Indiana":"40.3270127",
    "Iowa":"41.9216734",
    "Kansas":"38.27312",
    "Michigan":"43.6211955",
    "Minnesota":"45.9896587",
    "Mississippi":"32.9715285",
    "Missouri":"38.7604815",
    "North Carolina":"35.6729639",
    "Nebraska":"41.7370229",
    "New Jersey":"40.0757384",
    "Oregon":"43.9792797",
    "Pennsylvania":"40.9699889",
    "Tennessee":"35.7730076",
    "Texas":"31.2638905",
    "Utah":"39.4225192",
    "Washington state":"47.2868352",
    "Wisconsin":"44.4308975",
    "":""
}
lon_dict = {
    "Arkansas":"-92.4479108",
    "Arizona":"-111.763275",
    "California":"-118.755997",
    "Colorado":"-105.607716",
    "Delaware":"-75.4013315",
    "Illinois":"-89.4337288",
    "Indiana":"-86.1746933",
    "Iowa":"-93.3122705",
    "Kansas":"-98.5821872",
    "Michigan":"-84.6824346",
    "Minnesota":"-94.6113288",
    "Mississippi":"-89.7348497",
    "Missouri":"-92.5617875",
    "North Carolina":"-79.0392919",
    "Nebraska":"-99.5873816",
    "New Jersey":"-74.4041622",
    "Oregon":"-120.737257",
    "Pennsylvania":"-77.7278831",
    "Tennessee":"-86.2820081",
    "Texas":"-98.5456116",
    "Utah":"-111.714358",
    "Washington state":"-120.212613",
    "Wisconsin":"-89.6884637",
    "":""
}


df['lat'] = df['State'].map(lat_dict)
df['lon'] = df['State'].map(lon_dict)


df_e = pd.read_csv("mlst-EnteroBase.csv")
df_p = pd.read_csv("mlst-Pasteur.csv")
df_s = pd.read_csv("speciator.csv")

df = df.merge(df_e[["sample","ST_Enterobase"]], how='left')
df = df.merge(df_p[["sample","ST_Pasteur"]], how='left')
df = df.merge(df_s[["sample","speciator"]], how='left')

df.to_csv("sb27_microreact.csv",index=False)

print(df)
