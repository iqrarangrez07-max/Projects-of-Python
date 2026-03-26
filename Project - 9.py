# Prjoect - 9 Data Analysis and visualization :

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        self.data=None
        self.last_plot=None
    def __del__(self):
        print("\nExiting the program. Goodbye!")
    def load_data(self):
        path=input("Enter the path of the dataset (CSV file) : ")
        try:
            self.data=pd.read_csv(path)
            print("\nDataset loaded successfully!")
        except:
            print("Error loading dataset!\n")
    def explore_data(self):
        if self.data is None:
            print("\nLoad dataset first!")
            return
        print("\n=== Explore Data ===")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        choice=int(input("Entr your choice : "))
        if choice==1:
            print(self.data.head())
        elif choice==2:
            print(self.data.tail())
        elif choice==3:
            print(self.data.columns)
        elif choice==4:
            print(self.data.dtypes)
        elif choice==5:
            self.data.info()
    def dataframe_operations(self):
        if self.data is None:
            print("\nLoad data first!")
            return
        print("=== Dataframe Operations ===")
        print("1. Add Profit column")
        print("2. Sort by Sales")
        print("3. Filter by Region")
        choice=int(input("Enter your choice : "))
        if choice==1:
            self.data["Profit"]=self.data["Purchase_Amount"]*0.1
            print("Profit column added!")
        elif choice==2:
            print(self.data.sort_values(by="Purchase_Amount",ascending=False))
        elif choice==3:
            region=input("Enter region : ")
            print(self.data[self.data["Region"]==region])
    def handle_missing(self):
        if self.data is None:
            print("Load dataset first\n")
            return
        print("=== Handle Missing Data ===")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        choice=int(input("Enter your choice : "))
        if choice ==1:
            print(self.data[self.data.isnull().any(axis=1)])
        elif choice==2:
            self.data.fillna(self.data.mean(numeric_only=True),inplace=True)
            print("Missing values filled with mean!")
        elif choice==3:
            self.data.dropna(inplace=True)
            print("Rows dropped!")
        elif choice==4:
            value=input("Enter value : ")
            self.data.fillna(value,inplace=True)
            print("Missing values replaced!")
    def statistics(self):
        if self.data is None:
            print("Load dataset first\n")
            return
        print("\n=== Descriptive Statistics ===")
        print(self.data.describe())
    def visualize(self):
        if self.data is None:
            print("Load data first\n")
            return
        print("\n=== Data Visualization ===")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        choice=int(input("Enter your choice : "))
        if choice ==1:
            col=input("Enter column name : ")
            self.data[col].value_counts().plot(kind="bar")
            plt.title("Bar Plot")
            self.last_plot=plt
        elif choice ==2:
            col=input("Enter column name : ")
            self.data[col].plot(kind="line")
            plt.title("Line Plot")
            self.last_plot=plt
        elif choice==3:
            print("\n=== Scatter Plot ===")
            x=input("Enter x-axis column name : ")
            y=input("Enter y-axis column name : ") 
            plt.scatter(self.data[x],self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Scatter Plot")
            print("Generating scatter plot...")
            self.last_plot=plt
            print("Scatter plot displayed successfully!")
        elif choice==4:
            col=input("Enter column name : ")
            self.data[col].value_counts().plot(kind="pie",autopct="%1.1f%%")
            plt.title("Pie Chart")
            self.last_plot=plt
        elif choice==5:
            col=input("Enter column name : ")
            self.data[col].plot(kind="hist")
            plt.title("Histogram")
            self.last_plot=plt
        elif choice==6:
            cols=input("Enter columns (comma seperated) : ").split(",")
            cols=[col.strip() for col in cols]
            self.data[cols].plot.area()
            plt.title("Stack Plot")
            self.last_plot=plt
        plt.show()
    def save_plot(self):
        if self.last_plot is None:
            print("No plot available to save!\n")
            return
        print("\n=== Save Visualization ===")
        name=input("Enter file name to save the plot (eg.,plot.png) : ")
        self.last_plot.savefig(name)
        print(f"Visualization saved as {name} successfully!")
    def menu(self):
        while True:
            print("\n========== Data Analysis & Visualization Program ==========")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform Dataframe Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")
            choice=int(input("Enter your choice : "))
            if choice==1:
                self.load_data()
            elif choice==2:
                self.explore_data()
            elif choice==3:
                self.dataframe_operations()
            elif choice==4:
                self.handle_missing()
            elif choice==5:
                self.statistics()
            elif choice==6:
                self.visualize()
            elif choice==7:
                self.save_plot()
            elif choice==8:
                break
            else:
                print("Invalid choice!") 
obj=SalesDataAnalyzer()
obj.menu()       