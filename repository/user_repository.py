from database import Database

class UserRepository:
    def __init__(self):
        self.db = Database()

    def add_user(self, first_name, last_name, username, phone, email, hashed_password, role="customer"):
        query = """
        INSERT INTO users (first_name, last_name, username, phone, email, password, role)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        return self.db.execute_query(query, (first_name, last_name, username, phone, email, hashed_password, role))

    def get_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = %s"
        result = self.db.fetch_query(query, (username,))
        return result[0] if result else None

    def get_user_by_email(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        result = self.db.fetch_query(query, (email,))
        return result[0] if result else None

    def get_user_by_phone(self, phone):
        query = "SELECT * FROM users WHERE phone = %s"
        result = self.db.fetch_query(query, (phone,))
        return result[0] if result else None
