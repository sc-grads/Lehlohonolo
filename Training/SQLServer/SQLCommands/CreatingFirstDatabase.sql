USE [MyFirstDatabase]
GO
INSERT INTO [dbo].[PersonalInfo]
           ([FirstName]
           ,[LastName]
           ,[DateOfBirth]
           ,[ID])
     VALUES
           ('Lehlohonolo',
           'Kete',
           '01-01-2023'
           ,777)
GO
select * from [dbo].[PersonalInfo]



