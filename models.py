class Vehicle:
    """ 
    A class to represent a vehicle

    Attributes
    ----------
    vehicle_type : str
        vehicle type whether car or motorcycle
    vehicle_plate : str
        vehicle number plate
    start_time : int
        Entry time of the vehicle
    end_time : int
        Exit time of the vehicle
    car_lot : int
        Car lot number that the car is parked at
    fee: float
        Fee paid by the vehicle    
    """

    def __init__(self, vehicle_type, vehicle_plate, start_time, car_lot):
        """
        Constructs all the necessary attributes for the vehicle object.

        Parameters
        ----------
            vehicle_type : str
                vehicle type whether car or motorcycle
            vehicle_plate : str
                vehicle number plate
            start_time : int
                Entry time of the vehicle
            car_lot : int
                Car lot number that the car is parked at
        """
        self.vehicle_type = vehicle_type
        self.vehicle_plate = vehicle_plate
        self.start_time = start_time
        self.end_time = None
        self.car_lot = car_lot
        self.fee = 0

