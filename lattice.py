from collections import defaultdict
from pprint import pprint
import pandas as pd

class LatticeSquare:
    def __init__(self,n,m):

        self.neigbours2d = defaultdict(list)

        for i in range(n):
            for j in range(m):
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for direction in directions:
                    di,dj = direction
                    if  (0 <= i + di < n) and (0 <= j + dj < m):
                        self.neigbours2d[(i,j)].append((i+di,j+dj))

        self.sloop_dimension = {node:index for index, node in enumerate(self.neigbours2d)}
        self.grow_dimension = {index:node for index, node in enumerate(self.neigbours2d)}
        #
        self.neigbours = {self.sloop_dimension[key] : [self.sloop_dimension[neighbor] for neighbor in self.neigbours2d[key]]
                          for key in self.neigbours2d}

        self.adj_matrix = [[1 if neighbor in self.neigbours[index] else 0 for neighbor in range(len(self.neigbours))]
                           for index in range(len(self.neigbours))]

    def create_dataframe_for_plot(self,state,bubble_size=60):
        node2state = [(self.grow_dimension[i][0],self.grow_dimension[i][1],spin) for i,spin in enumerate(state)]
        df = pd.DataFrame(node2state, columns=['x', 'y', 'Colors'])
        df['bubble_size'] = 60
        return df





