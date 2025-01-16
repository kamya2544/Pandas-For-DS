# JSON : Big Datasets are normally stored and extracted as JSON, Format is as object. It is just a plain text.

import pandas as pd

#loading JSON into dataframe
x = pd.read_json("data.json")
print(x.to_string())

#Dictionary as JSON if JSON code is not in a file but in a Python dictionary
data = {"Duration": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
        "Pulse": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102},
        "Maxpulse": {"0": 130, "1": 145, "2": 135, "3": 175, "4": 148, "5": 127},
        "Calories": {"0": 409.1, "1": 479, "2": 340, "3": 282.4, "4": 408, "5": 300}}

data_new = pd.DataFrame(data)
print(data_new)
