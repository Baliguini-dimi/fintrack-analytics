depenses = [250, 1200, 800, 150, 3000]
print(sum(depenses))
print(max(depenses))
print(min(depenses))
print(len(depenses))

for depense in depenses:
    print(f"Dépense : {depense} FCFA")

for depense in depenses:
        if depense > 1000:
            print(f"Grosse dépense : {depense} FCFA")
            
for depense in depenses :
        if depense < 500 :
            print (f'petite dépense : {depense} FCFA')
            
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