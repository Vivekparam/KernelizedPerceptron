## Digit Recognizer Kernelized Perceptron Algorithm
## Implemented by Vivek Paramasivam for CSE 446 
## University of Washington Dept of Computer Science and Engineering
## WIN 2016
import csv
from datapoint import DataPoint
import random


class DataStore:

    def __init__(self, filename=None):
        print "Reading data file: ", filename
        if filename is None:
            print "Error no file name."
            return None

        with open(filename, 'rb') as csvfile:
            spamreader = csv.reader(csvfile)
            i = 0
            self.data_points = []
            # each data point is: yval, x0, x1, x2, x3, ..., x783
            for row in spamreader:
                if i == 0:
                    # data labels
                    self.feature_names = row
                else:
                    point = DataPoint(row)
                    self.data_points.append(point) # i-1 since we start i at 1
                
                # print i, ": ", row
                i = i + 1
        print "Done reading file. There are", len(self.data_points), "data points." 

    def getFeatureNames(self):
        return self.feature_names

    def getRandomDataPoint(self):
        point = random.choice(self.data)
        print "Randomly chose: ", point
        return point

    def getDataPoint(self, n):
        return self.data_points[i]

    def getDataPoints(self):
        return self.data_points

# reader = DataStore("validation.csv")
