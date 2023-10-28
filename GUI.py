from main import get_weather
import tkinter as tk

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city: ")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

temperature_label = tk.Label(root, text="")
temperature_label.pack()

root.mainloop()
