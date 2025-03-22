

class User:
    def __init__(self, user_id, first_name, last_name, username, phone, email, hashed_password, role="customer", reservation_id=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone = phone
        self.email = email
        self.hashed_password = hashed_password
        self.role = role
        self.reservation_id = reservation_id

