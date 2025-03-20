import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="otel_db",
            user="db_user",
            password="db_password",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()

    def execute_query(self, query, params=None):
        """SQL sorgusu çalıştırma"""
        try:
            self.cur.execute(query, params or ())
            self.conn.commit()
        except Exception as e:
            print("Database error:", e)

    def fetch_query(self, query, params=None):
        """SQL sorgusu çalıştır ve sonucu döndür"""
        self.cur.execute(query, params or ())
        return self.cur.fetchall()

    def close_connection(self):
        """Bağlantıyı kapat"""
        self.cur.close()
        self.conn.close()
