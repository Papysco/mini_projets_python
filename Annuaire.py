class Annuaire:
    list_contact = []

    def __init__(self):
        pass

    def add_contact(self, contact):
        self.list_contact.append(contact)

    def delete_contact(self, numero):
        for contact in self.list_contact:
            if contact.get_number() == numero:
                tmp = contact
                self.list_contact.remove(contact)
                return contact

    def modifier_nom(self, num, nom):
        trouve = False
        for contact in self.list_contact:
            if contact.get_number() == num:
                contact.set_nom(nom)
                trouve = True

        if trouve is False:
            return print("Contact non trouvé !")

    def modifier_prenom(self, num, prenom):
        trouve = False
        for contact in self.list_contact:
            if contact.get_number() == num:
                contact.set_prenom(prenom)
                trouve = True

        if trouve is False:
            return print("Contact non trouvé !")

    def modifier_email(self, num, email):
        trouve = False
        for contact in self.list_contact:
            if contact.get_number() == num:
                contact.set_email(email)
                trouve = True

        if trouve is False:
            return print("Contact non trouvé !")

    def get_all_contact(self):
        print("Liste Contact :")
        if len(self.list_contact) == 0:
            return print("Oups ! Liste vide ")

        for contact in self.list_contact:
            contact.afficher()

    def get_contact_by_prenom(self, name):
        for contact in self.list_contact:
            if str(contact.get_prenom()).find(name) >= 0 or str(contact.get_nom()).find(name) >= 0:
                return contact
        return None


