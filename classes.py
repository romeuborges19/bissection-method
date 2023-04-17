import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class BissectionMethod():
    def __init__(self, function):
        self.f = lambda x: eval(function)
        self.table = []
        self.valx = []

    def printFunction(self, x):
        print(self.f(x))

    def bissect(self, a, b, stop, n=1):
        if n == 1 and self.f(a)*self.f(b) >= 0:
            print("Invalid interval")
        else:
            middle = (a+b)/2
            self.valx.append(middle)
            param = 10**(-stop)
            
            if n-2 in range(len(self.valx)):
                epsilon = abs(self.valx[n-1] - self.valx[n-2])
                self.table.append([n, '{:.5f}'.format(a), 
                                  '{:.5f}'.format(b), 
                                  '{:.5f}'.format(middle), 
                                  '{:.5f}'.format(self.f(middle)), 
                                  '{:.5f}'.format(epsilon)])
                if epsilon < param:
                    return middle, "approximate root"
            else:
                self.table.append([n, a, b, middle, self.f(middle), '--'])
            
            if self.f(middle) == 0:
                return middle, "exact root"
            
            if self.f(a)*self.f(middle) < 0:
                return self.bissect(a, middle, stop, n+1)
            else:
                return self.bissect(middle, b, stop, n+1)
        
    def printTable(self):
        df = pd.DataFrame(columns=['n', 'An', 'Bn', 'Xn', 'f(Xn)', 'E'], 
                          data=self.table)
        print(df.to_string(index=False))

    def plotGraph(self, a, b):
        x = np.linspace(a, b, num=100)
        y = np.array(self.f(x))
        plt.figure()
        plt.grid()
        plt.plot(x, y)

        cont = 0
        for x in self.valx:
            plt.plot(x, self.f(x), 'ro')
            name='$x_' + str(cont) + '$'
            plt.text(x,0.8*self.f(x),name,fontsize=12)
            cont=cont+1

        plt.show()


