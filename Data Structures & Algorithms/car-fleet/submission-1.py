class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speeds = {position[i] : speed[i] for i in range(len(position))}
        position.sort(reverse=True)
        times = {p : (target-p)/speeds[p] for p in position}
        count = 1
        keys = list(times.keys())
        for index, pos in enumerate(keys):
            if index == 0:
                continue
            else:
                if times[pos] > times[keys[index-1]]:
                    count += 1
                else: 
                    times[pos] = times[keys[index-1]]
        return count