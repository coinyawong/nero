CREATE TABLE `cycle` (
  `cycle` int(11) NOT NULL,
  `roll` int(11) NOT NULL,
  `total` int(11) DEFAULT NULL,
  PRIMARY KEY (`cycle`)
);

CREATE TABLE `payout` (
  `address` varchar(100) NOT NULL,
  `cycle` int(11) NOT NULL,
  `reward` int(11) NOT NULL,
  `day` date DEFAULT NULL,
  PRIMARY KEY (`address`, `cycle`)
);

CREATE TABLE `user` (
  `name` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`address`)
);

CREATE TABLE `user_info` (
  `address` varchar(100) NOT NULL,
  `cycle` int(11) NOT NULL,
  `balance` int(11) NOT NULL,
  `day` date DEFAULT NULL,
  PRIMARY KEY (`address`, `cycle`)
);
INSERT INTO `user` VALUES ('코인야웅','-'),('무이투','tz1PrQjp38WaZAKtEGSM4RmgefBcZz838tX2'),('수호천사','tz1XERm1hayQWaAt6MriD3W1W7nQVCzbshKk'),('아기고래','tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF'),('HAN','tz1LqSfBZQXWiXwsYchUiYSFgkiNT3eY9Wij'),('김태현','tz1azNjsLJiaRZ6Zj43sHchvHYD3DLbvwUko'),('제임스','tz1ehBrvenpeUCKZBcgH34VMr5KPg9gxzkSP'),('아크머신','tz1UrUfcaEYaND4UuhkpX5Ao1auWVDMqvP49');
INSERT INTO `user_info` VALUES ('-',2,12000,'2018-08-09'),('tz1PrQjp38WaZAKtEGSM4RmgefBcZz838tX2',3,10000,'2018-08-09'),('tz1XERm1hayQWaAt6MriD3W1W7nQVCzbshKk',3,6000,'2018-08-09'),('tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF',3,12000,'2018-08-09'),('tz1LqSfBZQXWiXwsYchUiYSFgkiNT3eY9Wij',5,500,'2018-08-09'),('tz1azNjsLJiaRZ6Zj43sHchvHYD3DLbvwUko',5,1500,'2018-08-09'),('tz1ehBrvenpeUCKZBcgH34VMr5KPg9gxzkSP',5,9935,'2018-08-09'),('tz1UrUfcaEYaND4UuhkpX5Ao1auWVDMqvP49',5,1339,'2018-08-09'),('tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF',5,3875,'2018-08-09'),('tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF',7,1351,'2018-08-09'),('tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF',8,700,'2018-08-09'),('tz1XERm1hayQWaAt6MriD3W1W7nQVCzbshKk',13,10000,'2018-08-09'),('tz1WuEwAexbx1T7PwCPRnB4Ln3VjQyGrTLwF',14,800,'2018-08-09');

