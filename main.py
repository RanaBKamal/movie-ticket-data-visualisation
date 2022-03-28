import Models.ConnectionModel as ConnectionModel
import Models.UserModel as UserModel

connectionObject = ConnectionModel.Connection("Database/database.db")
userModel = UserModel.User(connectionObject)

if(userModel.dropUserTable()):
    print("Success creating table")
else:
    print("failure creating table")
