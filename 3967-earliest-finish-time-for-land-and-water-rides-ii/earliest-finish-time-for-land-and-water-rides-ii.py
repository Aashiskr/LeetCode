class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        # 1. Find the earliest possible finish time for the FIRST ride in the sequence
        min_land_finish = float('inf')
        for i in range(len(landStartTime)):
            finish_time = landStartTime[i] + landDuration[i]
            if finish_time < min_land_finish:
                min_land_finish = finish_time
                
        min_water_finish = float('inf')
        for j in range(len(waterStartTime)):
            finish_time = waterStartTime[j] + waterDuration[j]
            if finish_time < min_water_finish:
                min_water_finish = finish_time

        # 2. Calculate the best total time for Land -> Water
        best_land_then_water = float('inf')
        for j in range(len(waterStartTime)):
            # Start water ride either right after the best land ride finishes, or when the water ride opens
            total_time = max(min_land_finish, waterStartTime[j]) + waterDuration[j]
            if total_time < best_land_then_water:
                best_land_then_water = total_time

        # 3. Calculate the best total time for Water -> Land
        best_water_then_land = float('inf')
        for i in range(len(landStartTime)):
            # Start land ride either right after the best water ride finishes, or when the land ride opens
            total_time = max(min_water_finish, landStartTime[i]) + landDuration[i]
            if total_time < best_water_then_land:
                best_water_then_land = total_time

        # 4. Return the absolute minimum of both strategies
        return min(best_land_then_water, best_water_then_land)