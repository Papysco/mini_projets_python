from note import Note


class Carnet:
    list_of_notes = {}

    def __init__(self):
        pass

    def save(self):
        pass

    def add_note(self, note):
        self.list_of_notes[note.get_id()] = note

    def delete_note(self, id_note):
        try:
            self.list_of_notes.pop(id_note)
        except IndexError:
            print("Erreur d'ID potentiel ! ")

    def get_all_notes(self):
        for key, value in self.list_of_notes.items():
            print("ID : " + str(key))
            print("Title : " + value.get_title())
            print("Description : " + value.get_description())
            print("Date : " + str(value.get_creation_date()))
            print("\n")

    def update_titre(self, id_note, title):
        for key, value in self.list_of_notes.items():
            if key == id_note:
                value.set_title(title)

    def update_description(self, id_note, description):
        for key, value in self.list_of_notes.items():
            if key == id_note:
                value.set_description(description)
