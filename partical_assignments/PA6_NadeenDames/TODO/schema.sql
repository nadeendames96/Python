DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS task;

-- Create 'User' table
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  email TEXT NOT NULL
);

-- Create 'Post' table
CREATE TABLE task (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (task_id) REFERENCES user (id)
);

-- Create some dummy data

-- Create some users
INSERT INTO user (username, password,email)
VALUES ("Nadeen", "nadeen","nana@hotmail.com");

-- Create some posts
INSERT INTO task ( task_id,created, title, body)
VALUES (1,CURRENT_TIMESTAMP, "task 1", "Im' Flutter Developer.");
