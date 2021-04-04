# Setup

Please install python3 into your fresh ubuntu system if it is not already installed. 
Here are steps to install it:
1. `sudo apt update`
2. `sudo apt install software-properties-common`
3. `sudo add-apt-repository ppa:deadsnakes/ppa`
4. `sudo apt install python3.9`

No other packages are required to be installed, all imports used are installed by default with python

## File Infrastructure

1. db.py - contains database related queries and connection to sqlite3 database
* This is used to store the vehicles that have parked and exited in this automated valet car parking backend system. This is to simulate potential storing for future analytics and getting the total some earned should we have to taken into account more files to be loaded and have a culumulated over profit from this system
2. helper.py - contains helper functions
3. main.py - the main python script file to use to test out this backend prototype 
4. models.py - contains only the Vehicle Class so far 
* This is where more classes can be created and can be easily converted into MVC if a backend web framework is used
5. valet.py - contains the main logic for this entire Automated Valet Car Parking Backend System

## Additional non python based files & directories

1. car_entries - here should contain all possible csv or txt files that contains data for this Automated Valet Car Parking Backend System
2. store.db - SQLite3 DB for storing of data for potential future use
3. parkingSys.log - Created after running the programme for the first time

## Testing

car_entries contains mock test dataset that was used to test this backend system

# Getting Started

How to run:
1. `cd "./Automated Valet Car Parking"`
2. `python3 main.py car_entries/test_file.csv`

* Note that you can include more files in your command. Remember to deliminate using space
* Add all additional test files into the car_entries directory

# Assumptions

There will not be duplicate cars or motorcycles.