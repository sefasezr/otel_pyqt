from database import Database

class RoomRepository:
    def __init__(self):
        self.db = Database()

    def get_room_type_by_id(self, room_id):
        """
        Verilen room_id için rooms tablosundan room_type değerini döner.
        Eğer bulunamazsa None döner.
        """
        query = """
        SELECT room_type
        FROM rooms
        WHERE room_id = %s
        """
        try:
            result = self.db.fetch_query(query, (room_id,))
            if result:
                return result[0][0]
            return None
        except Exception as e:
            print(f"❌ get_room_type_by_id error: {e}")
            return None