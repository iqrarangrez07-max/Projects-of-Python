# Prjoect - 8 Numpy Analyzer :

import numpy as np
class DataAnalytics:
    def __init__(self):
        self.array=None
    def create_array(self):
        print("\n1. 1D Array \n2. 2D Array \n3. 3D Array")
        choice=int(input("Enter choice : "))
        if choice==1:
            elements=list(map(int,input("Enter elements : ").split()))
            self.array=np.array(elements)
        elif choice==2:
            r=int(input("Enter the number of rows : "))
            c=int(input("Enter the number of columns : "))
            elements=list(map(int,input("Enter elements : ").split()))
            self.array=np.array(elements).reshape(r,c)
        print("Array Created : \n", self.array)
        while True:
            print("\n Choose an operation : ")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            ch=int(input("Enter choice : "))
            if ch==1:
                if self.array.ndim==1:
                    i=int(input("Enter index : "))
                    print("Element :", self.array[i])
                else:
                    i=int(input("Enter roe index : "))
                    j=int(input("Enter column index :"))
                    print("Element : ", self.array[i][j])
            elif ch==2:
                r=input("Enter row range (start:end) : ")
                c=input("Enter column range (start:end) : ")
                row_slice=slice(*map(int,r.split(':')))
                col_slice=slice(*map(int,c.split(':')))
                print("Sliced Array :\n", self.array[row_slice,col_slice])
            elif ch==3:
                break
            else :
                print("Invalid choice!")
    def math_operations(self):
            print("\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
            ch=int(input("Enter choice : "))
            elements=list(map(int, input("Enter second array : ").split()))
            arr2=np.array(elements).reshape(self.array.shape)
            if ch==1:
                print("Result :\n", self.array+arr2)
            elif ch==2:
                print("\nResult :\n ", self.array-arr2)
            elif ch==3:
                print("\nResult : ", self.array*arr2)
            elif ch==4:
                print("\nResult : ", self.array/arr2)
    def combine_split(self):
            print("\n1. Combine Arrays \n2. Split Arrays")
            ch=int(input("Enter choice : "))
            if ch==1:
                elements=list(map(int, input("Enter second array : ").split()))
                arr2=np.array(elements).reshape(self.array.shape)
                combined=np.vstack((self.array,arr2))
                print("Combined Array :\n", combined)
            elif ch==2:
                split=np.array_split(self.array,2)
                print("Split Arrays : ")
                for s in split:
                    print(s)
    def search_sort_filter(self):
            print("\n1. Search a value \n2. Sort the array \n3. Filter values")
            ch=int(input("Enter choice : "))
            if ch==1:
                val=int(input("Enter value : "))
                print("Position : ", np.where(self.array==val))
            elif ch==2:
                print("Sorted Array :\n", np.sort(self.array))
            elif ch==3:
                val=int(input("Show values greater than : "))
                print("Filtered :\n", self.array[self.array>val])
    def statistics(self):
            print("\n1. Sum \n2. Mean \n3. Median \n4. Standard Deviation \n5. Variance \n6. Min \n7. Max")
            ch=int(input("Enter choice : "))
            if ch==1:
                print("Sum :", np.sum(self.array))
            elif ch==2:
                print("Mean :", np.mean(self.array))
            elif ch==3:
                print("Median :", np.median(self.array))
            elif ch==4:
                print("Standard Deviation :", np.std(self.array))
            elif ch==5:
                print("Variance :", np.var(self.array))
            elif ch==6:
                print("Minimum :", np.min(self.array))
            elif ch==7:
                print("Maximum :", np.max(self.array))
obj=DataAnalytics()
while True:
    print("\n===== Numpy Analyzer =====")
    print()
    print("Choose an option : ")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        obj.create_array()
    elif choice==2:
        obj.math_operations()
    elif choice==3:
        obj.combine_split()
    elif choice==4:
        obj.search_sort_filter()
    elif choice==5:
        obj.statistics()
    elif choice==6:
        print("Thank You! Goodbye!")
        break
    else:
        print("Invalid choice!")