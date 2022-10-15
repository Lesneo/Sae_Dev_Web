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

for i in range(taille) :
    for j in range(len(lables)) :
        aliment = tableSondage[lables[j]][i]
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
    if bio >= 3 :
        habitantBio.append(tableSondage.Nom[i])
    if halal >= 2 :
        habitantHalal.append(tableSondage.Nom[i])
    if vegan >= 3 :
        habitantVegan.append(tableSondage.Nom[i])
    if casher >= 2 :
        habitantCasher.append(tableSondage.Nom[i])

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



categorie = tableAliments.alim_grp_nom_fr.unique()
listeCat = []
for i in categorie :
    listeCat.append([i,0])
#print(listeCat)


for i in range(taille) :
    for j in range(len(lables)) :
        aliment = tableSondage[lables[j]][i]
        catAliment = tableAliments[tableAliments.alim_code==aliment].alim_grp_code
        listeCat[catAliment.values[0]-1][1]+=1


def takeSecond(elem):
    return elem[1]

#print(listeCat)
listeCat.sort(key=takeSecond, reverse=True)
#print(listeCat)
print("<br> <h2> Tableau des aliments les plus choisis dans le sondage </h2> <br>")
tableau = '<table class="table table-striped "><thead class="thead-dark"><tr class="table-dark"><th scope="col">Classement</th><th scope="col">Catégorie Aliment</th><th scope="col">Nombre d\'itérations</th></tr></thead><tbody id="content"> </tbody> </table>'
print(tableau)
element = document.getElementById("content")
def createHTML(ligne, i):
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

for i in range(len(listeCat)) :
    element.append(createHTML(listeCat[i], i))
