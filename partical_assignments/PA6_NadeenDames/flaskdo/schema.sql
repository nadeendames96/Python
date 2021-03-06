DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS TaskList;
DROP TABLE IF EXISTS Task;

-- Create 'User' table
CREATE TABLE User (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstname TEXT,
  lastname TEXT,
  username TEXT,
  email TEXT UNIQUE NOT NULL,
  picture TEXT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

  password TEXT NOT NULL
);

-- Create 'TaskList' table
CREATE TABLE TaskList (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  description TEXT,
  picture TEXT,
  FOREIGN KEY (user_id) REFERENCES user (id)
);

-- Create 'Task' table
CREATE TABLE Task (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_list_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  priority INTEGER NOT NULL,
  description TEXT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  picture TEXT,
  FOREIGN KEY (task_list_id) REFERENCES taskList (id)
);

