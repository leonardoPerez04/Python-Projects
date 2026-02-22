#Creacion de clases en Python
class User:
    #Constructor:
    def __init__(self,id,username):
        print("new user being create...")
        self.id = id
        self.username = username
        self.followers = 0  #podemos inicializar atributos sin tener que pasarlos como parametros al constructor
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following += 1
new_User_1 = User("001","drumboy")
new_User_2 = User("002","ferr.ly04")
# print(f"Id: {new_User.id} Username: {new_User.username}")
# print(f"Followers: {new_User.followers}")
new_User_1.follow(new_User_2)
new_User_2.follow(new_User_1)
print(f"Followers User: {new_User_1.username}: Followers: {new_User_1.followers} and Following: {new_User_1.following}")
print(f"Followers User: {new_User_2.username}: Followers: {new_User_2.followers} and Following: {new_User_2.following}")