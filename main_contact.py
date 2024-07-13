from Annuaire import Annuaire
from Contact import Contact

# Creation d'un nouveau annuaire
mon_annuaire = Annuaire()
while True:
    print("\nMENU")
    print("1 : Ajouter un contact ")
    print("2 : Supprimer un contact ")
    print("3 : Modifier un contact ")
    print("4 : Chercher un contact ")
    print("5 : Lister les contacts ")
    print("0 : Quitter l'application")
    res = int(input("Veuillez selectionner une option :"))

    match res:
        case 0:
            print("Merci d'avoir notre application !")
            break
        case 1:
            nom = input("Entrer le nom du contact : ")
            prenom = input("Entrez le prenom du contact : ")
            numero = input("Entrer le numero du contact : ")
            email = input("Entrer l'Email du contact : ")

            new_contact = Contact(nom, prenom, numero, email)
            mon_annuaire.add_contact(new_contact)

        case 2:
            numero = input("Entrez le numero : ")
            contact = mon_annuaire.delete_contact(numero)
            print("Numero supprimé  : " + contact.get_number())

        case 3:
            print("1: Nom ")
            print("2: prenom ")
            print("3: Numero ")
            print("4: Email ")
            numero = (input("Veuillez entrer le numero   : "))
            nbr = int(input("Veuillez choisir l'attribut : "))

            match nbr:
                case 1:
                    nom = input("Entrez le nouveau nom : ")
                    mon_annuaire.modifier_nom(numero, nom)
                case 2:
                    prenom = input("Entrez le nouveau prenom : ")
                    mon_annuaire.modifier_prenom(numero, prenom)
                case 3:
                    email = input("Entrez le nouveau email : ")
                    mon_annuaire.modifier_email(numero, email)
                case _:
                    print("Veuillez entrer une option valide !")
        case 4:
            prenom_nom = input("Entrez le prenom ou nom : ")
            response = mon_annuaire.get_contact_by_prenom(prenom_nom)
            if response is not None:
                response.afficher()
            else:
                print("Desolé Aucune Correspondance ! ")
        case 5:
            mon_annuaire.get_all_contact()
        case _:
            print("Veuillez entrer une option valide :")

