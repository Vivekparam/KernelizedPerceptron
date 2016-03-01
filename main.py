## Digit Recognizer Kernelized Perceptron Algorithm
## Implemented by Vivek Paramasivam for CSE 446 
## University of Washington Dept of Computer Science and Engineering
## WIN 2016
from __future__ import division
from datapoint import DataPoint
from reader import DataStore
from perceptron import KernelPerceptron
from util import *
from math import sqrt, exp

## Def kernels:

def basicKernel(u, v):
    return dot(u, v) + 1

def polynomialKernel(u, v, d):
    return basicKernel(u, v) ** d

def exponentialKernel(u, v):
    differenceList = []
    for i in range(0, len(u)):
        differenceList.append(u[i] - v[i])

    magnitude = 0
    for elm in differenceList:
        magnitude += elm ** 2
    magnitude = sqrt(magnitude)

    window_size = 10

    power = - magnitude / (2 * window_size **2)
    # print "Mag:",magnitude,"power",power
    return exp(power)

def q1():
    print "**********************"
    print "***** QUESTION 1 *****"
    kernel = basicKernel

    # read data:
    reader = DataStore("validation.csv")

    # train data
    print "*** Training perceptron with Basic Kernel"
    perceptron = KernelPerceptron(kernel)
    perceptron.addExamples(reader.getDataPoints())

    # # test data
    # testSet = "test.csv"
    # testReader = DataStore(testSet)
    # print "Using trained perceptron to predict data from", testSet
    # perceptron.predictAll(testReader.getDataPoints())

def q2():
    print "**********************"
    print "***** QUESTION 2 *****"
    # read data:
    reader = DataStore("validation.csv")

    # train data on different kernels
    d = [1, 3, 5, 7, 10, 15, 20]
    for dim in d:
        # we make a modified kernelFunc for each one
        def kernelFunc(u, v):
            return polynomialKernel(u, v, dim)
        print "*** Training perceptron w/ Poly Kernel d =", dim
        thisPerceptron = KernelPerceptron(kernelFunc)
        thisPerceptron.addExamples(reader.getDataPoints(), 1000)

def q3():
    print "**********************"
    print "***** QUESTION 3 *****"
    # read data:
    reader = DataStore("test.csv")

    ## Compute Loss every 100 points on best kernel from w2
    d = 5 # best loss from q2
    def kernelFunc(u, v):
            return polynomialKernel(u, v, d)
    print "*** Training perceptron w/ Poly Kernel d =", d
    thisPerceptron = KernelPerceptron(kernelFunc)
    thisPerceptron.addExamples(reader.getDataPoints())

    ## Compute Loss every 100 points on Exponential Kernel
    kernel = exponentialKernel

    print "*** Training perceptron w/ Exponential Kernel"
    thisPerceptron = KernelPerceptron(kernel)
    thisPerceptron.addExamples(reader.getDataPoints())

if __name__ == "__main__":
    q1()
    q2()
    q3()
    print "**********************"
    print "ALL QUESTIONS COMPLETE"



