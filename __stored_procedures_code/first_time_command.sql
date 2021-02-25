-- Create usertypes in the database

INSERT INTO [dbo].[accounts_usertype]
           ([UserType]
           ,[UpdatedDate]
           ,[IsActive])
     VALUES
           ('Professional',
		   '2021-02-24T22:55:20.1115409+05:30',
		   1)
GO

INSERT INTO [dbo].[accounts_usertype]
           ([UserType]
           ,[UpdatedDate]
           ,[IsActive])
     VALUES
           ('Client',
		   '2021-02-24T22:55:20.1115409+05:30',
		   1)
GO




-- Create languages

INSERT INTO [dbo].[accounts_languagelist]
           ([LanguageName])
     VALUES
           ('English')
GO



INSERT INTO [dbo].[accounts_languagelist]
           ([LanguageName])
     VALUES
           ('Hindi')
GO




-- Creating an application list

INSERT INTO [dbo].[accounts_appliationlist]
           ([ApplicationName]
           ,[Language_id])
     VALUES
           ('First',
		   1)
GO




-- Creating a country

INSERT INTO [dbo].[accounts_countrylist]
           ([Country]
           ,[IsActive])
     VALUES
           ('India',
		   1)
GO
