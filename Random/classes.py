class User: 
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # followers is set to a default of 0. It's being created with that default, which means we don't have to keep passing in 0 as an argument. 
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "user1")
user_2 = User("002", "user2")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)