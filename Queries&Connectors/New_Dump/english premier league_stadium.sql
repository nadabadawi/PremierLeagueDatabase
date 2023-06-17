-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: english premier league
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `stadium`
--

DROP TABLE IF EXISTS `stadium`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stadium` (
  `Name` varchar(50) NOT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  `PitchSize` varchar(15) DEFAULT NULL,
  `BuildingDate` int DEFAULT NULL,
  `LeagueAttendance` varchar(50) DEFAULT NULL,
  `Owning_Club_Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Name`),
  UNIQUE KEY `Name_UNIQUE` (`Name`),
  KEY `fk_Stadium_Club1_idx` (`Owning_Club_Name`),
  CONSTRAINT `stadium_ibfk_1` FOREIGN KEY (`Owning_Club_Name`) REFERENCES `club` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stadium`
--

LOCK TABLES `stadium` WRITE;
/*!40000 ALTER TABLE `stadium` DISABLE KEYS */;
INSERT INTO `stadium` VALUES ('Amex Stadium','American Express Community Stadium; Village Way; Brighton; BN1 9BL',30666,'105m x 68m',2011,'30565 v Everton (15 Oct 2017)','Brighton'),('Anfield',' Anfield;Anfield Road;Liverpool;L4 0TH',53394,' 101m x 68m',1884,'53292 v AFC Bournemouth (5 April 2017)','Liverpool'),('Brentford Community Stadium',' Brentford Community Stadium; Lionel Road South; Brentford; TW8 0RU',17250,' 105m x 68m',2020,'','Brentford'),('Carrow Road Stadium','Carrow Road; Norwich; NR1 1JE',27359,'104m x 68m',1935,'','Norwich'),('Elland Road','Elland Road; Leeds; LS11 0ES',37890,'106m x 69m',1897,'','Leeds'),('Emirates Stadium','Highbury House; 75 Drayton Park; London; N5 1BU',60260,' 105m x 68m',2006,' 60161 v Manchester United (3 November 2007)','Arsenal'),('Etihad Stadium',' Etihad Stadium;Etihad Campus;Manchester;M11 3FF',55017,' 105m x 68m',2002,'54693 v Leicester City (6 February 2016)','Man City'),('Goodison Park Stadium',' Goodison Park;Goodison Road;Liverpool;L4 4EL',39221,' 100.48m x 68m',1892,'40552 v Liverpool (11 December 2004)','Everton'),('King Power Stadium',' King Power Stadium;Filbert Way;Leicester;LE2 7FL',32273,' 105m x 68m',2002,' 32242 v Sunderland (8 August 2015)','Leicester'),('London Stadium',' London Stadium;Queen Elizabeth Olympic Park;London;E20 2ST',60000,'105m x 68m',2011,' 59946 v Arsenal (12 January 2019)','West Ham'),('Molineux Stadium','Molineux Stadium; Waterloo Rd; Wolverhampton; WV1 4QR',32050,'105m x 68m',1889,'31322 v Manchester City (25 August 2018)','Wolves'),('Old Trafford Stadium','Sir Matt Busby Way; Old Trafford; Manchester;M16 0RA',74879,' 105m x 68m',1909,' 76098 v Blackburn Rovers (31 March 2007)','Man Utd'),('Selhurst Park Stadium',' Selhurst Park Stadium;Holmesdale Road;London;SE25 6PU',25486,' 101m x 68m',1924,' 30115 v Manchester United (21 April 1993)','Crystal Palace'),('St Marys Stadium','St Marys Stadium;Britannia Road;Southampton;SO14 5FP',32384,' 105m x 68m',2001,' 32151 v Arsenal (29 December 2003)','Southampton'),('St. James\' Park','St. James\' Park; Strawberry Place; Newcastle Upon Tyne; NE1 4ST',52305,'105m x 68m',1892,'52490 v West Ham United (11 November 2012)','Newcastle'),('Stamford Bridge Stadium',' Stamford Bridge;Fulham Road;London;SW6 1HS',40853,' 103m x 67.5m',1877,' 42332 v Newcastle United (4 December 2004)','Chelsea'),('Tottenham Hotspur Stadium','Lilywhite House; 782 High Road; Tottenham; London; N17 0BX',62062,' 100m x 67m',2019,'','Spurs'),('Turf Moor Stadium',' Turf Moor;Harry Potts Way;Burnley;Lancashire;BB10 4BX',21944,' 105m x 68m',1883,' 21870 v Manchester United (24 April 2017)','Burnley'),('Vicarage Road Stadium','Vicarage Road Stadium; Watford; Hertfordshire; WD18 0ER',21000,' 105m x 68m',1922,' 21590 v Sunderland (27 November 1999)','Watford'),('Villa Park Stadium',' Villa Park;Trinity Road; Birmingham;B66HE',42682,' 105m x 68m',1897,'','Aston Villa');
/*!40000 ALTER TABLE `stadium` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-09 12:22:10
