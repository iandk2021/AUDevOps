import json

with open("medarbejdere.json", "r", encoding="utf-8") as fil:
    medarbejdere = json.load(fil)

id = input("Indtast medarbejder ID for at se detaljer: ")
print("Medarbejdere:")
for medarbejder in medarbejdere:
    if str(medarbejder['medarbejder_id']) == id:
        print(f"ID: {medarbejder['medarbejder_id']}, Navn: {medarbejder['navn']}, Afdeling: {medarbejder['afdeling']}, Email: {medarbejder['email']}")