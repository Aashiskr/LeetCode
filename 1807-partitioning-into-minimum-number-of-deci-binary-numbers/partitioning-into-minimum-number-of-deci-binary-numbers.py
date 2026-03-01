class Solution:
    def minPartitions(self, n: str) -> int:
        # String n mein se max digit nikal lo
        # Kyunki wahi decide karega kitne minimum numbers chahiye
        return int(max(n))