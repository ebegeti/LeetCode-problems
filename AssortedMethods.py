import numpy as np

class AssortedMethods():
    def _init_(self,x,m,n): #where x max number, m rows and n columns
        self.x=x
        self.m=m
        self.n=n
        
    def setRandomMatrix(self,x,m,n):
        A = np.random.randint(x, size=(m, n))
        return A