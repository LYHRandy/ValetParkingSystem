from models import *
import logging
from helper import *
from db import store_info

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO, filename='parkingSys.log')

car_list = list()
CAR_PARKING_PRICING = 2
motorcycle_list = list()
MOTORCYCLE_PARKING_PRICING = 1

""" Converts string to integer if able to

Parameters:
value_to_convert (str): String Value to convert to integer

Returns:
(int): Returns int value, if there is an exception, returns -1

"""
def convert_str_to_int(value_to_convert):
    try:
        return int(value_to_convert)
    except Exception as e:
        logging.error(f'Error in conversion {str(e)}')
        return -1


""" Process vechiels that exits

Parameters:
values (list): List containing delimited value of each line in file
conn (Connection): Connection object to store exited vehicles into the database

Returns:
None

"""
def register_exit(values, conn):
    exit_time = convert_str_to_int(values[2])
    if exit_time == -1:
        return

    veh_plate = values[1]

    for i, car in enumerate(car_list):
        if car:
            car_plate = car.vehicle_plate
            if car_plate == veh_plate:
                car.end_time = exit_time
                fee = calculate_fee(car.start_time, car.end_time, CAR_PARKING_PRICING)
                car.fee = fee
                to_print = f'CarLot{str(i+1)} {str(fee)}'
                logging.info(to_print)
                print(to_print)
                store_info(conn, car)
                car_list[i] = None
                return
    
    for i, motorcycle in enumerate(motorcycle_list):
        if motorcycle:
            motorcycle_plate = motorcycle.vehicle_plate
            if motorcycle_plate == veh_plate:
                motorcycle.end_time = exit_time
                fee = calculate_fee(motorcycle.start_time, motorcycle.end_time, MOTORCYCLE_PARKING_PRICING)
                motorcycle.fee = fee
                to_print = f'MotorcycleLot{str(i+1)} {str(fee)}'
                logging.info(to_print)
                print(to_print)
                store_info(conn, motorcycle)
                motorcycle_list[i] = None
                return

    logging.error(f'Invalid Vehicle Exiting {veh_plate}')



""" Checks if the carkpark has available lots to allow vehicles to enter

Parameters:
vehicle_type (str): Vehicle type, car or motorcycle

Returns:
(bool): If there is a available parking slot or False if invalid vehicle type detected

"""
def check_if_carpark_full(vehicle_type):

    if vehicle_type == 'car':
        return None in car_list
    elif vehicle_type == 'motorcycle':
        return None in motorcycle_list
    else:
        logging.error(f'Invalid Vehicle Type - {vehicle_type}')
        return False


""" Process vechiels that enters

Parameters:
values (list): List containing delimited value of each line in file

Returns:
None

"""
def register_enter(values):
    enter_time = convert_str_to_int(values[3])
    if enter_time == -1:
        return

    vehicle_type = values[1]
    vehicle_plate = values[2]

    if check_if_carpark_full(vehicle_type):
        # Pass in Vehicle Type, Vehicle Plate, Entered Time
        if vehicle_type == 'car':
            lot = check_empty_lot(car_list)
            car = Vehicle(vehicle_type, vehicle_plate, enter_time, lot+1)
            car_list[lot] = car
            to_print = f'Accept CarLot {str(lot+1)}'
        else:
            lot = check_empty_lot(motorcycle_list)
            motorcycle = Vehicle(vehicle_type, vehicle_plate, enter_time, lot+1)
            motorcycle_list[lot] = motorcycle
            to_print = f'Accept MotorcycleLot {str(lot+1)}'
    else:
        to_print = f'Reject {vehicle_plate}'

    logging.info(to_print)
    print(to_print)


""" Reads each file that is being inputted in command line

Parameters:
file_name (str): Filename of file to be read and processed
to_split (str): Delimiter to split each line in the file by.
conn (Connection): DB Connection object for storing of data

Returns:
None

"""
def read_file(file_name, to_split, conn):

    with open(file_name, 'r') as file:
        global car_list
        global motorcycle_list

        for i, line in enumerate(file):
            values = line.strip('\n').split(to_split)
            # Get First line which sets how much lots for motorcycles and cars
            if i == 0:
                car_list = [None for i in range(int(values[0]))]
                motorcycle_list = [None for i in range(int(values[1]))]

            else:
                veh_action = values[0]
                if veh_action.lower() == 'enter':
                    register_enter(values)
                elif veh_action.lower() == 'exit':
                    register_exit(values, conn)
                else:
                    logging.error(f'Invalid line - {line}')


    conn.close()