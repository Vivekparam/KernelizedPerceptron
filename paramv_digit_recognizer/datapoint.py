## Digit Recognizer Kernelized Perceptron Algorithm
## Implemented by Vivek Paramasivam for CSE 446 
## University of Washington Dept of Computer Science and Engineering
## WIN 2016
class DataPoint:
    def __init__(self, datarow):
        # takes a row of data from csvfile: yval, x0, x1, x2, x3, ..., x783
        self.label = int(datarow[0]) # -1 or 1
        self.data = [int(x) for x in datarow[1:len(datarow)]]
        # print "Data row length is ", len(self.data)

    def getLabel(self):
        return self.label

    def getFeatures(self):
        return self.data
    
    def getFeatureNum(self, n):
        return self.data[n]