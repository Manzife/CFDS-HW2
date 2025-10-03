###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #

def load_data(filename):
    import csv
    with open(filename, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    
    return data

def print_countries_information(data, thresholds):
    for threshold in thresholds:
        average_death_confirmed(countries_in_threshold(threshold, data))


def countries_in_threshold(threshold, data):
    countries = []
    for country in data:
        if int(country['Active']) > threshold:
            countries.append(country)
            print(country['Country'])
    return countries
            
def average_death_confirmed(countries):
    ratio = sum(int(row['Deaths']) / int(row['Confirmed']) for row in countries)/len(countries)
    print(f'Average Death/Confirmed is: {ratio}')

data = load_data('covid.csv')
print_countries_information(data,[500, 1000, 5000])