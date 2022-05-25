This is a simple Script that collects current weather information, which returns the following:
○ Temperature in Fahrenheit
○ Weather Conditions

To use the script do the following:

1. update your pip 
    python.exe -m pip install --upgrade pip 

2. install the requests library
    pip install requests

3. install the dotenv library
    pip install python-dotenv

4. UnZip the contents into your desired location

5. How to user your api_key:
    Option-1: Copy, paste and save your API KEY into the .env file ( do not use quotes )
    Option-2: Enter Your Api key by way of commandLine. (no quotes)

    NOTE: IF YOU DO NOT ENTER IN AN API KEY,  YOU WILL HAVE THE CHOICE OF USING WHATS IN THE .env file.
            SO MAKE SURE YOU HAVE ONE SAVED WITHIN .env, otherwise it will error out.

6. Create an instance for the desired location as a city and country code:
        EXAMPLE:
            toronto = Weather('toronto','ca')
        
       
        ALL COUNTRIES ARE SUPPORTED - MUST USE CORRECT ABBRIVIATIONS OTHERWISE PROGRAM WILL THROW ERROR.

        EXAMPLES ( !!!YOU CAN ONLY RUN ONE INSTANCE AT A TIME!!! ):
            toronto = Weather('toronto','ca')
            brooklyn = Weather('brooklyn','us')
            paris = Weather('paris','fr')
            virginia_beach = Weather('virginia_beach','va')

7. Run the get_current_weather method against your created instance.
    toronto.get_current_weather()

8. run the script "Jeffrey_Mcintyre_OpenWeather_project.py 



