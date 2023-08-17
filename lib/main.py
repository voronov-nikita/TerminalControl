from flask import Flask, jsonify, request
from database import DataBase



# <-------------------- MAIN LOGIC OF SERVER -------------------->
app = Flask(__name__)
database = DataBase("info.db")
# create new table with data of users
database.create_user_info()



# POST: { id:value, timer: value }
@app.route('/new_account', methods=['POST'])
def create_new_account():
    post_data = request.json
    result = database.creacte_new_account(post_data)
    
    return result


# POST: { login: value, password: value, email: value}
@app.route('/new_game', methods=['POST'])
def create_new_game():
    post_data = request.json
    user_data = database.get_user_info(post_data['id'])
    database.create_new_game(user_data[0], user_data[3], post_data['timer'])
    
    return "Succesfully"



# <------------ START SERVER ---------------->
if __name__=="__main__":
    
    app.run(debug=True, host='127.0.0.1', port=5000)