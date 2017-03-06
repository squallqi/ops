-- MySQL dump 10.13  Distrib 5.6.33, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: cmdb
-- ------------------------------------------------------
-- Server version	5.6.33-0ubuntu0.14.04.1

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
-- Table structure for table `CMDB_cabinet`
--

DROP TABLE IF EXISTS `CMDB_cabinet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CMDB_cabinet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `idc_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `CMDB_cabinet_idc_id_282c4bd5_fk_CMDB_idc_id` (`idc_id`),
  CONSTRAINT `CMDB_cabinet_idc_id_282c4bd5_fk_CMDB_idc_id` FOREIGN KEY (`idc_id`) REFERENCES `CMDB_idc` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CMDB_cabinet`
--

LOCK TABLES `CMDB_cabinet` WRITE;
/*!40000 ALTER TABLE `CMDB_cabinet` DISABLE KEYS */;
INSERT INTO `CMDB_cabinet` VALUES (1,'1','2017-02-12 21:12:38','2017-02-12 21:12:38',1);
/*!40000 ALTER TABLE `CMDB_cabinet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CMDB_host`
--

DROP TABLE IF EXISTS `CMDB_host`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CMDB_host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host_name` varchar(255) DEFAULT NULL,
  `kernel` varchar(255) DEFAULT NULL,
  `kernel_release` varchar(255) DEFAULT NULL,
  `virtual` varchar(255) DEFAULT NULL,
  `host` varchar(255) DEFAULT NULL,
  `osrelease` varchar(255) DEFAULT NULL,
  `saltversion` varchar(255) DEFAULT NULL,
  `osfinger` varchar(255) DEFAULT NULL,
  `os_family` varchar(255) DEFAULT NULL,
  `num_gpus` int(11) DEFAULT NULL,
  `system_serialnumber` varchar(255) DEFAULT NULL,
  `cpu_model` varchar(255) DEFAULT NULL,
  `productname` varchar(255) DEFAULT NULL,
  `osarch` varchar(255) DEFAULT NULL,
  `cpuarch` varchar(255) DEFAULT NULL,
  `os` varchar(255) DEFAULT NULL,
  `mem_total` int(11) DEFAULT NULL,
  `num_cpus` int(11) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `rack_id` int(11),
  PRIMARY KEY (`id`),
  KEY `CMDB_host_rack_id_c118cfdc_fk_CMDB_rack_id` (`rack_id`),
  CONSTRAINT `CMDB_host_rack_id_c118cfdc_fk_CMDB_rack_id` FOREIGN KEY (`rack_id`) REFERENCES `CMDB_rack` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CMDB_host`
--

LOCK TABLES `CMDB_host` WRITE;
/*!40000 ALTER TABLE `CMDB_host` DISABLE KEYS */;
INSERT INTO `CMDB_host` VALUES (1,'www.k2data.com.cn','','','','10.10.10.175','','','','',NULL,'','','','','','',NULL,NULL,'2017-02-12 16:44:53','2017-02-12 16:44:53',NULL);
/*!40000 ALTER TABLE `CMDB_host` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CMDB_hostip`
--

DROP TABLE IF EXISTS `CMDB_hostip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CMDB_hostip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `host_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `CMDB_hostip_host_id_f5db766f_fk_CMDB_host_id` (`host_id`),
  CONSTRAINT `CMDB_hostip_host_id_f5db766f_fk_CMDB_host_id` FOREIGN KEY (`host_id`) REFERENCES `CMDB_host` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CMDB_hostip`
--

LOCK TABLES `CMDB_hostip` WRITE;
/*!40000 ALTER TABLE `CMDB_hostip` DISABLE KEYS */;
/*!40000 ALTER TABLE `CMDB_hostip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CMDB_idc`
--

DROP TABLE IF EXISTS `CMDB_idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CMDB_idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `bandwidth` varchar(255) DEFAULT NULL,
  `phone` varchar(255) NOT NULL,
  `linkman` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `concat_email` varchar(254) DEFAULT NULL,
  `network` longtext,
  `comment` longtext,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `operator_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `CMDB_idc_operator_id_ad6f620c_fk_CMDB_isp_id` (`operator_id`),
  KEY `CMDB_idc_type_id_cc317445_fk_CMDB_idclevel_id` (`type_id`),
  CONSTRAINT `CMDB_idc_operator_id_ad6f620c_fk_CMDB_isp_id` FOREIGN KEY (`operator_id`) REFERENCES `CMDB_isp` (`id`),
  CONSTRAINT `CMDB_idc_type_id_cc317445_fk_CMDB_idclevel_id` FOREIGN KEY (`type_id`) REFERENCES `CMDB_idclevel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CMDB_idc`
--

LOCK TABLES `CMDB_idc` WRITE;
/*!40000 ALTER TABLE `CMDB_idc` DISABLE KEYS */;
INSERT INTO `CMDB_idc` VALUES (1,'虚拟机','','13910277341','齐胜杰','','','','','2017-02-12 21:11:50','2017-02-12 21:11:50',1,1);
/*!40000 ALTER TABLE `CMDB_idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CMDB_idclevel`
--

DROP TABLE IF EXISTS `CMDB_idclevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CMDB_idclevel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `comment` longtext NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CMDB_idclevel`
--

LOCK TABLES `CMDB_idclevel` WRITE;
/*!40000 ALTER TABLE `CMDB_idclevel` DISABLE KEYS */;
INSERT INTO `CMDB_idclevel` VALUES (1,'虚拟机','VM虚拟机','2017-02-12 21:11:46','2017-02-12 21:11:46');
/*!40000 ALTER TABLE `CMDB_idclevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CMDB_isp`
--

DROP TABLE IF EXISTS `CMDB_isp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CMDB_isp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CMDB_isp`
--

LOCK TABLES `CMDB_isp` WRITE;
/*!40000 ALTER TABLE `CMDB_isp` DISABLE KEYS */;
INSERT INTO `CMDB_isp` VALUES (1,'虚拟机','2017-02-12 21:11:25','2017-02-12 21:11:25');
/*!40000 ALTER TABLE `CMDB_isp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CMDB_rack`
--

DROP TABLE IF EXISTS `CMDB_rack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CMDB_rack` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `cabinet_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `CMDB_rack_cabinet_id_40e5ab9c_fk_CMDB_cabinet_id` (`cabinet_id`),
  CONSTRAINT `CMDB_rack_cabinet_id_40e5ab9c_fk_CMDB_cabinet_id` FOREIGN KEY (`cabinet_id`) REFERENCES `CMDB_cabinet` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CMDB_rack`
--

LOCK TABLES `CMDB_rack` WRITE;
/*!40000 ALTER TABLE `CMDB_rack` DISABLE KEYS */;
INSERT INTO `CMDB_rack` VALUES (1,'机架位置','2017-02-12 21:12:40','2017-02-12 21:12:40',1);
/*!40000 ALTER TABLE `CMDB_rack` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add 业务主机',7,'add_projecthost'),(20,'Can change 业务主机',7,'change_projecthost'),(21,'Can delete 业务主机',7,'delete_projecthost'),(22,'Can add 部署详情',8,'add_deployjobdetail'),(23,'Can change 部署详情',8,'change_deployjobdetail'),(24,'Can delete 部署详情',8,'delete_deployjobdetail'),(25,'Can add 业务模块',9,'add_projectmodule'),(26,'Can change 业务模块',9,'change_projectmodule'),(27,'Can delete 业务模块',9,'delete_projectmodule'),(28,'Can add 版本信息',10,'add_projectversion'),(29,'Can change 版本信息',10,'change_projectversion'),(30,'Can delete 版本信息',10,'delete_projectversion'),(31,'Can add 业务',11,'add_project'),(32,'Can change 业务',11,'change_project'),(33,'Can delete 业务',11,'delete_project'),(34,'Can add 历史作业',12,'add_deployjob'),(35,'Can change 历史作业',12,'change_deployjob'),(36,'Can delete 历史作业',12,'delete_deployjob'),(37,'Can add 机房等级',13,'add_idclevel'),(38,'Can change 机房等级',13,'change_idclevel'),(39,'Can delete 机房等级',13,'delete_idclevel'),(40,'Can add 主机IP',14,'add_hostip'),(41,'Can change 主机IP',14,'change_hostip'),(42,'Can delete 主机IP',14,'delete_hostip'),(43,'Can add ISP类型',15,'add_isp'),(44,'Can change ISP类型',15,'change_isp'),(45,'Can delete ISP类型',15,'delete_isp'),(46,'Can add 机柜',16,'add_cabinet'),(47,'Can change 机柜',16,'change_cabinet'),(48,'Can delete 机柜',16,'delete_cabinet'),(49,'Can add 主机',17,'add_host'),(50,'Can change 主机',17,'change_host'),(51,'Can delete 主机',17,'delete_host'),(52,'Can add 机架',18,'add_rack'),(53,'Can change 机架',18,'change_rack'),(54,'Can delete 机架',18,'delete_rack'),(55,'Can add 机房',19,'add_idc'),(56,'Can change 机房',19,'change_idc'),(57,'Can delete 机房',19,'delete_idc');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$bzBKKOro7onF$e7dtleeWIHo93qq+SxjLDwLDl0Dgx1sHriKR15QMldI=','2017-02-12 16:43:08',1,'admin','','','squallqi@126.com',1,1,'2017-02-12 16:43:00');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_manager_deployjob`
--

DROP TABLE IF EXISTS `deploy_manager_deployjob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_manager_deployjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_name` varchar(255) DEFAULT NULL,
  `deploy_status` int(11) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `project_version_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_version_id_53c00e26_fk_deploy_manager_projectversion_id` (`project_version_id`),
  CONSTRAINT `project_version_id_53c00e26_fk_deploy_manager_projectversion_id` FOREIGN KEY (`project_version_id`) REFERENCES `deploy_manager_projectversion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_manager_deployjob`
--

LOCK TABLES `deploy_manager_deployjob` WRITE;
/*!40000 ALTER TABLE `deploy_manager_deployjob` DISABLE KEYS */;
INSERT INTO `deploy_manager_deployjob` VALUES (1,'部署部署apache:0.0.1',0,'2017-02-12 21:03:00','2017-02-12 21:03:00',2);
/*!40000 ALTER TABLE `deploy_manager_deployjob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_manager_deployjobdetail`
--

DROP TABLE IF EXISTS `deploy_manager_deployjobdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_manager_deployjobdetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deploy_message` longtext,
  `job_cmd` longtext,
  `start_time` datetime DEFAULT NULL,
  `duration` decimal(10,2) DEFAULT NULL,
  `stderr` longtext,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `host_id` int(11) NOT NULL,
  `job_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `deploy_manager_deployjobdetail_host_id_9d1a7e3e_fk_CMDB_host_id` (`host_id`),
  KEY `deploy_manager_de_job_id_fe1eaac8_fk_deploy_manager_deployjob_id` (`job_id`),
  CONSTRAINT `deploy_manager_de_job_id_fe1eaac8_fk_deploy_manager_deployjob_id` FOREIGN KEY (`job_id`) REFERENCES `deploy_manager_deployjob` (`id`),
  CONSTRAINT `deploy_manager_deployjobdetail_host_id_9d1a7e3e_fk_CMDB_host_id` FOREIGN KEY (`host_id`) REFERENCES `CMDB_host` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_manager_deployjobdetail`
--

LOCK TABLES `deploy_manager_deployjobdetail` WRITE;
/*!40000 ALTER TABLE `deploy_manager_deployjobdetail` DISABLE KEYS */;
/*!40000 ALTER TABLE `deploy_manager_deployjobdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_manager_project`
--

DROP TABLE IF EXISTS `deploy_manager_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_manager_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `playbook` longtext,
  `job_script_type` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `project_module_id` int(11),
  PRIMARY KEY (`id`),
  KEY `de_project_module_id_090b2add_fk_deploy_manager_projectmodule_id` (`project_module_id`),
  CONSTRAINT `de_project_module_id_090b2add_fk_deploy_manager_projectmodule_id` FOREIGN KEY (`project_module_id`) REFERENCES `deploy_manager_projectmodule` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_manager_project`
--

LOCK TABLES `deploy_manager_project` WRITE;
/*!40000 ALTER TABLE `deploy_manager_project` DISABLE KEYS */;
INSERT INTO `deploy_manager_project` VALUES (1,'部署apache','apt-get  install apache',1,'2017-02-12 16:46:09','2017-02-12 21:02:52',1);
/*!40000 ALTER TABLE `deploy_manager_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_manager_projecthost`
--

DROP TABLE IF EXISTS `deploy_manager_projecthost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_manager_projecthost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `host_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deploy_manager_projecthost_host_id_1f6889f6_fk_CMDB_host_id` (`host_id`),
  KEY `deploy_manager__project_id_d5e63b7b_fk_deploy_manager_project_id` (`project_id`),
  CONSTRAINT `deploy_manager__project_id_d5e63b7b_fk_deploy_manager_project_id` FOREIGN KEY (`project_id`) REFERENCES `deploy_manager_project` (`id`),
  CONSTRAINT `deploy_manager_projecthost_host_id_1f6889f6_fk_CMDB_host_id` FOREIGN KEY (`host_id`) REFERENCES `CMDB_host` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_manager_projecthost`
--

LOCK TABLES `deploy_manager_projecthost` WRITE;
/*!40000 ALTER TABLE `deploy_manager_projecthost` DISABLE KEYS */;
INSERT INTO `deploy_manager_projecthost` VALUES (1,'2017-02-12 16:47:15','2017-02-12 16:47:15',1,1);
/*!40000 ALTER TABLE `deploy_manager_projecthost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_manager_projectmodule`
--

DROP TABLE IF EXISTS `deploy_manager_projectmodule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_manager_projectmodule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `deploy_manager_projectmodule_caf7cc51` (`lft`),
  KEY `deploy_manager_projectmodule_3cfbd988` (`rght`),
  KEY `deploy_manager_projectmodule_656442a0` (`tree_id`),
  KEY `deploy_manager_projectmodule_c9e9a848` (`level`),
  KEY `deploy_manager_projectmodule_6be37982` (`parent_id`),
  CONSTRAINT `deploy_man_parent_id_6bfe8c7a_fk_deploy_manager_projectmodule_id` FOREIGN KEY (`parent_id`) REFERENCES `deploy_manager_projectmodule` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_manager_projectmodule`
--

LOCK TABLES `deploy_manager_projectmodule` WRITE;
/*!40000 ALTER TABLE `deploy_manager_projectmodule` DISABLE KEYS */;
INSERT INTO `deploy_manager_projectmodule` VALUES (1,'apache','2017-02-12 16:45:26','2017-02-12 16:45:26',1,2,1,0,NULL);
/*!40000 ALTER TABLE `deploy_manager_projectmodule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deploy_manager_projectversion`
--

DROP TABLE IF EXISTS `deploy_manager_projectversion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deploy_manager_projectversion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `files` varchar(100) DEFAULT NULL,
  `is_default` tinyint(1) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `deploy_manager__project_id_2cd380e9_fk_deploy_manager_project_id` (`project_id`),
  CONSTRAINT `deploy_manager__project_id_2cd380e9_fk_deploy_manager_project_id` FOREIGN KEY (`project_id`) REFERENCES `deploy_manager_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deploy_manager_projectversion`
--

LOCK TABLES `deploy_manager_projectversion` WRITE;
/*!40000 ALTER TABLE `deploy_manager_projectversion` DISABLE KEYS */;
INSERT INTO `deploy_manager_projectversion` VALUES (2,'0.0.1','',1,'2017-02-12 21:02:52','2017-02-12 21:02:52',1);
/*!40000 ALTER TABLE `deploy_manager_projectversion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-02-12 16:44:53','1','www.k2data.com.cn',1,'[{\"added\": {}}]',17,1),(2,'2017-02-12 16:45:26','1','apache',1,'[{\"added\": {}}]',9,1),(3,'2017-02-12 16:46:09','1','部署apache',1,'[{\"added\": {}}]',11,1),(4,'2017-02-12 16:47:15','1','部署apache',2,'[{\"changed\": {\"fields\": [\"job_script_type\"]}}, {\"added\": {\"object\": \"www.k2data.com.cn\", \"name\": \"\\u4e1a\\u52a1\\u4e3b\\u673a\"}}]',11,1),(5,'2017-02-12 21:02:00','2','',1,'[{\"added\": {}}, {\"added\": {\"object\": \"---0.0.1\", \"name\": \"\\u7248\\u672c\\u4fe1\\u606f\"}}, {\"added\": {\"object\": \"www.k2data.com.cn\", \"name\": \"\\u4e1a\\u52a1\\u4e3b\\u673a\"}}]',11,1),(6,'2017-02-12 21:02:16','2','',3,'',11,1),(7,'2017-02-12 21:02:52','1','部署apache',2,'[{\"added\": {\"object\": \"\\u90e8\\u7f72apache---0.0.1\", \"name\": \"\\u7248\\u672c\\u4fe1\\u606f\"}}]',11,1),(8,'2017-02-12 21:11:25','1','虚拟机',1,'[{\"added\": {}}]',15,1),(9,'2017-02-12 21:11:46','1','虚拟机',1,'[{\"added\": {}}]',13,1),(10,'2017-02-12 21:11:50','1','虚拟机',1,'[{\"added\": {}}]',19,1),(11,'2017-02-12 21:12:38','1','1',1,'[{\"added\": {}}]',16,1),(12,'2017-02-12 21:12:40','1','机架位置',1,'[{\"added\": {}}]',18,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(16,'CMDB','cabinet'),(17,'CMDB','host'),(14,'CMDB','hostip'),(19,'CMDB','idc'),(13,'CMDB','idclevel'),(15,'CMDB','isp'),(18,'CMDB','rack'),(5,'contenttypes','contenttype'),(12,'deploy_manager','deployjob'),(8,'deploy_manager','deployjobdetail'),(11,'deploy_manager','project'),(7,'deploy_manager','projecthost'),(9,'deploy_manager','projectmodule'),(10,'deploy_manager','projectversion'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'CMDB','0001_initial','2017-02-12 16:38:26'),(2,'CMDB','0002_auto_20170213_0038','2017-02-12 16:38:26'),(3,'contenttypes','0001_initial','2017-02-12 16:38:27'),(4,'auth','0001_initial','2017-02-12 16:38:27'),(5,'admin','0001_initial','2017-02-12 16:38:27'),(6,'admin','0002_logentry_remove_auto_add','2017-02-12 16:38:27'),(7,'contenttypes','0002_remove_content_type_name','2017-02-12 16:38:27'),(8,'auth','0002_alter_permission_name_max_length','2017-02-12 16:38:27'),(9,'auth','0003_alter_user_email_max_length','2017-02-12 16:38:27'),(10,'auth','0004_alter_user_username_opts','2017-02-12 16:38:27'),(11,'auth','0005_alter_user_last_login_null','2017-02-12 16:38:27'),(12,'auth','0006_require_contenttypes_0002','2017-02-12 16:38:27'),(13,'auth','0007_alter_validators_add_error_messages','2017-02-12 16:38:28'),(14,'auth','0008_alter_user_username_max_length','2017-02-12 16:38:28'),(15,'deploy_manager','0001_initial','2017-02-12 16:38:28'),(16,'sessions','0001_initial','2017-02-12 16:38:28');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('do8zp6lbuaqv0nlgve3oop81q5b17dcb','NjYyODdlZWIzZTUyMThkN2FmYTVhNzAzMTRjMWY3MWI0Y2QzNmFlYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImNlZmFkNDA4OTVjOGNjYWYwMzI1YjIyMTg0N2RmOTBlMWM2NGU4NjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-02-26 16:43:09');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-06 16:24:25
