
import sqlite3

def create_table():
	conn = sqlite3.connect('api_data_database.db')

	conn.execute("CREATE TABLE IF NOT EXISTS api_data ( TEXT NOT NULL)")

	conn.commit()
	
	conn.close()

def insert(data):
	conn = sqlite3.connect('api_data_database.db')
	conn.execute("INSERT INTO api_data VALUES(?)",(data,))	
	conn.commit()
	conn.close()

