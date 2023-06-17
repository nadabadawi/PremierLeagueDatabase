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
-- Table structure for table `match_reviews_fan`
--

DROP TABLE IF EXISTS `match_reviews_fan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match_reviews_fan` (
  `Match_Date` date NOT NULL,
  `Away_Club_Name` varchar(20) NOT NULL,
  `Home_Club_Name` varchar(20) NOT NULL,
  `Fan_EmailAddress` varchar(45) NOT NULL,
  `Textual Rating` varchar(800) DEFAULT NULL,
  `Rating` int DEFAULT NULL,
  PRIMARY KEY (`Match_Date`,`Away_Club_Name`,`Home_Club_Name`,`Fan_EmailAddress`),
  KEY `fk_Match_has_Fan1_Fan1_idx` (`Fan_EmailAddress`),
  KEY `fk_Match_has_Fan1_Match1_idx` (`Match_Date`,`Away_Club_Name`,`Home_Club_Name`),
  KEY `Away_Club_Name` (`Away_Club_Name`),
  KEY `Home_Club_Name` (`Home_Club_Name`),
  CONSTRAINT `match_reviews_fan_ibfk_1` FOREIGN KEY (`Match_Date`) REFERENCES `match` (`Date`),
  CONSTRAINT `match_reviews_fan_ibfk_2` FOREIGN KEY (`Away_Club_Name`) REFERENCES `match` (`Away_Club_Name`),
  CONSTRAINT `match_reviews_fan_ibfk_3` FOREIGN KEY (`Home_Club_Name`) REFERENCES `match` (`Home_Club_Name`),
  CONSTRAINT `match_reviews_fan_ibfk_4` FOREIGN KEY (`Fan_EmailAddress`) REFERENCES `fan` (`EmailAddress`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match_reviews_fan`
--

LOCK TABLES `match_reviews_fan` WRITE;
/*!40000 ALTER TABLE `match_reviews_fan` DISABLE KEYS */;
/*!40000 ALTER TABLE `match_reviews_fan` ENABLE KEYS */;
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
