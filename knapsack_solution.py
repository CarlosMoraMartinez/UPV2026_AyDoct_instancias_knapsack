import sys
import os

import numpy as np
import pandas as pd

class Knapsack:
    def __init__(self, fname):
        self.filename = fname
        self.name = os.path.basename(fname).split('.')[0]
        self.n = None 
        self.k = None
        self.values = None
        self.weights = None

        self.solution = []
        self.is_solved = False
        self.solution_weight = None
        self.solution_value = None 
        self.is_solved = False

        self.read_instance(fname)
 
        self.DP = np.zeros((self.n + 1, self.k + 1), dtype=np.int64)

    def read_instance(self, fname):
        """Lee la instancia desde un fichero."""
        
        i = 0
        with open(fname) as f:
            while True:
                line = f.readline().strip()
                if not line:
                    continue
                if self.n is None:
                    self.n = int(line)
                    self.weights = [0] * self.n
                    self.values = [0] * self.n
                    print(f"Set n={self.n}")
                elif self.k is None:
                    self.k = int(line)
                    print(f"Set k={self.k}")
                else:
                    v, w = line.split()
                    self.values[i] = int(v)
                    self.weights[i] = int(w)
                    i += 1
                if i == self.n:
                    break
    def __str__ (self):
        
        
        str2print = f"PRINTING FILE: {self.name}\nn={self.n}\nk={self.k}\n"
        for i in range(self.n):
            str2print += f"{self.values[i]}\t{self.weights[i]}\n"
        return str2print
    
    def dp2file(self):
        """Guarda la matriz de programación dinámica en un fichero TSV."""
        
        pd.DataFrame(self.DP).to_csv(f"DP_{self.name}.tsv", sep="\t", index=False)

    def reset(self):
        """Reinicia la solución y la matriz de programación dinámica."""
        
        if self.is_solved:
            self.solution = []
            self.is_solved = False
            self.solution_weight = None
            self.solution_value = None 
            self.DP = np.zeros((self.n + 1, self.k + 1), dtype=np.int64)
    def solve(self):
        """Resuelve la instancia mediante programación dinámica."""
        
        self.reset()

        for i in range(1, self.n + 1):
          for j in range(0, self.k + 1):
            if(self.weights[i-1] > j):
              self.DP[i, j] = self.DP[i-1, j]
            else:
                self.DP[i, j] = max( [self.DP[i-1, j],  
                                      self.DP[i-1, j-self.weights[i-1]] + self.values[i-1]  
                                  ])
        #vuelta atras
        i=self.n
        j=self.k
        
        while i>0 and j>0:
          if self.DP[i, j] == self.DP[i-1, j]:
              i-= 1
          else:
              self.solution.append(i)
              j-= self.weights[i-1]
              i-= 1
        self.solution.reverse()
        self.is_solved = True      
        self.solution_weight = sum([self.weights[i-1] for i in self.solution])
        self.solution_value = sum([self.values[i-1] for i in self.solution])
    def print_solution(self):
          
        strout = (f"{self.name}, n={self.n}, k={self.k}\n"
                    f"Sol weight={self.solution_weight}\nSol value={self.solution_value}\n"
        )
          
        strout +=  '\n'.join([f"{i}: v={self.values[i-1]}, w={self.weights[i-1]}" for i in self.solution])
        print(strout + '\n****\n')
        print(self.DP)
        
  


if __name__ == "__main__":
    fname = sys.argv[1]
    knap = Knapsack(fname)
    print(knap)
    knap.solve()
    knap.dp2file()
    knap.print_solution()

  
                
