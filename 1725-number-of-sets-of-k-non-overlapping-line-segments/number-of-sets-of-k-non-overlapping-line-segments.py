class Solution(object):

  def numberOfSets(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    MOD = 10**9 + 7
    N = n + k - 1
    R = 2 * k

    if R > N:
      return 0

    ans = 1
    for i in range(1, R + 1):
      ans = ans * (N - i + 1) // i

    return ans % MOD