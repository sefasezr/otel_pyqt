from database import Database

class Reservation:
    def __init__(self):
        self.db = Database()

    def get_user_reservations(self, user_id):
        query = "SELECT * FROM reservations WHERE user_id = %s"
        return self.db.fetch_query(query, (user_id,))

    def cancel_reservation(self, reservation_id):
        query = "UPDATE reservations SET status = 'cancelled' WHERE reservation_id = %s"
        self.db.execute_query(query, (reservation_id,))
