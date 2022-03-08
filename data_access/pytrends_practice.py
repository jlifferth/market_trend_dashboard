# import the TrendReq method from the pytrends request module
from pytrends.request import TrendReq

# execute the TrendReq method by passing the host language (hl) and timezone (tz) parameters
pytrends = TrendReq(hl='en-US', tz=360)

# build list of keywords
kw_list = ["ai", "chicken", "space"]

# build the payload
pytrends.build_payload(kw_list, timeframe='2015-01-01 2021-01-01', geo='US')

# import pandas module
import pandas as pd

# store interest over time information in df
df = pytrends.interest_over_time()

# display the top 20 rows in dataframe
print(df.head(20))


# import matplotlib plotting module to visualize data (make sure matplotlib is installed using pip)
import matplotlib.pyplot as plt

# plot all three trends in same chart
plt.figure()
plt.plot(df.index,df.ai,'k*')
plt.plot(df.index,df.chicken,'r*')
plt.plot(df.index,df.space,'b*')
plt.legend(['ai','chicken','space'])
plt.show()