from django.db import connection
import datetime
from .notifications import Notification

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
            user = dictfetchall(cursor)
        return user

    @staticmethod
    def getUserWithId(user_id):
        user = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getUserWithId @id='{user_id}'")
            user = dictfetchall(cursor)
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
        query = f"EXEC dbo.addUser @first_name='{li[0]}',@last_name='{li[1]}',@email='{li[2]}',@ContactCell='{li[3]}',@password='{li[4]}',@UserTypeId='{li[5]}',@ApplicationId='{li[6]}',@date_joined='{datetime.datetime.now()}';"
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
    def getChatRecord(client_id, professional_id, room_name):
        messages = []
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getChatRecord @client_id='{client_id}', @professional_id='{professional_id}', @room_name='{room_name}'")
            messages = cursor.fetchall()
        return messages

    @staticmethod
    def createChatRecord(message, client_id, professional_id, room_name, side, topic_id):
        status = False
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.createChatRecord @topic_id='{topic_id}', @time_stamp='{datetime.datetime.now()}', @client_id='{client_id}', @professional_id='{professional_id}', @message='{message}', @room_name='{room_name}', @side='{side}'")
            status = True
        return status

    @staticmethod
    def getJobById(job_id):
        status = False
        job = []
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getJobById @job_id='{job_id}'")
            job = dictfetchall(cursor)
        return job

    @staticmethod
    def createjob(TopicName, content, Category, City, User, user_email, **kwargs):
        status = False
        id = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.addJobPost @TopicName='{TopicName}', @content='{content}', @TopicDate='{datetime.datetime.now()}', @AddedDate='{datetime.datetime.now()}', @Category_id='{Category}', @City_id='{City}', @User_id='{User}', @AddedBy_id='{User}', @IsActive='True', @IsClose='False', @IsNotification='True'")
            id = cursor.execute('SELECT @@IDENTITY AS [@@IDENTITY];')
            print(id)
            id = id.fetchall()
            status = True
        if id:
            Notification.createjobNoti(user_email, content, TopicName)
        else:
            id = [[None]]
        return status, id[0][0]



    @staticmethod
    def updatejob(id=None, TopicName=None, content=None, Category=None, SubCategory=None, City=None, User=None, AddedBy=None, UpdatedBy=None, IsActive=1, CloseBy=None, IsClose=0, ForceCloseReason=None, ForceCloseCategory=None, IsNotification=1, SMSText=None, WhatsAppText=None, **kwargs):
        status = False
        closeDate = None
        closeBy_id = None
        fc_id = None
        UpdatedBy = User
        if IsNotification=='on':
            IsNotification = 1
        if IsActive=="on":
            IsActive = 1
        if IsClose:
            IsClose = 0
            closeDate = datetime.datetime.now()
            closeBy_id = User
            query = f"EXEC dbo.updateJob @id='{id}', @content='{content}', @TopicName='{TopicName}', @UpdatedDate='{datetime.datetime.now()}', @IsActive='{IsActive}', @IsClose='{IsClose}', @CloseDate='{closeDate}', @ForceCloseReason='{ForceCloseReason}', @IsNotification='{IsNotification}', @SMS='{SMSText}', @whatsApp='{WhatsAppText}', @CloseBy_id='{closeBy_id}',@UpdatedBy_id='{UpdatedBy}' "
        else:
            query = f"EXEC dbo.updateJob @id='{id}', @content='{content}', @TopicName='{TopicName}', @UpdatedDate='{datetime.datetime.now()}', @IsActive='{IsActive}', @ForceCloseReason='{ForceCloseReason}', @IsNotification='{IsNotification}', @SMS='{SMSText}', @whatsApp='{WhatsAppText}', @UpdatedBy_id='{UpdatedBy}' "
        print(id)
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status


    @staticmethod
    def getjobs():
        with connection.cursor() as cursor:
            alljobs = cursor.execute(f"EXEC dbo.getAllJobs")
        return alljobs

    # @staticmethod
    # def updateJobPost(li):
    #     with connection.cursor() as cursor:
    #         alljobs = cursor.execute(f"EXEC dbo.updateJobPost @TopicName='{li[2]}', @UpdatedDate='{datetime.datetime.now()}', @IsActive=''")
    #     return alljobs

    @staticmethod
    def boolcheck(var):
        if var == 'on':
            return 1
        else:
            return 0






    @staticmethod
    def getCountry():
        with connection.cursor() as cursor:
            country = cursor.execute(f"EXEC dbo.getCountry")
            country = dictfetchall(country)
        return country

    @staticmethod
    def getState():
        with connection.cursor() as cursor:
            state = cursor.execute(f"EXEC dbo.getState")
            state = dictfetchall(state)
        return state

    @staticmethod
    def getCity():
        with connection.cursor() as cursor:
            city = cursor.execute(f"EXEC dbo.getCity")
            city = dictfetchall(city)
        return city

    @staticmethod
    def getCityByState():
        with connection.cursor() as cursor:
            city = cursor.execute(f"EXEC dbo.getCityByState")
            city = dictfetchall(city)
        return city

    @staticmethod
    def addressAddUser(li):
        status = False
        query = f"EXEC dbo.addUserAddressList  @street='{li[0]}',@zip_code='{li[8]}',@added_date='{datetime.datetime.now()}',@user_id='{li[9]}',@city='{li[6]}', @IsActive=1;"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status

    @staticmethod
    def getAddressList():
        with connection.cursor() as cursor:
            address = cursor.execute(f"EXEC dbo.getAddressList")
            address = dictfetchall(address)
        return address

    @staticmethod
    def getProfessionalConnections(user_id):
        connections = None
        with connection.cursor() as cursor:
            cursor.execute(f'EXEC dbo.getProfessionalConnections @professinoal_id="{user_id}"')
            connections = dictfetchall(cursor)
        return connections


    @staticmethod
    def getClientConnections(user_id):
        connections = None
        with connection.cursor() as cursor:
            cursor.execute(f'EXEC dbo.getClientConnections @client_id="{user_id}"')
            connections = dictfetchall(cursor)
        return connections

    @staticmethod
    def getUserAddress(user_id):
        address = None
        with connection.cursor() as cursor:
            address = cursor.execute(f"EXEC dbo.getUserAddress @user_id='{user_id}'")
            address = dictfetchall(address)
        return address

    @staticmethod
    def getFilterJobs(city_id, cat_id, subcat_id):
        jobs = None
        with connection.cursor() as cursor:
            cursor.execute(f"EXEC dbo.getFilterJobs @city_id='{city_id}', @subcat_id='{subcat_id}', @cat_id='{cat_id}'")
            jobs = dictfetchall(cursor)
        return jobs

    @staticmethod
    def updateUser(li,user_id):
        status = False
        query = f"EXEC dbo.UpdateUser @first_name='{li[0]}',@last_name='{li[1]}',@email='{li[2]}',@ContactCell='{li[3]}',@ApplicationId='{li[4]}',@user_id='{user_id}',@street='{li[5]}',@city='{li[8]}',@zip_code='{li[9]}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status

    @staticmethod
    def userPasswordChange(password,user_id):
        status = False
        query = f"EXEC dbo.userPasswordChange @password='{password}' ,@user_id='{user_id}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status

    @staticmethod
    def getMyCityJobs(user_id):
        status = False
        query = f"EXEC dbo.getMyCityJobs @user_id='{user_id}';"
        nearJobs = None
        with connection.cursor() as cursor:
            nearJobs = cursor.execute(query)
            nearJobs = dictfetchall(nearJobs)
        return nearJobs

    @staticmethod
    def getMyCityJobsP(user_id):
        status = False
        query = f"EXEC dbo.getMyCityJobsP @user_id='{user_id}';"
        nearJobs = None
        with connection.cursor() as cursor:
            nearJobs = cursor.execute(query)
            nearJobs = dictfetchall(nearJobs)
        return nearJobs

    @staticmethod
    def generateOTP(otp,email):
        status = False
        query = f"EXEC dbo.generateOTP @Otp='{otp}' ,@user_email='{email}' ,@expire_minute='{10}' ,@doc='{datetime.datetime.now()}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status

    @staticmethod
    def applyJob(user_id, job_id):
        status = False
        query = f"EXEC dbo.applyJob @user_id='{user_id}' ,@job_id='{job_id}' , @topic_date='{datetime.datetime.now()}';"
        job = AllProcedures.getJobById(job_id)[0]
        print(job)
        user = AllProcedures.getUserWithId(job['AddedBy_id'])[0]
        print(user)
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        if status:
            Notification.appliedOnJob(user['username'], job['TopicName'])
        return status


    def addCatInCity(cat_id, city_id):
        status = False
        query = f"EXEC dbo.addCatInCity @cat_id='{cat_id}' ,@city_id='{city_id}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        return status

    def jobHireStatus(user_id, job_id):
        status = False
        query = f"EXEC dbo.jobHireStatus @user_id='{user_id}' ,@job_id='{job_id}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = cursor.fetchall()
        return status[0][0]

    def hireProfessional(user_id, job_id):
        status = False
        query = f"EXEC dbo.hireProfessional @user_id='{user_id}' ,@job_id='{job_id}';"
        job = AllProcedures.getJobById(job_id)[0]
        user = AllProcedures.getUserWithId(user_id)[0]
        with connection.cursor() as cursor:
            cursor.execute(query)
            status = True
        if status:
            Notification.hiredNoti(user['username'], job['TopicName'], job_id)
        return status

    def getApplicationsForReview(user_id):
        jobsList = []
        query = f"EXEC dbo.getApplicationsForReview @user_id='{user_id}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            jobsList = dictfetchall(cursor)
        return jobsList


    def getHiredJobsList(user_id):
        jobsList = []
        query = f"EXEC dbo.getHiredJobsList @user_id='{user_id}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            jobsList = dictfetchall(cursor)
        res = []
        for i in jobsList:
            res.append(i['Topic_id'])
        return res


    def getAppliedJobsList(user_id):
        jobsList = []
        query = f"EXEC dbo.getAppliedJobsList @user_id='{user_id}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            jobsList = dictfetchall(cursor)
        res = []
        for i in jobsList:
            res.append(i['Topic_id'])
        ids = str(res).replace("[", "").replace("]", "")
        query = f"EXEC dbo.getJobsInId @job_id_list='{ids}';"
        with connection.cursor() as cursor:
            cursor.execute(query)
            jobsList = dictfetchall(cursor)
        print(jobsList)
        return res, jobsList



class FastProcedures:
    @staticmethod
    def execute_query(query):
        with connection.cursor() as cursor:
            cursor.execute(query)
        return True

    @staticmethod
    def subcat_query_add(topic_id, subcat_id):
        return f"EXEC dbo.createTopicSubCat @TopidId='{topic_id}', @subCatId='{subcat_id}';"

    @staticmethod
    def asset_query_add(file_name, file_ext, added_date, updated_date, addedby_id, topic_id, updatedby_id):
        return f"EXEC dbo.createTopicAsset @file_name='{file_name}', @file_ext='{file_ext}', @added_date='{added_date}', @updated_date='{updated_date}', @addedby_id='{addedby_id}', @topic_id='{topic_id}', @updatedby_id='{updatedby_id}';"
