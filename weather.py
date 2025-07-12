import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    converted_date=datetime.fromisoformat(iso_string)
    formatted_date=converted_date.strftime("%A %d %B %Y") 
    return formatted_date

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    float_temp= float(temp_in_fahrenheit)
    convert_temp=(float_temp -32) * 5/9
    result= round(convert_temp, 1)
    return result

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # return sum(weather_data)/ len(weather_data) ###this doesnt work
    numeric_values =[]
    for item in weather_data:
        try:
            numeric_values.append(float(item))
        except ValueError:
            pass    
    if not numeric_values:
        return 0.0

    return sum(numeric_values) / len(numeric_values)    

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data=[]
    with open(csv_file, "r") as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            if row!=[]:
                date=row[0]
                try:
                    min_temp=float(row[1])
                    max_temp=float(row[2])
                    data.append([date, min_temp,max_temp])
                except ValueError:
                    continue

    return data

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    min_index=0
    min_value=float(weather_data[0])
    for index , value in enumerate(weather_data):
        if float(value)<=min_value:
            min_index=index
            min_value=float(value)
    return (min_value, min_index)          
   
def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    max_index=0
    max_value=float(weather_data[0])
    for index, value in enumerate(weather_data):
        if float(value)>=max_value:
            max_index=index
            max_value=float(value)
    return (max_value,max_index)        


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    general_summary=[]
    general_min_temp=[]
    general_max_temp=[]

    for index, value in enumerate(weather_data):
        ###collecting data
        general_min_temp.append(float(value[1]))
        general_max_temp.append(float(value[2]))

    #### finding min result
    min_result=find_min(general_min_temp)
    min_temp_value=min_result[0]
    min_temp_index=min_result[1]  
    min_temp_date_str=weather_data[min_temp_index][0] 
    min_temp_date=convert_date(min_temp_date_str)     
    #### finding max result
    max_result=find_max(general_max_temp)
    max_temp_value=max_result[0]
    max_temp_index=max_result[1]
    max_temp_date_str=weather_data[max_temp_index][0] 
    max_temp_date=convert_date(max_temp_date_str)
    ### calculate average for min
    average_min_f=sum(general_min_temp)/ len(general_min_temp)
    average_min_c=convert_f_to_c(average_min_f)
    average_min_formatted=format_temperature(average_min_c)

    ### calculate average for max
    average_max_f=sum(general_max_temp)/ len(general_max_temp)
    average_max_c=convert_f_to_c(average_max_f)
    average_max_formatted=format_temperature(average_max_c)

    ##average
    general_summary.append(f"{len(weather_data)} Day Overview")
    general_summary.append(f" The lowest temperature will be {format_temperature(convert_f_to_c(min_temp_value))} and it will occur on {min_temp_date}.")
    general_summary.append(f" The highest temperature will be {format_temperature(convert_f_to_c(max_temp_value))} and it will occur on {max_temp_date}. ")
    general_summary.append(f" The average low this week is {average_min_formatted}. ")
    general_summary.append(f" The average high this week is {average_max_formatted}. ")

    return "\n".join(general_summary)        




def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary=[]
    for value in weather_data:
        date_string=convert_date(value[0])
        min_f=float(value[1])
        min_to_c=convert_f_to_c(min_f)
        min_temp=format_temperature(min_to_c)
        max_f=float(value[2])
        max_to_c=convert_f_to_c(max_f)                                                                                                                                                                                                                                                                  
        max_temp=format_temperature(max_to_c)

        summary.append(f"---- {date_string} ----")
        summary.append(f"  Minimum Temperature: {min_temp}")
        summary.append(f"  Maximum Temperature: {max_temp}")
        summary.append("")
    return "\n".join(summary)

#######Created a branch folder to test. No change are made 