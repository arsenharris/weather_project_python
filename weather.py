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
    #this function assumes the input is a valid ISO date string
    #e.g. "2021-07-06T07:00:00+08:00"
    #and converts it to a human-readable format
    converted_date = datetime.fromisoformat(iso_string)
    # A stands for the full weekday name, d for day of the month, B for full month name, Y for year with century
    # %A %d %B %Y will format it as "Tuesday 06 July 2021"
    # Note: The input string should be in the format "YYYY-MM-DDTHH:MM:SS+TZ"
    # where T is the time separator and +TZ
    return converted_date.strftime("%A %d %B %Y") 

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    # Convert the input to float in case it's a string
    float_temp = float(temp_in_fahrenheit)
    # Convert Fahrenheit to Celsius using the formula: C = (F - 32) * 5 / 9
    celsius_temp = (float_temp - 32) * 5 / 9
    # Round the result to 1 decimal place
    return round(celsius_temp, 1) 

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # start with empty list to store numeric values
    numeric_values =[]
    # iterate through the weather_data list , this is done by for loops
    for item in weather_data:
        # try block attempts to convert each item to a float
        try:
            numeric_values.append(float(item))
        # If the conversion fails (e.g., item is "N/A" or "abc"), Python raises a ValueError.    # 
        # except ValueError: pass tells Python to ignore that error and continue with the next item.
        except ValueError:
           pass 
    # if numeric_values is empty, return 0.0 to avoid division by zero
    # otherwise, return the mean value which is the sum of my appended list divided by length of the appended list.  
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
    # This function need to load data from csv. To store my data I start with empty list.
    data=[]

    #With open is default method and csv_file is the argument in my function and it is as a file. 
    with open(csv_file, "r") as file:
        # if I get value error ,it ignores and continue and I return to this stored list which is data. 
        reader=csv.reader(file)
        next(reader) # Skip the header row
        #To read each row in my reader I use for loop
        for row in reader:
            # If row is empty date is the 0th index of the row. 
            if row!=[]:
                date=row[0]
                try:
                    #And it converts the index 1 to to float and stores in min_temp, and index 2 to is converted float and stored max temp.     # 
                    min_temp=float(row[1])
                    max_temp=float(row[2])
                    # I add each date to each other and min temp and max temp together. it is like apple by apple, orange by orange. 
                    data.append([date, min_temp, max_temp])
                    # if I get value error ,it ignores and continue and I return to this stored list which is data.     
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
    for index, value in enumerate(weather_data):
        if float(value)<=min_value:
            min_index=index
            min_value=float(value)
    return (min_value,min_index)        
   
def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # if my weather data doesnt store value, it will return to empty. 
    if not weather_data:
        return()
    #To find it I need to have index and my value. I start with zeroth index and I convert zeroth value in weather data and store it in min value. 
    max_index=0
    max_value=float(weather_data[0])
    #Now I need to do this for each item in my weather data. 
    #I still need index and value and I use enumerate to get the index number of the each value.
    for index, value in enumerate(weather_data):
        # I convert my value to float and check if it is less than or equal to my min value which I get it from weather data and convert it to float.
        if float(value)>=max_value:
            #If this is true, it get the index if this and store it in the min index. and stores my value in min value until all list is gone thought the loop
            max_index=index
            max_value=float(value)
    # I return to my min value and min index.         # 
    return (max_value,max_index)   
       
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # for general summary, I need to store my summary, min and max temp and I assign them into a empty list. 
    general_summary=[]
    general_min_temp=[]
    general_max_temp=[]
    # for each item and index in the weather data  by their index number are added together. and converted to float. what I mean is index 1 is added together and index 2 are adde together. 
    for index, value in enumerate(weather_data):
        ###collecting data
        general_min_temp.append(float(value[1]))
        general_max_temp.append(float(value[2]))

    #### finding min result
    # we look at the values in the above stored indexed by using function
    # min temp value gets the 0th value and stored it 
    min_temp_value=find_min(general_min_temp)[0]
    # min temp index get the first index and stores it 
    min_temp_index=find_min(general_min_temp)[1]  
    min_temp_date=convert_date(weather_data[min_temp_index][0] )     
    #### finding max result
    # same for the max temp value and index
    max_temp_value=find_max(general_max_temp)[0]
    max_temp_index=find_max(general_max_temp)[1]
    max_temp_date=convert_date(weather_data[max_temp_index][0] )


    ### calculate average for min
    # I need to convert the sum of the general min temp to float and divide it by the length of the general min temp list.
    # I also need to convert this to celsius and format it by using my pre defined
    average_min_formatted=format_temperature(convert_f_to_c(sum(general_min_temp)/ len(general_min_temp)))

    ### calculate average for max
    # I need to convert the sum of the general max temp to float and divide it by the length of the general max temp list.
    # I also need to convert this to celsius and format it by using my pre defined
    average_max_formatted=format_temperature(convert_f_to_c(sum(general_max_temp)/ len(general_max_temp)))

    ##summary
    # I need to add all the information together in the general summary list.
    # I need to use f string to format my string and add the information together.
    general_summary.append(f"{len(weather_data)} Day Overview\n")
    general_summary.append(f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp_value))}, and will occur on {min_temp_date}.\n")
    general_summary.append(f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp_value))}, and will occur on {max_temp_date}.\n")
    general_summary.append(f"  The average low this week is {average_min_formatted}.\n")
    general_summary.append(f"  The average high this week is {average_max_formatted}.\n")
    return "".join(general_summary)        

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #I need to store it in the daily_summary variable and sign it as aj empty list. 
    daily_summary=[]
    # I need to run each index of the weather data by using for loop. 
    for i, value in enumerate(weather_data):
        # I start with converting 0th index to a date by using my function which I described earlier.
        date_string = convert_date(value[0])
        # my first index is the min value which I convert to float and store it in min_f. 
        # this is in fahrenheit  and I convert this to celsius by using my pre defined function. 
        min_f = float(value[1])
        # finally I format this Celsius by using the other function called format temp. 
        min_temp = format_temperature(convert_f_to_c(min_f))
        # I do the same for max which is the second index. 
        #  I convert it to float and some in max_f variable .
        max_f = float(value[2])
        # I convert this to celsius by using my previous function. then I format this by using another function. 
        max_temp = format_temperature(convert_f_to_c(max_f))
        # I convert this to celsius by using my previous function. then I format this by using another function. 
        daily_summary.append(f"---- {date_string} ----")
        daily_summary.append(f"  Minimum Temperature: {min_temp}")
        daily_summary.append(f"  Maximum Temperature: {max_temp}")
        # This condition ensures:A blank line is added between each day’s summary
        if i != len(weather_data) -1:
            daily_summary.append("")

    # daily_summary is a list of strings.
    daily_summary.append("")
    daily_summary.append("")
    #"\n".join(...) joins all those strings into one big string with newlines between them.        
    return "\n".join(daily_summary)  # Join the list into a single string       

weather_data = [ 
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62]
            ]
print(generate_daily_summary(weather_data))