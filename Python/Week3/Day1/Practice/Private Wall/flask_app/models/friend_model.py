from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
import datetime

class Friend:
    def __init__(self, data):
        self.friend_id = data['friend_id']
        self.message = data['message']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_new_friend(cls,data):
        query = "insert into friends (friend_id, message, user_id) values (%(friend_id)s, %(message)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def message(cls,data):
        query = "select * from friend join user on user.id = friend;user_id where friend_id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        list_message=[]
        t = datetime.datetime.now()
        for row in result:
            row["created_at"]= t - row["created_at"]
            list_message.append(row)
        return list_message
    
    @classmethod
    def delete(cls,data):
        query = "delete from friends where friend_id = %(friend_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

