# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:17:39 2023

@author: mypc
"""

import pandas as pd
import matplotlib.pyplot as plt


def lineplot(dataline, countries):
    print("Data for Line Plot")
    print(dataline)
    plt.figure(figsize=(8, 6))
    for x in countries:
        plt.plot(dataline["Year"], dataline[x], label=x)
    plt.xlim(2007, 2016)
    plt.ylim(0, 40)
    plt.xticks(dataline["Year"], labels=dataline["Year"], rotation='vertical')
    plt.xlabel("Year")
    plt.ylabel("Goods and Services export")
    plt.title("Exports of goods and services (% of GDP)")
    plt.legend()
    plt.savefig("Figure_line_Plot.png")
    plt.show()
    return





if __name__ == "__main__":

  line_data = pd.read_excel("data_line_plot.xlsx")

  lineplot(line_data, ["China", "United States", "United Kingdom", "India"])
 
