import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pickle
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("insurance.csv")
x = df[['age']]
y = df.bought_insurance

import matplotlib.pyplot as plt

plt.scatter(x, y, color="red")
plt.xlabel("age")
plt.ylabel("yea or no")
# plt.show()

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x, y)

value = int(input("Enter age: "))
value = model.predict([[value]])[0]

print("Price is", value)

pickle.dump(model, open("Insurance.pkl", "wb"))
