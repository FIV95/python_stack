mysql> CREATE DATABASE users;
Query OK, 1 row affected (0.01 sec)

mysql> USE users;
Database changed
mysql> CREATE TABLE users (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> first_name VARCHAR(50)
    -> last_name VARCHAR(50)
    -> email VARCHAR(100)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'last_name VARCHAR(50)
email VARCHAR(100)
)' at line 4
mysql> CREATE TABLE users (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> first_name VARCHAR(50),
    -> last_name VARCHAR(50),
    -> email VARCHAR(100)
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO users (first_name), last_name, email)
    -> VALUES ('Nelly', 'Turq', 'nellyistheQueen@aol.com'),
    -> ('Frankie', 'Law', franklaw@gmail.com),
    -> ('Frankie', 'Law', 'franklaw@gmail.com'),
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ', last_name, email)
VALUES ('Nelly', 'Turq', 'nellyistheQueen@aol.com'),
('Frank' at line 1
mysql> INSERT INTO users (first_name, last_name, email)
    -> VALUES ('Nelly', 'Turq', iamthequeen@aol.com);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '@aol.com)' at line 2
mysql> INSERT INTO users (first_name, last_name, email) VALUES ('Nelly', 'Turq', 'iamthequeen@aol.com');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO users (first_name, last_name, email) VALUES ('Frankie', 'Law', 'franklaw@gmail.com');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO users (first_name, last_name, email) VALUES ('Shadow', 'Escabar', 'Iamadog.com');
Query OK, 1 row affected (0.01 sec)

mysql> DESCRIBE users;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| first_name | varchar(50)  | YES  |     | NULL    |                |
| last_name  | varchar(50)  | YES  |     | NULL    |                |
| email      | varchar(100) | YES  |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+----+------------+-----------+---------------------+
| id | first_name | last_name | email               |
+----+------------+-----------+---------------------+
|  1 | Nelly      | Turq      | iamthequeen@aol.com |
|  2 | Frankie    | Law       | franklaw@gmail.com  |
|  3 | Shadow     | Escabar   | Iamadog.com         |
+----+------------+-----------+---------------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM users where email = franklaw@gmail.com
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '@gmail.com' at line 1
mysql> SELECT * FROM users WHERE email = franklaw@gmail.com
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '@gmail.com' at line 1
mysql> SELECT * FROM users WHERE email = 'franklaw@gmail.com'
    -> ;
+----+------------+-----------+--------------------+
| id | first_name | last_name | email              |
+----+------------+-----------+--------------------+
|  2 | Frankie    | Law       | franklaw@gmail.com |
+----+------------+-----------+--------------------+
1 row in set (0.00 sec)

mysql> SELECT * FROM users WHERE id = (SELECT MAX(id) FROM users);
+----+------------+-----------+-------------+
| id | first_name | last_name | email       |
+----+------------+-----------+-------------+
|  3 | Shadow     | Escabar   | Iamadog.com |
+----+------------+-----------+-------------+
1 row in set (0.00 sec)

mysql> UPDATE users SET last_name = 'Bugaboo-Escabar' WHERE id = 3;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> DELETE FROM users WHERE id = 2;
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM users ORDER_BY first_name;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'first_name' at line 1
mysql> SELECT *  FROM users ORDER BY first_name;
+----+------------+-----------------+---------------------+
| id | first_name | last_name       | email               |
+----+------------+-----------------+---------------------+
|  1 | Nelly      | Turq            | iamthequeen@aol.com |
|  3 | Shadow     | Bugaboo-Escabar | Iamadog.com         |
+----+------------+-----------------+---------------------+
2 rows in set (0.01 sec)

mysql> SELECT * FROM users ORDER BY first_name DESC;
+----+------------+-----------------+---------------------+
| id | first_name | last_name       | email               |
+----+------------+-----------------+---------------------+
|  3 | Shadow     | Bugaboo-Escabar | Iamadog.com         |
|  1 | Nelly      | Turq            | iamthequeen@aol.com |
+----+------------+-----------------+---------------------+
2 rows in set (0.01 sec)

mysql> notee
