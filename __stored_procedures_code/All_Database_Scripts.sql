USE [baghiService2]
GO
/****** Object:  UserDefinedFunction [dbo].[SplitString]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
Create FUNCTION [dbo].[SplitString]
(
      @Input NVARCHAR(MAX),
      @Character CHAR(1)
)
RETURNS @Output TABLE (
      Item NVARCHAR(1000)
)
AS
BEGIN
      DECLARE @StartIndex INT, @EndIndex INT

      SET @StartIndex = 1
      IF SUBSTRING(@Input, LEN(@Input) - 1, LEN(@Input)) <> @Character
      BEGIN
            SET @Input = @Input + @Character
      END

      WHILE CHARINDEX(@Character, @Input) > 0
      BEGIN
            SET @EndIndex = CHARINDEX(@Character, @Input)

            INSERT INTO @Output(Item)
            SELECT SUBSTRING(@Input, @StartIndex, @EndIndex - 1)

            SET @Input = SUBSTRING(@Input, @EndIndex + 1, LEN(@Input))
      END

      RETURN
END
GO
/****** Object:  Table [dbo].[accounts_addresslist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_addresslist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Street] [nvarchar](500) NULL,
	[ZipCode] [nvarchar](50) NULL,
	[AddedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[CityId_id] [int] NULL,
	[user_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_appliationlist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_appliationlist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ApplicationName] [nvarchar](100) NOT NULL,
	[Language_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_assetsdetaillist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_assetsdetaillist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[FileName] [nvarchar](100) NOT NULL,
	[FileExtension] [nvarchar](50) NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[Topic_id] [int] NULL,
	[UpdatedBy_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_categoryincity]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_categoryincity](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[category_id] [int] NULL,
	[city_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_categorylist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_categorylist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[CategoryName] [nvarchar](300) NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[UpdatedBy_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_chatrecord]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_chatrecord](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[message] [nvarchar](400) NOT NULL,
	[side] [bit] NULL,
	[room_name] [nvarchar](300) NOT NULL,
	[TimeStamp] [datetime2](7) NOT NULL,
	[IsActive] [bit] NOT NULL,
	[client_id] [int] NOT NULL,
	[professional_id] [int] NOT NULL,
	[topic_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_citylist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_citylist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[City] [nvarchar](100) NOT NULL,
	[Latitude] [float] NOT NULL,
	[Longitude] [float] NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NULL,
	[UpdatedBy_id] [int] NULL,
	[StateId_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_countrylist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_countrylist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Country] [nvarchar](100) NULL,
	[IsActive] [bit] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_forceclosecategorylist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_forceclosecategorylist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ForceCloseCategoryName] [nvarchar](300) NOT NULL,
	[DefaultValue] [nvarchar](300) NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[UpdatedBy_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_languagelist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_languagelist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[LanguageName] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_notificationlist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_notificationlist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[NotificationDate] [date] NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[AssetsDetail_id] [int] NULL,
	[Category_id] [int] NULL,
	[City_id] [int] NULL,
	[SubCategory_id] [int] NULL,
	[ToUser_id] [int] NOT NULL,
	[Topic_id] [int] NULL,
	[UpdatedBy_id] [int] NULL,
	[User_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_otp]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_otp](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Otp] [nvarchar](10) NOT NULL,
	[expire_minute] [nvarchar](100) NOT NULL,
	[user_email] [nvarchar](100) NOT NULL,
	[doc] [datetime2](7) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_responsetypelist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_responsetypelist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ResponseType] [nvarchar](100) NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[UpdatedBy_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_reviewlist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_reviewlist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ReviewDate] [date] NOT NULL,
	[ReviewNote] [nvarchar](3999) NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[IsAdminApproved] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[AssetsDetail_id] [int] NULL,
	[Category_id] [int] NULL,
	[City_id] [int] NULL,
	[FromUser_id] [int] NOT NULL,
	[SubCategory_id] [int] NULL,
	[ToUser_id] [int] NOT NULL,
	[Topic_id] [int] NULL,
	[UpdatedBy_id] [int] NULL,
	[User_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_statelist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_statelist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[State] [nvarchar](100) NULL,
	[IsActive] [bit] NOT NULL,
	[CountryId_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_subcategorylist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_subcategorylist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[SubCategoryName] [nvarchar](300) NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[Category_id] [int] NOT NULL,
	[UpdatedBy_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_subscriptiondetaillist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_subscriptiondetaillist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[SubscriptionItemItem] [nvarchar](300) NOT NULL,
	[ConfiguredValue] [nvarchar](300) NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[UpdatedBy_id] [int] NULL,
	[User_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_subscriptionitemlist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_subscriptionitemlist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[SubscriptionItemName] [nvarchar](300) NOT NULL,
	[DefaultValue] [nvarchar](300) NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[UpdatedBy_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_subscriptionlist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_subscriptionlist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[SubscriptionName] [nvarchar](300) NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[UpdatedBy_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_templatetypelist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_templatetypelist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[SMSTemplateType] [nvarchar](300) NOT NULL,
	[WhatsAppTemplateType] [nvarchar](1000) NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[UpdatedBy_id] [int] NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_topicdetaillist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_topicdetaillist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[TopicDate] [date] NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
	[AddedBy_id] [int] NOT NULL,
	[Topic_id] [int] NULL,
	[UpdatedBy_id] [int] NULL,
	[User_id] [int] NOT NULL,
	[Selected] [bit] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_topiclist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_topiclist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[TopicName] [nvarchar](300) NOT NULL,
	[TopicDate] [date] NOT NULL,
	[AddedDate] [date] NOT NULL,
	[UpdatedDate] [date] NULL,
	[IsActive] [bit] NOT NULL,
	[IsClose] [bit] NOT NULL,
	[CloseDate] [date] NULL,
	[ForceCloseReason] [nvarchar](3999) NULL,
	[IsNotification] [bit] NOT NULL,
	[SMSText] [nvarchar](150) NULL,
	[WhatsAppText] [nvarchar](1000) NULL,
	[AddedBy_id] [int] NOT NULL,
	[Category_id] [int] NOT NULL,
	[City_id] [int] NOT NULL,
	[CloseBy_id] [int] NULL,
	[ForceCloseCategory_id] [int] NULL,
	[UpdatedBy_id] [int] NULL,
	[User_id] [int] NOT NULL,
	[content] [nvarchar](max) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_topicsubcats]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_topicsubcats](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Topic_id] [int] NULL,
	[subcat_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_userlist]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_userlist](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[password] [nvarchar](128) NOT NULL,
	[last_login] [datetime2](7) NULL,
	[is_superuser] [bit] NOT NULL,
	[username] [nvarchar](150) NOT NULL,
	[first_name] [nvarchar](30) NOT NULL,
	[last_name] [nvarchar](150) NOT NULL,
	[email] [nvarchar](254) NOT NULL,
	[is_staff] [bit] NOT NULL,
	[is_active] [bit] NOT NULL,
	[date_joined] [datetime2](7) NOT NULL,
	[UserMiddleName] [nvarchar](100) NULL,
	[ContactCell] [nvarchar](100) NULL,
	[City] [nvarchar](30) NOT NULL,
	[Application_id] [int] NULL,
	[usertype_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED
(
	[email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_userlist_groups]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_userlist_groups](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[userlist_id] [int] NOT NULL,
	[group_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_userlist_user_permissions]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_userlist_user_permissions](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[userlist_id] [int] NOT NULL,
	[permission_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[accounts_usertype]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[accounts_usertype](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[UserType] [nvarchar](15) NOT NULL,
	[UpdatedDate] [date] NOT NULL,
	[IsActive] [bit] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_group]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_group](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](150) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [auth_group_name_a6ea08ec_uniq] UNIQUE NONCLUSTERED
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_group_permissions]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_group_permissions](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[group_id] [int] NOT NULL,
	[permission_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_permission]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_permission](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[content_type_id] [int] NOT NULL,
	[codename] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_admin_log]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_admin_log](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[action_time] [datetime2](7) NOT NULL,
	[object_id] [nvarchar](max) NULL,
	[object_repr] [nvarchar](200) NOT NULL,
	[action_flag] [smallint] NOT NULL,
	[change_message] [nvarchar](max) NOT NULL,
	[content_type_id] [int] NULL,
	[user_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_content_type]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_content_type](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[app_label] [nvarchar](100) NOT NULL,
	[model] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_migrations]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_migrations](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[app] [nvarchar](255) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[applied] [datetime2](7) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_session]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_session](
	[session_key] [nvarchar](40) NOT NULL,
	[session_data] [nvarchar](max) NOT NULL,
	[expire_date] [datetime2](7) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[session_key] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[social_auth_association]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[social_auth_association](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[server_url] [nvarchar](255) NOT NULL,
	[handle] [nvarchar](255) NOT NULL,
	[secret] [nvarchar](255) NOT NULL,
	[issued] [int] NOT NULL,
	[lifetime] [int] NOT NULL,
	[assoc_type] [nvarchar](64) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[social_auth_code]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[social_auth_code](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[email] [nvarchar](254) NOT NULL,
	[code] [nvarchar](32) NOT NULL,
	[verified] [bit] NOT NULL,
	[timestamp] [datetime2](7) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[social_auth_nonce]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[social_auth_nonce](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[server_url] [nvarchar](255) NOT NULL,
	[timestamp] [int] NOT NULL,
	[salt] [nvarchar](65) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[social_auth_partial]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[social_auth_partial](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[token] [nvarchar](32) NOT NULL,
	[next_step] [smallint] NOT NULL,
	[backend] [nvarchar](32) NOT NULL,
	[data] [nvarchar](max) NOT NULL,
	[timestamp] [datetime2](7) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[social_auth_usersocialauth]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[social_auth_usersocialauth](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[provider] [nvarchar](32) NOT NULL,
	[uid] [nvarchar](255) NOT NULL,
	[extra_data] [nvarchar](max) NOT NULL,
	[user_id] [int] NOT NULL,
	[created] [datetime2](7) NOT NULL,
	[modified] [datetime2](7) NOT NULL,
PRIMARY KEY CLUSTERED
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[accounts_addresslist]  WITH CHECK ADD  CONSTRAINT [accounts_addresslist_CityId_id_9ffb734e_fk_accounts_citylist_id] FOREIGN KEY([CityId_id])
REFERENCES [dbo].[accounts_citylist] ([id])
GO
ALTER TABLE [dbo].[accounts_addresslist] CHECK CONSTRAINT [accounts_addresslist_CityId_id_9ffb734e_fk_accounts_citylist_id]
GO
ALTER TABLE [dbo].[accounts_addresslist]  WITH CHECK ADD  CONSTRAINT [accounts_addresslist_user_id_7f43f514_fk_accounts_userlist_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_addresslist] CHECK CONSTRAINT [accounts_addresslist_user_id_7f43f514_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_appliationlist]  WITH CHECK ADD  CONSTRAINT [accounts_appliationlist_Language_id_6c76ac0d_fk_accounts_languagelist_id] FOREIGN KEY([Language_id])
REFERENCES [dbo].[accounts_languagelist] ([id])
GO
ALTER TABLE [dbo].[accounts_appliationlist] CHECK CONSTRAINT [accounts_appliationlist_Language_id_6c76ac0d_fk_accounts_languagelist_id]
GO
ALTER TABLE [dbo].[accounts_assetsdetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_assetsdetaillist_AddedBy_id_4531ea66_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_assetsdetaillist] CHECK CONSTRAINT [accounts_assetsdetaillist_AddedBy_id_4531ea66_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_assetsdetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_assetsdetaillist_Topic_id_4d491309_fk_accounts_topiclist_id] FOREIGN KEY([Topic_id])
REFERENCES [dbo].[accounts_topiclist] ([id])
GO
ALTER TABLE [dbo].[accounts_assetsdetaillist] CHECK CONSTRAINT [accounts_assetsdetaillist_Topic_id_4d491309_fk_accounts_topiclist_id]
GO
ALTER TABLE [dbo].[accounts_assetsdetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_assetsdetaillist_UpdatedBy_id_ba60cb9a_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_assetsdetaillist] CHECK CONSTRAINT [accounts_assetsdetaillist_UpdatedBy_id_ba60cb9a_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_categoryincity]  WITH CHECK ADD  CONSTRAINT [accounts_categoryincity_category_id_2b769ab1_fk_accounts_categorylist_id] FOREIGN KEY([category_id])
REFERENCES [dbo].[accounts_categorylist] ([id])
GO
ALTER TABLE [dbo].[accounts_categoryincity] CHECK CONSTRAINT [accounts_categoryincity_category_id_2b769ab1_fk_accounts_categorylist_id]
GO
ALTER TABLE [dbo].[accounts_categoryincity]  WITH CHECK ADD  CONSTRAINT [accounts_categoryincity_city_id_8b78246f_fk_accounts_citylist_id] FOREIGN KEY([city_id])
REFERENCES [dbo].[accounts_citylist] ([id])
GO
ALTER TABLE [dbo].[accounts_categoryincity] CHECK CONSTRAINT [accounts_categoryincity_city_id_8b78246f_fk_accounts_citylist_id]
GO
ALTER TABLE [dbo].[accounts_categorylist]  WITH CHECK ADD  CONSTRAINT [accounts_categorylist_AddedBy_id_f6671073_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_categorylist] CHECK CONSTRAINT [accounts_categorylist_AddedBy_id_f6671073_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_categorylist]  WITH CHECK ADD  CONSTRAINT [accounts_categorylist_UpdatedBy_id_ff27ba0e_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_categorylist] CHECK CONSTRAINT [accounts_categorylist_UpdatedBy_id_ff27ba0e_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_chatrecord]  WITH CHECK ADD  CONSTRAINT [accounts_chatrecord_client_id_e47739d3_fk_accounts_userlist_id] FOREIGN KEY([client_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_chatrecord] CHECK CONSTRAINT [accounts_chatrecord_client_id_e47739d3_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_chatrecord]  WITH CHECK ADD  CONSTRAINT [accounts_chatrecord_professional_id_0dd5ac75_fk_accounts_userlist_id] FOREIGN KEY([professional_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_chatrecord] CHECK CONSTRAINT [accounts_chatrecord_professional_id_0dd5ac75_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_chatrecord]  WITH CHECK ADD  CONSTRAINT [accounts_chatrecord_topic_id_84488537_fk_accounts_topiclist_id] FOREIGN KEY([topic_id])
REFERENCES [dbo].[accounts_topiclist] ([id])
GO
ALTER TABLE [dbo].[accounts_chatrecord] CHECK CONSTRAINT [accounts_chatrecord_topic_id_84488537_fk_accounts_topiclist_id]
GO
ALTER TABLE [dbo].[accounts_citylist]  WITH CHECK ADD  CONSTRAINT [accounts_citylist_AddedBy_id_a7578093_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_citylist] CHECK CONSTRAINT [accounts_citylist_AddedBy_id_a7578093_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_citylist]  WITH CHECK ADD  CONSTRAINT [accounts_citylist_StateId_id_b0da5673_fk_accounts_statelist_id] FOREIGN KEY([StateId_id])
REFERENCES [dbo].[accounts_statelist] ([id])
GO
ALTER TABLE [dbo].[accounts_citylist] CHECK CONSTRAINT [accounts_citylist_StateId_id_b0da5673_fk_accounts_statelist_id]
GO
ALTER TABLE [dbo].[accounts_citylist]  WITH CHECK ADD  CONSTRAINT [accounts_citylist_UpdatedBy_id_3fc06dd6_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_citylist] CHECK CONSTRAINT [accounts_citylist_UpdatedBy_id_3fc06dd6_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_forceclosecategorylist]  WITH CHECK ADD  CONSTRAINT [accounts_forceclosecategorylist_AddedBy_id_c78e4dd3_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_forceclosecategorylist] CHECK CONSTRAINT [accounts_forceclosecategorylist_AddedBy_id_c78e4dd3_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_forceclosecategorylist]  WITH CHECK ADD  CONSTRAINT [accounts_forceclosecategorylist_UpdatedBy_id_8b52bff7_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_forceclosecategorylist] CHECK CONSTRAINT [accounts_forceclosecategorylist_UpdatedBy_id_8b52bff7_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_notificationlist]  WITH CHECK ADD  CONSTRAINT [accounts_notificationlist_AddedBy_id_19ce8d2d_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_notificationlist] CHECK CONSTRAINT [accounts_notificationlist_AddedBy_id_19ce8d2d_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_notificationlist]  WITH CHECK ADD  CONSTRAINT [accounts_notificationlist_AssetsDetail_id_0882003e_fk_accounts_assetsdetaillist_id] FOREIGN KEY([AssetsDetail_id])
REFERENCES [dbo].[accounts_assetsdetaillist] ([id])
GO
ALTER TABLE [dbo].[accounts_notificationlist] CHECK CONSTRAINT [accounts_notificationlist_AssetsDetail_id_0882003e_fk_accounts_assetsdetaillist_id]
GO
ALTER TABLE [dbo].[accounts_notificationlist]  WITH CHECK ADD  CONSTRAINT [accounts_notificationlist_Category_id_bcf9c013_fk_accounts_categorylist_id] FOREIGN KEY([Category_id])
REFERENCES [dbo].[accounts_categorylist] ([id])
GO
ALTER TABLE [dbo].[accounts_notificationlist] CHECK CONSTRAINT [accounts_notificationlist_Category_id_bcf9c013_fk_accounts_categorylist_id]
GO
ALTER TABLE [dbo].[accounts_notificationlist]  WITH CHECK ADD  CONSTRAINT [accounts_notificationlist_City_id_1e42b4b7_fk_accounts_citylist_id] FOREIGN KEY([City_id])
REFERENCES [dbo].[accounts_citylist] ([id])
GO
ALTER TABLE [dbo].[accounts_notificationlist] CHECK CONSTRAINT [accounts_notificationlist_City_id_1e42b4b7_fk_accounts_citylist_id]
GO
ALTER TABLE [dbo].[accounts_notificationlist]  WITH CHECK ADD  CONSTRAINT [accounts_notificationlist_SubCategory_id_7d3b3397_fk_accounts_subcategorylist_id] FOREIGN KEY([SubCategory_id])
REFERENCES [dbo].[accounts_subcategorylist] ([id])
GO
ALTER TABLE [dbo].[accounts_notificationlist] CHECK CONSTRAINT [accounts_notificationlist_SubCategory_id_7d3b3397_fk_accounts_subcategorylist_id]
GO
ALTER TABLE [dbo].[accounts_notificationlist]  WITH CHECK ADD  CONSTRAINT [accounts_notificationlist_Topic_id_f513e060_fk_accounts_topiclist_id] FOREIGN KEY([Topic_id])
REFERENCES [dbo].[accounts_topiclist] ([id])
GO
ALTER TABLE [dbo].[accounts_notificationlist] CHECK CONSTRAINT [accounts_notificationlist_Topic_id_f513e060_fk_accounts_topiclist_id]
GO
ALTER TABLE [dbo].[accounts_notificationlist]  WITH CHECK ADD  CONSTRAINT [accounts_notificationlist_ToUser_id_845895c7_fk_accounts_userlist_id] FOREIGN KEY([ToUser_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_notificationlist] CHECK CONSTRAINT [accounts_notificationlist_ToUser_id_845895c7_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_notificationlist]  WITH CHECK ADD  CONSTRAINT [accounts_notificationlist_UpdatedBy_id_979dabcb_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_notificationlist] CHECK CONSTRAINT [accounts_notificationlist_UpdatedBy_id_979dabcb_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_notificationlist]  WITH CHECK ADD  CONSTRAINT [accounts_notificationlist_User_id_e27d652c_fk_accounts_userlist_id] FOREIGN KEY([User_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_notificationlist] CHECK CONSTRAINT [accounts_notificationlist_User_id_e27d652c_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_responsetypelist]  WITH CHECK ADD  CONSTRAINT [accounts_responsetypelist_AddedBy_id_b9511ed7_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_responsetypelist] CHECK CONSTRAINT [accounts_responsetypelist_AddedBy_id_b9511ed7_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_responsetypelist]  WITH CHECK ADD  CONSTRAINT [accounts_responsetypelist_UpdatedBy_id_4344451e_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_responsetypelist] CHECK CONSTRAINT [accounts_responsetypelist_UpdatedBy_id_4344451e_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_AddedBy_id_22cb8fcc_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_AddedBy_id_22cb8fcc_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_AssetsDetail_id_377cf081_fk_accounts_assetsdetaillist_id] FOREIGN KEY([AssetsDetail_id])
REFERENCES [dbo].[accounts_assetsdetaillist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_AssetsDetail_id_377cf081_fk_accounts_assetsdetaillist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_Category_id_0ccd69c6_fk_accounts_categorylist_id] FOREIGN KEY([Category_id])
REFERENCES [dbo].[accounts_categorylist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_Category_id_0ccd69c6_fk_accounts_categorylist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_City_id_92a179d8_fk_accounts_citylist_id] FOREIGN KEY([City_id])
REFERENCES [dbo].[accounts_citylist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_City_id_92a179d8_fk_accounts_citylist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_FromUser_id_0e1347bb_fk_accounts_userlist_id] FOREIGN KEY([FromUser_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_FromUser_id_0e1347bb_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_SubCategory_id_2a79ffca_fk_accounts_subcategorylist_id] FOREIGN KEY([SubCategory_id])
REFERENCES [dbo].[accounts_subcategorylist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_SubCategory_id_2a79ffca_fk_accounts_subcategorylist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_Topic_id_fb01d624_fk_accounts_topiclist_id] FOREIGN KEY([Topic_id])
REFERENCES [dbo].[accounts_topiclist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_Topic_id_fb01d624_fk_accounts_topiclist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_ToUser_id_01420149_fk_accounts_userlist_id] FOREIGN KEY([ToUser_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_ToUser_id_01420149_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_UpdatedBy_id_d90991c6_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_UpdatedBy_id_d90991c6_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_reviewlist]  WITH CHECK ADD  CONSTRAINT [accounts_reviewlist_User_id_18398aa7_fk_accounts_userlist_id] FOREIGN KEY([User_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_reviewlist] CHECK CONSTRAINT [accounts_reviewlist_User_id_18398aa7_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_statelist]  WITH CHECK ADD  CONSTRAINT [accounts_statelist_CountryId_id_0712049f_fk_accounts_countrylist_id] FOREIGN KEY([CountryId_id])
REFERENCES [dbo].[accounts_countrylist] ([id])
GO
ALTER TABLE [dbo].[accounts_statelist] CHECK CONSTRAINT [accounts_statelist_CountryId_id_0712049f_fk_accounts_countrylist_id]
GO
ALTER TABLE [dbo].[accounts_subcategorylist]  WITH CHECK ADD  CONSTRAINT [accounts_subcategorylist_AddedBy_id_2984cd6f_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_subcategorylist] CHECK CONSTRAINT [accounts_subcategorylist_AddedBy_id_2984cd6f_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_subcategorylist]  WITH CHECK ADD  CONSTRAINT [accounts_subcategorylist_Category_id_8a178960_fk_accounts_categorylist_id] FOREIGN KEY([Category_id])
REFERENCES [dbo].[accounts_categorylist] ([id])
GO
ALTER TABLE [dbo].[accounts_subcategorylist] CHECK CONSTRAINT [accounts_subcategorylist_Category_id_8a178960_fk_accounts_categorylist_id]
GO
ALTER TABLE [dbo].[accounts_subcategorylist]  WITH CHECK ADD  CONSTRAINT [accounts_subcategorylist_UpdatedBy_id_59760e5f_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_subcategorylist] CHECK CONSTRAINT [accounts_subcategorylist_UpdatedBy_id_59760e5f_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_subscriptiondetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_subscriptiondetaillist_AddedBy_id_f00a232f_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_subscriptiondetaillist] CHECK CONSTRAINT [accounts_subscriptiondetaillist_AddedBy_id_f00a232f_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_subscriptiondetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_subscriptiondetaillist_UpdatedBy_id_5947516e_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_subscriptiondetaillist] CHECK CONSTRAINT [accounts_subscriptiondetaillist_UpdatedBy_id_5947516e_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_subscriptiondetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_subscriptiondetaillist_User_id_fe594c74_fk_accounts_userlist_id] FOREIGN KEY([User_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_subscriptiondetaillist] CHECK CONSTRAINT [accounts_subscriptiondetaillist_User_id_fe594c74_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_subscriptionitemlist]  WITH CHECK ADD  CONSTRAINT [accounts_subscriptionitemlist_AddedBy_id_eab4d4a2_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_subscriptionitemlist] CHECK CONSTRAINT [accounts_subscriptionitemlist_AddedBy_id_eab4d4a2_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_subscriptionitemlist]  WITH CHECK ADD  CONSTRAINT [accounts_subscriptionitemlist_UpdatedBy_id_74d1a8bf_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_subscriptionitemlist] CHECK CONSTRAINT [accounts_subscriptionitemlist_UpdatedBy_id_74d1a8bf_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_subscriptionlist]  WITH CHECK ADD  CONSTRAINT [accounts_subscriptionlist_AddedBy_id_4eb9a3c0_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_subscriptionlist] CHECK CONSTRAINT [accounts_subscriptionlist_AddedBy_id_4eb9a3c0_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_subscriptionlist]  WITH CHECK ADD  CONSTRAINT [accounts_subscriptionlist_UpdatedBy_id_f78efd54_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_subscriptionlist] CHECK CONSTRAINT [accounts_subscriptionlist_UpdatedBy_id_f78efd54_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_templatetypelist]  WITH CHECK ADD  CONSTRAINT [accounts_templatetypelist_AddedBy_id_2a79227c_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_templatetypelist] CHECK CONSTRAINT [accounts_templatetypelist_AddedBy_id_2a79227c_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_templatetypelist]  WITH CHECK ADD  CONSTRAINT [accounts_templatetypelist_UpdatedBy_id_87bf70fb_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_templatetypelist] CHECK CONSTRAINT [accounts_templatetypelist_UpdatedBy_id_87bf70fb_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_topicdetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_topicdetaillist_AddedBy_id_c277352c_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_topicdetaillist] CHECK CONSTRAINT [accounts_topicdetaillist_AddedBy_id_c277352c_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_topicdetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_topicdetaillist_Topic_id_2af52a7b_fk_accounts_topiclist_id] FOREIGN KEY([Topic_id])
REFERENCES [dbo].[accounts_topiclist] ([id])
GO
ALTER TABLE [dbo].[accounts_topicdetaillist] CHECK CONSTRAINT [accounts_topicdetaillist_Topic_id_2af52a7b_fk_accounts_topiclist_id]
GO
ALTER TABLE [dbo].[accounts_topicdetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_topicdetaillist_UpdatedBy_id_aed5fb4c_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_topicdetaillist] CHECK CONSTRAINT [accounts_topicdetaillist_UpdatedBy_id_aed5fb4c_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_topicdetaillist]  WITH CHECK ADD  CONSTRAINT [accounts_topicdetaillist_User_id_8ceadc22_fk_accounts_userlist_id] FOREIGN KEY([User_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_topicdetaillist] CHECK CONSTRAINT [accounts_topicdetaillist_User_id_8ceadc22_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_topiclist]  WITH CHECK ADD  CONSTRAINT [accounts_topiclist_AddedBy_id_a558c643_fk_accounts_userlist_id] FOREIGN KEY([AddedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_topiclist] CHECK CONSTRAINT [accounts_topiclist_AddedBy_id_a558c643_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_topiclist]  WITH CHECK ADD  CONSTRAINT [accounts_topiclist_Category_id_105cd870_fk_accounts_categorylist_id] FOREIGN KEY([Category_id])
REFERENCES [dbo].[accounts_categorylist] ([id])
GO
ALTER TABLE [dbo].[accounts_topiclist] CHECK CONSTRAINT [accounts_topiclist_Category_id_105cd870_fk_accounts_categorylist_id]
GO
ALTER TABLE [dbo].[accounts_topiclist]  WITH CHECK ADD  CONSTRAINT [accounts_topiclist_City_id_4a408352_fk_accounts_citylist_id] FOREIGN KEY([City_id])
REFERENCES [dbo].[accounts_citylist] ([id])
GO
ALTER TABLE [dbo].[accounts_topiclist] CHECK CONSTRAINT [accounts_topiclist_City_id_4a408352_fk_accounts_citylist_id]
GO
ALTER TABLE [dbo].[accounts_topiclist]  WITH CHECK ADD  CONSTRAINT [accounts_topiclist_CloseBy_id_2dcfa0cb_fk_accounts_userlist_id] FOREIGN KEY([CloseBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_topiclist] CHECK CONSTRAINT [accounts_topiclist_CloseBy_id_2dcfa0cb_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_topiclist]  WITH CHECK ADD  CONSTRAINT [accounts_topiclist_ForceCloseCategory_id_2d380097_fk_accounts_forceclosecategorylist_id] FOREIGN KEY([ForceCloseCategory_id])
REFERENCES [dbo].[accounts_forceclosecategorylist] ([id])
GO
ALTER TABLE [dbo].[accounts_topiclist] CHECK CONSTRAINT [accounts_topiclist_ForceCloseCategory_id_2d380097_fk_accounts_forceclosecategorylist_id]
GO
ALTER TABLE [dbo].[accounts_topiclist]  WITH CHECK ADD  CONSTRAINT [accounts_topiclist_UpdatedBy_id_a71815ba_fk_accounts_userlist_id] FOREIGN KEY([UpdatedBy_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_topiclist] CHECK CONSTRAINT [accounts_topiclist_UpdatedBy_id_a71815ba_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_topiclist]  WITH CHECK ADD  CONSTRAINT [accounts_topiclist_User_id_2ac89a9b_fk_accounts_userlist_id] FOREIGN KEY([User_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_topiclist] CHECK CONSTRAINT [accounts_topiclist_User_id_2ac89a9b_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_topicsubcats]  WITH CHECK ADD  CONSTRAINT [accounts_topicsubcats_subcat_id_ce2d895c_fk_accounts_subcategorylist_id] FOREIGN KEY([subcat_id])
REFERENCES [dbo].[accounts_subcategorylist] ([id])
GO
ALTER TABLE [dbo].[accounts_topicsubcats] CHECK CONSTRAINT [accounts_topicsubcats_subcat_id_ce2d895c_fk_accounts_subcategorylist_id]
GO
ALTER TABLE [dbo].[accounts_topicsubcats]  WITH CHECK ADD  CONSTRAINT [accounts_topicsubcats_Topic_id_cf0bbe74_fk_accounts_topiclist_id] FOREIGN KEY([Topic_id])
REFERENCES [dbo].[accounts_topiclist] ([id])
GO
ALTER TABLE [dbo].[accounts_topicsubcats] CHECK CONSTRAINT [accounts_topicsubcats_Topic_id_cf0bbe74_fk_accounts_topiclist_id]
GO
ALTER TABLE [dbo].[accounts_userlist]  WITH CHECK ADD  CONSTRAINT [accounts_userlist_Application_id_ca1e0301_fk_accounts_appliationlist_id] FOREIGN KEY([Application_id])
REFERENCES [dbo].[accounts_appliationlist] ([id])
GO
ALTER TABLE [dbo].[accounts_userlist] CHECK CONSTRAINT [accounts_userlist_Application_id_ca1e0301_fk_accounts_appliationlist_id]
GO
ALTER TABLE [dbo].[accounts_userlist]  WITH CHECK ADD  CONSTRAINT [accounts_userlist_usertype_id_7bdd8b0e_fk_accounts_usertype_id] FOREIGN KEY([usertype_id])
REFERENCES [dbo].[accounts_usertype] ([id])
GO
ALTER TABLE [dbo].[accounts_userlist] CHECK CONSTRAINT [accounts_userlist_usertype_id_7bdd8b0e_fk_accounts_usertype_id]
GO
ALTER TABLE [dbo].[accounts_userlist_groups]  WITH CHECK ADD  CONSTRAINT [accounts_userlist_groups_group_id_e71efb12_fk_auth_group_id] FOREIGN KEY([group_id])
REFERENCES [dbo].[auth_group] ([id])
GO
ALTER TABLE [dbo].[accounts_userlist_groups] CHECK CONSTRAINT [accounts_userlist_groups_group_id_e71efb12_fk_auth_group_id]
GO
ALTER TABLE [dbo].[accounts_userlist_groups]  WITH CHECK ADD  CONSTRAINT [accounts_userlist_groups_userlist_id_46213270_fk_accounts_userlist_id] FOREIGN KEY([userlist_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_userlist_groups] CHECK CONSTRAINT [accounts_userlist_groups_userlist_id_46213270_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[accounts_userlist_user_permissions]  WITH CHECK ADD  CONSTRAINT [accounts_userlist_user_permissions_permission_id_3bdfac29_fk_auth_permission_id] FOREIGN KEY([permission_id])
REFERENCES [dbo].[auth_permission] ([id])
GO
ALTER TABLE [dbo].[accounts_userlist_user_permissions] CHECK CONSTRAINT [accounts_userlist_user_permissions_permission_id_3bdfac29_fk_auth_permission_id]
GO
ALTER TABLE [dbo].[accounts_userlist_user_permissions]  WITH CHECK ADD  CONSTRAINT [accounts_userlist_user_permissions_userlist_id_142db341_fk_accounts_userlist_id] FOREIGN KEY([userlist_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[accounts_userlist_user_permissions] CHECK CONSTRAINT [accounts_userlist_user_permissions_userlist_id_142db341_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[auth_group_permissions]  WITH CHECK ADD  CONSTRAINT [auth_group_permissions_group_id_b120cbf9_fk_auth_group_id] FOREIGN KEY([group_id])
REFERENCES [dbo].[auth_group] ([id])
GO
ALTER TABLE [dbo].[auth_group_permissions] CHECK CONSTRAINT [auth_group_permissions_group_id_b120cbf9_fk_auth_group_id]
GO
ALTER TABLE [dbo].[auth_group_permissions]  WITH CHECK ADD  CONSTRAINT [auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id] FOREIGN KEY([permission_id])
REFERENCES [dbo].[auth_permission] ([id])
GO
ALTER TABLE [dbo].[auth_group_permissions] CHECK CONSTRAINT [auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id]
GO
ALTER TABLE [dbo].[auth_permission]  WITH CHECK ADD  CONSTRAINT [auth_permission_content_type_id_2f476e4b_fk_django_content_type_id] FOREIGN KEY([content_type_id])
REFERENCES [dbo].[django_content_type] ([id])
GO
ALTER TABLE [dbo].[auth_permission] CHECK CONSTRAINT [auth_permission_content_type_id_2f476e4b_fk_django_content_type_id]
GO
ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id] FOREIGN KEY([content_type_id])
REFERENCES [dbo].[django_content_type] ([id])
GO
ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id]
GO
ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_user_id_c564eba6_fk_accounts_userlist_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_user_id_c564eba6_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[social_auth_usersocialauth]  WITH CHECK ADD  CONSTRAINT [social_auth_usersocialauth_user_id_17d28448_fk_accounts_userlist_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[accounts_userlist] ([id])
GO
ALTER TABLE [dbo].[social_auth_usersocialauth] CHECK CONSTRAINT [social_auth_usersocialauth_user_id_17d28448_fk_accounts_userlist_id]
GO
ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_action_flag_a8637d59_check] CHECK  (([action_flag]>=(0)))
GO
ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_action_flag_a8637d59_check]
GO
ALTER TABLE [dbo].[social_auth_partial]  WITH CHECK ADD  CONSTRAINT [social_auth_partial_next_step_0f2849be_check] CHECK  (([next_step]>=(0)))
GO
ALTER TABLE [dbo].[social_auth_partial] CHECK CONSTRAINT [social_auth_partial_next_step_0f2849be_check]
GO
/****** Object:  StoredProcedure [dbo].[activateCat]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[activateCat]
	@id int = NULL
AS
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=1  WHERE Category_id=@id;
UPDATE [dbo].[accounts_categorylist] SET IsActive=1 WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[activateCity]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[activateCity]
	@id int = NULL
AS
UPDATE [dbo].[accounts_topicdetaillist] SET IsActive=1 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id=@id);
UPDATE [dbo].[accounts_assetsdetaillist] SET IsActive=1 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id=@id);
UPDATE [dbo].[accounts_topiclist] SET IsActive=1  WHERE City_id=@id;
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=1  WHERE Category_id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id=@id);
UPDATE [dbo].[accounts_addresslist] SET IsActive=1 WHERE CityId_id=@id;
UPDATE [dbo].[accounts_categorylist] SET IsActive=1 WHERE id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id=@id);
UPDATE [dbo].[accounts_citylist] SET IsActive=1 WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[activateCountry]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[activateCountry]
	@id int = NULL
AS

UPDATE [dbo].[accounts_topicdetaillist] SET IsActive=1 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id)));
UPDATE [dbo].[accounts_assetsdetaillist] SET IsActive=1 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id)));
UPDATE [dbo].[accounts_topiclist] SET IsActive=1  WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id));
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=1  WHERE Category_id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id)));
UPDATE [dbo].[accounts_addresslist] SET IsActive=1 WHERE CityId_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id));
UPDATE [dbo].[accounts_categorylist] SET IsActive=1 WHERE id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id)));
UPDATE [dbo].[accounts_citylist] SET IsActive=1 WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id);
UPDATE [dbo].[accounts_statelist] SET IsActive=1 WHERE CountryId_id=@id;
UPDATE [dbo].[accounts_countrylist] SET IsActive=1 WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[activateState]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[activateState]
	@id int = NULL
AS
UPDATE [dbo].[accounts_topicdetaillist] SET IsActive=1 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id));
UPDATE [dbo].[accounts_assetsdetaillist] SET IsActive=1 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id));
UPDATE [dbo].[accounts_topiclist] SET IsActive=1  WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id);
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=1  WHERE Category_id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id));
UPDATE [dbo].[accounts_addresslist] SET IsActive=1 WHERE CityId_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id);
UPDATE [dbo].[accounts_categorylist] SET IsActive=1 WHERE id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id));
UPDATE [dbo].[accounts_citylist] SET IsActive=1 WHERE StateId_id=@id;
UPDATE [dbo].[accounts_statelist] SET IsActive=1 WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[activateSubCat]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[activateSubCat]
	@id int = NULL
AS
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=1 WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[addCatInCity]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
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
/****** Object:  StoredProcedure [dbo].[addJobPost]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
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
	@UpdatedBy_id int = NULL,
	@User_id int = NULL,
	@content nvarchar(1000) = NULL

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
		   ,[UpdatedBy_id]
		   ,[User_id]
		   ,[content])
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
		@UpdatedBy_id,
		@User_id,
		@content
	)
GO
/****** Object:  StoredProcedure [dbo].[addUser]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
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
	@date_joined datetime2(7) = NULL,
	@city nvarchar(30) = 'NA'
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
		   ,[date_joined]
		   ,[City])
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
		@date_joined,
		@city
	)
GO
/****** Object:  StoredProcedure [dbo].[addUserAddressList]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[addUserAddressList]
	@street nvarchar(500) = NULL,
	@zip_code nvarchar(50) = NULL,
	@added_date datetime2(7) = NULL,
	@user_id int = NULL,
	@city int = NULL,
	@isActive bit = 1

AS

INSERT INTO [dbo].[accounts_addresslist]
           ([Street]
           ,[ZipCode]
           ,[AddedDate]
           ,[user_id]
           ,[CityId_id]
		   ,[isActive])
     VALUES
           (@street
           ,@zip_code
           ,@added_date
           ,@user_id
           ,@city
		   ,@isActive)
GO
/****** Object:  StoredProcedure [dbo].[addUserWithType]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
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
	@date_joined datetime2(7) = NULL,
	@city nvarchar(30) = 'NA'
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
		   ,[date_joined]
		   ,[City])
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
		@date_joined,
		@city
	)
GO
/****** Object:  StoredProcedure [dbo].[AdminAllCategory]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[AdminAllCategory]
AS
SELECT a.id as cat_id, a.IsActive as cat_active, * FROM [dbo].[accounts_categorylist] a, [dbo].[accounts_citylist] b,[dbo].[accounts_statelist] c, [dbo].[accounts_countrylist] d, [dbo].[accounts_categoryincity] e WHERE e.category_id=a.id AND b.id=e.city_id AND c.id=b.StateId_id AND d.id=c.CountryId_id;
GO
/****** Object:  StoredProcedure [dbo].[AdminAllCountry]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[AdminAllCountry]
AS
Select * from dbo.accounts_CountryList
GO
/****** Object:  StoredProcedure [dbo].[AdminAllSubCategory]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[AdminAllSubCategory]
AS
SELECT d.id as subcat_id, d.IsActive as subcat_active, * FROM [dbo].[accounts_categorylist] a, [dbo].[accounts_citylist] b,[dbo].[accounts_statelist] c, dbo.accounts_subcategorylist d, [dbo].[accounts_categoryincity] e, [dbo].[accounts_countrylist] f WHERE e.category_id=a.id AND b.id=e.city_id AND c.id=b.StateId_id AND f.id=c.CountryId_id AND d.Category_id=e.category_id;
GO
/****** Object:  StoredProcedure [dbo].[AdminGetAllAdmin]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[AdminGetAllAdmin]
AS
Select * from [dbo].[accounts_userlist] WHERE is_superuser = 1
GO
/****** Object:  StoredProcedure [dbo].[AdminGetAllStaff]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[AdminGetAllStaff]
AS
Select * from [dbo].[accounts_userlist] WHERE is_staff = 1
GO
/****** Object:  StoredProcedure [dbo].[AdminGetCity]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[AdminGetCity]
AS
SELECT *, StateName=(SELECT State FROM [dbo].[accounts_statelist] WHERE id=StateId_id), CountryName=(SELECT [Country] FROM [dbo].[accounts_countrylist] WHERE id=(SELECT CountryId_id FROM [dbo].[accounts_statelist] WHERE id=StateId_id)) FROM [dbo].[accounts_citylist]
GO
/****** Object:  StoredProcedure [dbo].[AdminGetState]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[AdminGetState]
AS
SELECT *, CountryName=(Select Country From [dbo].[accounts_countrylist] WHERE id=CountryId_id) FROM [dbo].[accounts_statelist]
GO
/****** Object:  StoredProcedure [dbo].[allCategory]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[allCategory]
AS
SELECT * FROM [dbo].[accounts_categorylist]
GO
/****** Object:  StoredProcedure [dbo].[allCountry]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[allCountry]
AS
Select * from dbo.accounts_CountryList
GO
/****** Object:  StoredProcedure [dbo].[allSubCategory]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[allSubCategory]
AS
Select *, CategoryName=(SELECT CategoryName FROM [dbo].[accounts_categorylist] WHERE id=Category_id)  from dbo.accounts_subcategorylist WHERE IsActive=1
GO
/****** Object:  StoredProcedure [dbo].[applyJob]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[applyJob]
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
/****** Object:  StoredProcedure [dbo].[createCategory]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
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
		   ,[UpdatedDate]
		   ,[AddedDate]
           ,[IsActive])
VALUES
	(
		@CategoryName,
		@AddedBy,
		@AddedDate,
		@AddedDate,
		@IsActive
	)
GO
/****** Object:  StoredProcedure [dbo].[createChatRecord]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[createChatRecord]
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
GO
/****** Object:  StoredProcedure [dbo].[createCity]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[createCity]
	@state_id int = NULL,
	@lat float = NULL,
	@log float = NULL,
	@IsActive bit = 1,
	@city nvarchar(100) = NULL,
	@addedDate datetime2(7) = NULL,
	@addedby_id int = NULL
AS
INSERT INTO [dbo].[accounts_citylist]
           ([StateId_id]
           ,[Latitude]
           ,[Longitude]
		   ,[IsActive]
		   ,[City]
           ,[AddedDate]
           ,[UpdatedDate]
           ,[AddedBy_id]
           ,[UpdatedBy_id])
     VALUES
           (@state_id,
			@lat,
			@log,
			@IsActive,
			@city,
			@addedDate,
			@addedDate,
			@addedby_id,
			@addedby_id)
GO
/****** Object:  StoredProcedure [dbo].[createCountry]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[createCountry]
	@Country nvarchar(100) = NULL,
	@IsActive bit = 1
AS
INSERT INTO [dbo].[accounts_countrylist]
           ([Country]
           ,[IsActive])
     VALUES
           (@Country,
		   @IsActive)
GO
/****** Object:  StoredProcedure [dbo].[createState]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[createState]
	@country_id int = NULL,
	@IsActive bit = 1,
	@state nvarchar(100) = NULL
AS
INSERT INTO [dbo].[accounts_statelist]
           ([CountryId_id]
           ,[IsActive]
		   ,[State])
     VALUES
           (@country_id,
		   @IsActive,
		   @state)
GO
/****** Object:  StoredProcedure [dbo].[createSubCategory]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[createSubCategory]
	@SubCategoryName nvarchar(300) = NULL,
	@AddedBy int = NULL,
	@cat_id int = NULL,
	@AddedDate datetime2(7) = NULL,
	@IsActive bit = 1
AS
INSERT INTO [dbo].[accounts_subcategorylist]
           ([SubCategoryName]
           ,[AddedDate]
           ,[UpdatedDate]
           ,[IsActive]
           ,[AddedBy_id]
           ,[Category_id]
           ,[UpdatedBy_id])
VALUES
	(
		@SubCategoryName,
		@AddedDate,
		@AddedDate,
		@IsActive,
		@AddedBy,
		@cat_id,
		@AddedBy
	)


GO
/****** Object:  StoredProcedure [dbo].[createTopicAsset]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
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
/****** Object:  StoredProcedure [dbo].[createTopicSubCat]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[createTopicSubCat]
	@TopidId int = NULL,
	@subCatId int = NULL

AS

INSERT INTO [dbo].[accounts_topicsubcats]
           ([Topic_id]
           ,[subcat_id])
     VALUES
           (@TopidId
           ,@subCatId)
GO
/****** Object:  StoredProcedure [dbo].[deleteCat]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[deleteCat]
	@id int = NULL
AS
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=0  WHERE Category_id=@id;
UPDATE [dbo].[accounts_categorylist] SET IsActive=0 WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[deleteCategory]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[deleteCategory]
	@id int = NULL
AS
DELETE FROM [dbo].[accounts_categorylist] WHERE [id] = @id
GO
/****** Object:  StoredProcedure [dbo].[deleteCatFromCity]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[deleteCatFromCity]
	@city_id int = NULL,
	@cat_id int = NULL
AS
DELETE FROM [dbo].[accounts_categoryincity] WHERE [category_id] = @cat_id AND [city_id]=@city_id
DELETE FROM [dbo].[accounts_categorylist] WHERE [id]=@cat_id
GO
/****** Object:  StoredProcedure [dbo].[deleteCity]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[deleteCity]
	@id int = NULL
AS
UPDATE [dbo].[accounts_topicdetaillist] SET IsActive=0 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id=@id);
UPDATE [dbo].[accounts_assetsdetaillist] SET IsActive=0 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id=@id);
UPDATE [dbo].[accounts_topiclist] SET IsActive=0  WHERE City_id=@id;
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=0  WHERE Category_id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id=@id);
UPDATE [dbo].[accounts_addresslist] SET IsActive=0 WHERE CityId_id=@id;
UPDATE [dbo].[accounts_categorylist] SET IsActive=0 WHERE id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id=@id);
UPDATE [dbo].[accounts_citylist] SET IsActive=0 WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[deleteCountry]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[deleteCountry]
	@id int = NULL
AS

UPDATE [dbo].[accounts_topicdetaillist] SET IsActive=0 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id)));
UPDATE [dbo].[accounts_assetsdetaillist] SET IsActive=0 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id)));
UPDATE [dbo].[accounts_topiclist] SET IsActive=0  WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id));
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=0  WHERE Category_id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id)));
UPDATE [dbo].[accounts_addresslist] SET IsActive=0 WHERE CityId_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id));
UPDATE [dbo].[accounts_categorylist] SET IsActive=0 WHERE id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id)));
UPDATE [dbo].[accounts_citylist] SET IsActive=0 WHERE StateId_id IN (SELECT [id] FROM [dbo].[accounts_statelist] WHERE CountryId_id=@id);
UPDATE [dbo].[accounts_statelist] SET IsActive=0 WHERE CountryId_id=@id;
UPDATE [dbo].[accounts_countrylist] SET IsActive=0 WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[deleteState]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[deleteState]
	@id int = NULL
AS
UPDATE [dbo].[accounts_topicdetaillist] SET IsActive=0 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id));
UPDATE [dbo].[accounts_assetsdetaillist] SET IsActive=0 WHERE Topic_id IN (SELECT [id] FROM [dbo].[accounts_topiclist] WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id));
UPDATE [dbo].[accounts_topiclist] SET IsActive=0  WHERE City_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id);
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=0  WHERE Category_id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id));
UPDATE [dbo].[accounts_addresslist] SET IsActive=0 WHERE CityId_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id);
UPDATE [dbo].[accounts_categorylist] SET IsActive=0 WHERE id IN (SELECT [category_id] FROM [dbo].[accounts_categoryincity] WHERE city_id IN (SELECT [id] FROM [dbo].[accounts_citylist] WHERE StateId_id=@id));
UPDATE [dbo].[accounts_citylist] SET IsActive=0 WHERE StateId_id=@id;
UPDATE [dbo].[accounts_statelist] SET IsActive=0 WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[deleteSubCat]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[deleteSubCat]
	@id int = NULL
AS
UPDATE [dbo].[accounts_subcategorylist] SET IsActive=0  WHERE id=@id;
GO
/****** Object:  StoredProcedure [dbo].[generateOTP]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
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
/****** Object:  StoredProcedure [dbo].[getAddressList]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getAddressList]
AS
SELECT * FROM [dbo].[accounts_addresslist]  WHERE IsActive=1
GO
/****** Object:  StoredProcedure [dbo].[getAdminCity]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getAdminCity]
AS
SELECT *, StateName=(SELECT State FROM [dbo].[accounts_statelist] WHERE id=StateId_id) FROM [dbo].[accounts_citylist]
GO
/****** Object:  StoredProcedure [dbo].[getAllAdmin]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[getAllAdmin]
AS
Select * from [dbo].[accounts_userlist] WHERE is_superuser = 1
GO
/****** Object:  StoredProcedure [dbo].[getAllJobs]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getAllJobs]
AS
Select * from [dbo].[accounts_topiclist] WHERE IsActive=1
GO
/****** Object:  StoredProcedure [dbo].[getAllStaff]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[getAllStaff]
AS
Select * from [dbo].[accounts_userlist] WHERE is_staff = 1
GO
/****** Object:  StoredProcedure [dbo].[getApplicationsForReview]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[getApplicationsForReview]
	@user_id nvarchar(300) = NULL

AS
SELECT A.id as job_id, B.id as applied_id, B.AddedDate as applied_date, C.first_name as applier_name, C.id as applied_by_id, *  FROM [dbo].[accounts_topiclist] A, [dbo].[accounts_topicdetaillist] B, [dbo].[accounts_userlist] C  WHERE A.User_id=@user_id AND B.Topic_id=A.id AND C.id=B.User_id
GO
/****** Object:  StoredProcedure [dbo].[getAppliedJobsList]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[getAppliedJobsList]
	@user_id int = NULL

AS
SELECT * FROM [dbo].[accounts_topicdetaillist] WHERE [User_id]=@user_id
GO
/****** Object:  StoredProcedure [dbo].[getCategory]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getCategory]
	@city varchar(30) = NULL
AS
SELECT * FROM [dbo].[accounts_userlist] LEFT JOIN [dbo].[accounts_categorylist] ON accounts_userlist.ID=accounts_categorylist.ID WHERE [City]=@city AND [usertype_id] = 1
GO
/****** Object:  StoredProcedure [dbo].[getChatRecord]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getChatRecord]
	@client_id int = NULL,
	@professional_id int = NULL,
	@room_name nvarchar(300) = NULL
AS

SELECT [message],[side],[TimeStamp] FROM [dbo].[accounts_chatrecord] WHERE [client_id] = @client_id AND [professional_id] = @professional_id AND [room_name]=@room_name
GO
/****** Object:  StoredProcedure [dbo].[getCity]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getCity]
AS
SELECT *, StateName=(SELECT State FROM [dbo].[accounts_statelist] WHERE id=StateId_id) FROM [dbo].[accounts_citylist]  WHERE IsActive=1
GO
/****** Object:  StoredProcedure [dbo].[getCityByState]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getCityByState]
AS
SELECT [id]
      ,[City]
      ,[StateId_id]
  FROM [dbo].[accounts_citylist]  WHERE IsActive=1

GO
/****** Object:  StoredProcedure [dbo].[getClientConnections]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[getClientConnections]
	@client_id int = NULL
AS

SELECT DISTINCT [professional_id], [first_name], [room_name], [topic_id], TopicName=(SELECT [TopicName] FROM [dbo].[accounts_topiclist] WHERE id=topic_id) FROM [dbo].[accounts_chatrecord] INNER JOIN [dbo].[accounts_userlist] ON [dbo].[accounts_chatrecord].[professional_id]=[dbo].[accounts_userlist].[id] AND [dbo].[accounts_chatrecord].[client_id]=@client_id
GO
/****** Object:  StoredProcedure [dbo].[getCountry]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getCountry]
AS
SELECT * FROM [dbo].[accounts_countrylist]
GO
/****** Object:  StoredProcedure [dbo].[getEachJob]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getEachJob]
	@id int = NULL
AS
Select * from [dbo].[accounts_topiclist] WHERE id=@id
GO
/****** Object:  StoredProcedure [dbo].[getFilterJobs]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[getFilterJobs]
	@city_id int = NULL,
	@subcat_id int=NULL,
	@cat_id int = NULL
AS

SELECT DISTINCT A.id, A.TopicName, B.first_name FROM [dbo].[accounts_topiclist] A, dbo.accounts_userlist B, [dbo].[accounts_addresslist] C, [dbo].[accounts_topicsubcats] D WHERE A.City_id=@city_id AND A.Category_id=@cat_id AND B.id=A.AddedBy_id AND D.subcat_id=@subcat_id AND A.id=D.Topic_id;
GO
/****** Object:  StoredProcedure [dbo].[getJobById]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[getJobById]
	@job_id int = NULL
AS

SELECT * FROM [dbo].[accounts_topiclist] WHERE id=@job_id
GO
/****** Object:  StoredProcedure [dbo].[getJobsInId]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[getJobsInId]
	@job_id_list nvarchar(300) = NULL

AS
SELECT * FROM [dbo].[accounts_topiclist] WHERE [id] IN ((Select * from dbo.SplitString(@job_id_list, ',')))
GO
/****** Object:  StoredProcedure [dbo].[getMyCityJobs]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getMyCityJobs]
	@user_id int = NULL

AS
SELECT [dbo].[accounts_topiclist].[id], [dbo].[accounts_topiclist].[TopicName], first_name=(SELECT [first_name] FROM dbo.accounts_userlist WHERE id=[dbo].[accounts_topiclist].[User_id]) FROM [dbo].[accounts_addresslist] INNER JOIN [dbo].[accounts_userlist] ON [dbo].[accounts_addresslist].[user_id]=[dbo].[accounts_userlist].[id] INNER JOIN [dbo].[accounts_topiclist] ON [dbo].[accounts_addresslist].[CityId_id]=[dbo].[accounts_topiclist].[City_id] WHERE [dbo].[accounts_userlist].[id]=@user_id AND [dbo].[accounts_topiclist].[IsActive]=1
GO
/****** Object:  StoredProcedure [dbo].[getMyJobs]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getMyJobs]
	@user_id int = NULL
AS
Select * from [dbo].[accounts_topiclist] WHERE AddedBy_id=@user_id
GO
/****** Object:  StoredProcedure [dbo].[getProfessionalConnections]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[getProfessionalConnections]
	@professinoal_id int = NULL
AS
SELECT DISTINCT [client_id], [first_name], [room_name], [topic_id], TopicName=(SELECT [TopicName] FROM [dbo].[accounts_topiclist] WHERE id=topic_id) FROM [dbo].[accounts_chatrecord] INNER JOIN [dbo].[accounts_userlist] ON [dbo].[accounts_chatrecord].[client_id]=[dbo].[accounts_userlist].[id] AND [dbo].[accounts_chatrecord].[professional_id]=@professinoal_id
GO
/****** Object:  StoredProcedure [dbo].[getState]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getState]
AS
SELECT *, CountryName=(Select Country From [dbo].[accounts_countrylist] WHERE id=CountryId_id) FROM [dbo].[accounts_statelist]
GO
/****** Object:  StoredProcedure [dbo].[getUser]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getUser]
	@email nvarchar(100) = NULL
AS
SELECT * FROM [dbo].[accounts_userlist] WHERE [email]=@email
GO
/****** Object:  StoredProcedure [dbo].[getUserAddress]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getUserAddress]
	@user_id int = NULL
AS
SELECT * FROM [dbo].[accounts_addresslist]
INNER JOIN [dbo].[accounts_citylist] ON accounts_addresslist.CityId_id=accounts_citylist.id
INNER JOIN [dbo].[accounts_statelist] ON accounts_citylist.StateId_id= accounts_statelist.id
INNER JOIN [dbo].[accounts_countrylist] ON accounts_statelist.CountryId_id=accounts_countrylist.id
WHERE accounts_addresslist.user_id=@user_id

GO
/****** Object:  StoredProcedure [dbo].[getUserType]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getUserType]
	@id int = NULL
AS
SELECT [UserType] FROM [dbo].[accounts_usertype] WHERE [id] = @id
GO
/****** Object:  StoredProcedure [dbo].[getUserWithId]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[getUserWithId]
	@id int = NULL
AS
SELECT * FROM [dbo].[accounts_userlist] WHERE [id]=@id
GO
/****** Object:  StoredProcedure [dbo].[updateJob]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[updateJob]
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
GO
/****** Object:  StoredProcedure [dbo].[updateJobPost]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[updateJobPost]
	@id int = Null,
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
UPDATE [dbo].[accounts_topiclist]
   SET     [TopicName]=@TopicName,
		   [TopicDate]=@TopicDate,
           [AddedDate]=@AddedDate,
           [UpdatedDate]=@UpdatedDate,
		   [IsActive]=@IsActive,
           [IsClose]=@IsClose,
		   [CloseDate]=@CloseDate,
           [ForceCloseReason]=@ForceCloseReason,
           [IsNotification]=@IsNotification,
           [SMSText]=@SMSText,
           [WhatsAppText]=@WhatsAppText,
           [AddedBy_id]=@AddedBy_id,
		   [Category_id]=Category_id,
		   [City_id]=@City_id,
		   [CloseBy_id]=@CloseBy_id,
		   [ForceCloseCategory_id]=@ForceCloseCategory_id,
		   [UpdatedBy_id]=@UpdatedBy_id,
		   [User_id]=@User_id
WHERE id = @id
GO
/****** Object:  StoredProcedure [dbo].[UpdateUser]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[UpdateUser]
	@first_name nvarchar(30) = NULL,
	@last_name nvarchar(30) = NULL,
	@email nvarchar(100) = NULL,
	@ContactCell nvarchar(100) = NULL,
	@ApplicationId int = NULL,
	@street nvarchar(500) = NULL,
	@zip_code nvarchar(50) = NULL,
	@user_id int = NULL,
	@city int = NULL
AS

UPDATE [dbo].[accounts_userlist]
   SET [first_name] = @first_name
      ,[last_name] = @last_name
      ,[email] = @email
      ,[ContactCell] =@ContactCell
      ,[Application_id] = @ApplicationId
 WHERE [id] = @user_id

 UPDATE [dbo].[accounts_addresslist]
   SET [Street] = @street
      ,[ZipCode] = @zip_code
      ,[CityId_id] = @city
 WHERE [user_id]=@user_id

GO
/****** Object:  StoredProcedure [dbo].[userPasswordChange]    Script Date: 24-02-2021 10:39:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[userPasswordChange]
	@password nvarchar(128) = NULL,
	@user_id int = NULL
AS
UPDATE [dbo].[accounts_userlist]
   SET [password] = @password
 WHERE [id] = @user_id
GO
