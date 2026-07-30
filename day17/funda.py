#1.empty class
class Client():
  pass

#object creation from Client class
Client_1 = Client()

#2.Adding attributes (attribute is an variable that associated with object.)
Client_1.id = "U001"
Client_1.Clientname = "tmk"

print(Client_1.id)

#3.Constructor (what should happen when our object being constructor.)
#initilising object
#Using special function __init__ (use to initilise attributes.)
class friend:
  def __init__(self,id,nickname):
    self.id = id
    self.nickname = nickname
    self.fav = 0  #default attribute

frnd_1 = friend("F001","pussy")
print(frnd_1.id , frnd_1.nickname , frnd_1.fav)


#4.Creating Method
class User:
  def __init__(self,user_id,username):
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0

  def follow(self,user):
    self.following+=1
    user.followers+=1

user_1 = User("U001","tmk")
user_2 = User("U002","rishi")

user_1.follow(user_2)
print(f"user_2 followers: {user_2.followers}")
print(f"user_1 following: {user_1.following}")

