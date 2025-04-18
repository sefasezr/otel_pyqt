from database import Database

class ReservationRepository:
    def __init__(self):
        self.db = Database()

    def get_available_rooms_by_type_and_date(self, room_type, checkin_date, checkout_date):
        """Odaların tarih aralıklarına göre müsaitliğini kontrol et"""
        query = """
        SELECT room_id, room_type, status FROM rooms
        WHERE room_type = %s
        AND room_id NOT IN (
            SELECT room_id FROM reservations
            WHERE (check_in_date <= %s AND check_out_date >= %s)
        )
        """
        return self.db.fetch_query(query, (room_type, checkout_date, checkin_date))

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

    def get_upcoming_reservations_by_user(self, user_id):
        query = """
        SELECT * FROM reservations
        WHERE user_id = %s AND check_in_date >= CURRENT_DATE
        """
        try:
            print("Sorgu çalıştırılıyor...")
            result = self.db.fetch_query(query, (user_id,))
            print("Sorgu sonucu: ", result)  # Burada gelen veriyi kontrol et
            return result
        except Exception as e:
            print("Veritabanı hatası:", e)
            return []
