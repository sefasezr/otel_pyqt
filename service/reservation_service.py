import uuid

from PyQt5.QtCore import QDate

from repository.user_repository import UserRepository
from reservation import Reservation
from repository.reservation_repository import ReservationRepository

class ReservationService:
    def __init__(self):
        self.reservation_repository = ReservationRepository()
        self.user_repository = UserRepository()


    def fetch_available_rooms(self, room_type, checkin_date, checkout_date):
        """Tarih aralığına göre müsait odaları getir"""
        return self.reservation_repository.get_available_rooms_by_type_and_date(room_type, checkin_date, checkout_date)

    def make_reservation(self, user, room_id, checkin_date, checkout_date, people_count):
        # Eğer user nesnesi tuple şeklindeyse, onu User nesnesine dönüştür
        if isinstance(user, tuple):  # User nesnesi tuple ise
            user = self.user_repository.get_user_by_id(user[0])  # User'ı veritabanından al

        if not user:
            return None, "Kullanıcı bulunamadı."

        # Oda fiyatını al
        result = self.reservation_repository.get_room_price(room_id)
        if not result:
            return None, "Oda fiyatı alınamadı"

        room_price = float(result[0][0])

        # Tarihler arasındaki farkı hesapla (gün sayısı)
        checkin_date_obj = QDate.fromString(checkin_date, "yyyy-MM-dd")
        checkout_date_obj = QDate.fromString(checkout_date, "yyyy-MM-dd")

        # Geçersiz tarih aralığı kontrolü
        if checkin_date_obj >= checkout_date_obj:
            return None, "Geçersiz tarih aralığı"

        duration = checkin_date_obj.daysTo(checkout_date_obj)

        # Toplam fiyatı hesapla
        total_price = room_price * people_count * duration

        # Rezervasyonu ekle
        insert_result = self.reservation_repository.insert_reservation(user.user_id, room_id, checkin_date,
                                                                       checkout_date, total_price)

        if not insert_result:
            return None, "Rezervasyon oluşturulamadı"

        self.reservation_repository.update_room_status(room_id)

        reservation_id = insert_result[0]

        # Reservation nesnesini oluştururken, reservation_id'yi burada kullanıyoruz
        reservation = Reservation(
            reservation_id=reservation_id,  # Artık reservation_id'yi burada kullanıyoruz
            user_id=user.user_id,
            room_id=room_id,
            check_in_date=checkin_date,
            check_out_date=checkout_date,
            price=total_price,
            status="active"
        )
        user.reservations.append(reservation)
        return reservation, None

    def get_upcoming_reservations(self, user_id):
        try:
            # Doğru repo fonksiyonu çağırıldığından emin olalım
            reservations = self.reservation_repository.get_upcoming_reservations_by_user(user_id)
            print("Yapılacak rezervasyonlar:", reservations)
            return reservations
        except Exception as e:
            print("Hata alındı: ", e)
            return []