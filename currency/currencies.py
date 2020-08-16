import dateparser
import requests
from re import sub


def retrieve_currencies_data(data_url):
    response = requests.get(data_url)
    response.raise_for_status()
    lines = response.content.splitlines()
    headers = lines[0].split(b",")[:-1]
    content = [line.split(b",")[:-1] for line in lines[1:]]
    return headers, content


def currency_dict(headers, data):
    result = {}
    for line in data:
        currencies = result.get(line[0], {})
        currencies.update(
            {
                headers[index]: float(value)
                for index, value in enumerate(line[1:], start=1)
                if value != b"N/A"
            }
        )
        result.update({line[0]: currencies})

    return result


def retrieve_revenue_data(data_url):
    result = {}
    response = requests.get(data_url)
    response.raise_for_status()
    lines = response.text.splitlines()
    for line in lines:
        _date, revenue = line.split(",\t")
        _date = str(dateparser.parse(_date).date())
        revenue = float(sub(r"[^\d.]", "", revenue))
        result.update({_date: revenue})
    return result
