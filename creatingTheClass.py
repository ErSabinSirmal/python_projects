class Car:
    def __init__(self, user_id,username):
        self.id = user_id
        self.username = username
        #default attribute
        self.followers = 0 
        self.following = 0
    def follow(self, user):
        user.followers +=1 
        self.following +=1
        user.username = "rabin"   
 
              
user_1 = Car("001","sabin")
user_2 = Car("002","haris")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
print(user_2.username)
# print(user_1.followers)
# user_2 = Car()
