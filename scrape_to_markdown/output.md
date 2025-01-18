# backtesting API documentation

**URL:** https://kernc.github.io/backtesting.py/doc/backtesting/



![xkcd.com/1570](https://imgs.xkcd.com/comics/engineer_syllogism.png)

## Manuals

* [**Quick Start User Guide**](../examples/Quick%20Start%20User%20Guide.html)

## Tutorials

* [Library of Utilities and Composable Base Strategies](../examples/Strategies%20Library.html)
* [Multiple Time Frames](../examples/Multiple%20Time%20Frames.html)
* [**Parameter Heatmap & Optimization**](../examples/Parameter%20Heatmap%20&%20Optimization.html)
* [Trading with Machine Learning](../examples/Trading%20with%20Machine%20Learning.html)

These tutorials are also available as live Jupyter notebooks:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kernc/backtesting.py/master?urlpath=lab%2Ftree%2Fdoc%2Fexamples%2FQuick%20Start%20User%20Guide.ipynb)
[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kernc/backtesting.py/)
  
In Colab, you might have to `!pip install backtesting`.

## Example Strategies

* (contributions welcome)

Tip

For an overview of recent changes, see
[What's New](https://github.com/kernc/backtesting.py/blob/master/CHANGELOG.md).

## FAQ

Some answers to frequent and popular questions can be found on the
[issue tracker](https://github.com/kernc/backtesting.py/issues?q=label%3Aquestion+-label%3Ainvalid)
or on the [discussion forum](https://github.com/kernc/backtesting.py/discussions) on GitHub.
Please use the search!

## License

This software is licensed under the terms of [AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.html),
meaning you can use it for any reasonable purpose and remain in
complete ownership of all the excellent trading strategies you produce,
but you are also encouraged to make sure any upgrades to *Backtesting.py*
itself find their way back to the community.

# API Reference Documentation


## Sub-modules

`[backtesting.backtesting](backtesting.html "backtesting.backtesting")`

Core framework data structures.
Objects from this module can also be imported from the top-level
module directly, e.g …



`[backtesting.lib](lib.html "backtesting.lib")`

Collection of common building blocks, helper auxiliary functions and
composable strategy classes for reuse …



`[backtesting.test](test/index.html "backtesting.test")`

Data and utilities for testing.












---

# Backtesting.py - Backtest trading strategies in Python

**URL:** https://kernc.github.io/backtesting.py/




![](logo.png)
# Backtesting.py

## Backtest trading strategies in Python




Does it seem like you had missed getting rich during the recent crypto craze?
Fret not, the international financial markets continue their move rightwards
every day. You still have your chance.
But successful traders all agree emotions have no place in trading —
if you are ever to enjoy a fortune attained by your trading, better
first make sure your strategy or system is well-tested and working reliably
to consistent profit.
Mechanical or algorithmic trading, they call it. They'll usually recommend
signing up with a broker and trading on a demo account for a few months …
But you know better. You know some programming.

> It is far better to foresee even without certainty than not to foresee at all.
> 
> *— Henri Poincare*

**Backtesting.py** is a Python framework for inferring viability
of trading strategies on historical (past) data.
Of course, past performance is not indicative of future results,
but a strategy that proves itself resilient in a multitude of
market conditions can, with a little luck, remain just as reliable in the future.
Improved upon the vision of
[Backtrader](https://www.backtrader.com/),
and by all means surpassingly comparable to other accessible alternatives,
Backtesting.py is lightweight, fast, user-friendly, intuitive,
interactive, intelligent and, hopefully, future-proof.
It is also documented well, including a handful of tutorials.


* **Compatible with forex, crypto, stocks, futures ...**
  
  Backtest any financial instrument for which you have access to historical candlestick data.
* **Blazing fast, convenient**
  
  Built on top of cutting-edge ecosystem libraries (i.e. Pandas, NumPy, Bokeh) for maximum usability.
* **Small, clean API**
  
  The API reference is easy to wrap your head around and fits on a single page.

* **Technical indicator library agnostic**
  
  Compatible with any sensible technical analysis library, such as
  [TA-Lib](https://ta-lib.github.io/ta-lib-python/) or
  [Tulip](https://tulipindicators.org/).
* **Built-in optimizer**
  
  Test hundreds of strategy variants in mere seconds, resulting in heatmaps you can interpret at a glance.
* **High-level API**
  
  Think market timing, swing trading, money management, stop-loss and take-profit prices, leverage, machine learning ...

* **Interactive visualization**
  
  Simulated trading results in telling interactive charts you can zoom into. See [*Example*](#example).
* **Vectorized or event-based backtesting**
  
  Signal-driven or streaming, model your strategy enjoying the flexibility of both approaches.
* **Composable strategies**
  
  Contains a library of predefined utilities and general-purpose strategies that are made to stack.



### Download





[PyPI](https://pypi.org/project/backtesting/ "Backtesting on PyPI")
[GitHub](https://github.com/kernc/backtesting.py "Backtesting.py on GitHub")
[Docs](doc/backtesting/ "Backtesting.py documentation")


Backtesting.py works with Python 3.
You need to know some [Python](https://www.python.org) to effectively use this software.



### Example

The example shows a simple, unoptimized **moving average cross-over**
strategy. It's a common introductory strategy and a pretty decent strategy
overall, provided the market isn't whipsawing sideways.

We begin with **10,000 units of currency** in cash,
realistic **0.2% broker commission**, and we
trade through **9 years** worth of
**Alphabet Inc.** stock.

Whenever the fast, 10-period simple moving average of closing prices crosses
**above** the slower, 20-period moving average, we go **long**,
buying as many stocks as we can afford.
When it crosses **below**, we close our long position and go **short**
(assuming the underlying instrument is actually a
CFD and can be shorted).

We record most significant statistics this simple system produces on our data,
and we show a plot for further manual inspection.


```
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


bt = Backtest(GOOG, SmaCross,
              cash=10000, commission=.002,
              exclusive_orders=True)

output = bt.run()
bt.plot()
```


```
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                       94.27
Equity Final [$]                     68935.12
Equity Peak [$]                      68991.22
Return [%]                             589.35
Buy & Hold Return [%]                  703.46
Return (Ann.) [%]                       25.42
Volatility (Ann.) [%]                   38.43
Sharpe Ratio                             0.66
Sortino Ratio                            1.30
Calmar Ratio                             0.77
Max. Drawdown [%]                      -33.08
Avg. Drawdown [%]                       -5.58
Max. Drawdown Duration      688 days 00:00:00
Avg. Drawdown Duration       41 days 00:00:00
# Trades                                   93
Win Rate [%]                            53.76
Best Trade [%]                          57.12
Worst Trade [%]                        -16.63
Avg. Trade [%]                           1.96
Max. Trade Duration         121 days 00:00:00
Avg. Trade Duration          32 days 00:00:00
Profit Factor                            2.13
Expectancy [%]                           6.91
SQN                                      1.78
_strategy              SmaCross(n1=10, n2=20)
```



JavaScript is required.

Find **better examples**, including executable Jupyter notebooks, in the
project documentation.

[Documentation](doc/backtesting/ "Backtesting.py documentation")




### What Users are Saying

> The proof of [this] program's value is its existence.
> 
> Alan Perlis


> Some things are so unexpected that no one is prepared for them.
> 
> Leo Rosten


> When all else fails, read the instructions.
> 
> Cahn



> The financial markets generally are unpredictable. So that one has to have different scenarios … The idea that you can actually predict what's going to happen contradicts my way of looking at the market.
> 
> George Soros


> If you don’t find a way to make money while you sleep, you will work until you die.
> 
> Warren Buffet









---

# Trading with Machine Learning

**URL:** https://kernc.github.io/backtesting.py/doc/examples/Trading%20with%20Machine%20Learning.html


# Trading with Machine Learning Models[¶](#Trading-with-Machine-Learning-Models)

This tutorial will show how to train and backtest a
[machine learning](https://en.wikipedia.org/wiki/Machine_learning)
price forecast model with *backtesting.py* framework. It is assumed you're already familiar with
[basic framework usage](https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html)
and machine learning in general.

For this tutorial, we'll use almost a year's worth sample of hourly EUR/USD forex data:


In [1]:
```
from backtesting.test import EURUSD, SMA

data = EURUSD.copy()
data

```





Loading BokehJS ...




Out[1]:

|  | Open | High | Low | Close | Volume |
| --- | --- | --- | --- | --- | --- |
| 2017-04-19 09:00:00 | 1.07 | 1.07 | 1.07 | 1.07 | 1413 |
| 2017-04-19 10:00:00 | 1.07 | 1.07 | 1.07 | 1.07 | 1241 |
| 2017-04-19 11:00:00 | 1.07 | 1.07 | 1.07 | 1.07 | 1025 |
| 2017-04-19 12:00:00 | 1.07 | 1.07 | 1.07 | 1.07 | 1460 |
| 2017-04-19 13:00:00 | 1.07 | 1.07 | 1.07 | 1.07 | 1554 |
| ... | ... | ... | ... | ... | ... |
| 2018-02-07 11:00:00 | 1.23 | 1.24 | 1.23 | 1.24 | 2203 |
| 2018-02-07 12:00:00 | 1.24 | 1.24 | 1.23 | 1.23 | 2325 |
| 2018-02-07 13:00:00 | 1.23 | 1.23 | 1.23 | 1.23 | 2824 |
| 2018-02-07 14:00:00 | 1.23 | 1.23 | 1.23 | 1.23 | 4065 |
| 2018-02-07 15:00:00 | 1.23 | 1.23 | 1.23 | 1.23 | 6143 |

5000 rows × 5 columns







In
[supervised machine learning](https://en.wikipedia.org/wiki/Supervised_learning),
we try to learn a function that maps input feature vectors (independent variables) into known output values (dependent variable):

$$ f\colon X \to \mathbf{y} $$

That way, provided our model function is sufficient, we can predict future output values from the newly acquired input feature vectors to some degree of certainty.
In our example, we'll try to map several price-derived features and common technical indicators to the price point two days in the future.
We construct [model design matrix](https://en.wikipedia.org/wiki/Design_matrix) $X$ below:


In [2]:
```
def BBANDS(data, n_lookback, n_std):
    """Bollinger bands indicator"""
    hlc3 = (data.High + data.Low + data.Close) / 3
    mean, std = hlc3.rolling(n_lookback).mean(), hlc3.rolling(n_lookback).std()
    upper = mean + n_std*std
    lower = mean - n_std*std
    return upper, lower


close = data.Close.values
sma10 = SMA(data.Close, 10)
sma20 = SMA(data.Close, 20)
sma50 = SMA(data.Close, 50)
sma100 = SMA(data.Close, 100)
upper, lower = BBANDS(data, 20, 2)

# Design matrix / independent features:

# Price-derived features
data['X_SMA10'] = (close - sma10) / close
data['X_SMA20'] = (close - sma20) / close
data['X_SMA50'] = (close - sma50) / close
data['X_SMA100'] = (close - sma100) / close

data['X_DELTA_SMA10'] = (sma10 - sma20) / close
data['X_DELTA_SMA20'] = (sma20 - sma50) / close
data['X_DELTA_SMA50'] = (sma50 - sma100) / close

# Indicator features
data['X_MOM'] = data.Close.pct_change(periods=2)
data['X_BB_upper'] = (upper - close) / close
data['X_BB_lower'] = (lower - close) / close
data['X_BB_width'] = (upper - lower) / close
data['X_Sentiment'] = ~data.index.to_series().between('2017-09-27', '2017-12-14')

# Some datetime features for good measure
data['X_day'] = data.index.dayofweek
data['X_hour'] = data.index.hour

data = data.dropna().astype(float)

```






Since all our indicators work only with past values, we can safely precompute the design matrix in advance. Alternatively, we would reconstruct the matrix every time before training the model.

Notice the made-up *sentiment* feature. In real life, one would obtain similar features by parsing news sources, Twitter sentiment, Stocktwits or similar.
This is just to show input data can contain all sorts of additional explanatory columns.

As mentioned, our dependent variable will be the price (return) two days in the future, simplified into values $1$ when the return is positive (and significant), $-1$ when negative, or $0$ when the return after two days is roughly around zero. Let's write some functions that return our model matrix $X$ and dependent, class variable $\mathbf{y}$ as plain NumPy arrays:


In [3]:
```
import numpy as np


def get_X(data):
    """Return model design matrix X"""
    return data.filter(like='X').values


def get_y(data):
    """Return dependent variable y"""
    y = data.Close.pct_change(48).shift(-48)  # Returns after roughly two days
    y[y.between(-.004, .004)] = 0             # Devalue returns smaller than 0.4%
    y[y > 0] = 1
    y[y < 0] = -1
    return y


def get_clean_Xy(df):
    """Return (X, y) cleaned of NaN values"""
    X = get_X(df)
    y = get_y(df).values
    isnan = np.isnan(y)
    X = X[~isnan]
    y = y[~isnan]
    return X, y

```






Let's see how our data performs modeled using a simple
[k-nearest neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
(kNN) algorithm from the state of the art
[scikit-learn](https://scikit-learn.org)
Python machine learning package.
To avoid (or at least demonstrate)
[overfitting](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html),
always split your data into *train* and *test* sets; in particular, don't validate your model performance on the same data it was built on.


In [4]:
```
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

X, y = get_clean_Xy(data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=0)

clf = KNeighborsClassifier(7)  # Model the output based on 7 "nearest" examples
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

_ = pd.DataFrame({'y_true': y_test, 'y_pred': y_pred}).plot(figsize=(15, 2), alpha=.7)
print('Classification accuracy: ', np.mean(y_test == y_pred))

```





```
Classification accuracy:  0.4210960032962505

```


![](data:image/png;base64,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%0A)





We see the forecasts are all over the place (classification accuracy 42%), but is the model of any use under real backtesting?

Let's backtest a simple strategy that buys the asset for 20% of available equity with 20:1 leverage whenever the forecast is positive (the price in two days is predicted to go up),
and sells under the same terms when the forecast is negative, all the while setting reasonable stop-loss and take-profit levels. Notice also the steady use of
[`data.df`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Strategy.data)
accessor:


In [5]:
```
%%time

from backtesting import Backtest, Strategy

N_TRAIN = 400


class MLTrainOnceStrategy(Strategy):
    price_delta = .004  # 0.4%

    def init(self):        
        # Init our model, a kNN classifier
        self.clf = KNeighborsClassifier(7)

        # Train the classifier in advance on the first N_TRAIN examples
        df = self.data.df.iloc[:N_TRAIN]
        X, y = get_clean_Xy(df)
        self.clf.fit(X, y)

        # Plot y for inspection
        self.I(get_y, self.data.df, name='y_true')

        # Prepare empty, all-NaN forecast indicator
        self.forecasts = self.I(lambda: np.repeat(np.nan, len(self.data)), name='forecast')

    def next(self):
        # Skip the training, in-sample data
        if len(self.data) < N_TRAIN:
            return

        # Proceed only with out-of-sample data. Prepare some variables
        high, low, close = self.data.High, self.data.Low, self.data.Close
        current_time = self.data.index[-1]

        # Forecast the next movement
        X = get_X(self.data.df.iloc[-1:])
        forecast = self.clf.predict(X)[0]

        # Update the plotted "forecast" indicator
        self.forecasts[-1] = forecast

        # If our forecast is upwards and we don't already hold a long position
        # place a long order for 20% of available account equity. Vice versa for short.
        # Also set target take-profit and stop-loss prices to be one price_delta
        # away from the current closing price.
        upper, lower = close[-1] * (1 + np.r_[1, -1]*self.price_delta)

        if forecast == 1 and not self.position.is_long:
            self.buy(size=.2, tp=upper, sl=lower)
        elif forecast == -1 and not self.position.is_short:
            self.sell(size=.2, tp=lower, sl=upper)

        # Additionally, set aggressive stop-loss on trades that have been open 
        # for more than two days
        for trade in self.trades:
            if current_time - trade.entry_time > pd.Timedelta('2 days'):
                if trade.is_long:
                    trade.sl = max(trade.sl, low)
                else:
                    trade.sl = min(trade.sl, high)


bt = Backtest(data, MLTrainOnceStrategy, commission=.0002, margin=.05)
bt.run()

```





```
CPU times: user 5.08 s, sys: 35.6 ms, total: 5.11 s
Wall time: 5.11 s

```


Out[5]:
```
Start                     2017-04-25 12:00:00
End                       2018-02-07 15:00:00
Duration                    288 days 03:00:00
Exposure Time [%]                       79.41
Equity Final [$]                     14165.29
Equity Peak [$]                      14979.13
Return [%]                              41.65
Buy & Hold Return [%]                   12.87
Return (Ann.) [%]                       42.86
Volatility (Ann.) [%]                   26.90
Sharpe Ratio                             1.59
Sortino Ratio                            3.59
Calmar Ratio                             4.54
Max. Drawdown [%]                       -9.44
Avg. Drawdown [%]                       -1.11
Max. Drawdown Duration       41 days 23:00:00
Avg. Drawdown Duration        2 days 15:00:00
# Trades                                  354
Win Rate [%]                            52.54
Best Trade [%]                           0.58
Worst Trade [%]                         -0.52
Avg. Trade [%]                           0.02
Max. Trade Duration           3 days 09:00:00
Avg. Trade Duration           0 days 19:00:00
Profit Factor                            1.22
Expectancy [%]                           0.02
SQN                                      1.85
_strategy                 MLTrainOnceStrategy
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```




In [6]:
```
bt.plot()

```





Out[6]:
**Row**(id = '1542', …)align = 'start',aspect\_ratio = None,background = None,children = [GridBox(id='1539', ...), ToolbarBox(id='1541', ...)],cols = 'auto',css\_classes = [],disabled = False,height = None,height\_policy = 'auto',js\_event\_callbacks = {},js\_property\_callbacks = {},margin = (0, 0, 0, 0),max\_height = None,max\_width = None,min\_height = None,min\_width = None,name = None,sizing\_mode = 'stretch\_width',spacing = 0,subscribed\_events = [],syncable = True,tags = [],visible = True,width = None,width\_policy = 'auto')





Despite our lousy win rate, the strategy seems profitable. Let's see how it performs under
[walk-forward optimization](https://en.wikipedia.org/wiki/Walk_forward_optimization),
akin to k-fold or leave-one-out
[cross-validation](https://en.wikipedia.org/wiki/Cross-validation_%28statistics%29):


In [7]:
```
%%time

class MLWalkForwardStrategy(MLTrainOnceStrategy):
    def next(self):
        # Skip the cold start period with too few values available
        if len(self.data) < N_TRAIN:
            return

        # Re-train the model only every 20 iterations.
        # Since 20 << N_TRAIN, we don't lose much in terms of
        # "recent training examples", but the speed-up is significant!
        if len(self.data) % 20:
            return super().next()

        # Retrain on last N_TRAIN values
        df = self.data.df[-N_TRAIN:]
        X, y = get_clean_Xy(df)
        self.clf.fit(X, y)

        # Now that the model is fitted, 
        # proceed the same as in MLTrainOnceStrategy
        super().next()


bt = Backtest(data, MLWalkForwardStrategy, commission=.0002, margin=.05)
bt.run()

```





```
CPU times: user 6.38 s, sys: 8.01 ms, total: 6.39 s
Wall time: 6.39 s

```


Out[7]:
```
Start                     2017-04-25 12:00:00
End                       2018-02-07 15:00:00
Duration                    288 days 03:00:00
Exposure Time [%]                       71.72
Equity Final [$]                      5885.37
Equity Peak [$]                      10052.84
Return [%]                             -41.15
Buy & Hold Return [%]                   12.87
Return (Ann.) [%]                      -41.90
Volatility (Ann.) [%]                   10.79
Sharpe Ratio                             0.00
Sortino Ratio                            0.00
Calmar Ratio                             0.00
Max. Drawdown [%]                      -41.47
Avg. Drawdown [%]                      -14.36
Max. Drawdown Duration      261 days 18:00:00
Avg. Drawdown Duration       88 days 05:00:00
# Trades                                  324
Win Rate [%]                            41.67
Best Trade [%]                           0.38
Worst Trade [%]                         -0.51
Avg. Trade [%]                          -0.05
Max. Trade Duration           3 days 07:00:00
Avg. Trade Duration           0 days 18:00:00
Profit Factor                            0.67
Expectancy [%]                          -0.05
SQN                                     -2.79
_strategy                 MLWalkForwardStr...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object
```




In [8]:
```
bt.plot()

```





Out[8]:
**Row**(id = '2475', …)align = 'start',aspect\_ratio = None,background = None,children = [GridBox(id='2472', ...), ToolbarBox(id='2474', ...)],cols = 'auto',css\_classes = [],disabled = False,height = None,height\_policy = 'auto',js\_event\_callbacks = {},js\_property\_callbacks = {},margin = (0, 0, 0, 0),max\_height = None,max\_width = None,min\_height = None,min\_width = None,name = None,sizing\_mode = 'stretch\_width',spacing = 0,subscribed\_events = [],syncable = True,tags = [],visible = True,width = None,width\_policy = 'auto')





Apparently, when repeatedly retrained on past `N_TRAIN` data points in a rolling manner, our basic model generalizes poorly and performs not quite as well.

This was a simple and contrived, tongue-in-cheek example that shows one way to use machine learning forecast models with *backtesting.py* framework.
In reality, you will need a far better feature space, better models (cf.
[deep learning](https://en.wikipedia.org/wiki/Deep_learning#Deep_neural_networks)),
and better money management strategies to achieve
[consistent profits](https://en.wikipedia.org/wiki/Day_trading#Profitability)
in automated short-term forex trading. More proper data science is an exercise for the keen reader.

Some instant optimization tips that come to mind are:

* **Data is king.** Make sure your design matrix features as best as possible model and correlate with your chosen target variable(s) and not just represent random noise.
* Instead of modelling a single target variable $y$, model a multitude of target/class variables, possibly better designed than our "48-hour returns" above.
* **Model everything:** forecast price, volume, time before it "takes off", SL/TP levels,
  [optimal position size](https://en.wikipedia.org/wiki/Kelly_criterion#Application_to_the_stock_market)
  ...
* Reduce
  [false positives](https://en.wikipedia.org/wiki/False_positive_rate)
  by increasing the conviction needed and imposing extra domain expertise and discretionary limitations before entering trades.

Also make sure to familiarize yourself with the full
[Backtesting.py API reference](https://kernc.github.io/backtesting.py/doc/backtesting/index.html#header-submodules)





---

# Parameter Heatmap & Optimization

**URL:** https://kernc.github.io/backtesting.py/doc/examples/Parameter%20Heatmap%20&%20Optimization.html


# Parameter Heatmap[¶](#Parameter-Heatmap)

This tutorial will show how to optimize strategies with multiple parameters and how to examine and reason about optimization results.
It is assumed you're already familiar with
[basic *backtesting.py* usage](https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html).

First, let's again import our helper moving average function.
In practice, one should use functions from an indicator library, such as
[TA-Lib](https://github.com/mrjbq7/ta-lib) or
[Tulipy](https://tulipindicators.org).


In [1]:
```
from backtesting.test import SMA

```





Loading BokehJS ...







Our strategy will be a similar moving average cross-over strategy to the one in
[Quick Start User Guide](https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html),
but we will use four moving averages in total:
two moving averages whose relationship determines a general trend
(we only trade long when the shorter MA is above the longer one, and vice versa),
and two moving averages whose cross-over with daily *close* prices determine the signal to enter or exit the position.


In [2]:
```
from backtesting import Strategy
from backtesting.lib import crossover


class Sma4Cross(Strategy):
    n1 = 50
    n2 = 100
    n_enter = 20
    n_exit = 10
    
    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
        self.sma_enter = self.I(SMA, self.data.Close, self.n_enter)
        self.sma_exit = self.I(SMA, self.data.Close, self.n_exit)
        
    def next(self):
        
        if not self.position:
            
            # On upwards trend, if price closes above
            # "entry" MA, go long
            
            # Here, even though the operands are arrays, this
            # works by implicitly comparing the two last values
            if self.sma1 > self.sma2:
                if crossover(self.data.Close, self.sma_enter):
                    self.buy()
                    
            # On downwards trend, if price closes below
            # "entry" MA, go short
            
            else:
                if crossover(self.sma_enter, self.data.Close):
                    self.sell()
        
        # But if we already hold a position and the price
        # closes back below (above) "exit" MA, close the position
        
        else:
            if (self.position.is_long and
                crossover(self.sma_exit, self.data.Close)
                or
                self.position.is_short and
                crossover(self.data.Close, self.sma_exit)):
                
                self.position.close()

```






It's not a robust strategy, but we can optimize it.

[Grid search](https://en.wikipedia.org/wiki/Hyperparameter_optimization#Grid_search)
is an exhaustive search through a set of specified sets of values of hyperparameters. One evaluates the performance for each set of parameters and finally selects the combination that performs best.

Let's optimize our strategy on Google stock data using *randomized* grid search over the parameter space, evaluating at most (approximately) 200 randomly chosen combinations:


In [3]:
```
%%time 

from backtesting import Backtest
from backtesting.test import GOOG


backtest = Backtest(GOOG, Sma4Cross, commission=.002)

stats, heatmap = backtest.optimize(
    n1=range(10, 110, 10),
    n2=range(20, 210, 20),
    n_enter=range(15, 35, 5),
    n_exit=range(10, 25, 5),
    constraint=lambda p: p.n_exit < p.n_enter < p.n1 < p.n2,
    maximize='Equity Final [$]',
    max_tries=200,
    random_state=0,
    return_heatmap=True)

```





```
CPU times: user 194 ms, sys: 7.79 ms, total: 202 ms
Wall time: 7.56 s

```





Notice `return_heatmap=True` parameter passed to
[`Backtest.optimize()`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Backtest.optimize).
It makes the function return a heatmap series along with the usual stats of the best run.
`heatmap` is a pandas Series indexed with a MultiIndex, a cartesian product of all permissible (tried) parameter values.
The series values are from the `maximize=` argument we provided.


In [4]:
```
heatmap

```





Out[4]:
```
n1   n2   n_enter  n_exit
20   60   15       10       10102.87
     80   15       10        9864.22
     100  15       10       11003.22
30   40   20       15       11771.29
          25       15       16178.55
                              ...   
100  200  15       10       13118.25
          20       10       11308.46
                   15       16350.94
          25       10        8991.55
          30       10        9953.07
Name: Equity Final [$], Length: 177, dtype: float64
```





This heatmap contains the results of all the runs,
making it very easy to obtain parameter combinations for e.g. three best runs:


In [5]:
```
heatmap.sort_values().iloc[-3:]

```





Out[5]:
```
n1   n2   n_enter  n_exit
100  120  15       10       18159.06
     160  20       15       19216.54
50   160  20       15       19565.69
Name: Equity Final [$], dtype: float64
```





But we use vision to make judgements on larger data sets much faster.
Let's plot the whole heatmap by projecting it on two chosen dimensions.
Say we're mostly interested in how parameters `n1` and `n2`, on average, affect the outcome.


In [6]:
```
hm = heatmap.groupby(['n1', 'n2']).mean().unstack()
hm

```





Out[6]:

| n2 | 40 | 60 | 80 | 100 | 120 | 140 | 160 | 180 | 200 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n1 |  |  |  |  |  |  |  |  |  |
| 20 | NaN | 10102.87 | 9864.22 | 11003.22 | NaN | NaN | NaN | NaN | NaN |
| 30 | 13974.92 | 11696.32 | 11757.99 | 15092.99 | 13152.24 | 11518.69 | 11271.35 | 11384.55 | 10649.05 |
| 40 | NaN | 13666.45 | NaN | 7549.10 | 10629.48 | 12860.99 | 11405.29 | 10863.81 | 10658.14 |
| 50 | NaN | 8383.46 | 10180.50 | 10563.79 | 9081.95 | 14272.27 | 13575.86 | 11383.46 | 10053.47 |
| 60 | NaN | NaN | 9232.42 | 8046.49 | 10838.45 | 12876.59 | 10312.95 | 9427.55 | 9555.40 |
| 70 | NaN | NaN | 14712.14 | 7192.89 | 10403.01 | 10065.28 | 8293.73 | 9895.78 | 9360.48 |
| 80 | NaN | NaN | NaN | 10863.11 | 7721.24 | 9139.95 | 8813.95 | 10414.66 | 8908.49 |
| 90 | NaN | NaN | NaN | 8958.14 | 9538.05 | 9884.42 | 9685.92 | 11343.64 | 8806.57 |
| 100 | NaN | NaN | NaN | NaN | 11253.16 | 7101.26 | 11323.43 | 10163.32 | 11944.46 |







Let's plot this table using the excellent [*Seaborn*](https://seaborn.pydata.org) package:


In [7]:
```
%matplotlib inline

import seaborn as sns


sns.heatmap(hm[::-1], cmap='viridis')

```





Out[7]:
```
<AxesSubplot:xlabel='n2', ylabel='n1'>
```


![](data:image/png;base64,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%0A)





We see that, on average, we obtain the highest result using trend-determining parameters `n1=40` and `n2=60`,
and it's not like other nearby combinations work similarly well — in our particular strategy, this combination really stands out.

Since our strategy contains several parameters, we might be interested in other relationships between their values.
We can use
[`backtesting.lib.plot_heatmaps()`](https://kernc.github.io/backtesting.py/doc/backtesting/lib.html#backtesting.lib.plot_heatmaps)
function to plot interactive heatmaps of all parameter combinations simultaneously.


In [8]:
```
from backtesting.lib import plot_heatmaps


plot_heatmaps(heatmap, agg='mean')

```





Out[8]:
**Column**(id = '1271', …)align = 'start',aspect\_ratio = None,background = None,children = [ToolbarBox(id='1270', ...), GridBox(id='1268', ...)],css\_classes = [],disabled = False,height = None,height\_policy = 'auto',js\_event\_callbacks = {},js\_property\_callbacks = {},margin = (0, 0, 0, 0),max\_height = None,max\_width = None,min\_height = None,min\_width = None,name = None,rows = 'auto',sizing\_mode = None,spacing = 0,subscribed\_events = [],syncable = True,tags = [],visible = True,width = None,width\_policy = 'auto')





## Model-based optimization[¶](#Model-based-optimization)

Above, we used *randomized grid search* optimization method. Any kind of grid search, however, might be computationally expensive for large data sets. In the follwing example, we will use
[*scikit-optimize*](https://scikit-optimize.github.io)
package to guide our optimization better informed using forests of decision trees.
The hyperparameter model is sequentially improved by evaluating the expensive function (the backtest) at the next best point, thereby hopefully converging to a set of optimal parameters with as few evaluations as possible.

So, with `method="skopt"`:


In [9]:
```
%%capture

! pip install scikit-optimize  # This is a run-time dependency

```





In [10]:
```
%%time

stats_skopt, heatmap, optimize_result = backtest.optimize(
    n1=[10, 100],      # Note: For method="skopt", we
    n2=[20, 200],      # only need interval end-points
    n_enter=[10, 40],
    n_exit=[10, 30],
    constraint=lambda p: p.n_exit < p.n_enter < p.n1 < p.n2,
    maximize='Equity Final [$]',
    method='skopt',
    max_tries=200,
    random_state=0,
    return_heatmap=True,
    return_optimization=True)

```





```
CPU times: user 20.2 s, sys: 84.3 ms, total: 20.3 s
Wall time: 20.3 s

```




In [11]:
```
heatmap.sort_values().iloc[-3:]

```





Out[11]:
```
n1  n2   n_enter  n_exit
35  98   28       24       28365.15
68  96   29       24       28424.02
44  134  39       27       29941.38
Name: Equity Final [$], dtype: float64
```





Notice how the optimization runs somewhat slower even though `max_tries=` is the same. But that's due to the sequential nature of the algorithm and should actually perform rather comparably even in cases of *much larger parameter spaces* where grid search would effectively blow up, but likely (hopefully) reaching a better local optimum than a randomized search would.
A note of warning, again, to take steps to avoid
[overfitting](https://en.wikipedia.org/wiki/Overfitting)
insofar as possible.

Understanding the impact of each parameter on the computed objective function is easy in two dimensions, but as the number of dimensions grows, partial dependency plots are increasingly useful.
[Plotting tools from *scikit-optimize*](https://scikit-optimize.github.io/stable/modules/plots.html)
take care of many of the more mundane things needed to make good and informative plots of the parameter space:


In [12]:
```
from skopt.plots import plot_objective

_ = plot_objective(optimize_result, n_points=10)

```





![](data:image/png;base64,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%0A)




In [13]:
```
from skopt.plots import plot_evaluations

_ = plot_evaluations(optimize_result, bins=10)

```





![](data:image/png;base64,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%0A)





Learn more by exploring further
[examples](https://kernc.github.io/backtesting.py/doc/backtesting/index.html#tutorials)
or find more framework options in the
[full API reference](https://kernc.github.io/backtesting.py/doc/backtesting/index.html#header-submodules).





---

# Multiple Time Frames

**URL:** https://kernc.github.io/backtesting.py/doc/examples/Multiple%20Time%20Frames.html


# Multiple Time Frames[¶](#Multiple-Time-Frames)

Best trading strategies that rely on technical analysis might take into account price action on multiple time frames.
This tutorial will show how to do that with *backtesting.py*, offloading most of the work to
[pandas resampling](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#resampling).
It is assumed you're already familiar with
[basic framework usage](https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html).

We will put to the test this long-only, supposed
[400%-a-year trading strategy](http://jbmarwood.com/stock-trading-strategy-300/),
which uses daily and weekly
[relative strength index](https://en.wikipedia.org/wiki/Relative_strength_index)
(RSI) values and moving averages (MA).

In practice, one should use functions from an indicator library, such as
[TA-Lib](https://github.com/mrjbq7/ta-lib) or
[Tulipy](https://tulipindicators.org),
but among us, let's introduce the two indicators we'll be using.


In [1]:
```
import pandas as pd


def SMA(array, n):
    """Simple moving average"""
    return pd.Series(array).rolling(n).mean()


def RSI(array, n):
    """Relative strength index"""
    # Approximate; good enough
    gain = pd.Series(array).diff()
    loss = gain.copy()
    gain[gain < 0] = 0
    loss[loss > 0] = 0
    rs = gain.ewm(n).mean() / loss.abs().ewm(n).mean()
    return 100 - 100 / (1 + rs)

```






The strategy roughly goes like this:

Buy a position when:

* weekly RSI(30) $\geq$ daily RSI(30) $>$ 70
* Close $>$ MA(10) $>$ MA(20) $>$ MA(50) $>$ MA(100)

Close the position when:

* Daily close is more than 2% *below* MA(10)
* 8% fixed stop loss is hit

We need to provide bars data in the *lowest time frame* (i.e. daily) and resample it to any higher time frame (i.e. weekly) that our strategy requires.


In [2]:
```
from backtesting import Strategy, Backtest
from backtesting.lib import resample_apply


class System(Strategy):
    d_rsi = 30  # Daily RSI lookback periods
    w_rsi = 30  # Weekly
    level = 70
    
    def init(self):
        # Compute moving averages the strategy demands
        self.ma10 = self.I(SMA, self.data.Close, 10)
        self.ma20 = self.I(SMA, self.data.Close, 20)
        self.ma50 = self.I(SMA, self.data.Close, 50)
        self.ma100 = self.I(SMA, self.data.Close, 100)
        
        # Compute daily RSI(30)
        self.daily_rsi = self.I(RSI, self.data.Close, self.d_rsi)
        
        # To construct weekly RSI, we can use `resample_apply()`
        # helper function from the library
        self.weekly_rsi = resample_apply(
            'W-FRI', RSI, self.data.Close, self.w_rsi)
        
        
    def next(self):
        price = self.data.Close[-1]
        
        # If we don't already have a position, and
        # if all conditions are satisfied, enter long.
        if (not self.position and
            self.daily_rsi[-1] > self.level and
            self.weekly_rsi[-1] > self.level and
            self.weekly_rsi[-1] > self.daily_rsi[-1] and
            self.ma10[-1] > self.ma20[-1] > self.ma50[-1] > self.ma100[-1] and
            price > self.ma10[-1]):
            
            # Buy at market price on next open, but do
            # set 8% fixed stop loss.
            self.buy(sl=.92 * price)
        
        # If the price closes 2% or more below 10-day MA
        # close the position, if any.
        elif price < .98 * self.ma10[-1]:
            self.position.close()

```





Loading BokehJS ...







Let's see how our strategy fares replayed on nine years of Google stock data.


In [3]:
```
from backtesting.test import GOOG

backtest = Backtest(GOOG, System, commission=.002)
backtest.run()

```





Out[3]:
```
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                        2.79
Equity Final [$]                     10017.44
Equity Peak [$]                      10978.38
Return [%]                               0.17
Buy & Hold Return [%]                  703.46
Return (Ann.) [%]                        0.02
Volatility (Ann.) [%]                    4.94
Sharpe Ratio                             0.00
Sortino Ratio                            0.01
Calmar Ratio                             0.00
Max. Drawdown [%]                      -10.01
Avg. Drawdown [%]                       -9.34
Max. Drawdown Duration     2653 days 00:00:00
Avg. Drawdown Duration     1410 days 00:00:00
# Trades                                    4
Win Rate [%]                            25.00
Best Trade [%]                           9.69
Worst Trade [%]                         -4.46
Avg. Trade [%]                           0.08
Max. Trade Duration          35 days 00:00:00
Avg. Trade Duration          21 days 00:00:00
Profit Factor                            1.11
Expectancy [%]                           0.23
SQN                                      0.01
_strategy                              System
_equity_curve                          Equ...
_trades                      Size  EntryBa...
dtype: object
```





Meager four trades in the span of nine years and with zero return? How about if we optimize the parameters a bit?


In [4]:
```
%%time

backtest.optimize(d_rsi=range(10, 35, 5),
                  w_rsi=range(10, 35, 5),
                  level=range(30, 80, 10))

```





```
CPU times: user 108 ms, sys: 12 ms, total: 120 ms
Wall time: 6.2 s

```


Out[4]:
```
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                       22.49
Equity Final [$]                     22587.83
Equity Peak [$]                      23395.59
Return [%]                             125.88
Buy & Hold Return [%]                  703.46
Return (Ann.) [%]                       10.03
Volatility (Ann.) [%]                   13.12
Sharpe Ratio                             0.76
Sortino Ratio                            1.29
Calmar Ratio                             0.53
Max. Drawdown [%]                      -18.92
Avg. Drawdown [%]                       -3.80
Max. Drawdown Duration      778 days 00:00:00
Avg. Drawdown Duration       97 days 00:00:00
# Trades                                   23
Win Rate [%]                            65.22
Best Trade [%]                          25.03
Worst Trade [%]                         -6.30
Avg. Trade [%]                           3.66
Max. Trade Duration          63 days 00:00:00
Avg. Trade Duration          29 days 00:00:00
Profit Factor                            4.98
Expectancy [%]                           3.92
SQN                                      2.61
_strategy                 System(d_rsi=30,...
_equity_curve                          Equ...
_trades                       Size  EntryB...
dtype: object
```




In [5]:
```
backtest.plot()

```





Out[5]:
**Row**(id = '1627', …)align = 'start',aspect\_ratio = None,background = None,children = [GridBox(id='1624', ...), ToolbarBox(id='1626', ...)],cols = 'auto',css\_classes = [],disabled = False,height = None,height\_policy = 'auto',js\_event\_callbacks = {},js\_property\_callbacks = {},margin = (0, 0, 0, 0),max\_height = None,max\_width = None,min\_height = None,min\_width = None,name = None,sizing\_mode = 'stretch\_width',spacing = 0,subscribed\_events = [],syncable = True,tags = [],visible = True,width = None,width\_policy = 'auto')





Better. While the strategy doesn't perform as well as simple buy & hold, it does so with significantly lower exposure (time in market).

In conclusion, to test strategies on multiple time frames, you need to pass in OHLC data in the lowest time frame, then resample it to higher time frames, apply the indicators, then resample back to the lower time frame, filling in the in-betweens.
Which is what the function [`backtesting.lib.resample_apply()`](https://kernc.github.io/backtesting.py/doc/backtesting/lib.html#backtesting.lib.resample_apply) does for you.



Learn more by exploring further
[examples](https://kernc.github.io/backtesting.py/doc/backtesting/index.html#tutorials)
or find more framework options in the
[full API reference](https://kernc.github.io/backtesting.py/doc/backtesting/index.html#header-submodules).





---

# Strategies Library

**URL:** https://kernc.github.io/backtesting.py/doc/examples/Strategies%20Library.html


# Library of Composable Base Strategies[¶](#Library-of-Composable-Base-Strategies)

This tutorial will show how to reuse composable base trading strategies that are part of *backtesting.py* software distribution.
It is, henceforth, assumed you're already familiar with
[basic package usage](https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html).

We'll extend the same moving average cross-over strategy as in
[Quick Start User Guide](https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html),
but we'll rewrite it as a vectorized signal strategy and add trailing stop-loss.

Again, we'll use our helper moving average function.


In [1]:
```
from backtesting.test import SMA

```





Loading BokehJS ...







Part of this software distribution is
[`backtesting.lib`](https://kernc.github.io/backtesting.py/doc/backtesting/lib.html)
module that contains various reusable utilities for strategy development.
Some of those utilities are composable base strategies we can extend and build upon.

We import and extend two of those strategies here:

* [`SignalStrategy`](https://kernc.github.io/backtesting.py/doc/backtesting/lib.html#backtesting.lib.SignalStrategy)
  which decides upon a single signal vector whether to buy into a position, akin to
  [vectorized backtesting](https://www.google.com/search?q=vectorized+backtesting)
  engines, and
* [`TrailingStrategy`](https://kernc.github.io/backtesting.py/doc/backtesting/lib.html#backtesting.lib.TrailingStrategy)
  which automatically trails the current price with a stop-loss order some multiple of
  [average true range](https://en.wikipedia.org/wiki/Average_true_range)
  (ATR) away.

In [2]:
```
import pandas as pd
from backtesting.lib import SignalStrategy, TrailingStrategy


class SmaCross(SignalStrategy,
               TrailingStrategy):
    n1 = 10
    n2 = 25
    
    def init(self):
        # In init() and in next() it is important to call the
        # super method to properly initialize the parent classes
        super().init()
        
        # Precompute the two moving averages
        sma1 = self.I(SMA, self.data.Close, self.n1)
        sma2 = self.I(SMA, self.data.Close, self.n2)
        
        # Where sma1 crosses sma2 upwards. Diff gives us [-1,0, *1*]
        signal = (pd.Series(sma1) > sma2).astype(int).diff().fillna(0)
        signal = signal.replace(-1, 0)  # Upwards/long only
        
        # Use 95% of available liquidity (at the time) on each order.
        # (Leaving a value of 1. would instead buy a single share.)
        entry_size = signal * .95
                
        # Set order entry sizes using the method provided by 
        # `SignalStrategy`. See the docs.
        self.set_signal(entry_size=entry_size)
        
        # Set trailing stop-loss to 2x ATR using
        # the method provided by `TrailingStrategy`
        self.set_trailing_sl(2)

```






Note, since the strategies in `lib` may require their own intialization and next-tick logic, be sure to **always call `super().init()` and `super().next()` in your overridden methods**.

Let's see how the example strategy fares on historical Google data.


In [3]:
```
from backtesting import Backtest
from backtesting.test import GOOG

bt = Backtest(GOOG, SmaCross, commission=.002)

bt.run()
bt.plot()

```





Out[3]:
**Row**(id = '1517', …)align = 'start',aspect\_ratio = None,background = None,children = [GridBox(id='1514', ...), ToolbarBox(id='1516', ...)],cols = 'auto',css\_classes = [],disabled = False,height = None,height\_policy = 'auto',js\_event\_callbacks = {},js\_property\_callbacks = {},margin = (0, 0, 0, 0),max\_height = None,max\_width = None,min\_height = None,min\_width = None,name = None,sizing\_mode = 'stretch\_width',spacing = 0,subscribed\_events = [],syncable = True,tags = [],visible = True,width = None,width\_policy = 'auto')





Notice how managing risk with a trailing stop-loss secures our gains and limits our losses.

For other strategies of the sort, and other reusable utilities in general, see
[***backtesting.lib* module reference**](https://kernc.github.io/backtesting.py/doc/backtesting/lib.html).



Learn more by exploring further
[examples](https://kernc.github.io/backtesting.py/doc/backtesting/index.html#tutorials)
or find more framework options in the
[full API reference](https://kernc.github.io/backtesting.py/doc/backtesting/index.html#header-submodules).





---

# Quick Start User Guide

**URL:** https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html


# *Backtesting.py* Quick Start User Guide[¶](#Backtesting.py-Quick-Start-User-Guide)

This tutorial shows some of the features of *backtesting.py*, a Python framework for [backtesting](https://www.investopedia.com/terms/b/backtesting.asp) trading strategies.

*Backtesting.py* is a small and lightweight, blazing fast backtesting framework that uses state-of-the-art Python structures and procedures (Python 3.6+, Pandas, NumPy, Bokeh). It has a very small and simple API that is easy to remember and quickly shape towards meaningful results. The library *doesn't* really support stock picking or trading strategies that rely on arbitrage or multi-asset portfolio rebalancing; instead, it works with an individual tradeable asset at a time and is best suited for optimizing position entrance and exit signal strategies, decisions upon values of technical indicators, and it's also a versatile interactive trade visualization and statistics tool.

## Data[¶](#Data)

*You bring your own data.* Backtesting ingests \_all kinds of
[OHLC](https://en.wikipedia.org/wiki/Open-high-low-close_chart)
data\_ (stocks, forex, futures, crypto, ...) as a
[pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/10min.html)
with columns `'Open'`, `'High'`, `'Low'`, `'Close'` and (optionally) `'Volume'`. Such data is widely obtainable (see:
[pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/),
[Quandl](https://www.quandl.com/tools/python),
[findatapy](https://github.com/cuemacro/findatapy)).
Besides these, your data frames can have *additional columns* which are accessible in your strategies in a similar manner.

DataFrame should ideally be indexed with a *datetime index* (convert it with [`pd.to_datetime()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html)), otherwise a simple range index will do.


In [1]:
```
# Example OHLC daily data for Google Inc.
from backtesting.test import GOOG

GOOG.tail()

```





Loading BokehJS ...




Out[1]:

|  | Open | High | Low | Close | Volume |
| --- | --- | --- | --- | --- | --- |
| 2013-02-25 | 802.30 | 808.41 | 790.49 | 790.77 | 2303900 |
| 2013-02-26 | 795.00 | 795.95 | 784.40 | 790.13 | 2202500 |
| 2013-02-27 | 794.80 | 804.75 | 791.11 | 799.78 | 2026100 |
| 2013-02-28 | 801.10 | 806.99 | 801.03 | 801.20 | 2265800 |
| 2013-03-01 | 797.80 | 807.14 | 796.15 | 806.19 | 2175400 |







## Strategy[¶](#Strategy)

Let's create our first strategy to backtest on these Google data, a simple [moving average (MA) cross-over strategy](https://en.wikipedia.org/wiki/Moving_average_crossover).

*Backtesting.py* doesn't ship its own set of *technical analysis indicators*. Users favoring TA should probably refer to functions from proven indicator libraries, such as
[TA-Lib](https://github.com/mrjbq7/ta-lib) or
[Tulipy](https://tulipindicators.org),
but for this example, we can define a simple helper moving average function ourselves:


In [2]:
```
import pandas as pd


def SMA(values, n):
    """
    Return simple moving average of `values`, at
    each step taking into account `n` previous values.
    """
    return pd.Series(values).rolling(n).mean()

```






A new strategy needs to extend
[`Strategy`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Strategy)
class and override its two abstract methods:
[`init()`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Strategy.init) and
[`next()`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Strategy.next).

Method `init()` is invoked before the strategy is run. Within it, one ideally precomputes in efficient, vectorized manner whatever indicators and signals the strategy depends on.

Method `next()` is then iteratively called by the
[`Backtest`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Backtest)
instance, once for each data point (data frame row), simulating the incremental availability of each new full candlestick bar.

Note, *backtesting.py* cannot make decisions / trades *within* candlesticks — any new orders are executed on the next candle's *open* (or the current candle's *close* if
[`trade_on_close=True`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Backtest.__init__)).
If you find yourself wishing to trade within candlesticks (e.g. daytrading), you instead need to begin with more fine-grained (e.g. hourly) data.


In [3]:
```
from backtesting import Strategy
from backtesting.lib import crossover


class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 10
    n2 = 20
    
    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()

```






In `init()` as well as in `next()`, the data the strategy is simulated on is available as an instance variable
[`self.data`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Strategy.data).

In `init()`, we declare and **compute indicators indirectly by wrapping them in
[`self.I()`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Strategy.I)**.
The wrapper is passed a function (our `SMA` function) along with any arguments to call it with (our *close* values and the MA lag). Indicators wrapped in this way will be automatically plotted, and their legend strings will be intelligently inferred.

In `next()`, we simply check if the faster moving average just crossed over the slower one. If it did and upwards, we close the possible short position and go long; if it did and downwards, we close the open long position and go short. Note, we don't adjust order size, so *Backtesting.py* assumes *maximal possible position*. We use
[`backtesting.lib.crossover()`](https://kernc.github.io/backtesting.py/doc/backtesting/lib.html#backtesting.lib.crossover)
function instead of writing more obscure and confusing conditions, such as:


In [4]:
```
%%script echo

    def next(self):
        if (self.sma1[-2] < self.sma2[-2] and
                self.sma1[-1] > self.sma2[-1]):
            self.position.close()
            self.buy()

        elif (self.sma1[-2] > self.sma2[-2] and    # Ugh!
              self.sma1[-1] < self.sma2[-1]):
            self.position.close()
            self.sell()

```





```


```





In `init()`, the whole series of points was available, whereas **in `next()`, the length of `self.data` and all declared indicators is adjusted** on each `next()` call so that `array[-1]` (e.g. `self.data.Close[-1]` or `self.sma1[-1]`) always contains the most recent value, `array[-2]` the previous value, etc. (ordinary Python indexing of ascending-sorted 1D arrays).

**Note**: `self.data` and any indicators wrapped with `self.I` (e.g. `self.sma1`) are NumPy arrays for performance reasons. If you prefer pandas Series or DataFrame objects, use `Strategy.data.<column>.s` or `Strategy.data.df` accessors respectively. You could also construct the series manually, e.g. `pd.Series(self.data.Close, index=self.data.index)`.

We might avoid `self.position.close()` calls if we primed the
[`Backtest`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Backtest)
instance with `Backtest(..., exclusive_orders=True)`.



## Backtesting[¶](#Backtesting)

Let's see how our strategy performs on historical Google data. The
[`Backtest`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Backtest)
instance is initialized with OHLC data and a strategy *class* (see API reference for additional options), and we begin with 10,000 units of cash and set broker's commission to realistic 0.2%.


In [5]:
```
from backtesting import Backtest

bt = Backtest(GOOG, SmaCross, cash=10_000, commission=.002)
stats = bt.run()
stats

```





Out[5]:
```
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                       97.07
Equity Final [$]                     68221.97
Equity Peak [$]                      68991.22
Return [%]                             582.22
Buy & Hold Return [%]                  703.46
Return (Ann.) [%]                       25.27
Volatility (Ann.) [%]                   38.38
Sharpe Ratio                             0.66
Sortino Ratio                            1.29
Calmar Ratio                             0.76
Max. Drawdown [%]                      -33.08
Avg. Drawdown [%]                       -5.58
Max. Drawdown Duration      688 days 00:00:00
Avg. Drawdown Duration       41 days 00:00:00
# Trades                                   94
Win Rate [%]                            54.26
Best Trade [%]                          57.12
Worst Trade [%]                        -16.63
Avg. Trade [%]                           2.07
Max. Trade Duration         121 days 00:00:00
Avg. Trade Duration          33 days 00:00:00
Profit Factor                            2.19
Expectancy [%]                           2.61
SQN                                      1.99
_strategy                            SmaCross
_equity_curve                          Equ...
_trades                       Size  EntryB...
dtype: object
```





[`Backtest.run()`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Backtest.run)
method returns a pandas Series of simulation results and statistics associated with our strategy. We see that this simple strategy makes almost 600% return in the period of 9 years, with maximum drawdown 33%, and with longest drawdown period spanning almost two years ...

[`Backtest.plot()`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Backtest.plot)
method provides the same insights in a more visual form.


In [6]:
```
bt.plot()

```





Out[6]:
**Row**(id = '1450', …)align = 'start',aspect\_ratio = None,background = None,children = [GridBox(id='1447', ...), ToolbarBox(id='1449', ...)],cols = 'auto',css\_classes = [],disabled = False,height = None,height\_policy = 'auto',js\_event\_callbacks = {},js\_property\_callbacks = {},margin = (0, 0, 0, 0),max\_height = None,max\_width = None,min\_height = None,min\_width = None,name = None,sizing\_mode = 'stretch\_width',spacing = 0,subscribed\_events = [],syncable = True,tags = [],visible = True,width = None,width\_policy = 'auto')





## Optimization[¶](#Optimization)

We hard-coded the two lag parameters (`n1` and `n2`) into our strategy above. However, the strategy may work better with 15–30 or some other cross-over. **We declared the parameters as optimizable by making them [class variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)**.

We optimize the two parameters by calling
[`Backtest.optimize()`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Backtest.optimize)
method with each parameter a keyword argument pointing to its pool of possible values to test. Parameter `n1` is tested for values in range between 5 and 30 and parameter `n2` for values between 10 and 70, respectively. Some combinations of values of the two parameters are invalid, i.e. `n1` should not be *larger than* or equal to `n2`. We limit admissible parameter combinations with an *ad hoc* constraint function, which takes in the parameters and returns `True` (i.e. admissible) whenever `n1` is less than `n2`. Additionally, we search for such parameter combination that maximizes return over the observed period. We could instead choose to optimize any other key from the returned `stats` series.


In [7]:
```
%%time

stats = bt.optimize(n1=range(5, 30, 5),
                    n2=range(10, 70, 5),
                    maximize='Equity Final [$]',
                    constraint=lambda param: param.n1 < param.n2)
stats

```





```
CPU times: user 177 ms, sys: 16.1 ms, total: 193 ms
Wall time: 2.41 s

```


Out[7]:
```
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                       99.07
Equity Final [$]                    103949.43
Equity Peak [$]                     108327.72
Return [%]                             939.49
Buy & Hold Return [%]                  703.46
Return (Ann.) [%]                       31.61
Volatility (Ann.) [%]                   44.74
Sharpe Ratio                             0.71
Sortino Ratio                            1.49
Calmar Ratio                             0.72
Max. Drawdown [%]                      -44.00
Avg. Drawdown [%]                       -6.14
Max. Drawdown Duration      690 days 00:00:00
Avg. Drawdown Duration       43 days 00:00:00
# Trades                                  153
Win Rate [%]                            51.63
Best Trade [%]                          61.56
Worst Trade [%]                        -19.78
Avg. Trade [%]                           1.55
Max. Trade Duration          83 days 00:00:00
Avg. Trade Duration          21 days 00:00:00
Profit Factor                            1.98
Expectancy [%]                           1.98
SQN                                      1.60
_strategy                 SmaCross(n1=10,n...
_equity_curve                           Eq...
_trades                        Size  Entry...
dtype: object
```





We can look into `stats['_strategy']` to access the Strategy *instance* and its optimal parameter values (10 and 15).


In [8]:
```
stats._strategy

```





Out[8]:
```
<Strategy SmaCross(n1=10,n2=15)>
```




In [9]:
```
bt.plot(plot_volume=False, plot_pl=False)

```





Out[9]:
**Row**(id = '2059', …)align = 'start',aspect\_ratio = None,background = None,children = [GridBox(id='2056', ...), ToolbarBox(id='2058', ...)],cols = 'auto',css\_classes = [],disabled = False,height = None,height\_policy = 'auto',js\_event\_callbacks = {},js\_property\_callbacks = {},margin = (0, 0, 0, 0),max\_height = None,max\_width = None,min\_height = None,min\_width = None,name = None,sizing\_mode = 'stretch\_width',spacing = 0,subscribed\_events = [],syncable = True,tags = [],visible = True,width = None,width\_policy = 'auto')





Strategy optimization managed to up its initial performance *on in-sample data* by almost 50% and even beat simple
[buy & hold](https://en.wikipedia.org/wiki/Buy_and_hold).
In real life optimization, however, do **take steps to avoid
[overfitting](https://en.wikipedia.org/wiki/Overfitting)**.



## Trade data[¶](#Trade-data)

In addition to backtest statistics returned by
[`Backtest.run()`](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html#backtesting.backtesting.Backtest.run)
shown above, you can look into *individual trade returns* and the changing *equity curve* and *drawdown* by inspecting the last few, internal keys in the result series.


In [10]:
```
stats.tail()

```





Out[10]:
```
Expectancy [%]                                                 1.98
SQN                                                            1.60
_strategy                                     SmaCross(n1=10,n2=15)
_equity_curve                   Equity  DrawdownPct DrawdownDura...
_trades                Size  EntryBar  ExitBar  EntryPrice  Exit...
dtype: object
```





The columns should be self-explanatory.


In [11]:
```
stats['_equity_curve']  # Contains equity/drawdown curves. DrawdownDuration is only defined at ends of DD periods.

```





Out[11]:

|  | Equity | DrawdownPct | DrawdownDuration |
| --- | --- | --- | --- |
| 2004-08-19 | 10000.00 | 0.00 | NaT |
| 2004-08-20 | 10000.00 | 0.00 | NaT |
| 2004-08-23 | 10000.00 | 0.00 | NaT |
| 2004-08-24 | 10000.00 | 0.00 | NaT |
| 2004-08-25 | 10000.00 | 0.00 | NaT |
| ... | ... | ... | ... |
| 2013-02-25 | 103035.53 | 0.05 | NaT |
| 2013-02-26 | 102952.33 | 0.05 | NaT |
| 2013-02-27 | 104206.83 | 0.04 | NaT |
| 2013-02-28 | 104391.43 | 0.04 | NaT |
| 2013-03-01 | 103949.43 | 0.04 | 533 days |

2148 rows × 3 columns






In [12]:
```
stats['_trades']  # Contains individual trade data

```





Out[12]:

|  | Size | EntryBar | ExitBar | EntryPrice | ExitPrice | PnL | ReturnPct | EntryTime | ExitTime | Duration |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 87 | 20 | 60 | 114.65 | 185.23 | 6140.56 | 0.62 | 2004-09-17 | 2004-11-12 | 56 days |
| 1 | -87 | 60 | 69 | 184.86 | 175.80 | 788.18 | 0.05 | 2004-11-12 | 2004-11-26 | 14 days |
| 2 | 96 | 69 | 71 | 176.15 | 180.71 | 437.61 | 0.03 | 2004-11-26 | 2004-11-30 | 4 days |
| 3 | -96 | 71 | 75 | 180.35 | 179.13 | 116.98 | 0.01 | 2004-11-30 | 2004-12-06 | 6 days |
| 4 | 97 | 75 | 82 | 179.49 | 177.99 | -145.33 | -0.01 | 2004-12-06 | 2004-12-15 | 9 days |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 148 | 139 | 2085 | 2111 | 689.16 | 735.54 | 6447.44 | 0.07 | 2012-11-29 | 2013-01-08 | 40 days |
| 149 | -139 | 2111 | 2113 | 734.07 | 742.83 | -1217.79 | -0.01 | 2013-01-08 | 2013-01-10 | 2 days |
| 150 | 136 | 2113 | 2121 | 744.32 | 735.99 | -1132.29 | -0.01 | 2013-01-10 | 2013-01-23 | 13 days |
| 151 | -136 | 2121 | 2127 | 734.52 | 750.51 | -2174.91 | -0.02 | 2013-01-23 | 2013-01-31 | 8 days |
| 152 | 130 | 2127 | 2147 | 752.01 | 797.80 | 5952.57 | 0.06 | 2013-01-31 | 2013-03-01 | 29 days |

153 rows × 10 columns







Learn more by exploring further
[examples](https://kernc.github.io/backtesting.py/doc/backtesting/index.html#tutorials)
or find more framework options in the
[full API reference](https://kernc.github.io/backtesting.py/doc/backtesting/index.html#header-submodules).





---

# backtesting.test API documentation

**URL:** https://kernc.github.io/backtesting.py/doc/backtesting/test/index.html



Data and utilities for testing.



## Global variables

`var EURUSD`

DataFrame of hourly EUR/USD forex data from April 2017 to February 2018.



`var GOOG`

DataFrame of daily NASDAQ:GOOG (Google/Alphabet) stock price data from 2004 to 2013.





## Functions

`def SMA(arr, n)`

Returns `n`-period simple moving average of array `arr`.










---

# backtesting.lib API documentation

**URL:** https://kernc.github.io/backtesting.py/doc/backtesting/lib.html



Collection of common building blocks, helper auxiliary functions and
composable strategy classes for reuse.

Intended for simple missing-link procedures, not reinventing
of better-suited, state-of-the-art, fast libraries,
such as TA-Lib, Tulipy, PyAlgoTrade, NumPy, SciPy …

Please raise ideas for additions to this collection on the [issue tracker](https://github.com/kernc/backtesting.py).



## Global variables

`var OHLCV_AGG`

Dictionary of rules for aggregating resampled OHLCV data frames,
e.g.

```
df.resample('4H', label='right').agg(OHLCV_AGG).dropna()

```


`var TRADES_AGG`

Dictionary of rules for aggregating resampled trades data,
e.g.

```
stats['_trades'].resample('1D', on='ExitTime',
                          label='right').agg(TRADES_AGG)

```




## Functions

`def barssince(condition, default=inf)`

Return the number of bars since `condition` sequence was last `True`,
or if never, return `default`.

```
>>> barssince(self.data.Close > self.data.Open)
3

```


`def compute_stats(*, stats, data, trades=None, risk_free_rate=0.0)`

(Re-)compute strategy performance metrics.

`stats` is the statistics series as returned by `[Backtest.run()](backtesting.html#backtesting.backtesting.Backtest.run "backtesting.backtesting.Backtest.run")`.
`data` is OHLC data as passed to the `[Backtest](backtesting.html#backtesting.backtesting.Backtest "backtesting.backtesting.Backtest")`
the `stats` were obtained in.
`trades` can be a dataframe subset of `stats._trades` (e.g. only long trades).
You can also tune `risk_free_rate`, used in calculation of Sharpe and Sortino ratios.

```
>>> stats = Backtest(GOOG, MyStrategy).run()
>>> only_long_trades = stats._trades[stats._trades.Size > 0]
>>> long_stats = compute_stats(stats=stats, trades=only_long_trades,
...                            data=GOOG, risk_free_rate=.02)

```


`def cross(series1, series2)`

Return `True` if `series1` and `series2` just crossed
(above or below) each other.

```
>>> cross(self.data.Close, self.sma)
True

```


`def crossover(series1, series2)`

Return `True` if `series1` just crossed over (above)
`series2`.

```
>>> crossover(self.data.Close, self.sma)
True

```


`def plot_heatmaps(heatmap, agg='max', *, ncols=3, plot_width=1200, filename='', open_browser=True)`

Plots a grid of heatmaps, one for every pair of parameters in `heatmap`.

`heatmap` is a Series as returned by
`[Backtest.optimize()](backtesting.html#backtesting.backtesting.Backtest.optimize "backtesting.backtesting.Backtest.optimize")` when its parameter
`return_heatmap=True`.

When projecting the n-dimensional heatmap onto 2D, the values are
aggregated by 'max' function by default. This can be tweaked
with `agg` parameter, which accepts any argument pandas knows
how to aggregate by.

TODO

Lay heatmaps out lower-triangular instead of in a simple grid.
Like [`skopt.plots.plot_objective()`](https://scikit-optimize.github.io/stable/modules/plots.html#plot-objective) does.



`def quantile(series, quantile=None)`

If `[quantile()](#backtesting.lib.quantile "backtesting.lib.quantile")` is `None`, return the quantile *rank* of the last
value of `series` wrt former series values.

If `[quantile()](#backtesting.lib.quantile "backtesting.lib.quantile")` is a value between 0 and 1, return the *value* of
`series` at this quantile. If used to working with percentiles, just
divide your percentile amount with 100 to obtain quantiles.

```
>>> quantile(self.data.Close[-20:], .1)
162.130
>>> quantile(self.data.Close)
0.13

```


`def random_ohlc_data(example_data, *, frac=1.0, random_state=None)`

OHLC data generator. The generated OHLC data has basic
[descriptive statistics](https://en.wikipedia.org/wiki/Descriptive_statistics)
similar to the provided `example_data`.

`frac` is a fraction of data to sample (with replacement). Values greater
than 1 result in oversampling.

Such random data can be effectively used for stress testing trading
strategy robustness, Monte Carlo simulations, significance testing, etc.

```
>>> from backtesting.test import EURUSD
>>> ohlc_generator = random_ohlc_data(EURUSD)
>>> next(ohlc_generator)  # returns new random data
...
>>> next(ohlc_generator)  # returns new random data
...

```


`def resample_apply(rule, func, series, *args, agg=None, **kwargs)`

Apply `func` (such as an indicator) to `series`, resampled to
a time frame specified by `rule`. When called from inside
`[Strategy.init()](backtesting.html#backtesting.backtesting.Strategy.init "backtesting.backtesting.Strategy.init")`,
the result (returned) series will be automatically wrapped in
`[Strategy.I()](backtesting.html#backtesting.backtesting.Strategy.I "backtesting.backtesting.Strategy.I")`
wrapper method.

`rule` is a valid [Pandas offset string](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases) indicating
a time frame to resample `series` to.

`func` is the indicator function to apply on the resampled series.

`series` is a data series (or array), such as any of the
`[Strategy.data](backtesting.html#backtesting.backtesting.Strategy.data "backtesting.backtesting.Strategy.data")` series. Due to pandas
resampling limitations, this only works when input series
has a datetime index.

`agg` is the aggregation function to use on resampled groups of data.
Valid values are anything accepted by `pandas/resample/.agg()`.
Default value for dataframe input is `[OHLCV_AGG](#backtesting.lib.OHLCV_AGG "backtesting.lib.OHLCV_AGG")` dictionary.
Default value for series input is the appropriate entry from `[OHLCV_AGG](#backtesting.lib.OHLCV_AGG "backtesting.lib.OHLCV_AGG")`
if series has a matching name, or otherwise the value `"last"`,
which is suitable for closing prices,
but you might prefer another (e.g. `"max"` for peaks, or similar).

Finally, any `*args` and `**kwargs` that are not already eaten by
implicit `[Strategy.I()](backtesting.html#backtesting.backtesting.Strategy.I "backtesting.backtesting.Strategy.I")` call
are passed to `func`.

For example, if we have a typical moving average function
`SMA(values, lookback_period)`, *hourly* data source, and need to
apply the moving average MA(10) on a *daily* time frame,
but don't want to plot the resulting indicator, we can do:

```
class System(Strategy):
    def init(self):
        self.sma = resample_apply(
            'D', SMA, self.data.Close, 10, plot=False)

```

The above short snippet is roughly equivalent to:

```
class System(Strategy):
    def init(self):
        # Strategy exposes <code>self.data</code> as raw NumPy arrays.
        # Let's convert closing prices back to pandas Series.
        close = self.data.Close.s

        # Resample to daily resolution. Aggregate groups
        # using their last value (i.e. closing price at the end
        # of the day). Notice `label='right'`. If it were set to
        # 'left' (default), the strategy would exhibit
        # look-ahead bias.
        daily = close.resample('D', label='right').agg('last')

        # We apply SMA(10) to daily close prices,
        # then reindex it back to original hourly index,
        # forward-filling the missing values in each day.
        # We make a separate function that returns the final
        # indicator array.
        def SMA(series, n):
            from backtesting.test import SMA
            return SMA(series, n).reindex(close.index).ffill()

        # The result equivalent to the short example above:
        self.sma = self.I(SMA, daily, 10, plot=False)

```




## Classes

`class SignalStrategy`

A simple helper strategy that operates on position entry/exit signals.
This makes the backtest of the strategy simulate a [vectorized backtest](https://www.google.com/search?q=vectorized+backtest).
See [tutorials](index.html#tutorials) for usage examples.

To use this helper strategy, subclass it, override its
`[Strategy.init()](backtesting.html#backtesting.backtesting.Strategy.init "backtesting.backtesting.Strategy.init")` method,
and set the signal vector by calling
`[SignalStrategy.set_signal()](#backtesting.lib.SignalStrategy.set_signal "backtesting.lib.SignalStrategy.set_signal")` method from within it.

```
class ExampleStrategy(SignalStrategy):
    def init(self):
        super().init()
        self.set_signal(sma1 > sma2, sma1 < sma2)

```

Remember to call `super().init()` and `super().next()` in your
overridden methods.

### Ancestors

* [Strategy](backtesting.html#backtesting.backtesting.Strategy "backtesting.backtesting.Strategy")

### Methods

`def set_signal(self, entry_size, exit_portion=None, *, plot=True)`

Set entry/exit signal vectors (arrays).

A long entry signal is considered present wherever `entry_size`
is greater than zero, and a short signal wherever `entry_size`
is less than zero, following `[Order.size](backtesting.html#backtesting.backtesting.Order.size "backtesting.backtesting.Order.size")` semantics.

If `exit_portion` is provided, a nonzero value closes portion the position
(see `[Trade.close()](backtesting.html#backtesting.backtesting.Trade.close "backtesting.backtesting.Trade.close")`) in the respective direction
(positive values close long trades, negative short).

If `plot` is `True`, the signal entry/exit indicators are plotted when
`[Backtest.plot()](backtesting.html#backtesting.backtesting.Backtest.plot "backtesting.backtesting.Backtest.plot")` is called.



### Inherited members

* `[Strategy](backtesting.html#backtesting.backtesting.Strategy "backtesting.backtesting.Strategy")`:
  + `[I](backtesting.html#backtesting.backtesting.Strategy.I "backtesting.backtesting.Strategy.I")`
  + `[buy](backtesting.html#backtesting.backtesting.Strategy.buy "backtesting.backtesting.Strategy.buy")`
  + `[closed_trades](backtesting.html#backtesting.backtesting.Strategy.closed_trades "backtesting.backtesting.Strategy.closed_trades")`
  + `[data](backtesting.html#backtesting.backtesting.Strategy.data "backtesting.backtesting.Strategy.data")`
  + `[equity](backtesting.html#backtesting.backtesting.Strategy.equity "backtesting.backtesting.Strategy.equity")`
  + `[init](backtesting.html#backtesting.backtesting.Strategy.init "backtesting.backtesting.Strategy.init")`
  + `[next](backtesting.html#backtesting.backtesting.Strategy.next "backtesting.backtesting.Strategy.next")`
  + `[orders](backtesting.html#backtesting.backtesting.Strategy.orders "backtesting.backtesting.Strategy.orders")`
  + `[position](backtesting.html#backtesting.backtesting.Strategy.position "backtesting.backtesting.Strategy.position")`
  + `[sell](backtesting.html#backtesting.backtesting.Strategy.sell "backtesting.backtesting.Strategy.sell")`
  + `[trades](backtesting.html#backtesting.backtesting.Strategy.trades "backtesting.backtesting.Strategy.trades")`

`class TrailingStrategy`

A strategy with automatic trailing stop-loss, trailing the current
price at distance of some multiple of average true range (ATR). Call
`[TrailingStrategy.set_trailing_sl()](#backtesting.lib.TrailingStrategy.set_trailing_sl "backtesting.lib.TrailingStrategy.set_trailing_sl")` to set said multiple
(`6` by default). See [tutorials](index.html#tutorials) for usage examples.

Remember to call `super().init()` and `super().next()` in your
overridden methods.

### Ancestors

* [Strategy](backtesting.html#backtesting.backtesting.Strategy "backtesting.backtesting.Strategy")

### Methods

`def set_atr_periods(self, periods=100)`

Set the lookback period for computing ATR. The default value
of 100 ensures a *stable* ATR.



`def set_trailing_sl(self, n_atr=6)`

Sets the future trailing stop-loss as some multiple (`n_atr`)
average true bar ranges away from the current price.



### Inherited members

* `[Strategy](backtesting.html#backtesting.backtesting.Strategy "backtesting.backtesting.Strategy")`:
  + `[I](backtesting.html#backtesting.backtesting.Strategy.I "backtesting.backtesting.Strategy.I")`
  + `[buy](backtesting.html#backtesting.backtesting.Strategy.buy "backtesting.backtesting.Strategy.buy")`
  + `[closed_trades](backtesting.html#backtesting.backtesting.Strategy.closed_trades "backtesting.backtesting.Strategy.closed_trades")`
  + `[data](backtesting.html#backtesting.backtesting.Strategy.data "backtesting.backtesting.Strategy.data")`
  + `[equity](backtesting.html#backtesting.backtesting.Strategy.equity "backtesting.backtesting.Strategy.equity")`
  + `[init](backtesting.html#backtesting.backtesting.Strategy.init "backtesting.backtesting.Strategy.init")`
  + `[next](backtesting.html#backtesting.backtesting.Strategy.next "backtesting.backtesting.Strategy.next")`
  + `[orders](backtesting.html#backtesting.backtesting.Strategy.orders "backtesting.backtesting.Strategy.orders")`
  + `[position](backtesting.html#backtesting.backtesting.Strategy.position "backtesting.backtesting.Strategy.position")`
  + `[sell](backtesting.html#backtesting.backtesting.Strategy.sell "backtesting.backtesting.Strategy.sell")`
  + `[trades](backtesting.html#backtesting.backtesting.Strategy.trades "backtesting.backtesting.Strategy.trades")`







---

# backtesting.backtesting API documentation

**URL:** https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html



Core framework data structures.
Objects from this module can also be imported from the top-level
module directly, e.g.

```
from backtesting import Backtest, Strategy

```




## Classes

`class Backtest
(data, strategy, *, cash=10000, commission=0.0, margin=1.0, trade_on_close=False, hedging=False, exclusive_orders=False)`

Backtest a particular (parameterized) strategy
on particular data.

Upon initialization, call method
`[Backtest.run()](#backtesting.backtesting.Backtest.run "backtesting.backtesting.Backtest.run")` to run a backtest
instance, or `[Backtest.optimize()](#backtesting.backtesting.Backtest.optimize "backtesting.backtesting.Backtest.optimize")` to
optimize it.

Initialize a backtest. Requires data and a strategy to test.

`data` is a `pd.DataFrame` with columns:
`Open`, `High`, `Low`, `Close`, and (optionally) `Volume`.
If any columns are missing, set them to what you have available,
e.g.

```
df['Open'] = df['High'] = df['Low'] = df['Close']

```

The passed data frame can contain additional columns that
can be used by the strategy (e.g. sentiment info).
DataFrame index can be either a datetime index (timestamps)
or a monotonic range index (i.e. a sequence of periods).

`strategy` is a `[Strategy](#backtesting.backtesting.Strategy "backtesting.backtesting.Strategy")`
*subclass* (not an instance).

`cash` is the initial cash to start with.

`commission` is the commission ratio. E.g. if your broker's commission
is 1% of trade value, set commission to `0.01`. Note, if you wish to
account for bid-ask spread, you can approximate doing so by increasing
the commission, e.g. set it to `0.0002` for commission-less forex
trading where the average spread is roughly 0.2‰ of asking price.

`margin` is the required margin (ratio) of a leveraged account.
No difference is made between initial and maintenance margins.
To run the backtest using e.g. 50:1 leverge that your broker allows,
set margin to `0.02` (1 / leverage).

If `trade_on_close` is `True`, market orders will be filled
with respect to the current bar's closing price instead of the
next bar's open.

If `hedging` is `True`, allow trades in both directions simultaneously.
If `False`, the opposite-facing orders first close existing trades in
a [FIFO](https://www.investopedia.com/terms/n/nfa-compliance-rule-2-43b.asp) manner.

If `exclusive_orders` is `True`, each new order auto-closes the previous
trade/position, making at most a single trade (long or short) in effect
at each time.

### Methods

`def optimize(self, *, maximize='SQN', method='grid', max_tries=None, constraint=None, return_heatmap=False, return_optimization=False, random_state=None, **kwargs)`

Optimize strategy parameters to an optimal combination.
Returns result `pd.Series` of the best run.

`maximize` is a string key from the
`[Backtest.run()](#backtesting.backtesting.Backtest.run "backtesting.backtesting.Backtest.run")`-returned results series,
or a function that accepts this series object and returns a number;
the higher the better. By default, the method maximizes
Van Tharp's [System Quality Number](https://google.com/search?q=System+Quality+Number).

`method` is the optimization method. Currently two methods are supported:

* `"grid"` which does an exhaustive (or randomized) search over the
  cartesian product of parameter combinations, and
* `"skopt"` which finds close-to-optimal strategy parameters using
  [model-based optimization](https://scikit-optimize.github.io/stable/auto_examples/bayesian-optimization.html), making at most `max_tries` evaluations.

`max_tries` is the maximal number of strategy runs to perform.
If `method="grid"`, this results in randomized grid search.
If `max_tries` is a floating value between (0, 1], this sets the
number of runs to approximately that fraction of full grid space.
Alternatively, if integer, it denotes the absolute maximum number
of evaluations. If unspecified (default), grid search is exhaustive,
whereas for `method="skopt"`, `max_tries` is set to 200.

`constraint` is a function that accepts a dict-like object of
parameters (with values) and returns `True` when the combination
is admissible to test with. By default, any parameters combination
is considered admissible.

If `return_heatmap` is `True`, besides returning the result
series, an additional `pd.Series` is returned with a multiindex
of all admissible parameter combinations, which can be further
inspected or projected onto 2D to plot a heatmap
(see `[plot_heatmaps()](lib.html#backtesting.lib.plot_heatmaps "backtesting.lib.plot_heatmaps")`).

If `return_optimization` is True and `method = 'skopt'`,
in addition to result series (and maybe heatmap), return raw
[`scipy.optimize.OptimizeResult`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.OptimizeResult.html) for further
inspection, e.g. with [scikit-optimize](https://scikit-optimize.github.io)
[plotting tools](https://scikit-optimize.github.io/stable/modules/plots.html).

If you want reproducible optimization results, set `random_state`
to a fixed integer random seed.

Additional keyword arguments represent strategy arguments with
list-like collections of possible values. For example, the following
code finds and returns the "best" of the 7 admissible (of the
9 possible) parameter combinations:

```
backtest.optimize(sma1=[5, 10, 15], sma2=[10, 20, 40],
                  constraint=lambda p: p.sma1 < p.sma2)

```

TODO

Improve multiprocessing/parallel execution on Windos with start method 'spawn'.



`def plot(self, *, results=None, filename=None, plot_width=None, plot_equity=True, plot_return=False, plot_pl=True, plot_volume=True, plot_drawdown=False, smooth_equity=False, relative_equity=True, superimpose=True, resample=True, reverse_indicators=False, show_legend=True, open_browser=True)`

Plot the progression of the last backtest run.

If `results` is provided, it should be a particular result
`pd.Series` such as returned by
`[Backtest.run()](#backtesting.backtesting.Backtest.run "backtesting.backtesting.Backtest.run")` or
`[Backtest.optimize()](#backtesting.backtesting.Backtest.optimize "backtesting.backtesting.Backtest.optimize")`, otherwise the last
run's results are used.

`filename` is the path to save the interactive HTML plot to.
By default, a strategy/parameter-dependent file is created in the
current working directory.

`plot_width` is the width of the plot in pixels. If None (default),
the plot is made to span 100% of browser width. The height is
currently non-adjustable.

If `plot_equity` is `True`, the resulting plot will contain
an equity (initial cash plus assets) graph section. This is the same
as `plot_return` plus initial 100%.

If `plot_return` is `True`, the resulting plot will contain
a cumulative return graph section. This is the same
as `plot_equity` minus initial 100%.

If `plot_pl` is `True`, the resulting plot will contain
a profit/loss (P/L) indicator section.

If `plot_volume` is `True`, the resulting plot will contain
a trade volume section.

If `plot_drawdown` is `True`, the resulting plot will contain
a separate drawdown graph section.

If `smooth_equity` is `True`, the equity graph will be
interpolated between fixed points at trade closing times,
unaffected by any interim asset volatility.

If `relative_equity` is `True`, scale and label equity graph axis
with return percent, not absolute cash-equivalent values.

If `superimpose` is `True`, superimpose larger-timeframe candlesticks
over the original candlestick chart. Default downsampling rule is:
monthly for daily data, daily for hourly data, hourly for minute data,
and minute for (sub-)second data.
`superimpose` can also be a valid [Pandas offset string](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects),
such as `'5T'` or `'5min'`, in which case this frequency will be
used to superimpose.
Note, this only works for data with a datetime index.

If `resample` is `True`, the OHLC data is resampled in a way that
makes the upper number of candles for Bokeh to plot limited to 10\_000.
This may, in situations of overabundant data,
improve plot's interactive performance and avoid browser's
`Javascript Error: Maximum call stack size exceeded` or similar.
Equity & dropdown curves and individual trades data is,
likewise, [reasonably *aggregated*](lib.html#backtesting.lib.TRADES_AGG).
`resample` can also be a [Pandas offset string](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects),
such as `'5T'` or `'5min'`, in which case this frequency will be
used to resample, overriding above numeric limitation.
Note, all this only works for data with a datetime index.

If `reverse_indicators` is `True`, the indicators below the OHLC chart
are plotted in reverse order of declaration.

If `show_legend` is `True`, the resulting plot graphs will contain
labeled legends.

If `open_browser` is `True`, the resulting `filename` will be
opened in the default web browser.



`def run(self, **kwargs)`

Run the backtest. Returns `pd.Series` with results and statistics.

Keyword arguments are interpreted as strategy parameters.

```
>>> Backtest(GOOG, SmaCross).run()
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                     93.9944
Equity Final [$]                      51959.9
Equity Peak [$]                       75787.4
Return [%]                            419.599
Buy & Hold Return [%]                 703.458
Return (Ann.) [%]                      21.328
Volatility (Ann.) [%]                 36.5383
Sharpe Ratio                         0.583718
Sortino Ratio                         1.09239
Calmar Ratio                         0.444518
Max. Drawdown [%]                    -47.9801
Avg. Drawdown [%]                    -5.92585
Max. Drawdown Duration      584 days 00:00:00
Avg. Drawdown Duration       41 days 00:00:00
# Trades                                   65
Win Rate [%]                          46.1538
Best Trade [%]                         53.596
Worst Trade [%]                      -18.3989
Avg. Trade [%]                        2.35371
Max. Trade Duration         183 days 00:00:00
Avg. Trade Duration          46 days 00:00:00
Profit Factor                         2.08802
Expectancy [%]                        8.79171
SQN                                  0.916893
_strategy                            SmaCross
_equity_curve                           Eq...
_trades                       Size  EntryB...
dtype: object

```




`class Order`

Place new orders through `[Strategy.buy()](#backtesting.backtesting.Strategy.buy "backtesting.backtesting.Strategy.buy")` and `[Strategy.sell()](#backtesting.backtesting.Strategy.sell "backtesting.backtesting.Strategy.sell")`.
Query existing orders through `[Strategy.orders](#backtesting.backtesting.Strategy.orders "backtesting.backtesting.Strategy.orders")`.

When an order is executed or [filled](https://www.investopedia.com/terms/f/fill.asp), it results in a `[Trade](#backtesting.backtesting.Trade "backtesting.backtesting.Trade")`.

If you wish to modify aspects of a placed but not yet filled order,
cancel it and place a new one instead.

All placed orders are [Good 'Til Canceled](https://www.investopedia.com/terms/g/gtc.asp).

### Instance variables

`var is_contingent`

True for [contingent](https://www.investopedia.com/terms/c/contingentorder.asp) orders, i.e. [OCO](https://www.investopedia.com/terms/o/oco.asp) stop-loss and take-profit bracket orders
placed upon an active trade. Remaining contingent orders are canceled when
their parent `[Trade](#backtesting.backtesting.Trade "backtesting.backtesting.Trade")` is closed.

You can modify contingent orders through `[Trade.sl](#backtesting.backtesting.Trade.sl "backtesting.backtesting.Trade.sl")` and `[Trade.tp](#backtesting.backtesting.Trade.tp "backtesting.backtesting.Trade.tp")`.



`var is_long`

True if the order is long (order size is positive).



`var is_short`

True if the order is short (order size is negative).



`var limit`

Order limit price for [limit orders](https://www.investopedia.com/terms/l/limitorder.asp), or None for [market orders](https://www.investopedia.com/terms/m/marketorder.asp),
which are filled at next available price.



`var size`

Order size (negative for short orders).

If size is a value between 0 and 1, it is interpreted as a fraction of current
available liquidity (cash plus `[Position.pl](#backtesting.backtesting.Position.pl "backtesting.backtesting.Position.pl")` minus used margin).
A value greater than or equal to 1 indicates an absolute number of units.



`var sl`

A stop-loss price at which, if set, a new contingent stop-market order
will be placed upon the `[Trade](#backtesting.backtesting.Trade "backtesting.backtesting.Trade")` following this order's execution.
See also `[Trade.sl](#backtesting.backtesting.Trade.sl "backtesting.backtesting.Trade.sl")`.



`var stop`

Order stop price for [stop-limit/stop-market](https://www.investopedia.com/terms/s/stoporder.asp) order,
otherwise None if no stop was set, or the stop price has already been hit.



`var tp`

A take-profit price at which, if set, a new contingent limit order
will be placed upon the `[Trade](#backtesting.backtesting.Trade "backtesting.backtesting.Trade")` following this order's execution.
See also `[Trade.tp](#backtesting.backtesting.Trade.tp "backtesting.backtesting.Trade.tp")`.



### Methods

`def cancel(self)`

Cancel the order.





`class Position`

Currently held asset position, available as
`[Strategy.position](#backtesting.backtesting.Strategy.position "backtesting.backtesting.Strategy.position")` within
`[Strategy.next()](#backtesting.backtesting.Strategy.next "backtesting.backtesting.Strategy.next")`.
Can be used in boolean contexts, e.g.

```
if self.position:
    ...  # we have a position, either long or short

```
### Instance variables

`var is_long`

True if the position is long (position size is positive).



`var is_short`

True if the position is short (position size is negative).



`var pl`

Profit (positive) or loss (negative) of the current position in cash units.



`var pl_pct`

Profit (positive) or loss (negative) of the current position in percent.



`var size`

Position size in units of asset. Negative if position is short.



### Methods

`def close(self, portion=1.0)`

Close portion of position by closing `portion` of each active trade. See `[Trade.close()](#backtesting.backtesting.Trade.close "backtesting.backtesting.Trade.close")`.





`class Strategy`

A trading strategy base class. Extend this class and
override methods
`[Strategy.init()](#backtesting.backtesting.Strategy.init "backtesting.backtesting.Strategy.init")` and
`[Strategy.next()](#backtesting.backtesting.Strategy.next "backtesting.backtesting.Strategy.next")` to define
your own strategy.

### Subclasses

* [SignalStrategy](lib.html#backtesting.lib.SignalStrategy "backtesting.lib.SignalStrategy")
* [TrailingStrategy](lib.html#backtesting.lib.TrailingStrategy "backtesting.lib.TrailingStrategy")

### Instance variables

`var closed_trades`

List of settled trades (see `[Trade](#backtesting.backtesting.Trade "backtesting.backtesting.Trade")`).



`var data`

Price data, roughly as passed into
`[Backtest](#backtesting.backtesting.Backtest "backtesting.backtesting.Backtest")`,
but with two significant exceptions:

* `data` is *not* a DataFrame, but a custom structure
  that serves customized numpy arrays for reasons of performance
  and convenience. Besides OHLCV columns, `.index` and length,
  it offers `.pip` property, the smallest price unit of change.
* Within `[Strategy.init()](#backtesting.backtesting.Strategy.init "backtesting.backtesting.Strategy.init")`, `data` arrays
  are available in full length, as passed into
  `[Backtest](#backtesting.backtesting.Backtest "backtesting.backtesting.Backtest")`
  (for precomputing indicators and such). However, within
  `[Strategy.next()](#backtesting.backtesting.Strategy.next "backtesting.backtesting.Strategy.next")`, `data` arrays are
  only as long as the current iteration, simulating gradual
  price point revelation. In each call of
  `[Strategy.next()](#backtesting.backtesting.Strategy.next "backtesting.backtesting.Strategy.next")` (iteratively called by
  `[Backtest](#backtesting.backtesting.Backtest "backtesting.backtesting.Backtest")` internally),
  the last array value (e.g. `data.Close[-1]`)
  is always the *most recent* value.
* If you need data arrays (e.g. `data.Close`) to be indexed
  **Pandas series**, you can call their `.s` accessor
  (e.g. `data.Close.s`). If you need the whole of data
  as a **DataFrame**, use `.df` accessor (i.e. `data.df`).


`var equity`

Current account equity (cash plus assets).



`var orders`

List of orders (see `[Order](#backtesting.backtesting.Order "backtesting.backtesting.Order")`) waiting for execution.



`var position`

Instance of `[Position](#backtesting.backtesting.Position "backtesting.backtesting.Position")`.



`var trades`

List of active trades (see `[Trade](#backtesting.backtesting.Trade "backtesting.backtesting.Trade")`).



### Methods

`def I(self, func, *args, name=None, plot=True, overlay=None, color=None, scatter=False, **kwargs)`

Declare indicator. An indicator is just an array of values,
but one that is revealed gradually in
`[Strategy.next()](#backtesting.backtesting.Strategy.next "backtesting.backtesting.Strategy.next")` much like
`[Strategy.data](#backtesting.backtesting.Strategy.data "backtesting.backtesting.Strategy.data")` is.
Returns `np.ndarray` of indicator values.

`func` is a function that returns the indicator array(s) of
same length as `[Strategy.data](#backtesting.backtesting.Strategy.data "backtesting.backtesting.Strategy.data")`.

In the plot legend, the indicator is labeled with
function name, unless `name` overrides it.

If `plot` is `True`, the indicator is plotted on the resulting
`[Backtest.plot()](#backtesting.backtesting.Backtest.plot "backtesting.backtesting.Backtest.plot")`.

If `overlay` is `True`, the indicator is plotted overlaying the
price candlestick chart (suitable e.g. for moving averages).
If `False`, the indicator is plotted standalone below the
candlestick chart. By default, a heuristic is used which decides
correctly most of the time.

`color` can be string hex RGB triplet or X11 color name.
By default, the next available color is assigned.

If `scatter` is `True`, the plotted indicator marker will be a
circle instead of a connected line segment (default).

Additional `*args` and `**kwargs` are passed to `func` and can
be used for parameters.

For example, using simple moving average function from TA-Lib:

```
def init():
    self.sma = self.I(ta.SMA, self.data.Close, self.n_sma)

```


`def buy(self, *, size=.9999, limit=None, stop=None, sl=None, tp=None)`

Place a new long order. For explanation of parameters, see `[Order](#backtesting.backtesting.Order "backtesting.backtesting.Order")` and its properties.

See also `[Strategy.sell()](#backtesting.backtesting.Strategy.sell "backtesting.backtesting.Strategy.sell")`.



`def init(self)`

Initialize the strategy.
Override this method.
Declare indicators (with `[Strategy.I()](#backtesting.backtesting.Strategy.I "backtesting.backtesting.Strategy.I")`).
Precompute what needs to be precomputed or can be precomputed
in a vectorized fashion before the strategy starts.

If you extend composable strategies from `[backtesting.lib](lib.html "backtesting.lib")`,
make sure to call:

```
super().init()

```


`def next(self)`

Main strategy runtime method, called as each new
`[Strategy.data](#backtesting.backtesting.Strategy.data "backtesting.backtesting.Strategy.data")`
instance (row; full candlestick bar) becomes available.
This is the main method where strategy decisions
upon data precomputed in `[Strategy.init()](#backtesting.backtesting.Strategy.init "backtesting.backtesting.Strategy.init")`
take place.

If you extend composable strategies from `[backtesting.lib](lib.html "backtesting.lib")`,
make sure to call:

```
super().next()

```


`def sell(self, *, size=.9999, limit=None, stop=None, sl=None, tp=None)`

Place a new short order. For explanation of parameters, see `[Order](#backtesting.backtesting.Order "backtesting.backtesting.Order")` and its properties.

See also `[Strategy.buy()](#backtesting.backtesting.Strategy.buy "backtesting.backtesting.Strategy.buy")`.





`class Trade`

When an `[Order](#backtesting.backtesting.Order "backtesting.backtesting.Order")` is filled, it results in an active `[Trade](#backtesting.backtesting.Trade "backtesting.backtesting.Trade")`.
Find active trades in `[Strategy.trades](#backtesting.backtesting.Strategy.trades "backtesting.backtesting.Strategy.trades")` and closed, settled trades in `[Strategy.closed_trades](#backtesting.backtesting.Strategy.closed_trades "backtesting.backtesting.Strategy.closed_trades")`.

### Instance variables

`var entry_bar`

Candlestick bar index of when the trade was entered.



`var entry_price`

Trade entry price.



`var entry_time`

Datetime of when the trade was entered.



`var exit_bar`

Candlestick bar index of when the trade was exited
(or None if the trade is still active).



`var exit_price`

Trade exit price (or None if the trade is still active).



`var exit_time`

Datetime of when the trade was exited.



`var is_long`

True if the trade is long (trade size is positive).



`var is_short`

True if the trade is short (trade size is negative).



`var pl`

Trade profit (positive) or loss (negative) in cash units.



`var pl_pct`

Trade profit (positive) or loss (negative) in percent.



`var size`

Trade size (volume; negative for short trades).



`var sl`

Stop-loss price at which to close the trade.

This variable is writable. By assigning it a new price value,
you create or modify the existing SL order.
By assigning it `None`, you cancel it.



`var tp`

Take-profit price at which to close the trade.

This property is writable. By assigning it a new price value,
you create or modify the existing TP order.
By assigning it `None`, you cancel it.



`var value`

Trade total value in cash (volume × price).



### Methods

`def close(self, portion=1.0)`

Place new `[Order](#backtesting.backtesting.Order "backtesting.backtesting.Order")` to close `portion` of the trade at next market price.











---

# backtesting API documentation

**URL:** https://kernc.github.io/backtesting.py/doc/backtesting/index.html



![xkcd.com/1570](https://imgs.xkcd.com/comics/engineer_syllogism.png)

## Manuals

* [**Quick Start User Guide**](../examples/Quick%20Start%20User%20Guide.html)

## Tutorials

* [Library of Utilities and Composable Base Strategies](../examples/Strategies%20Library.html)
* [Multiple Time Frames](../examples/Multiple%20Time%20Frames.html)
* [**Parameter Heatmap & Optimization**](../examples/Parameter%20Heatmap%20&%20Optimization.html)
* [Trading with Machine Learning](../examples/Trading%20with%20Machine%20Learning.html)

These tutorials are also available as live Jupyter notebooks:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kernc/backtesting.py/master?urlpath=lab%2Ftree%2Fdoc%2Fexamples%2FQuick%20Start%20User%20Guide.ipynb)
[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kernc/backtesting.py/)
  
In Colab, you might have to `!pip install backtesting`.

## Example Strategies

* (contributions welcome)

Tip

For an overview of recent changes, see
[What's New](https://github.com/kernc/backtesting.py/blob/master/CHANGELOG.md).

## FAQ

Some answers to frequent and popular questions can be found on the
[issue tracker](https://github.com/kernc/backtesting.py/issues?q=label%3Aquestion+-label%3Ainvalid)
or on the [discussion forum](https://github.com/kernc/backtesting.py/discussions) on GitHub.
Please use the search!

## License

This software is licensed under the terms of [AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.html),
meaning you can use it for any reasonable purpose and remain in
complete ownership of all the excellent trading strategies you produce,
but you are also encouraged to make sure any upgrades to *Backtesting.py*
itself find their way back to the community.

# API Reference Documentation


## Sub-modules

`[backtesting.backtesting](backtesting.html "backtesting.backtesting")`

Core framework data structures.
Objects from this module can also be imported from the top-level
module directly, e.g …



`[backtesting.lib](lib.html "backtesting.lib")`

Collection of common building blocks, helper auxiliary functions and
composable strategy classes for reuse …



`[backtesting.test](test/index.html "backtesting.test")`

Data and utilities for testing.












---

