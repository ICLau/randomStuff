# This needs an account for plot.ly
import matplotlib.pyplot as plt
import plotly.plotly as py

dictionary = plt.figure()

D = {u'Label0':26, u'Label1': 17, u'Label2':30}

plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), D.keys())

plot_url = py.plot_mpl(dictionary, filename='mpl-dictionary')