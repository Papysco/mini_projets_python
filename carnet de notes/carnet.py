from note import Note
import database


class Carnet:
    list_of_notes = {}

    def __init__(self):
        self.dao = database.Dao()

    def save(self):
        pass

    def add_note(self, p_note):
        try:
            self.dao.add_notes(p_note)
            self.list_of_notes[p_note.get_id()] = p_note
        except Exception as e:
            print("Erreur d'insertion !", e)

    def delete_note(self, id_note):
        try:
            self.dao.delete_notes(id_note)
        except Exception as e:
            print("Erreur d'ID potentiel ! ", e)

    def get_all_note(self):
        list_of_note = self.dao.get_all_notes()
        for x in list_of_note:
            print("Id :" + str(x[0]))
            print("Titre :" + str(x[1]))
            print("Description :" + str(x[2]))
            print("Date :" + str(x[3]))
            print("\n")

    def update_titre(self, id_note, title):
        for key, value in self.list_of_notes.items():
            if key == id_note:
                value.set_title(title)

    def update_description(self, id_note, description):
        for key, value in self.list_of_notes.items():
            if key == id_note:
                value.set_description(description)
