-- Create a new database named 'League'
CREATE DATABASE IF NOT EXISTS League;

-- Use the 'League' database
USE League;

-- Create a table to store card details
CREATE TABLE IF NOT EXISTS card_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_number VARCHAR(16) NOT NULL,
    nickname VARCHAR(50) NOT NULL,
    expiry_date VARCHAR(7) NOT NULL,
    cvc VARCHAR(4) NOT NULL,
    RP VARCHAR(4) NOT NULL
);