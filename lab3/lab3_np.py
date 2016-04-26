import numpy as np
import pandas as pd
import random

def read_array():
    path = './household_power_consumption_clean.csv'
    df = pd.read_csv(path, index_col=False, header=8, delimiter=';',
                     names=['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'])
    my_data = df.values
    return my_data

def active_power():
    array = read_array()
    print 'Households with Global_active_power more than 5 kW'
    array = array[array[:,2] > 5]
    np.set_printoptions(edgeitems=9)
    print array

active_power()

def voltage():
    array = read_array()
    print 'Households with Voltage more than 235 V'
    array = array[array[:,4] > 235]
    np.set_printoptions(edgeitems=9)
    print array

voltage()

def intensity():
    array = read_array()
    print 'Households with Global_intensity in range from 19 to 20 A and where washer and fridge comsump more than boiler and the conditioner'
    array = array[(array[:,5] > 19) & (array[:,5] < 20) & (array[:,7] > array[:,8])]
    np.set_printoptions(edgeitems=9)
    print array
intensity()

def unique(a):
    order = np.lexsort(a.T)
    a = a[order]
    diff = np.diff(a, axis=0)
    ui = np.ones(len(a), 'bool')
    ui[1:] = (diff != 0).any(axis=1)
    return a[ui]

def average_consumption():
    array = read_array()
    print '500000 random households with average consumption found'
    array = array[np.random.randint(array.shape[0],size=50000), :]
    average = np.array((array[:,6] + array[:,7]  + array[:,8])/3)
    average = average.reshape((50000,1))
    array = np.concatenate((array, average), axis=1)
    np.set_printoptions(edgeitems=9)
    print array

average_consumption()
