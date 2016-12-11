


import pickle
from pandas import DataFrame

# What are the maximum and minimum values taken by the "exercised_stock_options" feature used in this example?
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

df = DataFrame(data_dict)

stock_options = df.T["exercised_stock_options"]

print "Minimum \"exercised_stock_options\": ", stock_options.min()

# Now we have to clear 'NaN'
stock_options = stock_options.where(stock_options != 'NaN', 0)
print "Maximum \"exercised_stock_options\": ", stock_options.max()