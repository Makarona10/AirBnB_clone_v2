CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USE IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON performance_schema . * to 'hbnb_dev'@'localhost'; 