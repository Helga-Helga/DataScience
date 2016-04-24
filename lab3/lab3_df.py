import csv

def clean_data():

    raw_data_path = './household_power_consumption.csv'
    clean_data_path = './household_power_consumption_clean.csv'

    with open(raw_data_path, 'rb') as old_file:
        reader = csv.reader(old_file, delimiter=';')

        with open(clean_data_path, 'wb') as new_file:
            f = csv.writer(new_file, delimiter=';')

            for line in reader:
                if '?' in line:
                    continue
                f.writerow(line)

clean_data()

import pandas as pd

def read_frame():
    path = './household_power_consumption_clean.csv'
    df = pd.read_csv(path, index_col=False, header=8, delimiter=';',
                     names=['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'])
    return df

def active_power():
    df = read_frame()
    print 'Households with Global_active_power more than 5 kW'
    df1 = df[df['Global_active_power'] > 5]
    print df1[:5]

active_power()
