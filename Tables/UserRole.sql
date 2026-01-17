CREATE TABLE [dbo].[UserRole] (
    [Id] INT IDENTITY(1,1) NOT NULL,
    [UserId] INT NOT NULL,
    [RoleId] INT NOT NULL,

    CONSTRAINT [UserRole_PK] PRIMARY KEY ([Id]),

    CONSTRAINT [FK_UserRole_User]
    FOREIGN KEY ([UserId])
    REFERENCES [dbo].[User] ([Id])
    ON DELETE CASCADE,

    CONSTRAINT [FK_UserRole_Role]
    FOREIGN KEY ([RoleId])
    REFERENCES [dbo].[Role] ([Id])
    ON DELETE CASCADE,

    CONSTRAINT [UQ_UserRole_User_Role]
    UNIQUE ([UserId], [RoleId])
);