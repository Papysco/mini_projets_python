import datetime
from carnet import Carnet
from note import Note

# Creation d'un nouveau carnet
my_carnet = Carnet()

# print(type(datetime.date.today()))
while True:
    print("\n   MENU")
    print("1 : Ajouter une note ")
    print("2 : Supprimer une note ")
    print("3 : Modifier une note ")
    print("4 : Chercher une note ")
    print("5 : Lister les notes ")
    print("0 : Quitter l'application")
    res = int(input("Veuillez selectionner une option : "))

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
            note_id = input("Entrez l'id de la note : ")
            my_carnet.delete_note(note_id)

        case 3:
            note_id = int(input("Entrez l'id de la note : "))
            while True:
                detail = int(input("Tapez 1 pour le titre ou 2 pour la description : "))
                if detail != 1 and detail != 2:
                    print("Veuillez saisir un nombre valide !")
                else:
                    texte = input("Entrez saisir la modification : ")
                    break

            my_carnet.update_note(note_id, texte, detail)

        case 4:
            id_note = input("Entrez l'id de la note : ")
            my_carnet.search_note(id_note)
        case 5:
            print("\nLa liste des notes : ")
            my_carnet.get_all_note()
        case _:
            print("Veuillez entrer une option valide :")
