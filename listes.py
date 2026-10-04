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