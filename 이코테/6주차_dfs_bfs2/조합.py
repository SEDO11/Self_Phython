#순열

# solution 1
from typing import List

class Solution:
    def combine(self, n: List[int], k: int) -> List[List[int]]:
        results = []
        
        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
                
            for i in range(start, n+1):        
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
                    
            dfs([], 1, k)
            return results
        
import itertools
from typing import List

class Solution:
    def permute(self, n: List[int], k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))