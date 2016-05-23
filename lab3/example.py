import pandas as pd
import urllib2
import matplotlib.pyplot as plt
from lab3_df import read_frame
import argparse

parser = argparse.ArgumentParser(description='Date')

parser.add_argument('-d', action='store', type=int, help='Day')
parser.add_argument('-m', action='store', type=int, help='Month')
parser.add_argument('-y', action='store', type=int, help='Year')
parser.add_argument('-hour', action='store', type=int, help='Hour')

inputs = parser.parse_args()
print inputs

in_day = inputs.d
in_month = inputs.m
in_year = inputs.y
in_hour = inputs.hour

path = './household_power_consumption_clean_small.csv'
df = pd.read_csv(path, index_col=False, header=8, delimiter=';',
                 names=['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 'Voltage',
                 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'])

df['day'] = pd.to_datetime(df['Date']).dt.day
df['month'] = pd.to_datetime(df['Date']).dt.month
df['year'] = pd.to_datetime(df['Date']).dt.year
df['hour'] = pd.to_datetime(df['Time']).dt.hour
df['minute'] = pd.to_datetime(df['Time']).dt.minute

df1 = df[(df['year'] == in_year) & (df['month'] == in_month) & (df['day'] == in_day) & (df['hour'] == in_hour)]

df1 = df1[['Voltage', 'Time', 'day', 'month', 'year', 'hour', 'minute']]

print df1

df1.plot(kind='scatter', x='minute', y='Voltage', title='Voltage for {day}:{month}:{year} in {hour} oclock'.format(day=in_day, month=in_month, year=in_year, hour=in_hour));
plt.show()
