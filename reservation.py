class Reservation:
    def __init__(self, reservation_id, user_id, room_id, check_in_date, check_out_date, price, status="active"):
        self.reservation_id = reservation_id
        self.user_id = user_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.price = price  # 💰 yeni alan
        self.status = status
