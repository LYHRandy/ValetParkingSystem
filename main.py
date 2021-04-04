import sys
import logging
from valet import *
from db import get_conn

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO, filename='parkingSys.log')

# for loop to accept all arguments after main.py
for file in sys.argv[1:]:
    # Allows only csv or text files. If not, there will be an error
    if file.endswith('.csv'):
        read_file(file, ',', get_conn())
    elif file.endswith('.txt'):
        read_file(file, ' ', get_conn())
    else:
        logging.error("Invalid file type, please use only csv or txt files")