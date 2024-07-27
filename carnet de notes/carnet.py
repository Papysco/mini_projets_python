from note import Note
import database


class Carnet:

    def __init__(self):
        self.dao = database.Dao()

    def add_note(self, p_note):
        self.dao.add_notes(p_note)

    def delete_note(self, id_note):
        self.dao.delete_notes(id_note)

    def get_all_note(self):
        list_of_note = self.dao.get_all_notes()
        for x in list_of_note:
            print("Id :" + str(x[0]))
            print("Titre :" + str(x[1]))
            print("Description :" + str(x[2]))
            print("Date :" + str(x[3]))
            print("\n")

    def update_note(self, id_note, texte, option):
        if option == 1:
            self.dao.update_titres(id_note, texte)
        else:
            self.dao.update_descriptions(id_note, texte)

    def search_note(self, id_note):
        note = self.dao.search(id_note)
        print("Id :" + str(note[0]))
        print("Titre :" + str(note[1]))
        print("Description :" + str(note[2]))
        print("Date :" + str(note[3]))
        print("\n")

