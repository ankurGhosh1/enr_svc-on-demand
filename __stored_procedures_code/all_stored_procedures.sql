USE [baghiService]
GO
CREATE PROCEDURE dbo.allUserTypeExceptMe @userId nvarchar(30) = NULL, @userType nvarchar(30) = NULL
AS 
SELECT [id]
      ,[username]
      ,[first_name]
      ,[last_name] FROM [dbo].[clients_user] WHERE (id<>@userId AND is_staff=0 AND usertype=@userType)
GO