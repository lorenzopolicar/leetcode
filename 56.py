class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        sort in terms of lowest start
        
        |-----|
            |-------|
                |--------------|
                    |---|
                            |-------|

        """
        res = []
        intervals.sort(key=lambda x : x[0])
        start, finish = intervals[0]
        for i in range(len(intervals)):
            current_start, current_finish = intervals[i]
            if current_start <= finish and current_finish > finish:
                finish = current_finish
            if current_start > finish:
                res.append([start, finish])
                start, finish = current_start, current_finish
        res.append([start, finish])

        return res
