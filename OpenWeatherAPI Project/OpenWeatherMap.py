# Author David Culhane
# 2/23/24

import requests
import json
import string


# Functions to call Geocoding API for latitude/longitude
# Details for API found at https://openweathermap.org/api/geocoding-api; Used for zip_location, city_location functions
def zip_location(zip_code):  # For location by entering zip code
    api_key = '************************'  # Personal API key for OpenWeather
    country_code = 'US'  # ISO-3166 country code for the United States
    url = "http://api.openweathermap.org/geo/1.0/zip?zip={},{}&appid={}".format(
        zip_code, country_code, api_key)
    # Constructs the url for the API query based on input zip code
    try:
        response = requests.request("GET", url)  # Gets the lat/long data from OpenWeather
    except requests.exceptions.InvalidURL as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.HTTPError as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.Timeout as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.ConnectionError as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    else:
        response_code = response.status_code
        print('HTTP request madefor latitude and longitude coordinates! HTTP response code received: {}'.format(
            response_code))
        zip_location_data = json.loads(response.text)  # Loads retrieved data into a dictionary
        latitude = zip_location_data["lat"]  # Setting the latitude variable for return
        longitude = zip_location_data["lon"]  # Setting the longitude variable for return
        return latitude, longitude


def city_location(city, state):  # For location by entering city and state
    api_key = '************************'  # Personal API key for OpenWeather
    country_code = 'US'  # ISO-3166 country code for the United States
    url = 'http://api.openweathermap.org/geo/1.0/direct?q={},{},{}&limit=1&appid={}'.format(
        city, state, country_code, api_key)
    # Constructs the url for the API query based on input city and state in the US
    try:
        response = requests.request("GET", url)  # Gets the lat/long data from OpenWeather
    except requests.exceptions.InvalidURL as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.HTTPError as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.Timeout as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.ConnectionError as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    else:
        response_code = response.status_code
        print('HTTP request made for latitude and longitude coordinates! HTTP response code received: {}'.format(
            response_code))
        city_location_data_list = json.loads(response.text)
        # Loads retrieved data; Comes as list with a dictionary inside
        city_location_data = city_location_data_list[0]
        # Extracts the dictionary with the data from within the given list
        latitude = city_location_data["lat"]  # Sets latitude variable for return
        longitude = city_location_data["lon"]  # Sets longitude variable for return
        return latitude, longitude


# The name and state of the location requested is also required to display, so we will need to use a reverse lookup
# using lat/lon information. This will save time with wrestling with upper vs lower case, so we'll use the information
# from OpenWeather
def reverse_lookup(latitude, longitude):
    api_key = '************************'  # Personal API key for OpenWeather
    url = 'http://api.openweathermap.org/geo/1.0/reverse?lat={}&lon={}&appid={}'.format(
        latitude, longitude, api_key)
    try:
        response = requests.request("GET", url)
    except requests.exceptions.InvalidURL as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.HTTPError as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.Timeout as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.ConnectionError as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    else:
        reverse_lookup_list = json.loads(response.text)
        # OpenWeather returns a list when the reverse lookup API is called
        location_city = reverse_lookup_list[0]['name']
        # Indexes the list for the first entry in the list, a dictionary to set the city name
        location_state = reverse_lookup_list[0]['state']
        # Indexes the list for the first entry in the list, a dictionary to set the state name
        return location_city, location_state


# Function to call OpenWeather Map API for current weather.
# Details for API found at https://openweathermap.org/current#data
def current_weather(latitude, longitude, unit):
    api_key = '************************'
    # Conditional block to determine if/what the unit_suffix for the API call should be.
    if unit == 'kelvin':
        unit_suffix = ''  # Blank suffix since Kelvin is the API default and has no suffix
    elif unit == 'celsius':
        unit_suffix = '&units=metric'  # Metric suffix for Celsius unit
    elif unit == 'fahrenheit':
        unit_suffix = '&units=imperial'  # Imperial suffix for Fahrenheit unit
    else:
        print('Invalid Unit Entered. Please use Kelvin, Fahrenheit, or Celsius for the temperature unit')
        return
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}{}'.format(
        latitude, longitude, api_key, unit_suffix)  # url for API call
    try:
        response = requests.request("GET", url)  # OpenWeather API call
    except requests.exceptions.InvalidURL as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.HTTPError as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.Timeout as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    except requests.exceptions.ConnectionError as error:
        print('An error occurred with making the connection to OpenWeather')
        print('The following exception occurred: ', error)
        return
    else:
        response_code = response.status_code
        print('HTTP request made for weather data! HTTP response code received: {}'.format(
            response_code))
        weather_data = json.loads(response.text)  # Loads JSON response into a dictionary
        return weather_data


# Text normalizing function
def text_cleaner(text):
    text = text.rstrip()  # Removes possible extra spaces from user input
    text = text.lower()  # Makes user input lowercase
    text = text.translate(text.maketrans('', '', string.punctuation))  # Removes any punctuation from user input
    return text


def main():
    # Greeting for the user at program start.
    print('Thank You for using OpenWeatherMap!')

    loop_state = 0  # Initializing the loop_state variable for the program loop

    while loop_state != 'no':  # Establishes loop for user to check the weather information
        loop_state = input('Would you like to check the current weather information for a specific place/area in the '
                           'United States? Enter yes or no\n')
        loop_state = text_cleaner(loop_state)  # Runs the text cleaning function for user input of loop_state

        # Conditional block for the loop to continue running, stop running, and validate input
        if loop_state == 'yes':
            choice = input('Would you like to use a zip code or city and state for the location? Enter zip for using '
                           'a zip code or city for using city and state\n')
            choice = text_cleaner(choice)  # Runs text_cleaner to normalize user input for conditional block

            # Using another conditional block to check the text of this user input for zip, city, or invalid input
            # Initial part of if block for user choosing to use zip codes to get lat/long data
            if choice == 'zip':
                zip_code = input('Please enter the five digit zip code you would like weather information for.\n')
                # Try block to run the zip_location function in order to get lat/long data based on zip code
                try:
                    zip_check = int(zip_code)  # Checks if user input is a number using a dummy variable
                except ValueError:
                    print('Invalid Input - zip code entered is not a number\n', 'Restarting')
                    continue  # Abandons current loop iteration
                else:
                    pass  # If entered zip code is a number
                if len(zip_code) != 5:  # Checks if zip code entered has five numbers
                    print('Invalid Input - zip code entered does not have five characters\n', 'Restarting')
                    continue  # Abandons current loop iteration
                else:  # If entered zip code does have five numbers
                    try:  # Attempts to get latitude and longitude information of given zip code
                        latitude, longitude = zip_location(zip_code)
                    except KeyError:
                        print('Zip code entered does not exist and created an invalid URL.\n', 'Restarting')
                        # When an invalid zip code is sent to OpenWeather, a dictionary with the key-value pair
                        # "cod" : "404" is given, indicating a 404 error. In this situation when the zip_location
                        # function attempts to set the latitude, there is no "latitude" key, producing a KeyError.
                        continue  # Abandons current loop iteration
                    else:  # If entered zip code exists
                        print('Valid zip code entered. Location data retrieved.')

            # elif block for users choosing to use city/state to get lat/long data
            elif choice == 'city':
                city = input('Please enter the name of the city.\n')
                state = input('Please enter the two character state code.\n')
                # Running text_cleaner on city and state for the url
                city = text_cleaner(city)
                state = text_cleaner(state)
                # Try block to run the city_location function in order to get lat/long data based on city/state
                try:
                    # Attempts to get latitude and longitude of given city and state
                    latitude, longitude = city_location(city, state)
                except IndexError:
                    print('City and state combination provided do not exist. Empty dataset returned.\n', 'Restarting')
                    # If a combination that does not exist is given, OpenWeather returns an empty list. When the
                    # city_location function attempts to set the latitude using the empty list, an IndexError occurs.
                    continue  # Abandons current loop iteration
                else:
                    print('Valid city and state combination entered. Location data retrieved.')

            # Else block for if a user does not enter zip or city to choose a method to get location data
            else:
                print('Invalid Input - User did not enter "zip" or "city."\n', 'Restarting')
                continue  # Resets the loop

            # After the latitude and longitude have been acquired, we can move to getting the weather data. We will need
            # the desired unit in order to retrieve the correct information from OpenWeather.
            unit = input('What units would you like the temperature displayed in? Fahrenheit, Celsius, or '
                         'Kelvin? Please enter one of those three units\n')  # Asks for the desired temperature unit
            unit = text_cleaner(unit)  # Running text_cleaner since the user was asked for input
            if unit != 'kelvin' and unit != 'fahrenheit' and unit != 'celsius':
                print('Invalid unit entered.\n', 'Restarting')
                continue  # If the user does not input one of the three specified units, then the print statement
                # executes and the loop restarts
            else:
                # If a correct unit is given, then we call for the weather data in the OpenWeather API
                try:
                    weather_data = current_weather(latitude, longitude, unit)  # Gets the weather data
                except requests.exceptions.InvalidURL:
                    print('Information passed into current_weather created invalid URL.\n', 'Restarting')
                    continue
                else:
                    pass

            # We need to display the name of city and state as part of the weather information, regardless of the user's
            # method to acquire latitude and longitude information. If city/state were used, these will now be lowercase
            # because they were normalized. So we can use the latitude and longitude from the user's method to do a
            # reverse lookup and get a name and state with proper capitalization. By this point in the function, valid
            # latitude and longitude should already be acquired by the function used by the user.
            try:
                city_name, state_name = reverse_lookup(latitude, longitude)
            except requests.exceptions.InvalidURL:
                print('Latitude and longitude passed into reverse_lookup created an invalid url.\n', 'Restarting')
                continue
            else:
                pass

            # Now the desired data needs to be organized for display to the user
            # To display the correct unit as part of the information, we will need to re-use the unit input from the
            # previous step and a conditional block. This should already be cleaned and vetted by the program, so there
            # won't be additional input issues. The else statement will prepare for that just in case, though.
            if unit == 'kelvin':
                display_unit = 'K'
            elif unit == 'fahrenheit':
                display_unit = '\N{DEGREE SIGN}F'
            elif unit == 'celsius':
                display_unit = '\N{DEGREE SIGN}C'
            else:
                print('Somehow you got weather information without specifying a unit.\n', 'Restarting')
                # In theory, the program should have broken if a unit was not given successfully or if an unsupported
                # unit was given.
                continue  # Abandons current loop iteration

            # The display_data block will organize the data for display by parsing through the converted JSON data and
            # adding units by converting the numerical data into usable strings that can be added to.
            display_data = dict()  # Initialising a dictionary to store the data being displayed to the user
            display_data['Location'] = '{}, {}'.format(city_name, state_name)
            display_data['Current Temperature'] = str(weather_data['main']['temp']) + display_unit
            display_data['Temperature Feels Like'] = str(weather_data['main']['feels_like']) + display_unit
            display_data['Low Temp'] = str(weather_data['main']['temp_min']) + display_unit
            display_data['High Temp'] = str(weather_data['main']['temp_max']) + display_unit
            display_data['Pressure'] = str(weather_data['main']['pressure']) + ' hPa'
            display_data['Humidity'] = str(weather_data['main']['humidity']) + '%'
            display_data['Current Weather Description'] = string.capwords(weather_data['weather'][0]['description'])

            # After getting the weather data, the information needs to be displayed in a neat and organized manner
            print('Thank you for using OpenWeather! Here is the requested current weather information!')
            for key in display_data:
                print(key, ': ', display_data[key])

        elif loop_state == 'no':
            break
        else:
            print('Invalid Input - Please enter "yes" or "no."\n', 'Restarting')
            continue


if __name__ == "__main__":
    main()


'''
Change Log
Program Created: 2/23/24

Change # 1
Changes Made:
    Added/moved exceptions from the requests library inside the functions used to call APIs for weather or location data
    Converted numerical data from weather_data dictionary into strings to allow for adding units with ease of display
    Added units to be displayed in the display_data dictionary, including a conditional block for temperature units.
    Added capwords method to value for Current Weather Description.
    Added explanatory comments in zip_location and city_location errors in main to explain why they occur when invalid
        inputs are given by the user.
Date of Change: 2/26/24
Author: David Culhane
Approved By: David Culhane
Put Into Production: 2/26/24
'''

'''
Project Checklist:
    The user should be able to input either the city or zip code desired.                                         [X]
    The user should be able to choose what temperature displays between Fahrenheit, Celsius, or Kelvin.           [X]
    Weather information displayed should at least include:
        Location Requested                                                                                        [X]
        Current Temperature                                                                                       [X]
        Feels Like Temperature                                                                                    [X]
        Low Temperature                                                                                           [X]
        High Temperature                                                                                          [X]
        Pressure                                                                                                  [X]
        Humidity                                                                                                  [X]
        Current Weather Description                                                                               [X]
    Two different API calls should be used: one for latitude and longitude and one for the weather information    [X]
    Allow the user to run the program multiple times until the decide to finish. (While loop with sentinel)       [X]
    Validate user data - program should not crash due to invalid user input                                       [X]
    Multiple functions should be used within the program                                                          [X]
    Use try blocks to connect to webservices - display to the user that connection using API was successful       [X]
    
API Key to OpenWeather: ************************
Current Weather API Call Structure:
    https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    Default call uses "standard" units including Kelvin for temperature
    For Celsius, add &units=metric to end of call
    For Fahrenheit, add &units=imperial to end of call
    Returns current weather information in JSON when given valid latitude and longitude information.
GeoCoding API Call Structure: 
  By city and state code:
    http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit=1&appid={API key}
  By zip code:
    http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={API key}
    Returns latitude and longitude information when given zip code or city name and state code
Reverse Lookup API Call Structure:
    http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&appid={API key}
    Returns city and state names when given latitude and longitude information
'''