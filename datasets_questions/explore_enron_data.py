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
        if poi_count.get(person) == 1:
            poi_count[person] = poi_count[person] + 1
        else:
            poi_count[person] = 1

print "Number of pois: " + str(len(poi_count))

print "Total value of the stock belonging to James Prentice: " + str(enron_data['PRENTICE JAMES']['total_stock_value'])