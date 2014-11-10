CREATE TABLE `code_analysis` (
  `project` varchar(255) DEFAULT NULL,
  `commit_hash` varchar(255) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `message_count` int(11) DEFAULT NULL,
  `creation_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `code_score` (
  `project` varchar(255) DEFAULT NULL,
  `commit_hash` varchar(255) DEFAULT NULL,
  `statement_count` int(11) DEFAULT NULL,
  `score` float(4,2) DEFAULT NULL,
  `creation_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8