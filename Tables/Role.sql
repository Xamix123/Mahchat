CREATE TABLE [dbo].[Role] (
    [Id] INT IDENTITY(1,1) NOT NULL,
    [Name] VARCHAR(40) NOT NULL,
    CONSTRAINT [Role_PK] PRIMARY KEY ([Id]),
    CONSTRAINT [UQ_Role_Name] UNIQUE ([Name])
);