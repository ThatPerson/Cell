import random

genome = [ # an array of all proteins present in the cell - ie NaK ATPase, RuBisCo.
    {
        "name": "Aldehyde Reductase", # Not real
        "in": ["D-GLUCOSE", "NADPH"],
        "out": ["D-SORBITOL", "NADP"],
        "abundance": 7,
        "reversible": True
    },
    {
        "name": "L-Iditol Dehydrogenase",
        "in": ["D-SORBITOL", "NAD"],
        "out": ["D-FRUCTOSE", "NADH"],
        "abundance": 7,
        "reversible": True
    },
    {
        "name": "Fructo-kinase",
        "in": ["D-FRUCTOSE", "ATP"],
        "out": ["FRUCTOSE 6-P", "ADP"],
        "abundance": 7,
        "reversible": True
    },
    {
        "name": "6-Phospho-Fructo-1-Kinase",
        "in": ["FRUCTOSE 6-P", "ATP"],
        "out": ["FRUCTOSE 1,6-P", "ADP"],
        "abundance":7,
        "reversible": True
    },
    {
        "name": "Fructose Biphosphate Aldolase",
        "in": ["FRUCTOSE 1,6-P", "H2O"],
        "out": ["D-GLYCERAL-DEHYDE 3-P", "GLYCERONE-P(DIHYDROXY-ACETONE-P)"],
        "abundance": 7,
        "reversible": True
    },
    {
        "name": "Triose-P Isomerase",
        "in": ["GLYCERONE-P(DIHYDROXY-ACETONE-P)"],
        "out": ["D-GLYCERAL-DEHYDE 3-P"],
        "abundance": 7,
        "reversible": True
    },
    {
        "name": "Glyceraldehyde-P Dehydrogenase",
        "in": ["D-GLYCERAL-DEHYDE 3-P", "NAD"],
        "out": ["P", "1,3-P-D-GLYCERATE", "NADH"],
        "abundance": 7,
        "reversible": True
    },
    {
        "name": "3-Phospho-Glycerate Kinase",
        "in": ["ADP", "1-3-P-D-GLYCERATE"],
        "out": ["ATP", "3-P-D-GLYCERATE"],
        "abundance": 7,
        "reversible": True
    },
    {
        "name" : "Phospho-Glycero-Mutase",
        "in" : ["3-P-D-GLYCERATE"],
        "out" : ["2-P-D-GLYCERATE"],
        "abundance" : 7,
        "reversible" : True
    },
    {
        "name" : "Enolase",
        "in" : ["2-P-D-GLYCERATE"],
        "out" : ["H2O", "P-ENOL-PYRUVATE"],
        "abundance" : 7,
        "reversible" : True
    },
    {
        "name" : "Pyruvate Kinase",
        "in" : ["P-ENOL-PYRUVATE", "ADP"],
        "out" : ["ATP", "PYRUVATE"],
        "abundance" : 7,
        "reversible" : True
    },
    {
        "name" : "Formate Acetyltransferase",
        "in" : ["PYRUVATE", "CoA", "NAD"],
        "out" : ["FORMATE", "Acetyl CoA", "NADH", "CO2"],
        "abundance" : 7,
        "reversible" : True
    },
    {
        "name": "AcetylCoADeath",
        "in": ["Acetyl CoA"],
        "out": ["Pico", "CoA"],
        "abundance": 7,
        "reversible": True
    },
    {
        "name": "ATP Synthase",
        "in": ["ADP", "P", "NADH"],
        "out": ["ATP", "NAD"],
        "abundance": 5,
        "reversible": True
    }
]

cell_mix = ["D-GLUCOSE", "D-GLUCOSE", "D-GLUCOSE", "ATP", "ATP", "ATP", "ADP", "ADP", "CoA", "CoA"]

cell_mix = []
for i in range(0, 300):
    cell_mix.append("NAD")
    cell_mix.append("NADPH")
    cell_mix.append("D-GLUCOSE")
    cell_mix.append("ATP")
    cell_mix.append("ATP")
    cell_mix.append("ADP")
    cell_mix.append("CoA")
    cell_mix.append("H2O")
    cell_mix.append("NADH")


def get_printable(s):
    u = []
    for x in s:
        if x not in u:
            u.append(x)
    return u

def find_enzyme(d):
    enzymes = []
    for i in genome:
        if d in i["in"] or (d in i["out"] and i["reversible"] == True):
            enzymes.append(i)
    sum_abundance = 0
    for i in enzymes:
        sum_abundance = sum_abundance + i["abundance"]
    q = random.randint(0, sum_abundance)
    for i in enzymes:
        if (q <= i["abundance"]):
            return i
        else:
            q = q - i["abundance"]
    return -1

for i in range(0, 1000): # Cycles to run for
    print ("======== RUN "+str(i)+" ===========")
    q = get_printable(cell_mix)
    for l in q:
        print (l+": "+str(cell_mix.count(l)))
        
    new_cell_mix = []
    for p in cell_mix:
        s = find_enzyme(p)
        print(s["name"])
        if (s != -1):
            if (p in s["in"]):
                cont = 1
                for d in s["in"]:
                    if d not in cell_mix:
                        cont = 0
                if (cont == 1):
                    for l in s["in"]:
                        cell_mix.remove(l)
                    for o in s["out"]:
                        new_cell_mix.append(o)
            elif (p in s["out"]):
                cont = 1
                for d in s["out"]:
                    if d not in cell_mix:
                        cont = 0
                if (cont == 1):
                    for l in s["out"]:
                        cell_mix.remove(l)
                    for o in s["in"]:
                        new_cell_mix.append(o)
    for z in cell_mix:
        new_cell_mix.append(z)
    cell_mix = new_cell_mix

    
