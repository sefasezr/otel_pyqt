import hashlib
from database import Database

class User:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password):
        """Şifreyi SHA-256 ile hashleme"""
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, username, password):
        """Kullanıcı girişi"""
        hashed_password = self.hash_password(password)
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        user = self.db.fetch_query(query, (username, hashed_password))
        return user if user else None

    def register(self, first_name, last_name, username, phone, email, password, role="customer"):
        """Kullanıcı kaydı"""
        hashed_password = self.hash_password(password)
        query = """
        INSERT INTO users (first_name, last_name, username, phone, email, password, role)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.db.execute_query(query, (first_name, last_name, username, phone, email, hashed_password, role))
            return True
        except Exception as e:
            print("Kayıt hatası:", e)
            return False
