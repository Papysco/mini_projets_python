import mysql.connector
from note import Note


class Dao:

    def __init__(self, host="localhost", user="root", password="p@ssword", database="carnet_notes"):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.mydb.cursor()

    def add_notes(self, note):
        try:
            sql = "INSERT INTO notes (id, titre, description, date_creation) VALUES (%s, %s, %s, %s)"
            values = (note.get_id(), note.get_title(), note.get_description(), note.get_creation_date())
            self.cursor.execute(sql, values)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(f"Erreur d'insertion ! {err}")

    def delete_notes(self, id_note):
        try:
            sql = "DELETE FROM notes WHERE id="+str(id_note)
            self.cursor.execute(sql)
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(f"Erreur d'insertion ! {err}")

    def get_all_notes(self):
        try:
            sql = "SELECT * FROM notes"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except mysql.connector.Error as err:
            print(f"Erreur d'insertion ! {err}")
