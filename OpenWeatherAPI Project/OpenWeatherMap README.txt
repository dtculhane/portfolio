OpenWeatherMap README
David Culhane

The OpenWeatherMap script accesses the OpenWeatherAPI to give the user current weather information on a US location of the user's choosing. 

The script loops through prompts for user input to ask if the user wants weather information, whether or not they wish to use a zip code or a city/state combination, the information about the location, and the unit the user would like the temperature to be presented in. Once this information has been keyed, the script calls the OpenWeather API for JSON data about the given location and displays location, temperature, barometric pressure, humidity, and current weather description. The script then re-initializes the loop with a sentinel value of "no" breaking the loop. Invalid inputs reset the script to the beginning prompt.