from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        
        # Helper function for Disjoint Set Union (Find with path compression)
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
            
        # Helper function for Disjoint Set Union (Union)
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                
        # 1. Build the connected components based on allowed swaps
        for u, v in allowedSwaps:
            union(u, v)
            
        # 2. Group indices by their component root
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
            
        hamming_distance = 0
        
        # 3. For each component, calculate the mismatches between source and target
        for indices in components.values():
            # Count available numbers in the source for this specific component
            source_counts = Counter(source[i] for i in indices)
            
            # Try to match them with the target numbers at the same indices
            for i in indices:
                if source_counts[target[i]] > 0:
                    # We found a match, consume one occurrence
                    source_counts[target[i]] -= 1
                else:
                    # No match available, this increases our Hamming distance
                    hamming_distance += 1
                    
        return hamming_distance