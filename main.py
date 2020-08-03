import pandas as pd
import numpy as np


# This script will search in a text file for desired value and return the index
if __name__ == '__main__':
    # Input Number
    number = input("Please enter number to find: ")

    # Checking if it is a number or not
    if number.isnumeric():
        with open("Source.txt", 'r') as file:
            # Creating Dataframe from Text File
            dataframe = pd.read_fwf(file, header=None)

            # Converting Dataframe to Numpy Array
            numpy_array = np.array(dataframe)

            # Finding desired value from the array
            index = np.where(numpy_array == int(number))

            if len(index[0]) == 0:
                print("Not found!")
            else:
                # Splitting Rows and Columns
                row_index = int(index[0][0]) + 1
                col_index = int(index[1][0]) + 1

                print("Row: %d, Column: %d" % (row_index, col_index))
    else:
        print("Only number are allowed")
