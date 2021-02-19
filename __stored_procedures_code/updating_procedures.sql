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
