CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);

INSERT INTO users(username, password_hash)
VALUES ('michael', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8')