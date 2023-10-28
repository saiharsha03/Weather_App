from get_weather import get_weather
import tkinter as tk

def display_weather():
    city_name = city_entry.get()

    temperature = get_weather(city_name)

    if temperature is not None:
        weather_label.config(text=f'Temperature: {temperature}°C)')
    else:
        weather_label.config(text='City not found')

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city: ")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather",width=50,fg= 'blue', command=display_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

root.mainloop()
