class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        n = len(tickets)
        sec= 0

        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    sec+= 1
                    if i == k and tickets[k] == 0:
                        return sec

        return sec
