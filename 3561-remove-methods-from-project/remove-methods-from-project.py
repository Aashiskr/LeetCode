class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Build the adjacency list for the graph
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 2: Use BFS to find all suspicious methods starting from k
        suspicious = set([k])
        queue = [k]
        
        for node in queue:
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        can_remove = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                can_remove = False
                break
                
        # Step 4: Return the result based on the condition
        if can_remove:
            return [i for i in range(n) if i not in suspicious]
        else:
            return list(range(n))