#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Size of dataset: " + str(len(enron_data))
print "Number of features: " + str(len(enron_data.itervalues().next()))

poi_count = {}
for person in enron_data:
    if enron_data[person]['poi']:
        if person in poi_count:
            poi_count[person] += 1
        else:
            poi_count[person] = 1

print "Number of pois: " + str(len(poi_count))

print "Total value of the stock belonging to James Prentice: " + str(enron_data['PRENTICE JAMES']['total_stock_value'])

colwell = enron_data['COLWELL WESLEY'] 
print "Email messages from Wesley Colwell to POIs: " + str(colwell['from_this_person_to_poi'])

skilling = enron_data['SKILLING JEFFREY K']
print "Stock options exercised by Jeffrey K Skilling: " + str(skilling['exercised_stock_options'])

from pandas import DataFrame

df = DataFrame(enron_data)
sfl_total_payments_series = df[['SKILLING JEFFREY K', 'FASTOW ANDREW S', 'LAY KENNETH L']].ix['total_payments']
print sfl_total_payments_series.idxmax() + " took the most money home: " + str(sfl_total_payments_series.max())

print "Known salaries: " + str(df.T.loc[df.T['salary'] != 'NaN']['salary'].count())
print "Known email addresses: " + str(df.T.loc[df.T['email_address'] != 'NaN']['email_address'].count())
