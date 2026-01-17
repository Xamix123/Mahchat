CREATE TABLE [dbo].[ChatUser] (
    [Id] INT IDENTITY(1,1) NOT NULL,
    [UserId] INT NOT NULL,
    [ChatId] INT NOT NULL,

    CONSTRAINT [ChatUser_PK] PRIMARY KEY ([Id]),

    CONSTRAINT [FK_ChatUser_User]
    FOREIGN KEY ([UserId])
    REFERENCES [dbo].[User] ([Id])
    ON DELETE CASCADE,

    CONSTRAINT [FK_ChatUser_Chat]
    FOREIGN KEY ([ChatId])
    REFERENCES [dbo].[Chat] ([Id])
    ON DELETE CASCADE,

    CONSTRAINT [UQ_ChatUser_User_Chat]
    UNIQUE ([UserId], [ChatId])
    );