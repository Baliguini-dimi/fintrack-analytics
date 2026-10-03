nom = "Dem's"
objectif = "Data Analyst"
budget = 1000
print(f"Bonjour, je m'appelle {nom}")
print(f"Mon objectif est de devenir un {objectif}.")
print(f"Mon budget est de {budget} FCFA.")
print (f"Je suis motivé à atteindre mon objectif et je suis prêt à investir dans ma formation pour y parvenir.")
depense = 250
reste = budget - depense
print(f"il me reste {reste} FCFA.")
pourcentage = depense / budget * 100
print(f"J'ai dépensé {pourcentage}% de mon budget.")
if pourcentage < 50 :
        print ("situation saine : tu a depensé moins de la moitié de ton budget")
elif pourcentage < 80 :
        print ( " Attention, surveille tesd depenses")
        print ("attention, surveille tes depenses. ")
else :
        print ("alerte : ton budget est epuiser ! ")