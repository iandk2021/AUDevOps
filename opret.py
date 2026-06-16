import json

with open("medarbejdere.json", "r", encoding="utf-8") as fil:
    medarbejdere = json.load(fil)

navn = input("Navn: ")
afdeling = input("Afdeling: ")
email = input("Email: ")

ny_medarbejder = {
    "medarbejder_id": medarbejdere[-1]["medarbejder_id"] + 1,
    "navn": navn,
    "afdeling": afdeling,
    "email": email
}

medarbejdere.append(ny_medarbejder)

with open("medarbejdere.json", "w", encoding="utf-8") as fil:
    json.dump(medarbejdere, fil, ensure_ascii=False, indent=4)

print("Medarbejder oprettet!")
