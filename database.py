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

    def create_tables(self):
        """Veritabanında tabloların oluşturulması"""
        user_table = """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            username VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(15) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role VARCHAR(50) DEFAULT 'customer'
        );
        """

        room_table = """
        CREATE TABLE IF NOT EXISTS rooms (
            room_id SERIAL PRIMARY KEY,
            room_type VARCHAR(50) NOT NULL,
            price NUMERIC(10, 2) NOT NULL,
            status VARCHAR(20) DEFAULT 'available'
        );
        """

        reservation_table = """
        CREATE TABLE IF NOT EXISTS reservations (
            reservation_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(user_id),
            room_id INTEGER NOT NULL REFERENCES rooms(room_id),
            check_in_date DATE NOT NULL,
            check_out_date DATE NOT NULL,
            status VARCHAR(20) DEFAULT 'active'
        );
        """

        # Tabloları oluşturma
        self.execute_query(user_table)
        self.execute_query(room_table)
        self.execute_query(reservation_table)
