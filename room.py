from database import Database


class Room:
    def __init__(self):
        self.db = Database()

    def get_available_rooms(self):
        query = "SELECT room_id, room_type, price FROM rooms WHERE status = 'available'"
        return self.db.fetch_query(query)

    def book_room(self, user_id, room_id, check_in, check_out, total_price):
        query = """INSERT INTO reservations (user_id, room_id, check_in, check_out, total_price, status) 
                   VALUES (%s, %s, %s, %s, %s, 'confirmed')"""
        self.db.execute_query(query, (user_id, room_id, check_in, check_out, total_price))

        # Oda durumunu güncelle
        update_query = "UPDATE rooms SET status='booked' WHERE room_id=%s"
        self.db.execute_query(update_query, (room_id,))
