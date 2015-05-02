
CREATE database IF NOT EXISTS indexdb;

USE indexdb;

CREATE TABLE IF NOT EXISTS mailing (addr VARCHAR(255) NOT NULL);

CREATE TABLE IF NOT EXISTS `domain_count` (
  `domain` varchar(100) NOT NULL DEFAULT 'NOT NULL',
  `count` int(11) NOT NULL,
  `date` date NOT NULL
);

ALTER TABLE `domain_count`ADD PRIMARY KEY (`domain`,`date`), ADD UNIQUE KEY `domain_date_index` (`domain`,`count`,`date`);
