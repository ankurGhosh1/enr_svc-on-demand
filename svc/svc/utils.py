from django.db import connection
from collections import namedtuple
import datetime

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

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
            user = namedtuplefetchall(cursor)
        return user

    @staticmethod
    def createUser(li):
        status = False
        query = f"EXEC dbo.addUser  @first_name='{li[0]}',@last_name='{li[1]}',@email='{li[2]}',@ContactCell='{li[3]}',@password='{li[4]}',@UserTypeId='{li[5]}',@ApplicationId='{li[6]}',@date_joined='{datetime.datetime.now()}';"
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