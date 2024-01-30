import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")

matplotlib.rcParams['figure.figsize'] = (80, 40)
sb.set(font_scale=1.)

df = pd.read_csv('ваш_файл.csv', sep=',')
df.head()
df['Year'] = pd.to_datetime(df['Year'])
df = df.set_index('Year')

# 1. način - train_test_split() funkcija koja vraća numpy nizove
# x_train, y_train, x_val, y_val = train_test_split(df['Passengers'], df['Month'], train_size=0.8, shuffle=False)

# 2.način - ekvivalentno kao i gore, samo što će nam biti lakše da radimo sa DataFrame objektom
# izdvaja prvih 80% u train_df, a preostalih 20% u val_df
dataset_split = int(len(df['summ']) * 0.8)
train_df = df[:dataset_split].copy()
val_df  =  df[dataset_split:].copy()

plt.plot(train_df['summ'], color='b', linewidth=4, alpha=0.3, label='train')
plt.plot(val_df['summ'], color='mediumblue', linewidth=4, alpha=0.3, label='val')
plt.legend()
plt.show()
train_df['log10(summ)'] = np.log10(train_df['summ'])
train_df['stationary_data'] = train_df['log10(summ)'].diff().diff()

p, d, q = 12, 2, 0
ar_model = ARIMA(train_df['log10(summ)'], order=(p, d, 0)).fit()
y_train_pred = ar_model.predict(start=2010, end=2013)

plt.plot(train_df['log10(summ)'], color='b', linewidth=4, alpha=0.3, label='train')
plt.plot(y_train_pred, color='darkorange', label='AR model prediction')
plt.title('predikcije za log10(summ)')
plt.legend()
plt.show()