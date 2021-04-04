import datetime

""" Calculate the amount needed to be paid for the vehicle

Parameters:
start_time (int): Epoch Time of when the vehicle entered the carpark
end_time (int): Epoch Time of when the vehicle exits the carpark
price_per_hour (float): Price per hour for vehicle

Returns:
(int): Returns fee charged to exiting vehicle

"""
def calculate_fee(start_time, end_time, price_per_hour):
    start_date_time = datetime.datetime.fromtimestamp(start_time)
    end_date_time = datetime.datetime.fromtimestamp(end_time)

    total_mins = ((end_date_time - start_date_time).total_seconds())/60

    return (int(total_mins/60)+1)*price_per_hour


""" Checks at which parking lot for vehicle type is available and returns the parking lot number

Parameters:
veh_list (list): List containing the parking lots(Taken/ Available) of specific vehicle type

Returns:
i (int): Parking lot index or None

"""
def check_empty_lot(veh_list):
    for i, value in enumerate(veh_list):
        if not value:
            return i


""" Checks if vehicle plates exists in vehicle (Invalid vehicle)

Parameters:
vehicle_plate (str): Vehicle plate number

Returns:
(bool): True if vehicle exists

"""
def check_if_vehicle_exists(car_list, motorcycle_list, vehicle_plate):
    for car in car_list:
        if vehicle_plate == car.vehicle_plate:
            return True
    for motorcycle in motorcycle_list:
        if vehicle_plate == motorcycle.vehicle_plate:
            return True

    return False