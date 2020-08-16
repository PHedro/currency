import unittest

from currency.currencies import (
    currency_dict,
    retrieve_currencies_data,
    retrieve_revenue_data,
)


class FileHandlerTestCase(unittest.TestCase):
    def test_retrieve_revenue_data(self):
        expected = {
            "2020-05-23": 51191.12,
            "2020-05-22": 45710.12,
            "2020-05-21": 25867.33,
            "2020-05-20": 23780.45,
            "2020-05-19": 38794.74,
            "2020-05-18": 38814.34,
            "2020-05-17": 37682.75,
            "2020-05-16": 14399.13,
            "2020-05-15": 29976.42,
            "2020-05-14": 25622.93,
        }
        result = retrieve_revenue_data(
            "https://gist.githubusercontent.com/ger-f/0fd94e0cac53ab5e393fdc20dd40e8e1/raw/421744b058df6e727e9c8fb5915dc9d80a6b0f69/revenue.csv"
        )
        self.assertEqual(expected, result)

    def test_retrieve_currencies_data(self):
        result_header, result_content = retrieve_currencies_data(
            "https://gist.githubusercontent.com/ger-f/f4701ce5dad91f13028cd6ebfc740ba7/raw/181f764da55cb5bcbd2c6a65f4b412665bf3f2b5/csv"
        )
        expected_header = [
            b"Date",
            b"USD",
            b"JPY",
            b"BGN",
            b"CYP",
            b"CZK",
            b"DKK",
            b"EEK",
            b"GBP",
            b"HUF",
            b"LTL",
            b"LVL",
            b"MTL",
            b"PLN",
            b"ROL",
            b"RON",
            b"SEK",
            b"SIT",
            b"SKK",
            b"CHF",
            b"ISK",
            b"NOK",
            b"HRK",
            b"RUB",
            b"TRL",
            b"TRY",
            b"AUD",
            b"BRL",
            b"CAD",
            b"CNY",
            b"HKD",
            b"IDR",
            b"ILS",
            b"INR",
            b"KRW",
            b"MXN",
            b"MYR",
            b"NZD",
            b"PHP",
            b"SGD",
            b"THB",
            b"ZAR",
        ]
        expected_first_line = [
            b"2020-07-14",
            b"1.1375",
            b"122.17",
            b"1.9558",
            b"N/A",
            b"26.638",
            b"7.4447",
            b"N/A",
            b"0.90778",
            b"355.48",
            b"N/A",
            b"N/A",
            b"N/A",
            b"4.4781",
            b"N/A",
            b"4.8435",
            b"10.3855",
            b"N/A",
            b"N/A",
            b"1.0691",
            b"159.4",
            b"10.711",
            b"7.5295",
            b"80.837",
            b"N/A",
            b"7.8111",
            b"1.6348",
            b"6.0925",
            b"1.5488",
            b"7.9805",
            b"8.8171",
            b"16436.88",
            b"3.9092",
            b"85.7725",
            b"1371.98",
            b"25.7383",
            b"4.8588",
            b"1.7417",
            b"56.305",
            b"1.5846",
            b"35.922",
            b"19.0732",
        ]
        expected_line_99 = [
            b"2020-02-21",
            b"1.0801",
            b"120.96",
            b"1.9558",
            b"N/A",
            b"25.061",
            b"7.4702",
            b"N/A",
            b"0.8351",
            b"337.1",
            b"N/A",
            b"N/A",
            b"N/A",
            b"4.2835",
            b"N/A",
            b"4.804",
            b"10.569",
            b"N/A",
            b"N/A",
            b"1.061",
            b"138.3",
            b"10.0873",
            b"7.449",
            b"69.548",
            b"N/A",
            b"6.6131",
            b"1.6363",
            b"4.755",
            b"1.432",
            b"7.5945",
            b"8.4117",
            b"14867.58",
            b"3.6985",
            b"77.754",
            b"1309.45",
            b"20.5183",
            b"4.5294",
            b"1.7104",
            b"54.955",
            b"1.5131",
            b"34.164",
            b"16.2965",
        ]

        self.assertEqual(expected_header, result_header)
        self.assertEqual(expected_first_line, result_content[0])
        self.assertEqual(expected_line_99, result_content[99])

    def test_currency_dict(self):
        expected = {
            b"USD": 1.129,
            b"JPY": 121.61,
            b"BGN": 1.9558,
            b"CZK": 26.681,
            b"DKK": 7.4522,
            b"GBP": 0.9015,
            b"HUF": 353.62,
            b"PLN": 4.4683,
            b"RON": 4.8393,
            b"SEK": 10.4555,
            b"CHF": 1.0643,
            b"ISK": 157.0,
            b"NOK": 10.6428,
            b"HRK": 7.549,
            b"RUB": 80.8888,
            b"TRY": 7.7508,
            b"AUD": 1.6261,
            b"BRL": 6.0701,
            b"CAD": 1.5317,
            b"CNY": 7.9287,
            b"HKD": 8.7499,
            b"IDR": 16302.76,
            b"ILS": 3.895,
            b"INR": 84.4645,
            b"KRW": 1349.06,
            b"MXN": 25.4764,
            b"MYR": 4.8259,
            b"NZD": 1.726,
            b"PHP": 55.892,
            b"SGD": 1.5751,
            b"THB": 35.262,
            b"ZAR": 19.2908,
        }
        result = currency_dict(
            *retrieve_currencies_data(
                "https://gist.githubusercontent.com/ger-f/f4701ce5dad91f13028cd6ebfc740ba7/raw/181f764da55cb5bcbd2c6a65f4b412665bf3f2b5/csv"
            )
        )

        self.assertEqual(expected, result.get(b"2020-07-07"))