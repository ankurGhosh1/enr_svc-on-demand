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
		   ,[UserEmail]
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
		   ,[UserEmail]
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
