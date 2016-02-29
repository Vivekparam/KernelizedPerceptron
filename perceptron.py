## Digit Recognizer Kernelized Perceptron Algorithm
## Implemented by Vivek Paramasivam for CSE 446 
## University of Washington Dept of Computer Science and Engineering
## WIN 2016
from __future__ import division
from datapoint import DataPoint
from numpy import sign
import sys

class KernelPerceptron:
    def __init__(self, kernel):
        self.a = [] # a
        self.kernelFunc = kernel # K
        self.numExamples = 0 # k

        self.x = [] # x examples seen so far


    # Attempts to predict the label from x. If correctly predicted, 
    # returns 0. If incorrectly predicted,
    # updates a, and returns 1.
    def addExample(self, x, label):
        self.x.append(x)
        self.numExamples += 1
        self.a.append(0) # weight for this example is currently 0

        # Assertion: len(a) == self.numExamples
        if len(self.a) != self.numExamples:
            print "ERROR: len(a) [", len(self.a), "] != self.numExamples [", self.numExamples, "]" 
            sys.exit(1)

        # Steps:
        # 1) calc sum over each data point so far
        prediction = self.predict(x)

        if prediction != label:
            # print "Prediction [", prediction,"] != label [", label ,"]. Updating \"a\""
            self.a[self.numExamples - 1] += label # update a[i] with this label
            return 1 #
        else :
            # print "Predicted correctly."
            return 0

    def kernelTransform(self, xk, x):
        return self.kernelFunc(xk, x)

    def predict(self, x):
        """Returns a prediction (-1 or 1) for x based 
        on the current weights"""
        total = 0
        for k in range(0, self.numExamples):
            if self.a[k] != 0: # no point wasting cycles if a[k] is zero
                total += self.a[k] * self.kernelTransform(self.x[k], x)
        prediction = sign(total)
        return prediction

    def predictAll(self, testPoints):
        numPoints = len(testPoints)
        numCorrect = 0
        for point in testPoints:
            label = point.getLabel()
            prediction = self.predict(point.getFeatures())
            if prediction == label: numCorrect +=1
        print "Got ", numCorrect, "/", numPoints,"correct: ", numCorrect / numPoints * 100, "% accuracy"
        return numCorrect / numPoints

    def addExamples(self, dataPoints, reportRate=100):
        """
        takes in a list of DataPoint objects and a reportRate
        dataPoints - List of DataPoint Objects to use to train this perceptron
        reportRate - number of points to pass by before reporting Loss function value
        """
        print "Reporting on Loss every", reportRate,"points."
        T = 0
        numErrors  = 0
        L_T = 0
        for dataPoint in dataPoints:
            numErrors += self.addExample(dataPoint.getFeatures(), dataPoint.getLabel())
            
            # update loss
            T += 1
            if T % reportRate == 0:
                L_T = numErrors / T
                print "L(", T,") =", L_T, "(", numErrors, "errors )"


        # print "Training complete."
        return L_T




