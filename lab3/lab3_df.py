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
