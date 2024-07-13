class Contact:

    def __init__(self, nom, prenom, num, email):
        self.nom = nom
        self.prenom = prenom
        self.num = num
        self.email = email

    def modifier(self):
        pass

    def get_number(self):
        return self.num

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_email(self):
        return self.email

    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_email(self, email):
        self.email = email

    def afficher(self):
        print("Nom      : " + self.nom)
        print("Prenom   : " + self.prenom)
        print("Numero   : " + self.num)
        print("Email    : " + self.email)
        print("\n")
