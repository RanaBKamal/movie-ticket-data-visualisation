import Models.ConnectionModel as ConnectionModel
import Models.UserModel as UserModel
import Models.CustomerModel as CustomerModel

connectionObject = ConnectionModel.Connection("Database/database.db")

customerModel = CustomerModel.Customer(connectionObject)

if(customerModel.createCustomerTable()):
    print("Success creating table")
    if customerModel.insertData("Kamal N. Rana", "hello@gmail", "Male", 32):
        print("insert success")
    else:
        print("insert fail")
else:
    print("failure creating table")

connectionObject.closeConnection()
