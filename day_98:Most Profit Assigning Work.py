class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        n = len(difficulty)
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        total = 0
        max_profit = 0
        job_index = 0
        # print(jobs)    for understanding
        for ability in worker:
            # print(ability,worker)
            while job_index < len(jobs) and ability >= jobs[job_index][0]:
                # print(ability,"i am in while loop ",job_index)
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            total+= max_profit
        
        return total
