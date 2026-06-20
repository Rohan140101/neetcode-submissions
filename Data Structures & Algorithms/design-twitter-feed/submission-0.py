from collections import deque, defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.userTweets = defaultdict(list)
        self.userFollows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(userId)
        answer = []
        minHeap = []
        self.userFollows[userId].add(userId)
        for followeeId in self.userFollows[userId]:
            # print(userId, followeeId)
            if followeeId in self.userTweets:
                index = len(self.userTweets[followeeId]) - 1
                count, tweetId = self.userTweets[followeeId][index]
                minHeap.append((count, tweetId, followeeId, index - 1))

        heapq.heapify(minHeap)

        while minHeap and len(answer) < 10:
            # print(minHeap, answer)
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            answer.append(tweetId)
            if index >= 0:
                count, tweetId = self.userTweets[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))
        return answer



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)