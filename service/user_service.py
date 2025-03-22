import hashlib
from repository.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def hash_password(self, password):
        """Şifreyi SHA-256 ile hashle"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, first_name, last_name, username, phone, email, password):
        """Kayıt işlemini gerçekleştir"""
        if not all([first_name, last_name, username, phone, email, password]):
            return False, "Tüm alanlar doldurulmalıdır."

        if self.repo.get_user_by_username(username):
            return False, "Bu kullanıcı adı zaten kullanılıyor."
        if self.repo.get_user_by_email(email):
            return False, "Bu e-posta adresi zaten kayıtlı."
        if self.repo.get_user_by_phone(phone):
            return False, "Bu telefon numarası zaten kullanılıyor."

        hashed = self.hash_password(password)
        self.repo.add_user(first_name, last_name, username, phone, email, hashed)
        return True, "Kayıt başarılı."

    def login_user(self, username, password):
        """Giriş işlemini gerçekleştir"""
        user = self.repo.get_user_by_username(username)
        if not user:
            return False, "Kullanıcı bulunamadı."

        hashed_input = self.hash_password(password)
        if user[6] != hashed_input:  # 6. sütun şifre
            return False, "Şifre yanlış."

        return True, user  # Başarılı girişte kullanıcı verisi döndürülür
