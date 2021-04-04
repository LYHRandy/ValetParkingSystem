import sqlite3
import logging

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO, filename='parkingSys.log')


""" Gets connection to sqlite3 and create table if it doesn't initially exist

Parameters:


Returns:
conn (Connection): Returns Connection object, if there is an error returns None

"""
def get_conn():
    try:
        conn = sqlite3.connect('store.db')
        conn.execute('''
            create table if not exists ParkingInfo
            (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicleType CHAR(25) NOT NULL,
                vehicleNum CHAR(25) NOT NULL,
                startTime INTEGER NOT NULL,
                endTime INTEGER NOT NULL,
                carLot INTEGER NOT NULL,
                fee REAL NOT NULL
            )
        ''')
        return conn
    except Exception as e:
        logging.error(f'Error with connecting to sqlite db {str(e)}')
        return None


""" Stores vehicle that have exited info

Parameters:
conn (Connection): Connection object to execute SQL commands
vehicle (Vehicle): Vehicle object (Car/ Motorcycle)

Returns:
None

"""
def store_info(conn, vehicle):
    try:
        sql_query = ''' INSERT INTO ParkingInfo (vehicleType, vehicleNum, startTime, endTime, carLot, fee) VALUES (?, ?, ?, ?, ?, ?) '''
        conn.execute(sql_query, (vehicle.vehicle_type, vehicle.vehicle_plate, vehicle.start_time, vehicle.end_time, vehicle.car_lot, vehicle.fee))
        conn.commit()
    except Exception as e:
        logging.error(f'Error storing info: {str(e)}')
