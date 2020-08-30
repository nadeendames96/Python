DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS tasklist;


-- Create 'User' table
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fname TEXT NOT NULL,
  lname TEXT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  email TEXT NOT NULL
);

-- Create 'task' table
CREATE TABLE task (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  prorites INTEGER NOT NULL,
  tasklist_id INTEGER

  -- FOREIGN KEY (tasklist_id) REFERENCES tasklist (id)
);

-- Create 'tasklist ' table
CREATE TABLE tasklist (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tasklistname TEXT NOT NULL,
  tasklistdescription TEXT NOT NULL,
  tasklistphoto TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  -- task_id INTEGER
  -- FOREIGN KEY (task_id) REFERENCES task (task_id)
  );

-- Create some dummy data

-- Create some users
INSERT INTO user (username,fname,lname, password,email)
VALUES ("Nadeen","Nadeen","Dames", "nadeen","nana@hotmail.com");
-- Create some posts
INSERT INTO task ( task_id,created, title, body,prorites)
VALUES (1,CURRENT_TIMESTAMP, "task 1", "Im' Flutter Developer.","LOW");

INSERT INTO tasklist (tasklistname,tasklistdescription,tasklistphoto,created)
VALUES ("Personality List","personality list","https://www.iconspng.com/images/task/task.jpg",CURRENT_TIMESTAMP)