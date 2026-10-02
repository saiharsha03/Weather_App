# Weather App

A small desktop app that shows the current temperature for a city, built with Python and Tkinter.

Type a city and click **Get Weather**. The app calls the [Weatherstack](https://weatherstack.com/) API and shows the temperature with a short tip: sunscreen at 30°C and above, an umbrella at 20°C and above, a jacket at 0°C and above, and a freezing warning below that. An unknown city shows "City not found".

## Files

- `GUI.py`: the window and the temperature messages
- `get_weather.py`: the API request
- `get_api.py`: reads the API key from `secret.txt`

## Run it

```bash
pip install requests
```

Create a git-ignored `secret.txt` next to the code containing your own Weatherstack API key (the free plan works), then:

```bash
python GUI.py
```

## Known issues

- The free Weatherstack plan only supports plain `http`, so requests are not encrypted.
- `get_weather.py` does not handle network errors or a missing `secret.txt`; the app will raise an exception instead of showing a message.
