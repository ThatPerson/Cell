import random

genome = [ # an array of all proteins present in the cell - ie NaK ATPase, RuBisCo.
    {
        "name" = "Aldehyde Reductase", # Not real
        "in" = ["D-GLUCOSE", "NADH"],
        "out" = ["D-SORBITOL", "NAD"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "L-Iditol Dehydrogenase",
        "in" = ["D-SORBITOL", "NAD"],
        "out" = ["D-FRUCTOSE", "NADH"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "Fructo-kinase",
        "in" = ["D-FRUCTOSE", "ATP"],
        "out" = ["FRUCTOSE 6-P", "ADP"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "6-Phospho-Fructo-1-Kinase",
        "in" = ["FRUCTOSE 6-P", "ATP"],
        "out" = ["FRUCTOSE 1,6-P", "ADP"],
        "abundance"= 7,
        "reversible" = True
    },
    {
        "name" = "Fructose Biphosphate Aldolase",
        "in" = ["FRUCTOSE 1,6-P", "H2O"],
        "out" = ["D-GLYCERAL-DEHYDE 3-P", "GLYCERONE-P(DIHYDROXY-ACETONE-P)"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "Triose-P Isomerase",
        "in" = ["GLYCERONE-P(DIHYDROXY-ACETONE-P)"],
        "out" = ["D-GLYCERAL-DEHYDE 3-P"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "Glyceraldehyde-P Dehydrogenase",
        "in" = ["D-GLYCERAL-DEHYDE 3-P", "NAD"],
        "out" = ["P", "1,3-P-D-GLYCERATE", "NADH"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "3-Phospho-Glycerate Kinase",
        "in" = ["ADP", "1-3-P-D-GLYCERATE"],
        "out" = ["ATP", "3-P-D-GLYCERATE"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "Phospho-Glycero-Mutase",
        "in" = ["3-P-D-GLYCERATE"],
        "out" = ["2-P-D-GLYCERATE"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "Enolase",
        "in" = ["2-P-D-GLYCERATE"],
        "out" = ["H2O", "P-ENOL-PYRUVATE"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "Pyruvate Kinase",
        "in" = ["P-ENOL-PYRUVATE", "ADP"],
        "out" = ["ATP", "PYRUVATE"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "Formate Acetyltransferase",
        "in" = ["PYRUVATE", "CoA", "NAD"],
        "out" = ["FORMATE", "Acetyl CoA", "NADH", "CO2"],
        "abundance" = 7,
        "reversible" = True
    },
    {
        "name" = "AcetylCoADeath",
        "in" = ["Acetyl CoA"],
        "out" = ["Pico", "CoA"],
        "abundance" = 7,
        "reversible" = True
    }
]

cell_mix = ["D-GLUCOSE", "D-GLUCOSE", "D-GLUCOSE", "ATP", "ATP", "ATP", "ADP", "ADP", "CoA", "CoA"]

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

for i in range(0, 100): # Cycles to run for
    new_cell_mix = []
    for p in cell_mix:
        s = find_enzyme(p)
        if (p in s["in"]):
            cont = 1
            for d in s["in"]:
                if d not in cell_mix:
                    cont = 0
            if (cont == 1):
                for l in s["in"]:
                    cell_mix.remove(l):
                for o in s["out"]:
                    new_cell_mix.append(o)
        elif (p in s["out"]):
            cont = 1
            for d in s["out"]:
                if d not in cell_mix:
                    cont = 0
            if (cont == 1):
                for l in s["out"]:
                    cell_mix.remove(l):
                for o in s["in"]:
                    new_cell_mix.append(o)
    cell_mix = new_cell_mix
    print(str(i) + ": " + str(cell_mix.count("D-GLUCOSE")) + " // " + str(cell_mix.count("Pico"))
    
