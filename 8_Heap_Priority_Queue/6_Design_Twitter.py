class Twitter:

    def __init__(self):
        self.tweetTime = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append(self.tweetTime, tweetId)
        self.tweetTime -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        minHeap = []

        self.followMap[userId].add(userId)
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
