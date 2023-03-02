USE [MyFirstDatabase]
GO
INSERT INTO [dbo].[PersonalInfo]
           ([FirstName]
           ,[LastName]
           ,[DateOfBirth]
           ,[ID])
     VALUES
           ('Lehlohonolo',
           'Tladi',
           '01-01-2023'
           ,999)
GO
select * from [dbo].[PersonalInfo]


