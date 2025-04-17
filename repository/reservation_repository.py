from database import Database

class ReservationRepository:
    def __init__(self):
        self.db = Database()

    def get_available_rooms_by_type(self, room_type):
        query = """
        SELECT room_id, room_type, status FROM rooms
        WHERE room_type = %s AND status = 'available'
        """
        return self.db.fetch_query(query, (room_type,))

    def get_room_price(self, room_id):
        query = "SELECT price FROM rooms WHERE room_id = %s"
        return self.db.fetch_query(query, (room_id,))

    def insert_reservation(self, user_id, room_id, checkin, checkout, price, status="active"):
        # SQL sorgusu ile rezervasyonu ekliyoruz. reservation_id otomatik olarak oluşturulacak.
        query = """
        INSERT INTO reservations (user_id, room_id, check_in_date, check_out_date, price, status)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING reservation_id;
        """
        try:
            # Veritabanına veri ekliyoruz ve eklenen satırdaki reservation_id'yi döndürüyoruz.
            self.db.cur.execute(query, (user_id, room_id, checkin, checkout, price, status))
            result = self.db.cur.fetchone()  # reservation_id'yi alıyoruz
            self.db.conn.commit()
            return result  # result[0] olarak reservation_id'yi döndüreceğiz
        except Exception as e:
            print("❌ insert_reservation error:", e)
            return None

    def update_room_status(self, room_id, status="booked"):
        query = "UPDATE rooms SET status = %s WHERE room_id = %s"
        self.db.execute_query(query, (status, room_id))