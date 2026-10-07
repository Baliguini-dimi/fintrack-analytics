transactions = {
    "montant": 1200,
    "catégorie": "Transport",
    "date": "2023-10-15"
}
print(transactions["montant"])
print(transactions["catégorie"])
print(transactions["date"])
transactions["montant"] = 1500
transactions["moyen"] = "Mobile Money"
print(transactions)


Famille = {
    "Père": "Joseph",
    "mère": "Annie",
    "Nombre de frères": 2,
    "Nombre de sœurs": 3
}
print(Famille["Père"])
print(Famille["Nombre de frères"])
print(Famille["Nombre de sœurs"])
Famille["Fils"] = "Dimitri"
Famille["Adresse"] = "Bangui"
print(Famille)