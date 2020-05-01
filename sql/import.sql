-- user : mysql / pass : Password
-- mysql  Ver 14.14 Distrib 5.7.29, for Linux (x86_64) using  EditLine wrapper

CREATE DATABASE `rt` DEFAULT CHARACTER SET utf8;

use `rt`;

CREATE TABLE `airport`(
    `id` int AUTO_INCREMENT,
    `Name` varchar(74) DEFAULT NULL,
    `City` varchar(35) DEFAULT NULL,
    `Country` varchar(34) DEFAULT NULL,
    `IATA` varchar(16) DEFAULT NULL,
    `ICAO` varchar(6) DEFAULT NULL,
    `Latitude` double(9,6) DEFAULT NULL,
    `Longitude` double(9,6) DEFAULT NULL,
    `Altitude` varchar(19) DEFAULT NULL,
    `Timezone` varchar(5) DEFAULT NULL,
    `DST` varchar(3) DEFAULT NULL,
    `Tz database time` varchar(32) DEFAULT NULL,
    `zone` varchar(21) DEFAULT NULL,
    `Type` varchar(13) DEFAULT NULL,
    `Source` varchar(13) DEFAULT NULL,
    PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE "/var/www/html/random-travelers/sql/airport.csv" -- your path
INTO TABLE `airport`
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"';
