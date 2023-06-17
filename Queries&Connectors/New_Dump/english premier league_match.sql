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
-- Table structure for table `match`
--

DROP TABLE IF EXISTS `match`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match` (
  `Season` int NOT NULL,
  `Date` date NOT NULL,
  `Stadium_Name` varchar(25) NOT NULL,
  `Home_Club_Name` varchar(20) NOT NULL,
  `Away_Club_Name` varchar(20) NOT NULL,
  `Away_Possession%` int DEFAULT NULL,
  `Home_Possession%` int DEFAULT NULL,
  `Home_Goals` int DEFAULT NULL,
  `Away_Goals` int DEFAULT NULL,
  `Home_YellowCard` int DEFAULT NULL,
  `Away_YellowCard` int DEFAULT NULL,
  `Home_RedCard` int DEFAULT NULL,
  `Away_RedCard` int DEFAULT NULL,
  `Home_Shots` int DEFAULT NULL,
  `Away_Shots` int DEFAULT NULL,
  `Home_Fouls` int DEFAULT NULL,
  `Away_Fouls` int DEFAULT NULL,
  PRIMARY KEY (`Date`,`Away_Club_Name`,`Home_Club_Name`),
  KEY `fk_Match_Stadium1_idx` (`Stadium_Name`),
  KEY `fk_Match_Club2_idx` (`Home_Club_Name`),
  KEY `fk_Match_Club1_idx` (`Away_Club_Name`),
  CONSTRAINT `fk_Match_Club1` FOREIGN KEY (`Away_Club_Name`) REFERENCES `club` (`Name`),
  CONSTRAINT `fk_Match_Club2` FOREIGN KEY (`Home_Club_Name`) REFERENCES `club` (`Name`),
  CONSTRAINT `match_ibfk_1` FOREIGN KEY (`Stadium_Name`) REFERENCES `stadium` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match`
--

LOCK TABLES `match` WRITE;
/*!40000 ALTER TABLE `match` DISABLE KEYS */;
INSERT INTO `match` VALUES (4,'2022-04-23','Emirates Stadium','Arsenal','Man Utd',45,55,3,1,3,4,0,0,14,14,9,12),(4,'2022-05-01','London Stadium','West Ham','Arsenal',43,56,1,2,2,2,0,0,8,13,7,9),(4,'2022-05-08','King Power Stadium','Leicester','Everton',34,66,1,2,3,0,0,0,9,4,11,6),(4,'2022-05-08','Emirates Stadium','Arsenal','Leeds',37,63,2,1,2,2,0,1,19,3,13,15);
/*!40000 ALTER TABLE `match` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-09 12:31:05
