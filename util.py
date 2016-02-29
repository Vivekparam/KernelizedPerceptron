## Utilities for digitRecognizer and perceptron
## Implemented by Vivek Paramasivam for CSE 446 
## University of Washington Dept of Computer Science and Engineering
## WIN 2016
def dot(x, y):
        s = 0
        for i in range(0, len(x)):
            s += x[i] * y[i]
        return s