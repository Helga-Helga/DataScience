import numpy as np

def read_frame():
    path = './household_power_consumption_clean.csv'
    my_data = np.genfromtxt(path, delimiter=';', dtype=None,
                     names=['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'])
    print my_data
    return my_data

read_frame()
