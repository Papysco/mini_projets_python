import datetime
from carnet import Carnet
from note import Note

# Creation d'un nouveau carnet
my_carnet = Carnet()

# print(type(datetime.date.today()))
while True:
    print("\nMENU")
    print("1 : Ajouter une note ")
    print("2 : Supprimer une note ")
    print("3 : Modifier une note ")
    print("4 : Chercher une note ")
    print("5 : Lister les notes ")
    print("0 : Quitter l'application")
    res = int(input("Veuillez selectionner une option :"))

    match res:
        case 0:
            print("Merci d'avoir notre application !")
            break
        case 1:
            title = input("\nEntrez le titre : ")
            description = input("Entrez la description : ")
            note = Note(title, description)
            my_carnet.add_note(note)

        case 2:
            note_id = input("Entrez le titre de la note : ")
            my_carnet.delete_note(note_id)

        case 3:
            pass
        case 4:
            pass
        case 5:
            print("La liste des notes : ")
            my_carnet.get_all_notes()
        case _:
            print("Veuillez entrer une option valide :")
