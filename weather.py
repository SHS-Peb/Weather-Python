import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):#COMPLETED
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

#print(format_temperature(25))

def convert_date(iso_string): #COMPLETED
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    fancy_date = date.strftime("%A %d %B %Y")
    return f"{fancy_date}"

#print(convert_date("2021-07-06T07:00:00+00:00"))

def convert_f_to_c(temp_in_fahrenheit): #COMPLETED
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    faren_to_celsius = (float(temp_in_fahrenheit) - 32) * 5.0 / 9.0
    rounded_celsius = round(faren_to_celsius, 1)
    return rounded_celsius

#print(convert_f_to_c(100.0))

def calculate_mean(weather_data): #COMPLETED
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    int_weather = [float(item) for item in weather_data]
    sum_weather = sum(int_weather)
    mean_weather = sum_weather / len(weather_data) 
    return mean_weather

#print(calculate_mean([10, 20, 30]))

def load_data_from_csv(csv_file):#COMPLETED
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_list = []
    with open(csv_file) as file: #AS FILE IS USED TO GIVE A REFERENCE TO THE OPENED FILE
        reader = csv.reader(file)
        for row in reader:
            if not row: #skips empty rows
                continue
            if row[0] == "date": #skips header row
                continue
            date = row[0]
            minimum = int(row[1])
            maximum = int(row[2])
            csv_list.append([date, minimum, maximum])
    return csv_list

#print(load_data_from_csv("./tests/data/example_one.csv"))

def find_min(weather_data):#COMPLETED
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    min_value = min(weather_data)
    min_index = len(weather_data) - 1 - weather_data[::-1].index(min_value)
    min_value = float(min_value)
    return min_value, min_index

#print(find_min([10, 5, 3, 7, 3, 9]))

def find_max(weather_data):#COMPLETED
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    max_value = max(weather_data)
    max_index = len(weather_data) - 1 - weather_data[::-1].index(max_value)
    max_value = float(max_value)
    return max_value, max_index

#print(find_max([10, 5, 3, 7, 10, 9]))

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data: #fixes tuple issue from find_min and find_max
        return ""

    date = [item[0] for item in weather_data]
    low_temp = [item[1] for item in weather_data]
    high_temp = [item[2] for item in weather_data]

    if not low_temp or not high_temp: #fixes tuple issue from find_min and find_max
        return ""

    min_temp_f, min_index_f = find_min(low_temp)
    max_temp_f, max_index_f = find_max(high_temp)
    avg_low_f = calculate_mean(low_temp)
    avg_high_f = calculate_mean(high_temp)

    min_temp = format_temperature(convert_f_to_c(min_temp_f))
    max_temp = format_temperature(convert_f_to_c(max_temp_f))
    avg_low = format_temperature(convert_f_to_c(avg_low_f))
    avg_high = format_temperature(convert_f_to_c(avg_high_f))

    min_date = convert_date(date[min_index_f])
    max_date = convert_date(date[max_index_f])

    summary = (f"{len(weather_data)} Day Overview\n"
               f"  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n"
               f"  The highest temperature will be {max_temp}, and will occur on {max_date}.\n"
               f"  The average low this week is {avg_low}.\n"
               f"  The average high this week is {avg_high}.\n"
    )
    

    return summary

#print(generate_summary("./tests/data/example_one.csv"))

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information. Readable
    """
    #weather_data = load_data_from_csv(".example_one.csv")
    
    if not weather_data:
        return  ""

    daily_summary = []

    for date_raw, low, high in weather_data:

        date = convert_date(date_raw)
        min = convert_f_to_c(low)
        max = convert_f_to_c(high)

        daily_template = (f"---- {date} ----\n"
                     f"  Minimum Temperature: {format_temperature(min)}\n" 
                     f"  Maximum Temperature: {format_temperature(max)}\n")
    
        daily_summary.append(daily_template)
    return "\n".join(daily_summary) + "\n"

#print(generate_daily_summary("./tests/data/example_one.csv"))