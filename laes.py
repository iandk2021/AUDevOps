import json

with open("medarbejdere.json", "r", encoding="utf-8") as fil:
    medarbejdere = json.load(fil)

print("Medarbejdere:")
for medarbejder in medarbejdere:
    print(f"ID: {medarbejder['medarbejder_id']}, Navn: {medarbejder['navn']}, Afdeling: {medarbejder['afdeling']}, Email: {medarbejder['email']}")