# Stock Volume Benford's Law

## Executive Summary
Analyzing, determining, and predicting the volatility of the stock market is extremely important to managing risk when entering the market; moreover, applying seemingly simple mathematical laws to the market can help highlight some potential or current risk. For this project, I applied Benford's law to the daily traded volume and the absolute value change of the open and close price of the last 100 days starting April 14th. Fortunately for this project, but less fortunate for anyone invested in the stock market, we recently saw an economic downturn and rally due to Covid-19. Taking advantage of this opportunity, I separated the dates prior to the downturn, during the sell off, and during the rally. Before separating the dates, it wasn't clear on whether or not a stock truly followed Benford's law, since trading volume could average 2 - 4 million and the stock itself could be considered more volatile, such as Tesla. However, once the separation was established, certain companies, such as GE, experienced drastic trading differences. What was more interesting was applying it to Dow Jones and the S&P indexes, DIA and SPY, respectively. Separating the timeframes showcase a large shift with what digits are showing up the most.

![S&P 500 Volume]('./Images/S&PFirstDigitVolume.png')

This can be taken a step further by applying these results to previous economic downturns to see if there are similar trends.

## Introduction
#### Benford's Law
Benford's law is based on the frequency of the leading digit of a naturally occurring numeric data, where 1 is the most frequent followed sequentially until 9. A graphical example of this trend is shown below, and is applied to the following charts as reference.
![benford's law]("./Images/benfords.png")

This law can be applied to a wide range of numerical data, such as the areas of rivers and molecular weights of a group of molecules outlined in Benford's paper (F. Benford, The law of anomalous numbers, Proc. Amer. Philos. Soc. 78 (1938), 551-572). It
The trend, highlighted above, is the following equation. Where is n is 1 through 9.

`$$P_{n} = \log_{10} (1 + n^-1)$$`

This trend is taken a step further by looking at the second digit, where the probability of each digit is far closer together but still follows the trend of 1 through 9 sequentially. Explained in (T. P. Hill, Base-Invariance Implies Benford's Law, American Mathematical Society, Vol. 123, No. 3, March 1995) the following equation to solve for this is listed below.

`$$P_{n} = \sum_{k=1}^9 \log_{10} (1 + (10k + n)^-1)$$`


#### Alpha Vantage API
Gathering the data I used Alpha Vantage API, which would provide the previous 100 days of open, close, and volume data. Following the free tier guidelines, I pulled down `Dow Jones, S&P 500, Apple, 3M, Tesla, & GE` stock.

#### Data Cleaning
Because the data-frames had the full open, close, and daily volume values for each day, I applied a lambda function to pull the first and second digits, while also normalizing the value counts to be graphed. Applying this lambda function was not before finding the absolute difference in open and close price each day and removing any leading 0s or decimals.

Since we have seen great economic growth in 2019, a sudden downturn due to coronavirus, and a ~50% rally, I thought this would be a great opportunity to apply this law and observe some of the differences in trading. For this I separated the data-frame to consider everything prior to February 19th (which was the sell off), the market sell off (Feb. 19th to March 23rd), and the rally starting March 24th up until the last date data was collected (April 14th).


## Results & Discussion

### Benford's law
#### Daily Volume
##### 100 Day Volume
![Volume]('./Images/AllDatesFirstDigitVolume.png')
At initial observations the trends of daily market price follows along what would be expected with a few exceptions. Personally, I do not see that as something that raises any flags since interests in companies varies and often can be additive not subtractive. Meaning any external focus may increase the total volume, but won't change a more likely 2 million daily average to 1 million. Both 3M and Apple are good examples of this because the most occurring digits are 2 and 3, but has a decreasing trend in the following digits.



##### Separation Based on Market Reaction
Taking it a step further, I looked at the different market time frames to see if there were any differences in trading. I focused on Dow Jones (DIA) and the S&P 500 (SPY).
![Dow Jones Volume]('./Images/DowJonesFirstDigitVolume.png')
Prior to the February 19th, the first digit daily volume does follow along with Benford's law, with a large drop off from 4 on. Surprising, both the rally and sell off exhibit an increase in the number 5 and an decrease in the number 2.

![S&P 500 Volume]('./Images/S&PFirstDigitVolume.png')
The S&P 500 index has the complete opposite reaction. Even prior to the sell off and rally, the S&P 500 completely ignores digits 1-3 and starts its decline in frequency from 4 on. This is the reverse for the sell off and rally, since both of these see a large shift to 1-2 being more frequent. The only distinction is an increase in the number 3 during the sell off and a large increase in the number 1 during the rally.

#### Difference of Close and Open Price
##### 100 Day difference
![Difference]('./Images/AllDatesFirstDigitChange.png')
Similar to volume, the difference in open and close price does follow a Benford's law with the exceptions of Tesla and GE, where the leading digit of 1 is never seen.

##### Separation Based on Market Reaction
![Dow Jones Change]("./Images/DowJonesFirstDigitChange.png")
The largest change during these time frames is an increase in the digit 6, whereas the rest of the trends remain relatively constant.

![S&P Change]("./Images/S&PFirstDigitChange.png")
The daily price changes of the S&P during these time frames highlight a few shifts, such as the peak digit, besides 1, moves one or more digits to the left or right. During the bull market leading to the sell off, the changes in opening and closing prices followed along with Benford's law quite well, with one small peak at the number 5. The sell off, however, exhibited a decrease in numbers 2 - 5 and increase in the numbers 6 and 7. Taking into account the short time frame this sell off happened in, I'm not too surprised by that shift since the difference in the open and close price would need to be fairly large. On the other side, there was a shift to the increasing value of the number 4 and a small decrease in 3. Again, since we are currently at the 50% retracement, the differences in the open and close price wouldn't need to be so drastic, as seen in the sell off.

### Second Digit Probability
Second digit frequency shows no really  trend for both the daily price change or volume change, shown in the graphs below. Looking at the indexes exclusively, there isn't any obvious trends, especially when taking a broader view. Not to say that these stocks are closely related, which could provide some trends, but it looks to be random probability. However, this isn't too surprising since the frequency of the second digits are closer than the first digit.
![Daily Change]("./Images/AllDatesSecondDigitChange.png")
![Volume Change]("./Images/AllDatesSecondDigitVolume.png")

## Conclusion
Applying Benford's Law to various stocks may help distinguish fluctuations in the market or within the stock itself. It may be more valuable to have this information to compare against current data, since Dow Jones and the S&P did exhibit large changes before and after a high volatility sell off. Furthermore, knowing the basis how each company is trades, such as Tesla's large swings in price, may help explain the values shown here. In summary this wouldn't be the best modality to predict the volatility based on deviating from Benford's law, but can provide some guideance on how the stock is trading each day.

There are a few other considerations, such as how would taking the volume difference between days effect the results, much like taking the rolling average. Another consideration is to take the difference of price every hour or every 30 minutes to see if the changes are more in line with Benford's Law. The same could be said for the volume. If there was a consistant trend and there was a large unloading of a stock, it may be able to pick up that change due to the spikes in volume.
