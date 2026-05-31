class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        # Sort the asteroids from smallest to largest
        asteroids.sort()
        
        # Iterate through the sorted asteroids
        for asteroid in asteroids:
            if mass >= asteroid:
                # The planet is large enough, so it absorbs the asteroid
                mass += asteroid
            else:
                # The planet is too small and is destroyed
                return False
                
        # If we made it through all asteroids, return True
        return True