import pandas as pd
import matplotlib.pyplot as plt
import random

sTime = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]
tired = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
hours = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]
device = ["Phone", "Computer", "Xbox", "Playstation", "Other"]
bTime = ["Before 8", "Between 8-9", "Between 9-10", "Between 10-11", "After 11"]
amount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

data = {
    "Screen Time": [random.choice(sTime) for _ in amount],
    "Tiredness": [random.choice(tired) for _ in amount],
    "Hours": [random.choice(hours) for _ in amount],
    "Device": [random.choice(device) for _ in amount],
    "Bed time": [random.choice(bTime) for _ in amount]
}

surveyData = pd.DataFrame(data)
print(surveyData)