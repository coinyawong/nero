-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: yawong
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cycle`
--

DROP TABLE IF EXISTS `cycle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cycle` (
  `cycle` int(11) NOT NULL,
  `roll` int(11) NOT NULL,
  `total` int(11) DEFAULT NULL,
  PRIMARY KEY (`cycle`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cycle`
--

LOCK TABLES `cycle` WRITE;
/*!40000 ALTER TABLE `cycle` DISABLE KEYS */;
/*!40000 ALTER TABLE `cycle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payout`
--

DROP TABLE IF EXISTS `payout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payout` (
  `id` int(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `cycle` int(11) NOT NULL,
  `reward` int(11) NOT NULL,
  `day` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payout`
--

LOCK TABLES `payout` WRITE;
/*!40000 ALTER TABLE `payout` DISABLE KEYS */;
/*!40000 ALTER TABLE `payout` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `i_address` varchar(100) NOT NULL,
  `o_address` varchar(100) NOT NULL,
  `cycle` int(11) NOT NULL,
  `balance` int(11) NOT NULL,
  `day` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'yawong','-','-',2,12000,'2018-08-09'),(2,'mooitu','tz1PrQjp38WaZAKtEGSM4RmgefBcZz838tX2','tz1PrQjp38WaZAKtEGSM4RmgefBcZz838tX2',3,10000,'2018-08-09'),(3,'sooho','tz1XERm1hayQWaAt6MriD3W1W7nQVCzbshKk','tz1XERm1hayQWaAt6MriD3W1W7nQVCzbshKk',3,6000,'2018-08-09'),(4,'badydolphin','tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF','tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF',3,12000,'2018-08-09'),(5,'han','tz1LqSfBZQXWiXwsYchUiYSFgkiNT3eY9Wij','tz1LqSfBZQXWiXwsYchUiYSFgkiNT3eY9Wij',5,500,'2018-08-09'),(6,'kimteahun','tz1azNjsLJiaRZ6Zj43sHchvHYD3DLbvwUko','tz1azNjsLJiaRZ6Zj43sHchvHYD3DLbvwUko',5,3000,'2018-08-09'),(7,'kimteahun','tz1azNjsLJiaRZ6Zj43sHchvHYD3DLbvwUko','tz1azNjsLJiaRZ6Zj43sHchvHYD3DLbvwUko',8,-700,'2018-08-09'),(8,'james','tz1ehBrvenpeUCKZBcgH34VMr5KPg9gxzkSP','tz1ehBrvenpeUCKZBcgH34VMr5KPg9gxzkSP',5,9935,'2018-08-09'),(9,'arc_machine','tz1UrUfcaEYaND4UuhkpX5Ao1auWVDMqvP49','tz1UrUfcaEYaND4UuhkpX5Ao1auWVDMqvP49',5,1339,'2018-08-09'),(10,'badydolphin2','tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF','tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF',5,3875,'2018-08-09'),(11,'badydolphin3','tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF','tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF',7,1351,'2018-08-09'),(12,'badydolphin4','tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF','tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF',8,700,'2018-08-09'),(13,'sooho2','tz1XERm1hayQWaAt6MriD3W1W7nQVCzbshKk','tz1XERm1hayQWaAt6MriD3W1W7nQVCzbshKk',13,10000,'2018-08-09');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-09 23:21:24
