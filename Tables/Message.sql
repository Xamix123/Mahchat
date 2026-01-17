CREATE TABLE [dbo].[Message] (
    [Id] INT IDENTITY(1,1) NOT NULL,
    [Content] VARCHAR(500) NOT NULL,
    [UserId] INT NOT NULL,
    [ChatId] INT NOT NULL,
    [CreatedAt] DATETIME2 NOT NULL DEFAULT GETDATE(),
    [UpdatedAt] DATETIME2 NULL,

    CONSTRAINT [Message_PK] PRIMARY KEY ([Id]),

    CONSTRAINT [FK_Message_User]
    FOREIGN KEY ([UserId])
    REFERENCES [dbo].[User] ([Id])
    ON DELETE CASCADE,

    CONSTRAINT [FK_Message_Chat]
    FOREIGN KEY ([ChatId])
    REFERENCES [dbo].[Chat] ([Id])
    ON DELETE CASCADE
);