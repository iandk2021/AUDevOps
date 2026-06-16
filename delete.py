import json

def delete_medarbejder(id):
    with open("medarbejdere.json", "r", encoding="utf-8") as fil:
        medarbejdere = json.load(fil)

    for medarbejder in medarbejdere:
        if str(medarbejder['medarbejder_id']) == id:
            medarbejdere.remove(medarbejder)
            break

    with open("medarbejdere.json", "w", encoding="utf-8") as fil:
        json.dump(medarbejdere, fil, ensure_ascii=False, indent=4)

    print("Medarbejder slettet!")

if __name__ == '__main__':
    id = input("Indtast medarbejder ID for at slette medarbejder: ")
    delete_medarbejder(id)