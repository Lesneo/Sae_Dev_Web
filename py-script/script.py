# On importe les bibliothèques qui nous seront utiles
from pandas import *  # pour lire, importer et manipuler des données sous forme tableur
from pyodide.http import open_url
tableAliments = read_csv(open_url('https://raw.githubusercontent.com/Lesneo/Sae_Dev_Web/main/mission2/Aliments.csv'), sep=';')
tableSondage = read_csv(open_url('https://raw.githubusercontent.com/Lesneo/Sae_Dev_Web/main/mission2/Sondage_1.csv'), sep=';')

lables = tableSondage.columns[8:]
taille = len(tableSondage.Nom)
bio = 0
halal = 0
vegan = 0
casher = 0
habitantBio = []
habitantHalal = []
habitantVegan = []
habitantCasher = []
categorie = tableAliments.alim_grp_nom_fr.unique()
listeCat = []
for i in categorie :
    listeCat.append([i,0])

kjLable = tableAliments.columns[tableAliments.columns == "Energie, Règlement UE N° 1169/2011 (kJ/100 g)"] #J
sugarLabel = tableAliments.columns[tableAliments.columns == "Sucres (g/100 g)"] #S
agsLabel = tableAliments.columns[tableAliments.columns == "AG saturés (g/100 g)"] #AF
sodiumLabel = tableAliments.columns[tableAliments.columns == "Sodium (mg/100 g)"] #BI
fibreLabel = tableAliments.columns[tableAliments.columns == "Fibres alimentaires (g/100 g)"] #AA
protLabel = tableAliments.columns[tableAliments.columns == "Protéines, N x facteur de Jones (g/100 g)"] #O
alimHabitant = []

def createHTML1(ligne, i):
    tr_element = document.createElement('tr')
    th_ligne = document.createElement('th')
    th_ligne.setAttribute("scope","row")
    first_name_element = document.createElement('td')
    last_name_element = document.createElement('td')
    

    th_ligne.innerText = i+1
    first_name_element.innerText = ligne[0]
    last_name_element.innerText = ligne[1]
    
    tr_element.append(th_ligne)
    tr_element.append(first_name_element)
    tr_element.append(last_name_element)
    
    return tr_element



def createHTML2(ligne, s, i):
    tr_element = document.createElement('tr')
    th_ligne = document.createElement('th')
    th_ligne.setAttribute("scope","row")
    first_name_element = document.createElement('td')
    score_moyen = document.createElement('td')
    

    th_ligne.innerText = i
    first_name_element.innerText = s
    score_moyen.innerText = ligne
    
    tr_element.append(th_ligne)
    tr_element.append(first_name_element)
    tr_element.append(score_moyen)
    
    return tr_element

def calculKj(kj) :
    if kj == "-" :
        return 0
    elif float(kj) > 3350 :
        return 10
    elif float(kj) > 3015 :
        return 9
    elif float(kj) > 2680 :
        return 8
    elif float(kj) > 2345 :
        return 7
    elif float(kj) > 2010 :
        return 6
    elif float(kj) > 1675 :
        return 5
    elif float(kj) > 1340 :
        return 4
    elif float(kj) > 1005 :
        return 3
    elif float(kj) > 670 :
        return 2
    elif float(kj) > 335 :
        return 1
    else :
        return 0

def calculSugar(valeur) :
    if valeur == "traces" or valeur == "-" :
        return 0
    elif float(valeur) > 13.5 :
        return 10
    elif float(valeur) <= 13.5 :
        return 9
    elif float(valeur) <= 12 :
        return 8
    elif float(valeur) <= 10.5 :
        return 7
    elif float(valeur) <= 9 :
        return 6
    elif float(valeur) <= 7.5 :
        return 5
    elif float(valeur) <= 6 :
        return 4
    elif float(valeur) <= 4.5 :
        return 3
    elif float(valeur) <= 3 :
        return 2
    elif float(valeur) <= 1.5 :
        return 1
    else :
        return 0

def calculAGS(valeur) :
    if valeur == "-" :
        return 0
    elif float(valeur) > 10 :
        return 10
    elif float(valeur) > 9 :
        return 9
    elif float(valeur) > 8 :
        return 8
    elif float(valeur) > 7 :
        return 7
    elif float(valeur) > 6 :
        return 6
    elif float(valeur) > 5 :
        return 5
    elif float(valeur) > 4 :
        return 4
    elif float(valeur) > 3 :
        return 3
    elif float(valeur) > 2 :
        return 2
    elif float(valeur) > 1 :
        return 1
    else :
        return 0

def calculSodium(valeur) :
    if valeur == "-" :
        return 0
    elif float(valeur) > 900 :
        return 10
    elif float(valeur) > 810 :
        return 9
    elif float(valeur) > 720 :
        return 8
    elif float(valeur) > 630 :
        return 7
    elif float(valeur) > 540 :
        return 6
    elif float(valeur) > 450 :
        return 5
    elif float(valeur) > 360 :
        return 4
    elif float(valeur) > 270 :
        return 3
    elif float(valeur) > 180 :
        return 2
    elif float(valeur) > 90 :
        return 1
    else :
        return 0

def calculFibre(valeur) :
    if valeur == "-" or valeur == "traces":
        return 0
    elif float(valeur) > 3.5 :
        return 5
    elif float(valeur) > 2.8 :
        return 4
    elif float(valeur) > 2.1 :
        return 3
    elif float(valeur) > 1.4 :
        return 2
    elif float(valeur) > 0.7 :
        return 1
    else :
        return 0

def calculProt(valeur) :
    if valeur == "-" :
        return 0
    elif float(valeur) > 8 :
        return 5
    elif float(valeur) > 6.4 :
        return 4
    elif float(valeur) > 4.8 :
        return 3
    elif float(valeur) > 3.2 :
        return 2
    elif float(valeur) > 1.6 :
        return 1
    else :
        return 0

def calculScore(valeur) :
    if valeur > 19 :
        return 5
    elif valeur > 11 :
        return 4
    elif valeur > 3 :
        return 3
    elif valeur > 0 :
        return 2
    else :
        return 1
    
dictScore = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E"
    }

for i in range(taille) :
    alimHabitant.append([])
    for j in range(len(lables)) :
        aliment = tableSondage[lables[j]][i]
        #bio vegan casher halal
        nomAliment = tableAliments[tableAliments.alim_code==aliment].alim_nom_fr
        catAliment = tableAliments[tableAliments.alim_code==aliment].alim_ssssgrp_nom_fr
        if "bio" in nomAliment.values[0] :
            bio+=1
        if "halal" in catAliment.values[0] :
            halal+=1
        if "vegan" in nomAliment.values[0] :
            vegan+=1
        if "casher" in catAliment.values[0] :
            casher+=1

        #catégorie
        catAliment = tableAliments[tableAliments.alim_code==aliment].alim_grp_code
        listeCat[catAliment.values[0]-1][1]+=1
        
        #score santé
        valeur = tableAliments[kjLable][tableAliments.alim_code==aliment].values[0][0].replace(",",".")
        #print(valeur)
        alimHabitant[i].append(calculKj(valeur))
        valeur = tableAliments[sugarLabel][tableAliments.alim_code==aliment].values[0][0].replace(",",".").replace("<","").replace(" ","")
        #print(valeur)
        #print(valeur)
        alimHabitant[i][j] = alimHabitant[i][j]+calculSugar(valeur)
        valeur = tableAliments[agsLabel][tableAliments.alim_code==aliment].values[0][0].replace(",",".").replace("<","").replace(" ","")
        #print(valeur)
        alimHabitant[i][j] = alimHabitant[i][j]+calculAGS(valeur)
        valeur = tableAliments[sodiumLabel][tableAliments.alim_code==aliment].values[0][0].replace(",",".")
        alimHabitant[i][j] = alimHabitant[i][j]+calculSodium(valeur)
        valeur = tableAliments[fibreLabel][tableAliments.alim_code==aliment].values[0][0].replace(",",".").replace("<","").replace(" ","")
        alimHabitant[i][j] = alimHabitant[i][j]-calculFibre(valeur)
        valeur = tableAliments[protLabel][tableAliments.alim_code==aliment].values[0][0].replace(",",".").replace("<","").replace(" ","")
        alimHabitant[i][j] = alimHabitant[i][j]-calculProt(valeur)
    
    #suite bio vegan casher halal
    if bio >= 3 :
        habitantBio.append(tableSondage.Nom[i] + " " + tableSondage.Prénom[i])
    if halal >= 2 :
        habitantHalal.append(tableSondage.Nom[i] + " " + tableSondage.Prénom[i])
    if vegan >= 3 :
        habitantVegan.append(tableSondage.Nom[i] + " " + tableSondage.Prénom[i])
    if casher >= 2 :
        habitantCasher.append(tableSondage.Nom[i] + " " + tableSondage.Prénom[i])
        score = 0

    bio = 0
    halal = 0
    vegan = 0
    casher = 0
    
#bio
if habitantBio == [] :
    bio = "Aucun habitant préfère les aliments Bio"
else :
    bio = "Liste des habitants qui préfèrent les aliments Bio : <ul>"
    for i in habitantBio :
        bio += "<li>" + i + "</li> "
    bio += "</ul>"
print(bio)

#halal
if habitantHalal == [] :
    bio = "Aucun habitant préfère les aliments Halal"
else :
    bio = "Liste des habitants qui préfèrent les aliments Halal : <ul>"
    for i in habitantHalal :
        bio += "<li>" + i + "</li> "
    bio += "</ul>"
print(bio)

#vegan
if habitantVegan == [] :
    bio = "Aucun habitant préfère les aliments Vegan"
else :
    bio = "Liste des habitants qui préfèrent les aliments Vegan : <ul>"
    for i in habitantVegan :
        bio += "<li>" + i + "</li> "
    bio += "</ul>"
print(bio)

#casher
if habitantCasher == [] :
    bio = "Aucun habitant préfère les aliments Casher"
else :
    bio = "Liste des habitants qui préfèrent les aliments Casher : <ul>"
    for i in habitantCasher :
        bio += "<li>" + i + "</li> "
    bio += "</ul>"
print(bio)


#catégorie
def takeSecond(elem):
    return elem[1]

listeCat.sort(key=takeSecond, reverse=True)
print("<br> <h2> Tableau des aliments les plus choisis dans le sondage </h2> <br>")
tableau = '<table class="table table-striped "><thead class="thead-dark"><tr class="table-dark"><th scope="col">Classement</th><th scope="col">Catégorie Aliment</th><th scope="col">Nombre d\'itérations</th></tr></thead><tbody id="content"> </tbody> </table>'
print(tableau)
element = Element("content")
for i in range(len(listeCat)) :
    element.element.innerHTML(createHTML1(listeCat[i], i))


#score habitant
scoreAlim = []
for i in range(len(alimHabitant)) :
    scoreAlim.append([])
    for j in range(len(alimHabitant[i]))  :
        scoreAlim[i].append(calculScore(alimHabitant[i][j]))

scoreHabit = []
for i in scoreAlim :
    scoreHabit.append(sum(i)/len(i))

print("<br> <h2> Tableau des aliments les plus choisis dans le sondage </h2> <br> <p> Le score est calculé avec la moyenne du Nutriscore des 10 produits : </p> <br>")
tableau = '<table class="table table-striped "><thead class="thead-dark"><tr class="table-dark"><th scope="col">Habitant</th><th scope="col">Score Santé</th><th scope="col">Score moyen des produits</th></tr></thead><tbody id="contentScore"> </tbody> </table>'
print(tableau)
element = document.getElementById("contentScore")


nomLabel = tableSondage.columns[tableSondage.columns == "Nom"]
prenomLabel = tableSondage.columns[tableSondage.columns == "Prénom"]
for i in range(len(scoreHabit)) :
    nomPrenom = tableSondage[nomLabel].values[i][0] + " " + tableSondage[prenomLabel].values[i][0]
    element.append(createHTML2(scoreHabit[i], dictScore[round(scoreHabit[i])], nomPrenom))
