CREATE TABLE contact_info (
    id BIGSERIAL PRIMARY KEY,

    user_id BIGINT NOT NULL UNIQUE,
    contact_type_id BIGINT NOT NULL,

    value VARCHAR(255) NOT NULL,

    CONSTRAINT fk_contact_info_user
        FOREIGN KEY (user_id)
        REFERENCES app_user(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_contact_info_contact_type
        FOREIGN KEY (contact_type_id)
        REFERENCES contact_type(id)
);