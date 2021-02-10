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