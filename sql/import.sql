CREATE DATABASE IF NOT EXISTS `rt` DEFAULT CHARACTER SET utf8;

use `rt`;

CREATE TABLE IF NOT EXISTS `airport`(
    `id` int AUTO_INCREMENT,
    `name` varchar(74) DEFAULT NULL,
    `city` varchar(35) DEFAULT NULL,
    `country` varchar(34) DEFAULT NULL,
    `IATA` varchar(16) DEFAULT NULL,
    `ICAO` varchar(6) DEFAULT NULL,
    `latitude` float DEFAULT NULL,
    `longitude` float DEFAULT NULL,
    `altitude` varchar(19) DEFAULT NULL,
    `tz_offset` varchar(5) DEFAULT NULL,
    `DST` varchar(3) DEFAULT NULL,
    `tz_dbtime` varchar(32) DEFAULT NULL,
    `types` varchar(13) DEFAULT NULL,
    `datasource` varchar(13) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE "./sql/airport.csv"
INTO TABLE `airport`
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"';
