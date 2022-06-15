import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x = [10,20,30]
y = [40,50,60]

df = pd.DataFrame(zip(x,y), columns=['A', 'B'])

sns.scatterplot(x='A', y = 'B', data=df)
plt.show()

