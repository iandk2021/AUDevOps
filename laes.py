import json

def read_all_medarbejdere():
    with open("medarbejdere.json", "r", encoding="utf-8") as fil:
        medarbejdere = json.load(fil)

    print("Medarbejdere:")
    print_medarbejdere = []
    for medarbejder in medarbejdere:
        print_medarbejdere.append(f"ID: {medarbejder['medarbejder_id']}, Navn: {medarbejder['navn']}, Afdeling: {medarbejder['afdeling']}, Email: {medarbejder['email']}")
    return print_medarbejdere

if __name__ == '__main__':
    print(read_all_medarbejdere())