import requests

API_KEY = "2c07eacd94667842d04919a6f3bba171"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    # the reason we get data['list'] is because list is a dictionary with about 40 odd dictionaries
    # which contains the values of many tings which we need to extract.
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
