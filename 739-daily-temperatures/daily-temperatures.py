class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n  # Result array (default 0)
        stack = []  # Isme hum INDEX (days) store karenge
        
        # enumerate humein index (curr_day) aur value (curr_temp) dono deta hai
        for curr_day, curr_temp in enumerate(temperatures):
            
            # Jab tak stack khali nahi hai AUR aaj ka temp pichle wale se zyada hai
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()  # Pichla thanda din nikalo
                answer[prev_day] = curr_day - prev_day  # Wait time calculate karo
            
            # Aaj ka din stack mein daal do (taaki future mein isse bada mile)
            stack.append(curr_day)
            
        return answer