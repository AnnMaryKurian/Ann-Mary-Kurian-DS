# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:17:39 2023

@author: mypc
"""

import pandas as pd
import matplotlib.pyplot as plt


'''
function named lineplot is defined for creating the line graph.
arguments such as line_data and an array of countries that passed from function call are
received here as dataline and countries and used for fetching data required for plotting
line graph
'''


def lineplot(dataline, countries):
    print("\n Data for Line Plot \n")
    print(dataline)

    # creating figure and setting the figure size
    plt.figure(figsize = (8, 6))

    # Using a for loop the data for each row and column is ploted
    for cntry in countries:
        plt.plot(dataline["Year"], dataline[cntry], label=cntry)

    # limits for x axis and y axis are given
    plt.xlim(2007, 2016)
    plt.ylim(0, 40)
    plt.xticks(dataline["Year"], labels=dataline["Year"], rotation='vertical')

    # labelling the x, y axis and title of the graph
    plt.xlabel("Year")
    plt.ylabel("Goods and Services export")
    plt.title("Exports of goods and services (% of GDP)")

    #code for creating legend
    plt.legend()

    # saving the figure of lineplot as png
    plt.savefig("Figure_line_Plot.png")
    plt.show()
    return  # return statement should be the finishing statement of a function


'''
function named piechart is defined for creating pie chart 
argument named pie_data is passed from the function call are received here as datapie.
The data fetched from the arguments are used for creating pie chart
'''


def piechart(datapie):
    print("\n Data for Pie Chart \n")
    print(datapie)

    # creating the pie chart
    plt.figure()
    plt.pie(datapie["2016"], labels=datapie["Country"])
    plt.title("Access to Electricity in 2016")  # given title of the figure
    plt.savefig("Figure_Pie_Chart.png")  # saving the figure of pie chart
    plt.show()
    return


'''
function named barplot is used to create bar graph.
argument is passed from function call as bar_data and   received  here as databar.
data from databar is fetched to plot bar graph
'''


def barplot(databar):
    print("\n Data for Bar Graph \n")
    print(databar)

    #creating new figure and figure size is set
    plt.figure(figsize = (8, 6))

    # data for each row and coloumn are fetched and plotted
    plt.bar(databar["Year"], databar["South Sudan"], label="South Sudan")
    plt.title("Access to electricity (% of population)")
    plt.xticks(databar["Year"], labels=databar["Year"], rotation='vertical')

    # labelling x and y axis
    plt.xlabel("Year")
    plt.ylabel("Electricity Access")
    plt.legend()

    # saving the figure as png
    plt.savefig("Figure_Bar_Graph.png")
    plt.show()
    return


'''
main function is the function where a program starts its working
Program execution starts from main function
'''


if __name__ == "__main__":

    
  '''
  The following three variables are used to store the data read from the 
  excel data sources for Line Plot, Pie Chart and Bar Graph.
  '''


  line_data = pd.read_excel("data_line_plot.xlsx")
  pie_data = pd.read_excel("data_pie_chart.xlsx")
  bar_data = pd.read_excel("data_bar_graph.xlsx")


  # calling lineplot function.Data source and an array is passed as arguments
  lineplot(line_data, ["China", "United States", "United Kingdom", "India"])


  # calling piechart function along with data source as argument
  piechart(pie_data)


  # calling barplot function along with its data source as argument
  barplot(bar_data)

