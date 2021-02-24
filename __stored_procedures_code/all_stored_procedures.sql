USE [baghiService]
GO
CREATE PROCEDURE dbo.allUserTypeExceptMe @userId integer(30) = NULL, @userType nvarchar(30) = NULL
AS
SELECT [id]
      ,[username]
      ,[first_name]
      ,[last_name] FROM [dbo].[clients_user] WHERE (id<>@userId AND is_staff=0 AND usertype=@userType)
GO


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[addUser]
	@first_name nvarchar(30) = NULL,
	@last_name nvarchar(30) = NULL,
	@email nvarchar(100) = NULL,
	@ContactCell nvarchar(100) = NULL,
	@password nvarchar(128) = NULL,
	@UserTypeId int = NULL,
	@ApplicationId int = NULL,
	@is_su bit = 0,
	@is_staff bit = 0,
	@is_active bit = 1,
	@date_joined datetime2(7) = NULL
AS
INSERT INTO [dbo].[accounts_userlist]
           ([username]
		   ,[first_name]
           ,[last_name]
           ,[email]
           ,[ContactCell]
		   ,[password]
           ,[UserType_id]
           ,[Application_id]
           ,[is_superuser]
           ,[is_staff]
           ,[is_active]
		   ,[date_joined])
VALUES
	(
		@email,
		@first_name,
		@last_name,
		@email,
		@ContactCell,
		@password,
		@UserTypeId,
		@ApplicationId,
		@is_su,
		@is_staff,
		@is_active,
		@date_joined
	)
GO

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getUser]
	@email nvarchar(100) = NULL
AS
SELECT * FROM [dbo].[accounts_userlist] WHERE [email]=@email
GO


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getUserWithId]
	@id int = NULL
AS
SELECT * FROM [dbo].[accounts_userlist] WHERE [id]=@id
GO


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getChatRecord]
	@client_id int = NULL,
	@professional_id int = NULL
AS

SELECT [message],[side] FROM [dbo].[accounts_chatrecord] WHERE [client_id] = @client_id AND [professional_id] = @professional_id
GO




USE [baghiService]
GO


CREATE PROCEDURE [dbo].[getClientConnections]
	@client_id int = NULL
AS
SELECT [professional_id], [first_name] FROM [dbo].[accounts_chatrecord] LEFT JOIN [dbo].[accounts_userlist] ON [dbo].[accounts_chatrecord].[professional_id]=[dbo].[accounts_userlist].[id] AND [dbo].[accounts_chatrecord].[client_id]=@client_id


CREATE PROCEDURE [dbo].[getProfessionalConnections]
	@professinoal_id int = NULL
AS
SELECT [client_id], [first_name] FROM [dbo].[accounts_chatrecord] LEFT JOIN [dbo].[accounts_userlist] ON [dbo].[accounts_chatrecord].[client_id]=[dbo].[accounts_userlist].[id] AND [dbo].[accounts_chatrecord].[professional_id]=@professinoal_id






USE [baghiService]
GO
CREATE PROCEDURE [dbo].[createChatRecord]
	@client_id int = NULL,
	@professional_id int = NULL,
	@room_name nvarchar(300) = NULL,
	@is_active bit = True,
	@time_stamp datetime2(7) = NULL,
	@side bit = True,
	@message nvarchar(400) = NULL
AS
INSERT INTO [dbo].[accounts_chatrecord]
    ([message]
    ,[side]
    ,[room_name]
    ,[TimeStamp]
    ,[IsActive]
    ,[client_id]
    ,[professional_id])
VALUES
    (
		@message,
		@side,
		@room_name,
		@time_stamp,
		@is_active,
		@client_id,
		@professional_id
	)
GO


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getUserType]
	@id int = NULL
AS
SELECT [UserType] FROM [dbo].[accounts_usertype] WHERE [id] = @id
GO




USE [baghiService]
GO
CREATE PROCEDURE [dbo].[addUserWithType]
	@first_name nvarchar(30) = NULL,
	@last_name nvarchar(30) = NULL,
	@email nvarchar(100) = NULL,
	@ContactCell nvarchar(100) = NULL,
	@password nvarchar(128) = NULL,
	@UserType nvarchar(128) = NULL,
	@ApplicationId int = NULL,
	@is_su bit = 0,
	@is_staff bit = 0,
	@is_active bit = 1,
	@date_joined datetime2(7) = NULL
AS
INSERT INTO [dbo].[accounts_userlist]
           ([username]
		   ,[first_name]
           ,[last_name]
           ,[email]
           ,[ContactCell]
		   ,[password]
           ,[UserType_id]
           ,[Application_id]
           ,[is_superuser]
           ,[is_staff]
           ,[is_active]
		   ,[date_joined])
VALUES
	(
		@email,
		@first_name,
		@last_name,
		@email,
		@ContactCell,
		@password,
		(SELECT [id] FROM [dbo].[accounts_usertype] WHERE [UserType]=@UserType),
		@ApplicationId,
		@is_su,
		@is_staff,
		@is_active,
		@date_joined
	)
GO

-- Create a job

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[addJobPost]
	@TopicName nvarchar(300) = NULL,
	@TopicDate datetime2(7) = NULL,
	@AddedDate datetime2(7) = NULL,
	@UpdatedDate datetime2(7) = NULL,
	@IsActive bit = 0,
	@IsClose bit = 1,
	@CloseDate datetime2(7) = NULL,
	@ForceCloseReason nvarchar(3999) = NULL,
	@IsNotification bit = 0,
	@SMSText nvarchar(150) = NULL,
	@WhatsAppText nvarchar(1000) = NULL,
	@AddedBy_id int = NULL,
	@Category_id int = NULL,
	@City_id int = NULL,
	@CloseBy_id int = NULL,
	@ForceCloseCategory_id int = NULL,
	@SubCategory_id int = NULL,
	@UpdatedBy_id int = NULL,
	@User_id int = NULL

AS
INSERT INTO [dbo].[accounts_topiclist]
           ([TopicName]
		   ,[TopicDate]
           ,[AddedDate]
           ,[UpdatedDate]
		   ,[IsActive]
           ,[IsClose]
		   ,[CloseDate]
           ,[ForceCloseReason]
           ,[IsNotification]
           ,[SMSText]
           ,[WhatsAppText]
           ,[AddedBy_id]
		   ,[Category_id]
		   ,[City_id]
		   ,[CloseBy_id]
		   ,[ForceCloseCategory_id]
		   ,[SubCategory_id]
		   ,[UpdatedBy_id]
		   ,[User_id])
VALUES
	(
		@TopicName,
		@TopicDate,
		@AddedDate,
		@UpdatedDate,
		@IsActive,
		@IsClose,
		@CloseDate,
		@ForceCloseReason,
		@IsNotification,
		@SMSText,
		@WhatsAppText,
		@AddedBy_id,
		@Category_id,
		@City_id,
		@CloseBy_id,
		@ForceCloseCategory_id,
		@SubCategory_id,
		@UpdatedBy_id,
		@User_id
	)
GO


-- Filter category by City

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getCategory]
	@city varchar(30) = NULL
AS
SELECT * FROM [dbo].[accounts_userlist] LEFT JOIN [dbo].[accounts_categorylist] ON accounts_userlist.ID=accounts_categorylist.ID WHERE [City]=@city AND [usertype_id] = 1
GO

-- Update Job Post

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[updateJobPost]
	@id int = Null,
	@TopicName nvarchar(300) = NULL,
	@UpdatedDate datetime2(7) = NULL,
	@IsActive bit = 0,
	@IsClose bit = 1,
	@CloseDate datetime2(7) = NULL,
	@ForceCloseReason nvarchar(3999) = NULL,
	@IsNotification bit = 0,
	@SMSText nvarchar(150) = NULL,
	@WhatsAppText nvarchar(1000) = NULL,
	@Category_id int = NULL,
	@City_id int = NULL,
	@CloseBy_id int = NULL,
	@ForceCloseCategory_id int = NULL,
	@SubCategory_id int = NULL,
	@User_id int = NULL

AS
UPDATE [dbo].[accounts_topiclist]
   SET     [TopicName]=@TopicName,
           [UpdatedDate]=@UpdatedDate,
		   [IsActive]=@IsActive,
           [IsClose]=@IsClose,
		   [CloseDate]=@CloseDate,
           [ForceCloseReason]=@ForceCloseReason,
           [IsNotification]=@IsNotification,
           [SMSText]=@SMSText,
           [WhatsAppText]=@WhatsAppText,
		   [Category_id]=Category_id,
		   [City_id]=@City_id,
		   [CloseBy_id]=@CloseBy_id,
		   [ForceCloseCategory_id]=@ForceCloseCategory_id,
		   [SubCategory_id]=@SubCategory_id,
		   [User_id]=@User_id
WHERE id = @id
GO

--  Delete Job

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[deleteJob]
	@id int = NULL
AS
DELETE FROM [dbo].[accounts_topiclist] WHERE [id] = @id
GO


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getEachJob]
	@id int = NULL
AS
Select * from [dbo].[accounts_topiclist] WHERE id=@id
GO




USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getMyJobs]
	@user_id int = NULL
AS
Select * from [dbo].[accounts_topiclist] WHERE AddedBy_id=@user_id
GO


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getAllJobs]
AS
Select * from [dbo].[accounts_topiclist]
GO




USE [baghiService]
GO
CREATE PROCEDURE [dbo].[createTopicAsset]
	@addedby_id int = NULL,
	@updatedby_id int = NULL,
	@added_date datetime2(7) = NULL,
	@updated_date datetime2(7) = NULL,
	@topic_id int = NULL,
	@file_name nvarchar(100) = NULL,
	@file_ext nvarchar(50) = NULL
AS

INSERT INTO [dbo].[accounts_assetsdetaillist]
           ([FileName]
           ,[FileExtension]
           ,[AddedDate]
           ,[UpdatedDate]
           ,[IsActive]
           ,[AddedBy_id]
           ,[Topic_id]
           ,[UpdatedBy_id])
     VALUES
           (@file_name
		   ,@file_ext
		   ,@added_date
		   ,@updated_date
		   ,1
		   ,@addedby_id
		   ,@topic_id
		   ,@updatedby_id)
GO




-- Update Job


USE [baghiService]
GO

CREATE PROCEDURE [dbo].[updateJob]
	@id int = NULL,
	@content nvarchar(max) = NULL,
	@TopicName nvarchar(300) = NULL,
	@TopicDate datetime2(7) = NULL,
	@AddedDate datetime2(7) = NULL,
	@UpdatedDate datetime2(7) = NULL,
	@IsActive bit = 0,
	@IsClose bit = 1,
	@CloseDate datetime2(7) = NULL,
	@ForceCloseReason nvarchar(3999) = NULL,
	@IsNotification bit = 0,
	@SMS nvarchar(150) = NULL,
	@whatsApp nvarchar(1000) = NULL,
	@AddedBy_id int = NULL,
	@Category_id int = NULL,
	@City_id int = NULL,
	@CloseBy_id int = NULL,
	@ForceClose_id int = NULL,
	@subCat_id int = NULL,
	@UpdatedBy_id int = NULL


AS
UPDATE [dbo].[accounts_topiclist]
   SET [TopicName] = @TopicName
      ,[UpdatedDate] = @UpdatedDate
      ,[IsActive] = @isActive
      ,[IsClose] = @isClose
      ,[CloseDate] = @closeDate
      ,[ForceCloseReason] = @ForceCloseReason
      ,[IsNotification] = @isNotification
      ,[SMSText] = @SMS
      ,[WhatsAppText] = @whatsApp
      ,[Category_id] = @category_id
      ,[City_id] = @City_id
      ,[CloseBy_id] = @closeBy_id
      ,[ForceCloseCategory_id] = @ForceClose_id
      ,[SubCategory_id] = @subCat_id
      ,[UpdatedBy_id] = @UpdatedBy_id
      ,[content] = @content
 WHERE id=@id
GO



USE [baghiService]
GO
CREATE PROCEDURE [dbo].[userPasswordChange]
	@password nvarchar(128) = NULL,
	@user_id int = NULL
AS
UPDATE [dbo].[accounts_userlist]
   SET [password] = @password
 WHERE [id] = @user_id
GO


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[addreview]
	@Topic int = NULL,
	@ReviewDate datetime2(7) = NULL,
	@ToUser int = NULL,
	@FromUser int = NULL,
	@ReviewNote nvarchar(3999) = 0,
	@User int = null,
	@AddedBy int = NULL,
	@AddedDate datetime2(7) = NULL,
	@IsActive bit = 1,
	@IsAdminApproved bit = 1
AS
INSERT INTO [dbo].[accounts_reviewlist]
           ([Topic_id]
		   ,[ReviewDate]
           ,[ToUser_id]
           ,[FromUser_id]
		   ,[ReviewNote]
           ,[User_id]
		   ,[AddedBy_id]
           ,[AddedDate]
           ,[IsActive]
           ,[IsAdminApproved])
VALUES
	(
		@Topic,
		@ReviewDate,
		@ToUser,
		@FromUser,
		@ReviewNote,
		@User,
		@AddedBy,
		@AddedDate,
		@IsActive,
		@IsAdminApproved
	)
GO

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getAllReview]
AS
Select * from [dbo].[accounts_reviewlist]
GO

-- Get Jobs In My City

CREATE PROCEDURE [dbo].[getMyCityJobs]
	@user_id int = NULL

AS
SELECT * FROM [dbo].[accounts_addresslist] INNER JOIN [dbo].[accounts_userlist] ON [dbo].[accounts_addresslist].[user_id]=[dbo].[accounts_userlist].[id] INNER JOIN [dbo].[accounts_topiclist] ON [dbo].[accounts_addresslist].[CityId_id]=[dbo].[accounts_topiclist].[City_id] WHERE [dbo].[accounts_userlist].[id]=@user_id



--- generate OTP
USE [baghiService]
GO
CREATE PROCEDURE [dbo].[generateOTP]
	@Otp nvarchar(10) = NULL,
	@expire_minute nvarchar(100) = NULL,
	@user_email nvarchar(100) = NULL,
	@doc datetime2(7) = NULL

AS
INSERT INTO [dbo].[accounts_otp]
           ([Otp]
           ,[expire_minute]
           ,[user_email]
           ,[doc])
     VALUES
           (@Otp
           ,@expire_minute
           ,@user_email
           ,@doc)
GO


-- Apply Job

USE [baghiService]
GO

CREATE PROCEDURE dbo.applyJob
	@user_id int = NULL,
	@job_id int = NULL,
	@topic_date datetime2(7) = NULL

AS

INSERT INTO [dbo].[accounts_topicdetaillist]
           ([TopicDate]
           ,[AddedDate]
           ,[UpdatedDate]
           ,[IsActive]
           ,[AddedBy_id]
           ,[Topic_id]
           ,[UpdatedBy_id]
           ,[User_id]
           ,[Selected])
     VALUES
           (@topic_date,
		   @topic_date,
		   @topic_date,
		   1,
		   @user_id,
		   @job_id,
		   @user_id,
		   @user_id,
		   0)
GO


-- Get My Applied Jobs


USE [baghiService]
GO

CREATE PROCEDURE dbo.getAppliedJobsList
	@user_id int = NULL

AS
SELECT [id] FROM [dbo].[accounts_topicdetaillist] WHERE [User_id]=@user_id
GO




-- Get Job By Id

USE [baghiService]
GO

CREATE PROCEDURE [dbo].[getJobById]
	@job_id int = NULL
AS

SELECT * FROM [dbo].[accounts_topiclist] WHERE id=@job_id



-- filter jobs



USE [baghiService]
GO

CREATE PROCEDURE [dbo].[getFilterJobs]
	@city_id int = NULL,
	@subcat_id int=NULL,
	@cat_id int = NULL
AS

SELECT * FROM [dbo].[accounts_topiclist] INNER JOIN [dbo].[accounts_topicsubcats] ON [dbo].[accounts_topiclist].[id] = [dbo].[accounts_topicsubcats].[Topic_id]  WHERE [dbo].[accounts_topicsubcats].[subcat_id]=@subcat_id AND [dbo].[accounts_topiclist].[City_id]=@city_id

GO






--  Add Category

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[createCategory]
	@CategoryName nvarchar(300) = NULL,
	@AddedBy int = NULL,
	@AddedDate datetime2(7) = NULL,
	@IsActive bit = 1
AS
INSERT INTO [dbo].[accounts_categorylist]
           ([CategoryName]
		   ,[AddedBy_id]
		   ,[AddedDate]
           ,[IsActive])
VALUES
	(
		@CategoryName,
		@AddedBy,
		@AddedDate,
		@IsActive
	)
GO

--  Sub Category

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[createSubCategory]
	@SubCategoryName nvarchar(300) = NULL,
	@Category int = NULL,
	@AddedBy int = NULL,
	@AddedDate datetime2(7) = NULL,
	@IsActive bit = 1
AS
INSERT INTO [dbo].[accounts_subcategorylist]
           ([SubCategoryName]
		   ,[Category_id]
		   ,[AddedBy_id]
		   ,[AddedDate]
           ,[IsActive])
VALUES
	(
		@SubCategoryName,
		@Category,
		@AddedBy,
		@AddedDate,
		@IsActive
	)
GO

-- All Staff

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getAllStaff]
AS
Select * from [dbo].[accounts_userlist] WHERE is_staff = 1
GO

-- All Admin

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[getAllAdmin]
AS
Select * from [dbo].[accounts_userlist] WHERE is_superuser = 1
GO


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[deleteCategory]
	@id int = NULL
AS
DELETE FROM [dbo].[accounts_categorylist] WHERE [id] = @id
GO

USE [baghiService]
GO
CREATE PROCEDURE [dbo].[deleteCountry]
	@id int = NULL
AS
DELETE FROM [dbo].[accounts_countrylist] WHERE [id] = @id
GO


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[allCategory]
AS
SELECT * FROM [dbo].[accounts_categorylist]
GO




-- Adding category in a area


USE [baghiService]
GO
CREATE PROCEDURE [dbo].[addCatInCity]
	@cat_id int = NULL,
	@city_id int = NULL
AS

INSERT INTO [dbo].[accounts_categoryincity]
           ([category_id]
           ,[city_id])
     VALUES
           (@cat_id
           ,@city_id)
GO
