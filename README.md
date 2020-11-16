# Stock Volume Benford's Law

## Executive Summary
Analyzing, determining, and predicting the volatility of the stock market is extremely important to managing risk when entering the market; moreover, applying seemingly simple mathematical laws to the market can help highlight some potential or current risk. For this project, I created a class to apply Benford's law to the daily traded volume and the absolute value change of the open and closing price for a given stock. I further separated the days of gains from loses to potentially highlight any distinction between the two. I should be noted that although this law does appear in several sets of large data, there may be some deviations that can quickly be explained with some further research.

## Introduction
#### Benford's Law
Benford's law is based on the frequency of the leading digit of a naturally occurring numeric data, where 1 is the most frequent followed sequentially until 9. A graphical example of this trend is shown below, and is applied to the following charts as reference.
![benford's law]("./Images/benfords-law.png")

This law can be applied to a wide range of numerical data, such as the areas of rivers and molecular weights of a group of molecules outlined in Benford's paper (F. Benford, The law of anomalous numbers, Proc. Amer. Philos. Soc. 78 (1938), 551-572). It often is used in detecting fruadulent activity, where a large deviation from the expected curve is significant.
The trend, highlighted above, is the following equation. Where is n is 1 through 9.

`$$P_{n} = \log_{10} (1 + n^-1)$$`

This trend is taken a step further by looking at the second digit, where the probability of each digit is far closer together but still follows the trend of 1 through 9 sequentially. Explained in (T. P. Hill, Base-Invariance Implies Benford's Law, American Mathematical Society, Vol. 123, No. 3, March 1995) the following equation to solve for this is listed below.

`$$P_{n} = \sum_{k=1}^9 \log_{10} (1 + (10k + n)^-1)$$`


Other forms of Benford's Law are analyzing the first two digits, last two digits, etc. For the purpose of this project I only added the first two digits to the mix; however, other digits can be added quickly for a more robust analysis.

#### Alpha Vantage API
Gathering the data I used Alpha Vantage API, which would provide the previous 100 days of open, close, and volume data. Following the free tier guidelines, I pulled down `Apple's` daily stock market data for the past twenty years, known as TIME_SERIES_DAILY.

#### Data Cleaning
Because the data-frames had the full open, close, and daily volume values for each day, I applied a lambda function to pull the first, second digits, and first two digits, while also normalizing the value counts to be graphed. Applying this lambda function was not before finding the absolute difference in open and close price each day and removing any leading 0s or decimals.

## Notebooks
There are currently two files, benford and showcasing. Benford provides a python class and a series of functions to quickly pull up to date stock market data and display results of Benford's law being applied.
