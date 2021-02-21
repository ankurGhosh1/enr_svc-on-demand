USE [baghiService]
GO
/****** Object:  StoredProcedure [dbo].[updateJob]    Script Date: 19-02-2021 12:21:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[updateJob]
	@id int = NULL,
	@content nvarchar(max) = NULL,
	@TopicName nvarchar(300) = NULL,
	@UpdatedDate datetime2(7) = NULL,
	@IsActive bit = 1,
	@IsClose bit = 0,
	@CloseDate datetime2(7) = NULL,
	@ForceCloseReason nvarchar(3999) = NULL,
	@IsNotification bit = 0,
	@SMS nvarchar(150) = NULL,
	@whatsApp nvarchar(1000) = NULL,
	@CloseBy_id int = NULL,
	@ForceClose_id int = NULL,
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
      ,[CloseBy_id] = @closeBy_id
      ,[ForceCloseCategory_id] = @ForceClose_id
      ,[UpdatedBy_id] = @UpdatedBy_id
      ,[content] = @content
 WHERE id=@id



 USE [baghiService]
 GO
 /****** Object:  StoredProcedure [dbo].[getChatRecord]    Script Date: 21-02-2021 01:30:57 PM ******/
 SET ANSI_NULLS ON
 GO
 SET QUOTED_IDENTIFIER ON
 GO
 ALTER PROCEDURE [dbo].[getChatRecord]
 	@client_id int = NULL,
 	@professional_id int = NULL,
 	@room_name nvarchar(300) = NULL
 AS

 SELECT [message],[side] FROM [dbo].[accounts_chatrecord] WHERE [client_id] = @client_id AND [professional_id] = @professional_id AND [room_name]=@room_name




 USE [baghiService]
GO
/****** Object:  StoredProcedure [dbo].[getMyCityJobs]    Script Date: 21-02-2021 12:28:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[getMyCityJobs]
	@user_id int = NULL

AS
SELECT [dbo].[accounts_topiclist].[id], [dbo].[accounts_topiclist].[TopicName], first_name=(SELECT [first_name] FROM dbo.accounts_userlist WHERE id=[dbo].[accounts_topiclist].[User_id]) FROM [dbo].[accounts_addresslist] INNER JOIN [dbo].[accounts_userlist] ON [dbo].[accounts_addresslist].[user_id]=[dbo].[accounts_userlist].[id] INNER JOIN [dbo].[accounts_topiclist] ON [dbo].[accounts_addresslist].[CityId_id]=[dbo].[accounts_topiclist].[City_id] WHERE [dbo].[accounts_userlist].[id]=@user_id




USE [baghiService]
GO
/****** Object:  StoredProcedure [dbo].[createChatRecord]    Script Date: 21-02-2021 02:03:26 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[createChatRecord]
	@client_id int = NULL,
	@professional_id int = NULL,
	@room_name nvarchar(300) = NULL,
	@is_active bit = True,
	@time_stamp datetime2(7) = NULL,
	@side bit = True,
	@message nvarchar(400) = NULL,
	@topic_id int = NULL
AS
INSERT INTO [dbo].[accounts_chatrecord]
    ([message]
    ,[side]
    ,[room_name]
    ,[TimeStamp]
    ,[IsActive]
    ,[client_id]
    ,[professional_id]
	,[topic_id])
VALUES
    (
		@message,
		@side,
		@room_name,
		@time_stamp,
		@is_active,
		@client_id,
		@professional_id,
		@topic_id
	)


	USE [baghiService]
	GO
	/****** Object:  StoredProcedure [dbo].[getProfessionalConnections]    Script Date: 21-02-2021 01:59:34 PM ******/
	SET ANSI_NULLS ON
	GO
	SET QUOTED_IDENTIFIER ON
	GO

	ALTER PROCEDURE [dbo].[getProfessionalConnections]
		@professinoal_id int = NULL
	AS
	SELECT DISTINCT [client_id], [first_name], [room_name], [topic_id], TopicName=(SELECT [TopicName] FROM [dbo].[accounts_topiclist] WHERE id=topic_id) FROM [dbo].[accounts_chatrecord] LEFT JOIN [dbo].[accounts_userlist] ON [dbo].[accounts_chatrecord].[client_id]=[dbo].[accounts_userlist].[id] AND [dbo].[accounts_chatrecord].[professional_id]=@professinoal_id



	USE [baghiService]
	GO
	/****** Object:  StoredProcedure [dbo].[getClientConnections]    Script Date: 21-02-2021 01:50:29 PM ******/
	SET ANSI_NULLS ON
	GO
	SET QUOTED_IDENTIFIER ON
	GO

	ALTER PROCEDURE [dbo].[getClientConnections]
		@client_id int = NULL
	AS
	SELECT DISTINCT [professional_id], [first_name], [room_name], [topic_id], TopicName=(SELECT [TopicName] FROM [dbo].[accounts_topiclist] WHERE id=topic_id) FROM [dbo].[accounts_chatrecord] LEFT JOIN [dbo].[accounts_userlist] ON [dbo].[accounts_chatrecord].[professional_id]=[dbo].[accounts_userlist].[id] AND [dbo].[accounts_chatrecord].[client_id]=@client_id
