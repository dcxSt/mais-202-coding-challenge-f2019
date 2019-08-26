#!/home/steve/anaconda3/bin/python3

# import statements
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd


def load_data():
    # returns dictionaries with the home ownership and the useful data by client id
    with open('home_ownership_data.csv') as f:
        raw_home = [row for row in csv.reader(f)]
        home_dic = {}
        for i in raw_home[1:]: home_dic[int(i[0])] = i[1]
    with open('loan_data.csv') as f:
        raw_loan = [row for row in csv.reader(f)]
        amnt_dic = {}
        for i in raw_loan[1:]: amnt_dic[int(i[0])] = int(i[1])
    return home_dic,amnt_dic

def main():
    # load and parse the data sets, returns two dictionaries with the essential info
    home_dic,amnt_dic = load_data()
    
    # create a list where each entry is the tuple ('status',loan_amnt)
    try: amt_status = [[home_dic[i],amnt_dic[i]] for i in home_dic]
    except: 
        print("Something went wrong, perhaps the member ids don t match...")
        raise Exception

    # determines the average loan amount for each of the home ownership statuses
    # perhaps not most efficient, but it's concise to write...
    status_own = [i[1] for i in amt_status if i[0]=="OWN"]
    status_rent = [i[1] for i in amt_status if i[0]=="RENT"]
    status_mortgage = [i[1] for i in amt_status if i[0]=="MORTGAGE"]
    
    means = [np.mean(status_own),np.mean(status_rent),np.mean(status_mortgage)]

    # plot the graphs
    fig = plt.figure(figsize=(6,6))
    plt.bar(np.arange(3),means,align='center',color='r')

    plt.xticks(np.arange(3),("OWN","RENT","MORTGAGE"))
    plt.ylabel("mean loans ($)")
    plt.title("Mean loan amounts per ownership status")
    for counter,value in enumerate(means):
        plt.text(counter - 0.5,value + 30, str(value),color='blue',fontweight='bold')

    plt.savefig("means per ownership bar plot.png")
    plt.show()


# call the main method which generates the graph
main()
