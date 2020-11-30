# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

class stocks(object):
    """
    - name     Name of the company
    - ticker   Ticker of the company
    - api_key  API key for Alpha Vantage
    """

    def __init__(self, name, ticker, api_key):
        self.name = name,
        self.ticker = ticker,
        self.api_key = api_key

    def daily_volume(self):

        res = requests.get(
            "https://www.alphavantage.co/query",
            params = {
                "function": "time_series_daily",
                "outputsize": "full",
                "symbol": self.ticker,
                "apikey": self.api_key
            }
            )
        data = pd.DataFrame(res.json()['Time Series (Daily)']).T

        """
        Positive or Negative Day
        """

        # Determing if the day was positive or negative
        data['diff'] = data['4. close'].astype(float) - data['1. open'].astype(float)
        data['value'] = data['diff'].map(lambda a: True if a < 0 else False)

        """
        Volume
        """
        # Collecting the first digit of volume
        data['first_digit_volume'] = data['5. volume'].map(lambda a:str(a)[0]).astype(int)

        # Collecting the second digit of volume
        data['second_digit_volume'] = data['5. volume'].map(lambda a:str(a)[1]).astype(int)

        # Collecting the first two digits of volume
        data['first_two_digits_volume'] = data['5. volume'].map(lambda a:str(a)[0:2]).astype(int)


        # Normalizing digits of volume based on positive and negative days
        # First digit
        true_values_first = data.loc[data['value'] == True]['first_digit_volume'].value_counts(normalize = True).sort_index()
        false_values_first = data.loc[data['value'] != True]['first_digit_volume'].value_counts(normalize = True).sort_index()

        # Second digit
        true_values_second = data.loc[data['value'] == True]['second_digit_volume'].value_counts(normalize = True).sort_index()
        false_values_second = data.loc[data['value'] != True]['second_digit_volume'].value_counts(normalize = True).sort_index()

        # First two digits
        true_values_two = data.loc[data['value'] == True]['first_two_digit_volume'].value_counts(normalize = True).sort_index()
        false_values_two = data.loc[data['value'] != True]['first_two_digit_volume'].value_counts(normalize = True).sort_index()

        """
        Creating Beford's Law
        """
        # First digit Benford
        digits_first = list(range(1,10))
        benford_first = [np.log10(1 + 1/d) for d in digits_first]

        # Second digit Benford
        digits_second = list(range(0,10))
        benford_second = [np.log10(1 + ((10 + d)**-1)) for d in digits_second]

        # First two digits Beford
        digits_two = list(range(10,100))
        beford_two = [np.log10(1 + 1/d) for d in digits]

        # Subplots
        fig, (ax1, ax2, ax3)= plt.subplots(3, 1)

        # Subplot 1
        ax1.bar(digits_first, benford_first, label = "Expected")
        ax1.plot(true_values_first, color='black', label='Positive Day')
        ax1.plot(false_values_first, color='red', label='Negative Day')
        ax1.legend()

        # Subplot 2
        ax2.bar(digits_second, benford_second, label = "Expected")
        ax2.plot(true_values_second, color='black', label='Positive Day')
        ax2.plot(false_values_second, color='red', label='Negative Day')
        ax2.legend()

        # Subplot 3
        ax3.bar(digits_two, benford_two, label = "Expected")
        ax3.plot(true_values_two, color='r', label='Positive Day')
        ax3.plot(false_values_two, color='b', label='Negative Day')
        ax3.legend();


    def daily_delta(self):

        res = requests.get(
            "https://www.alphavantage.co/query",
            params = {
                "function": "time_series_daily",
                "outputsize": "full",
                "symbol": self.ticker,
                "apikey": self.api_key
            }
            )
        data = pd.DataFrame(res.json()['Time Series (Daily)']).T

        """
        Positive or Negative Day
        """

        # Determing if the day was positive or negative
        data['diff'] = data['4. close'].astype(float) - data['1. open'].astype(float)
        data['value'] = data['diff'].map(lambda a: True if a < 0 else False)

        """
        Price Change
        """
        # Finding the difference in open and close

        data['diff'] = np.abs(data['4. close'].astype(float) - data['1. open'].astype(float)).astype(float)

        # Removing the decimal and zeros in the difference in price
        for i, price in enumerate(data['diff']):
            string = str(price).replace(".","")
            if string[:3] == "000":
                data['diff'][ i] = string.replace(string[:3], "")
            elif string[:2] == "00":
                data['diff'][i] = string.replace(string[:2], "")
            elif string[0] == "0":
                data['diff'][i] = string.replace(string[0], "")
            else:
                data['diff'][i] = string + "00"

        # Collecting the first digit of the daily price change
        data['first_digit_diff'] = data['diff'].map(lambda a: str(a)[0]).astype(int)

        # Collecting the second digit of the daily price change
        data['second_digit_diff'] = data['diff'].map(lambda a: str(a)[1]).astype(int)

        # Collecting the first two digits of the daily price change
        data['first_two_digits_diff'] = data['diff'].map(lambda a: str(a)[0:2]).astype(int)

        # Normalizing digits of volume based on positive and negative days
        # First digit
        true_values_first = data.loc[data['value'] == True]['first_digit_diff'].value_counts(normalize = True).sort_index()
        false_values_first = data.loc[data['value'] != True]['first_digit_diff'].value_counts(normalize = True).sort_index()

        # Second digit
        true_values_second = data.loc[data['value'] == True]['second_digit_diff'].value_counts(normalize = True).sort_index()
        false_values_second = data.loc[data['value'] != True]['second_digit_diff'].value_counts(normalize = True).sort_index()

        # First two digits
        true_values_two = data.loc[data['value'] == True]['first_two_digit_diff'].value_counts(normalize = True).sort_index()
        false_values_two = data.loc[data['value'] != True]['first_two_digit_diff'].value_counts(normalize = True).sort_index()

        """
        Creating Beford's Law
        """

        # First digit Benford
        digits_first = list(range(1,10))
        benford_first = [np.log10(1 + 1/d) for d in digits]

        # Second digit Benford
        digits_second = list(range(0,10))
        beford_second = [np.log10(1 + ((10 + d)**-1)) for d in digits_second]

        # First two digits Beford
        digits_two = list(range(10,100))
        beford_two = [np.log10(1 + 1/d) for d in digits]

        # Subplots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

        # Subplot 1
        ax1.bar(digits_first, benford_first, label = "Expected")
        ax1.plot(true_values_first, color='black', label='Positive Day')
        ax1.plot(false_values_first, color='red', label='Negative Day')
        ax1.legend()

        # Subplot 2
        ax2.bar(digits_second, benford_second, label = "Expected")
        ax2.plot(true_values_second, color='black', label='Positive Day')
        ax2.plot(false_values_second, color='red', label='Negative Day')
        ax2.legend()

        # Subplot 3
        ax3.bar(digits_two, benford_two, label = "Expected")
        ax3.plot(true_values_two, color='black', label='Positive Day')
        ax3.plot(false_values_two, color='red', label='Negative Day')
        ax3.legend();
