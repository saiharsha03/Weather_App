from get_weather import get_weather
import tkinter as tk

def display_weather():
    city_name = city_entry.get()

    resp = get_weather(city_name)

    if 'current' not in resp:
        weather_label.config(text='City not found')
    else:
        city = resp['location']['name']
        country = resp['location']['country']
        temp = resp['current']['temperature']
        weather_label.config(text=f'The temperature in {city}, {country} is {temp}°C)',fg="blue")
        if(temp>=30):
            update_label.config(text="Better get your sunscreen")
        elif(temp>=20):
            update_label.config(text="Good Weather, carry an umbrella just in case")
        elif(temp>=0):
            update_label.config(text="Get your jacket on, it's cold")
        else:
            update_label.config("It's below freezing point. Gear up")

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
update_label = tk.Label(root,text="")
update_label.pack()

root.mainloop()
