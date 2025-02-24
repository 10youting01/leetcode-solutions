#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
import queue
class RecentCounter:

    def __init__(self):
        self.RecentCounter = 0
        self.q = queue.Queue()

    def ping(self, t: int) -> int:
        self.q.put(t)       
        while self.q.queue[0] < (t-3000):
            self.q.get()
        return self.q.qsize()


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

