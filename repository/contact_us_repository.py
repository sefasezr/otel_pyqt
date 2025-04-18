from database import Database

class ContactUsRepository:
    def __init__(self):
        self.db = Database()

    def insert_message(self, name, phone, subject, message):
        query = """
        INSERT INTO contact (name, phone, title, content, date)
        VALUES (%s, %s, %s, %s, CURRENT_DATE)  -- Tarih zaten veritabanında otomatik alınacak
        """
        try:
            self.db.execute_query(query, (name, phone, subject, message))
            return True
        except Exception as e:
            print(f"❌ Error in insert_message: {e}")
            return False