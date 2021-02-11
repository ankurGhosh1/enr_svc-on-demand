from django.db import connection
import datetime

class AllProcedures:

    @staticmethod
    def getUserWithEmail(email):
        user = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getUser @email='{email}'")
            user = cursor.fetchone()
        return user

    @staticmethod
    def getUserWithId(user_id):
        user = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getUserWithId @id='{user_id}'")
            user = cursor.fetchone()
        return user

    @staticmethod
    def getUserType(id):
        type = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getUserType @id='{id}'")
            type = cursor.fetchone()
        return type

    @staticmethod
    def createUser(li):
        status = False
        query = f"EXEC dbo.addUser  @first_name='{li[0]}',@last_name='{li[1]}',@email='{li[2]}',@ContactCell='{li[3]}',@password='{li[4]}',@UserTypeId='{li[5]}',@ApplicationId='{li[6]}',@date_joined='{datetime.datetime.now()}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status


    @staticmethod
    def createUserWithType(li):
        status = False
        query = f"EXEC dbo.addUserWithType  @first_name='{li[0]}',@last_name='{li[1]}',@email='{li[2]}',@ContactCell='{li[3]}',@password='{li[4]}',@UserType='{li[5]}',@ApplicationId='{li[6]}',@date_joined='{datetime.datetime.now()}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status

    @staticmethod
    def getChatRecord(client_id, professional_id):
        messages = []
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getChatRecord @client_id='{client_id}', @professional_id='{professional_id}'")
            messages = cursor.fetchall()
        return messages

    @staticmethod
    def createChatRecord(message, client_id, professional_id, room_name, side):
        status = False
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.createChatRecord @time_stamp='{datetime.datetime.now()}', @client_id='{client_id}', @professional_id='{professional_id}', @message='{message}', @room_name='{room_name}', @side='{side}'")
            status = True
        return status