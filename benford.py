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
        true_values_two = data.loc[data['value'] == True]['first_two_digits_volume'].value_counts(normalize = True).sort_index()
        false_values_two = data.loc[data['value'] != True]['first_two_digits_volume'].value_counts(normalize = True).sort_index()

        """
        Creating Beford's Law
        """
        digits_first = list(range(1,10))
        digits_second = list(range(0,10))
        digits_two = list(range(10,100))

        benford = [np.log10(1 + 1/d) for d in digits_first]
        benford_second = [np.log10(1 + ((10 + d)**-1)) for d in digits_second]
        benford_two = [np.log10(1 + 1/d) for d in digits_two]

        # Subplots
        fig, (ax1, ax2, ax3)= plt.subplots(3, 1, figsize = (15,15))

        # Subplot 1
        ax1.bar(digits_first, benford, label = "Expected")
        ax1.plot(true_values_first, color='green', label='Positive Day')
        ax1.plot(false_values_first, color='pink', label='Negative Day')
        ax1.set_title("First Digit Benford's Law")
        ax1.legend()

        # Subplot 2
        ax2.bar(digits_second, benford_second, label = "Expected")
        ax2.plot(true_values_second, color='green', label='Positive Day')
        ax2.plot(false_values_second, color='pink', label='Negative Day')
        ax2.set_title("Second Digit Benford's Law")
        ax2.legend()

        # Subplot 3
        ax3.bar(digits_two, benford_two, label = "Expected")
        ax3.plot(true_values_two, color='green', label='Positive Day')
        ax3.plot(false_values_two, color='pink', label='Negative Day')
        ax3.set_title("First Two Digits Benford's Law")
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

        data['diff'] = np.abs(data["diff"])

        # Removing the decimal and zeros in the difference in price
        for i, price in enumerate(data["diff"]):
            string = str(round(price, 4)).replace(".", "")
            if int(string) == 0:
                data["diff"][i] = string + "00"
            elif string[:3] == "000":
                data["diff"][i] = string.replace(string[:3], "") + "00"
            elif string[:2] == "00":
                data["diff"][i] = string.replace(string[:2], "") + "00"
            elif string[0] == "0":
                data["diff"][i] = string.replace(string[0], "") + "00"
            else:
                pass

        # Collecting the first digit of the daily price change
        data['first_digit_diff'] = data['diff'].map(lambda a: str(a).replace(".","")[0]).astype(int)

        # Collecting the second digit of the daily price change
        data['second_digit_diff'] = data['diff'].map(lambda a: str(a).replace(".","")[1]).astype(int)

        # Collecting the first two digits of the daily price change
        data['first_two_digits_diff'] = data['diff'].map(lambda a: str(a).replace(".","")[0:2]).astype(int)

        # Normalizing digits of volume based on positive and negative days
        # First digit
        true_values_first = data.loc[data['value'] == True]['first_digit_diff'].value_counts(normalize = True).sort_index()
        false_values_first = data.loc[data['value'] != True]['first_digit_diff'].value_counts(normalize = True).sort_index()

        # Second digit
        true_values_second = data.loc[data['value'] == True]['second_digit_diff'].value_counts(normalize = True).sort_index()
        false_values_second = data.loc[data['value'] != True]['second_digit_diff'].value_counts(normalize = True).sort_index()

        # First two digits
        true_values_two = data.loc[data['value'] == True]['first_two_digits_diff'].value_counts(normalize = True).sort_index()
        false_values_two = data.loc[data['value'] != True]['first_two_digits_diff'].value_counts(normalize = True).sort_index()

        """
        Creating Beford's Law
        """
        digits_first = list(range(1,10))
        digits_second = list(range(0,10))
        digits_two = list(range(10,100))

        benford = [np.log10(1 + 1/d) for d in digits_first]
        benford_second = [np.log10(1 + ((10 + d)**-1)) for d in digits_second]
        benford_two = [np.log10(1 + 1/d) for d in digits_two]

        # Subplots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (15,15))

        # Subplot 1
        ax1.bar(digits_first, benford, label = "Expected")
        ax1.plot(true_values_first, color='green', label='Positive Day')
        ax1.plot(false_values_first, color='pink', label='Negative Day')
        ax1.set_title("First Digit Benford's Law")
        ax1.legend()

        # Subplot 2
        ax2.bar(digits_second, benford_second, label = "Expected")
        ax2.plot(true_values_second, color='green', label='Positive Day')
        ax2.plot(false_values_second, color='pink', label='Negative Day')
        ax2.set_title("Second Digit Benford's Law")
        ax2.legend()

        # Subplot 3
        ax3.bar(digits_two, benford_two, label = "Expected")
        ax3.plot(true_values_two, color='green', label='Positive Day')
        ax3.plot(false_values_two, color='pink', label='Negative Day')
        ax3.set_title("First Two Digits Benford's Law")
        ax3.legend();
