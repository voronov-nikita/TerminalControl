import sqlite3 as sql
import datetime
import random


# <----------------- CONSTANTS ----------------->
LIST_WORDS:list = [chr(word) for word in range(ord("A"), ord("Z")+1)]


# <---------------- DATABASE ------------------->
class DataBase():
    def __init__(self, name_database:str):
        self.name_database:str = name_database
        self.count_accounts:int = 0
        self.new_code:str = ""
        self.len_code:int = 6
    
    
    def create_user_info(self) -> None:
        db = sql.connect(self.name_database)
        cursor = db.cursor()
        
        # create table with name: ** users **
        cursor.execute(
            """CREATE TABLE users(
                id INTEGER,
                login TEXT,
                password TEXT,
                email TEXT
                )""")
        db.commit()
        db.close()
        
    
    def add_list_games(self, game_code:str, timer:str) -> None:
        db = sql.connect(self.name_database)
        cursor = db.cursor()
        
        try:
            now = datetime.datetime.now()
            cursor.execute(
                f"""INSERT INTO InfoGames (codeId, timer, date)
                VALUES ('{game_code}', '{timer}', '{now}')"""
            )
        except:
            # create table
            cursor.execute(
            f"""CREATE TABLE InfoGames(
                codeId TEXT,
                timer TEXT,
                date TEXT
                )"""
            )
            
            now = datetime.datetime.now()
            cursor.execute(
                f"""INSERT INTO InfoGames (codeId, timer, date)
                VALUES ('{game_code}', '{timer}', '{now}')"""
            )
        
        
        db.commit()
        db.close()
        
    
    def create_new_game(self, authorID:int, authorEmail:str, timer:str) -> None:
        db = sql.connect(self.name_database)
        cursor = db.cursor()
        # generate new unique code for game
        self.new_code = self.generate_code(self.len_code)
        # create new game in database with games
        self.add_list_games(game_code=self.new_code, timer=timer)
        
        # create table with name: ** game#{self.count_games} **
        cursor.execute(
        f"""CREATE TABLE #{self.new_code}(
            userId INTEGER,
            userEmail TEXT,
            userRoule TEXT,
            isAlive INTEGER
            )"""
        )
        
        # add first user -> author
        cursor.execute(
            f"""INSERT INTO #{self.new_code} (userId, userEmail, userRoule, isAlive)
            VALUES ({authorID}, '{authorEmail}', 'None', {1})"""
        )
        
        db.commit()
        db.close()
    
    
    def creacte_new_account(self, UserData:dict) -> str:
        db = sql.connect(self.name_database)
        cursor = db.cursor()
        
        # check free login
        cursor.execute(
            f"""SELECT * FROM users WHERE login={UserData['login']}"""
        )
        check_replay = cursor.fetchone()
        if check_replay is not None:
            return "{'Failed': 'The username is already taken.}'"
        
        # check free email
        cursor.execute(
            f"""SELECT * FROM users WHERE email={UserData['email']}"""
        )
        check_replay = cursor.fetchone()
        
        if check_replay is not None:
            return "{'Failed': 'This email is already registered.}'"
        
        # else add info in database
        cursor.execute(
            f"""INSERT INTO users (id, login, password, email)
            VALUES (
            {self.count_accounts}, 
            '{UserData['login']}', 
            '{UserData['password']}', 
            '{UserData['email']}')"""
        )
        
        db.commit()
        self.count_accounts += 1
        db.close()
        return "Successfully."
    
    
    def delete_account(self, userId:int) -> str:
        db = sql.connect(self.name_database)
        cursor = db.cursor()
        
        cursor.execute(
            f"""SELECT * FROM users WHERE id={userId}"""
        )
        
        if cursor.fetchone() is not None:
            cursor.execute(
            f"""DELETE FROM users WHERE id={userId} LIMIT 1"""
        )
            
        db.commit()
        db.close()
        return "Succesfull."
        
        
    def get_user_info(self, userId:int) -> tuple:
        db = sql.connect(self.name_database)
        cursor = db.cursor()
        
        cursor.execute(
            f"""SELECT * FROM users WHERE id={userId}"""
        )
        
        user_data:tuple = cursor.fetchone()
        
        db.close()
        
        return user_data
    
    
    # generates a 'len_code'-digit code for the game
    def generate_code(self, len_code:int) -> str :
        return ''.join([random.choice(LIST_WORDS) for _ in range(len_code)])
        
