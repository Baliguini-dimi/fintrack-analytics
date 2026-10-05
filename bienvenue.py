nom = "Dem's"
objectif = "Data Analyst"
budget = 5000
print(f"Bonjour, je m'appelle {nom}")
print(f"Mon objectif est de devenir un {objectif}.")
print(f"Mon budget est de {budget} FCFA.")
print (f"Je suis motivé à atteindre mon objectif et je suis prêt à investir dans ma formation pour y parvenir.")
depense = 3000
reste = budget - depense
print(f"il me reste {reste} FCFA.")
pourcentage = depense / budget * 100
print(f"J'ai dépensé {pourcentage}% de mon budget.")
if pourcentage < 50 :
        print ("situation saine : tu as dépensé moins de la moitié de ton budget")
        print ("situation saine : tu a dépensé moins de la moitié de ton budget")
elif pourcentage < 80 :
        print ("situation à surveiller : tu as dépensé plus de la moitié de ton budget")
        print ( " Attention, surveille tesd depenses")
        print ("attention, surveille tes depenses. ")
else :
        print ("Alerte : ton budget est épuisé ! Tu as dépassé ton budget ! ")
if reste < 0 : 
    print (" Tu as depasser ton budget !") 
           