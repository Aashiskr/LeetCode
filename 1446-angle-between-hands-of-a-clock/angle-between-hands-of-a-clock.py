class Solution(object):
    def angleClock(self, hour, minutes):
        # Calculate the angle of the minute hand
        minute_angle = minutes * 6
        
        # Calculate the angle of the hour hand
        # hour % 12 ensures that 12 o'clock is treated as 0 degrees
        hour_angle = (hour % 12 * 30) + (minutes * 0.5)
        
        # Find the absolute difference between the two angles
        diff = abs(hour_angle - minute_angle)
        
        # We want the smaller angle (it can't be strictly greater than 180)
        return min(diff, 360 - diff)