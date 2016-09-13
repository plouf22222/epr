'''
Created on 13 sept. 2016

@author: bfayolle
'''
import os
import csv
from decimal import *

tableau = dict()
table = dict()
table["P201"] = ["LVA", "PEA", "PEP", "LVJ", "CEL", "PEL", "LDD", "LEP"]
table["P202"] = ["LEP"]
table["P203"] = ["LDD", "LEP", "LVJ", "PEA", "PEP"]
table["P205"] = ["LDD", "LEP", "LVJ", "PEA"]
table["P206"] = ["CEL", "LDD", "LEP", "LVA", "LVJ"]
table["P207"] = ["PEA", "PEL", "PEP"]
table["P208"] = ["PEL"]

L = [os.path.join(os.getcwd(), f) for f in os.listdir('.')
     if os.path.isfile(os.path.join(os.getcwd(), f))]
for fichier in L:
    if fichier[-3:] == 'txt':
        f_in = open(fichier, 'r')
        sample = f_in.read(1000000)
        mon_dialect = csv.Sniffer().sniff(sample)
        isheader = csv.Sniffer.has_header(csv.Sniffer(), sample)
        sample = ""
        f_in.seek(0)
        data = csv.reader(f_in, mon_dialect)
        print("==> Fichier : ", fichier)
        if isheader:
            header = next(data)
        print("delimiter = " + mon_dialect.delimiter)
        try:
            nom_pdt = header.index("NomPdt")
            int_index = header.index("IntEx")
            P201_index = header.index("P201")
            P202_index = header.index("P202")
            P203_index = header.index("P203")
            P205_index = header.index("P205")
            P206_index = header.index("P206")
            P207_index = header.index("P207")
            P208_index = header.index("P208")
            amd_index = header.index("Amende")
            datclo_idx = header.index("DatClo")
            print("Le fichier FEC : " + str(f_in.name) + " est charge")
            for ligne in data:
                nb_ano = 0
                if ligne[nom_pdt] in tableau:
                    if ligne[P201_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P201"][0] += 1
                        tableau[ligne[nom_pdt]]["P201"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P201"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P201"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P202_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P202"][0] += 1
                        tableau[ligne[nom_pdt]]["P202"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P202"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P202"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P203_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P203"][0] += 1
                        tableau[ligne[nom_pdt]]["P203"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P203"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P203"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P205_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P205"][0] += 1
                        tableau[ligne[nom_pdt]]["P205"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P205"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P205"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P206_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P206"][0] += 1
                        tableau[ligne[nom_pdt]]["P206"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P206"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P206"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P207_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P207"][0] += 1
                        tableau[ligne[nom_pdt]]["P207"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P207"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P207"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P208_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P208"][0] += 1
                        tableau[ligne[nom_pdt]]["P208"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P208"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P208"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                else:
                    tableau[ligne[nom_pdt]] = dict()
                    tableau[ligne[nom_pdt]]["P201"] = [0, Decimal("0"), Decimal("0"), Decimal("0")]
                    tableau[ligne[nom_pdt]]["P202"] = [0, Decimal("0"), Decimal("0"), Decimal("0")]
                    tableau[ligne[nom_pdt]]["P203"] = [0, Decimal("0"), Decimal("0"), Decimal("0")]
                    tableau[ligne[nom_pdt]]["P205"] = [0, Decimal("0"), Decimal("0"), Decimal("0")]
                    tableau[ligne[nom_pdt]]["P206"] = [0, Decimal("0"), Decimal("0"), Decimal("0")]
                    tableau[ligne[nom_pdt]]["P207"] = [0, Decimal("0"), Decimal("0"), Decimal("0")]
                    tableau[ligne[nom_pdt]]["P208"] = [0, Decimal("0"), Decimal("0"), Decimal("0")]
                    if ligne[P201_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P201"][0] += 1
                        tableau[ligne[nom_pdt]]["P201"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P201"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P201"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P202_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P202"][0] += 1
                        tableau[ligne[nom_pdt]]["P202"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P202"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P202"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P203_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P203"][0] += 1
                        tableau[ligne[nom_pdt]]["P203"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P203"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P203"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P205_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P205"][0] += 1
                        tableau[ligne[nom_pdt]]["P205"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P205"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P205"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P206_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P206"][0] += 1
                        tableau[ligne[nom_pdt]]["P206"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P206"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P206"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P207_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P207"][0] += 1
                        tableau[ligne[nom_pdt]]["P207"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P207"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P207"][3] += Decimal(ligne[amd_index].replace(',', '.'))
                    if ligne[P208_index] == "O":
                        nb_ano += 1
                        tableau[ligne[nom_pdt]]["P208"][0] += 1
                        tableau[ligne[nom_pdt]]["P208"][1] += Decimal(ligne[int_index].replace(',', '.'))
                        tableau[ligne[nom_pdt]]["P208"][2] += Decimal(ligne[amd_index].replace(',', '.'))
                        if nb_ano < 2:
                            tableau[ligne[nom_pdt]]["P208"][3] += Decimal(ligne[amd_index].replace(',', '.'))
            
        except ValueError as e:
            PrintError(e)
        f_in.close()
f_out = open("cumul.csv", 'w')
f_out.write("Type cpt;ANO;NB;IntEx;Amende;Amende unique\n")
for key in sorted(tableau):
    for k in sorted(tableau[key]):
        if key in table[k]:
            f_out.write(key + ";" + k + ";" + str(tableau[key][k][0]) + ";" + str(tableau[key][k][1]).replace('.', ',') + ";" + str(tableau[key][k][2]).replace('.', ',') + ";" + str(tableau[key][k][3]).replace('.', ',') + '\n')
f_out.close()

