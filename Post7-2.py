#I.G : @deeplearningindia


"""
4x  + 3y = 20
-5x + 9y = 26
"""
import numpy as np

A = np.matrix ( [[ 4  ,3],
     [-5  ,9]] )

B = np.matrix ( [[20],
     [26]] )

X = A **(-1) * B

print(X)