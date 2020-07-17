#I.G : @deeplearningindia
"""

4x + 3y + 2z = 25
-2x + 2y + 3z = -10
3x -5y + 2z = -4

"""
import numpy as np

A = np.matrix ( [ [4, 3, 2],
				  [-2, 2, 3],
				  [3, -5, 2]  ] )

B = np.matrix ( [ [25],
    			  [-10],
    			  [-4]   ] )

X = A **(-1) * B

print(X)