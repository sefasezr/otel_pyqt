from repository.contact_us_repository import ContactUsRepository

class ContactUsService:
    def __init__(self):
        self.repository = ContactUsRepository()

    def send_message(self, name, phone, subject, message):
        """Mesajı veritabanına kaydet"""
        result = self.repository.insert_message(name, phone, subject, message)
        if not result:
            return "Mesaj gönderilemedi!"
        return "Mesajınız başarıyla gönderildi."