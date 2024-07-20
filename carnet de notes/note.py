import datetime


class Note:
    compteur = 0

    def __init__(self, title, description):
        self.id = self.compteur + 1
        self.title = title
        self.description = description
        self.creation_date = datetime.date.today()
        Note.compteur += 1

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_creation_date(self):
        return self.creation_date

