-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 01, 2018 at 05:24 PM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 5.6.36

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `meatritedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_emailaddress`
--

CREATE TABLE `account_emailaddress` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `account_emailaddress`
--

INSERT INTO `account_emailaddress` (`id`, `email`, `verified`, `primary`, `user_id`) VALUES
(1, 'test11@test11.com', 0, 1, 10),
(2, 'test12@test12.com', 0, 1, 11),
(3, 'test13@test13.com', 0, 1, 12),
(4, 'test14@test14.com', 0, 1, 13),
(5, 'test15@test15.com', 0, 1, 14),
(6, 'a@a.com', 0, 1, 15);

-- --------------------------------------------------------

--
-- Table structure for table `account_emailconfirmation`
--

CREATE TABLE `account_emailconfirmation` (
  `id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('de8e0a2b364a78578f7983a880d9808712c499e2', '2018-05-30 09:40:04.902529', 8),
('e93747953048fe954ea084e9e696906b7db2a5fa', '2018-05-30 14:02:35.281659', 9);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add Token', 7, 'add_token'),
(20, 'Can change Token', 7, 'change_token'),
(21, 'Can delete Token', 7, 'delete_token'),
(22, 'Can add site', 8, 'add_site'),
(23, 'Can change site', 8, 'change_site'),
(24, 'Can delete site', 8, 'delete_site'),
(25, 'Can add social application', 9, 'add_socialapp'),
(26, 'Can change social application', 9, 'change_socialapp'),
(27, 'Can delete social application', 9, 'delete_socialapp'),
(28, 'Can add social account', 10, 'add_socialaccount'),
(29, 'Can change social account', 10, 'change_socialaccount'),
(30, 'Can delete social account', 10, 'delete_socialaccount'),
(31, 'Can add social application token', 11, 'add_socialtoken'),
(32, 'Can change social application token', 11, 'change_socialtoken'),
(33, 'Can delete social application token', 11, 'delete_socialtoken'),
(34, 'Can add email address', 12, 'add_emailaddress'),
(35, 'Can change email address', 12, 'change_emailaddress'),
(36, 'Can delete email address', 12, 'delete_emailaddress'),
(37, 'Can add email confirmation', 13, 'add_emailconfirmation'),
(38, 'Can change email confirmation', 13, 'change_emailconfirmation'),
(39, 'Can delete email confirmation', 13, 'delete_emailconfirmation'),
(40, 'Can add tbl productlist', 14, 'add_tblproductlist'),
(41, 'Can change tbl productlist', 14, 'change_tblproductlist'),
(42, 'Can delete tbl productlist', 14, 'delete_tblproductlist'),
(43, 'Can add api bucketlist', 15, 'add_apibucketlist'),
(44, 'Can change api bucketlist', 15, 'change_apibucketlist'),
(45, 'Can delete api bucketlist', 15, 'delete_apibucketlist'),
(46, 'Can add api bucketlist', 16, 'add_apibucketlist'),
(47, 'Can change api bucketlist', 16, 'change_apibucketlist'),
(48, 'Can delete api bucketlist', 16, 'delete_apibucketlist'),
(49, 'Can add api bucketlist', 17, 'add_apibucketlist'),
(50, 'Can change api bucketlist', 17, 'change_apibucketlist'),
(51, 'Can delete api bucketlist', 17, 'delete_apibucketlist'),
(52, 'Can add tbl productlist', 18, 'add_tblproductlist'),
(53, 'Can change tbl productlist', 18, 'change_tblproductlist'),
(54, 'Can delete tbl productlist', 18, 'delete_tblproductlist'),
(55, 'Can add batchgroups', 19, 'add_batchgroups'),
(56, 'Can change batchgroups', 19, 'change_batchgroups'),
(57, 'Can delete batchgroups', 19, 'delete_batchgroups'),
(58, 'Can add productlist', 20, 'add_productlist'),
(59, 'Can change productlist', 20, 'change_productlist'),
(60, 'Can delete productlist', 20, 'delete_productlist');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$eYovGpnyLlJ3$kkjOx/tSboQxVUxDLeOfXa+2xXFy8Ls56dn8/oIT5sk=', '2018-06-01 13:24:13.114650', 1, 'gray', '', '', 'gray@gray.com', 1, 1, '2018-05-28 13:36:18.535983'),
(2, 'pbkdf2_sha256$100000$6uwuQr78SbL2$5MrFRvMhtpWhXA8G0BF/bp6QI84o0fiP2Fvgvajb+h8=', NULL, 0, 'test1', '', '', '', 0, 1, '2018-05-29 05:13:11.785073'),
(3, 'pbkdf2_sha256$100000$gC9I2WyRMPnJ$VS5sXrcNRGy7g6CO4IUHaSdi9h85phz6zoVLUUiavrI=', NULL, 0, 'test2', '', '', '', 0, 1, '2018-05-29 05:15:49.858004'),
(4, 'pbkdf2_sha256$100000$rmcccpY3fasH$kr8j2wNEyBQK67icqrrPADM2ya6Enr7jb/KKD04ejdo=', NULL, 0, 'test3', '', '', '', 0, 1, '2018-05-30 07:00:40.499542'),
(5, 'pbkdf2_sha256$100000$Qu7OvbHOeQ37$9ghR22Pif+vjFc3MafU1Hukb14wWM4OslBNqIu8JVqg=', NULL, 0, 'test4', '', '', '', 0, 1, '2018-05-30 07:08:25.598555'),
(6, 'test5test5', NULL, 0, 'test5', '', '', 'test5@test5.com', 0, 1, '2018-05-30 07:24:03.369360'),
(7, 'test7test7', NULL, 0, 'test7', '', '', '', 0, 1, '2018-05-30 07:29:47.197296'),
(8, 'pbkdf2_sha256$100000$vaqgSrerjlCh$Jb04Y8/MLAU8mw3LmW/sUtAV+szfLDUiXrW6Q/FtVH0=', NULL, 0, 'Test8', '', '', 'Test8@test8.com', 0, 1, '2018-05-30 09:40:04.745276'),
(9, 'pbkdf2_sha256$100000$eDjHiP4lY9dh$u54vrhnZoioQzvKrV0yzR31d3w4kK4JbhL2FjSEmepA=', NULL, 0, 'test10', '', '', 'test10@gmail.com', 0, 1, '2018-05-30 14:02:34.715221'),
(10, 'pbkdf2_sha256$100000$c9tf0dZcnfqR$/znBOOmf4zwNPpBuKv/PZCSBG+RMETt6QEzolDiT0n0=', NULL, 0, 'test11', '', '', 'test11@test11.com', 0, 1, '2018-05-31 06:40:03.437487'),
(11, 'pbkdf2_sha256$100000$f52CHf9Xh1u4$EU2V2j8+Ovs+NMngd/XIjW0aB/d2upFa8h8KwEBv7Sw=', NULL, 0, 'test12', '', '', 'test12@test12.com', 0, 1, '2018-05-31 06:41:51.302991'),
(12, 'pbkdf2_sha256$100000$NACVYGOSSs0Z$tj8nhpYM/OdFcQG6WMz726YoEtzTy0YE282aDA7Wieo=', '2018-05-31 06:44:33.150378', 0, 'test13', '', '', 'test13@test13.com', 0, 1, '2018-05-31 06:44:32.699646'),
(13, 'pbkdf2_sha256$100000$5mtpVm9Sd32i$O3pZvty2i95z0hlbuqqqD1FBBHyRbzxKbaKy2FHyzAI=', '2018-05-31 06:45:01.098610', 0, 'test14', '', '', 'test14@test14.com', 0, 1, '2018-05-31 06:45:00.894599'),
(14, 'pbkdf2_sha256$100000$wowj65RbScL1$lv4MatPTdL1wUaOhl/A+Tmc973TNL6gh+cMOdXnwKVI=', '2018-05-31 07:17:07.496691', 0, 'test15', '', '', 'test15@test15.com', 0, 1, '2018-05-31 07:17:06.987904'),
(15, 'pbkdf2_sha256$100000$PosQzy1jdDCv$lQKpFQyBSo8yD6QVWN2BRsA1YBPwjZiCmo5xB0nv8JE=', '2018-06-01 14:32:54.142237', 0, 'a', '', '', 'a@a.com', 0, 1, '2018-06-01 05:55:44.188434');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2018-05-29 05:13:11.906808', '2', 'test1', 1, '[{\"added\": {}}]', 4, 1),
(2, '2018-05-29 05:14:19.408172', '1', 'admin', 1, '[{\"added\": {}}]', 3, 1),
(3, '2018-05-29 05:15:49.957186', '3', 'test2', 1, '[{\"added\": {}}]', 4, 1),
(4, '2018-05-30 07:00:40.786033', '4', 'test3', 1, '[{\"added\": {}}]', 4, 1),
(5, '2018-05-30 07:08:25.740518', '5', 'test4', 1, '[{\"added\": {}}]', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(12, 'account', 'emailaddress'),
(13, 'account', 'emailconfirmation'),
(1, 'admin', 'logentry'),
(10, 'allauth', 'socialaccount'),
(9, 'allauth', 'socialapp'),
(11, 'allauth', 'socialtoken'),
(15, 'api', 'apibucketlist'),
(14, 'api', 'tblproductlist'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'authtoken', 'token'),
(5, 'contenttypes', 'contenttype'),
(19, 'mrDatabaseModels', 'batchgroups'),
(20, 'mrDatabaseModels', 'productlist'),
(16, 'mrdb', 'apibucketlist'),
(17, 'myapp', 'apibucketlist'),
(18, 'myapp', 'tblproductlist'),
(6, 'sessions', 'session'),
(8, 'sites', 'site');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-05-28 13:31:43.541707'),
(2, 'auth', '0001_initial', '2018-05-28 13:31:53.125275'),
(3, 'admin', '0001_initial', '2018-05-28 13:31:55.392092'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-05-28 13:31:55.454578'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-05-28 13:31:56.439475'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-05-28 13:31:57.447118'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-05-28 13:31:58.649722'),
(8, 'auth', '0004_alter_user_username_opts', '2018-05-28 13:31:58.730536'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-05-28 13:31:59.385227'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-05-28 13:31:59.526860'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-05-28 13:31:59.695353'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-05-28 13:32:01.701848'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-05-28 13:32:02.838465'),
(14, 'sessions', '0001_initial', '2018-05-28 13:32:03.340740'),
(15, 'authtoken', '0001_initial', '2018-05-30 09:25:06.009344'),
(16, 'authtoken', '0002_auto_20160226_1747', '2018-05-30 09:25:07.263585'),
(17, 'account', '0001_initial', '2018-05-31 06:39:44.657195'),
(18, 'account', '0002_email_max_length', '2018-05-31 06:39:45.563822'),
(19, 'sites', '0001_initial', '2018-05-31 06:39:45.773021'),
(20, 'sites', '0002_alter_domain_unique', '2018-05-31 06:39:46.191776'),
(21, 'api', '0001_initial', '2018-05-31 10:56:14.839184'),
(22, 'api', '0002_apibucketlist', '2018-05-31 12:22:04.502298'),
(23, 'mrdb', '0001_initial', '2018-05-31 13:13:35.938807'),
(24, 'api', '0002_auto_20180531_1601', '2018-05-31 14:01:13.391112'),
(25, 'api', '0003_auto_20180531_1603', '2018-05-31 14:03:25.075015'),
(26, 'myapp', '0001_initial', '2018-05-31 14:09:15.182075'),
(27, 'api', '0004_auto_20180601_1116', '2018-06-01 09:16:25.906219'),
(28, 'mrDatabaseModels', '0001_initial', '2018-06-01 09:22:22.173720');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0607u6ifreq44e4m0opubhpynbd69pzx', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-14 09:14:18.935666'),
('3a3kquyujv93j9rnh79tdft09q14agl8', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 06:19:10.231847'),
('50scdwjuw6a6vpuzus626vd1vdlqu8n8', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 06:26:40.342585'),
('50yo1l3ulvcmg3n811ns544v4yl4i0jp', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 10:33:26.103020'),
('5khdw008eq7srezh5o0bwftmzbvznqzn', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 07:37:45.675321'),
('66s65j220rrbqm3nlfxoc6km8bo5bk4f', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-15 06:25:31.239271'),
('70f0v4n6qjj370otjhpb4zpvm9h7v1m0', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-14 09:29:46.358983'),
('7f4n9v7nci81fwiuw4ejji47mqhxpita', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 07:29:28.894058'),
('7ptzd3m4d5q8zu6ykxhrnmf35ima1y9w', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 08:54:42.503775'),
('8b3ct8y41tt1rd0rct7emely2uw0x2ht', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 13:28:06.848288'),
('8su4chhl5svx6j2yr9t44l5kr4g4c61e', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-15 05:48:42.168596'),
('9c90xcz5wsz5yqephpnrtf3r54pgnzkn', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 06:25:19.076229'),
('9ihwtqi1mn1xscjlhxfsbwdblak1fm6r', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 05:58:19.338209'),
('9qtyttlpp8psoczq22ekxs9misqc7iqw', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 05:58:45.149411'),
('9yj3i002uvycu1ycxbuybca7l5isxds4', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 08:34:38.221661'),
('cip9xomzz4mosysgzzbvhu40tlv1i2ql', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 10:27:14.523482'),
('cmq2z89umpe56uqxzazkwfijp2554mjs', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 13:22:28.428135'),
('dny2znpyv1lkyewh042911481hitriuq', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 06:24:10.565509'),
('do2kv07owqgpvcy65tloi9mmklokmi2f', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-14 07:55:09.832827'),
('epl9ffljj2dx4371bf40g697akz354nz', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 12:59:37.231540'),
('ezihe6op2g8jh3291mdppqw7q9cs4qec', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 06:28:21.238366'),
('fblvzmth0k62mmqlwhnbpkzodt7aa12a', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 07:11:52.521114'),
('fu8u1a16a0thx6x78t147fhuxd788tnc', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-15 13:24:13.225758'),
('g5tpg6qvyhegblsc6nb1kn97dgosnsea', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 14:32:54.205050'),
('g8ws7hx9eazrmeaiwf8kr14ftxwhlmm7', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 08:53:18.047273'),
('glbmhp3i723sf6vv8swl8q2hbiiaalvd', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 13:34:39.892254'),
('gpcff7uco0nlagdqt68ay4claysrlkr9', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 14:04:01.625580'),
('h26lekxhdplk8gu0bmdghy2e43936asw', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 14:07:14.422872'),
('isyoaot6tt5zzjnn72l9v5ucf0og8rxn', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 07:25:14.828935'),
('jg8qse1l9odyi7xffsbg2vu9c3g86hjp', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-14 09:15:01.537714'),
('jjrdvm81v0pzugy7fu3yp06bf7j9ex0q', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-14 09:52:01.027167'),
('jlmv4ihg0z2c5v5w3550zla4d5ewyixt', 'MWQ0ZDAxODc5ZmYxNDc0MWM2ZGI1Y2JiYWJjZjlhNjQ1OGNhZWExZTp7ImFjY291bnRfdmVyaWZpZWRfZW1haWwiOm51bGwsImFjY291bnRfdXNlciI6ImUiLCJfYXV0aF91c2VyX2lkIjoiMTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImZjNGVmYThiNjAxMGM1MTIxMDE4NzRlYzRkYzk2OGYxZDFiODA1Y2EifQ==', '2018-06-14 07:17:07.756934'),
('k2xq72453g0e3d795zdc35wuexlrgume', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 10:07:11.356177'),
('k57if8gjmolfa9uvej7qgn7ckpbs6iq2', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-14 09:04:50.079532'),
('kjcne8s1ymkumcl57nr3co934jh75nnw', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 10:34:57.412671'),
('kpkdkmc3jwsr9gdko2zlmrb4iomo9row', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 08:18:10.798533'),
('lbjwi50yzwih1zt35r3pa85vbgfdrpps', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 07:29:12.594967'),
('mjoo6njg00eyoqcpaliqkrv4xyoj2a78', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-14 07:59:13.269941'),
('nke68tm3obf89bv7tvvvxcyed9pk4syn', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 13:47:35.326751'),
('oklwxmb3r3ll0rcrh4086dsu8lvqgib4', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 06:30:38.266299'),
('p9ag55zvctt6ccyw85mhxt7u3fga6do5', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 06:23:36.686305'),
('ppzeoy9qujwzw1gs6a3dj455jew3dz69', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 06:29:44.706057'),
('q7gkm7wlbebx1k5n5jynicg9ru1ebt8c', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-15 05:50:30.333454'),
('s2rgs4dd2fm23scz571a4r5p9eog79mj', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 12:18:04.075084'),
('t18nr4io54pcht615w0gouriwqw4f64q', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 05:57:38.872000'),
('xy834w8lzkb1aq4aixcdg9evztihudlw', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 10:29:53.564247'),
('yorvmmw4936cs9fsbw4ussu8g9cubz8p', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 05:56:08.571592'),
('z6odfutxrl940mzyzqnijg8i5wud1z28', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 13:33:20.184854'),
('zikjw9ytzejs00oekvljk5r20nw0458k', 'ZjNlZjRmZmRiYzZiNDU0ZTYwOGU2YjlhMmI2NTYyYTkzOWM1Y2U5ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTg5NTY0MDM3NTRmM2FiNGYxMWNjZDFjNjEyZWU5OWFmOGVjZjZmIn0=', '2018-06-14 15:26:05.517599'),
('zkrr0c6mmx3hes9l15ga2bovvpsgwck9', 'ZDJmNDE0MTFhMGNlNzEzMjYzMzZkZjAwOGQxMGI4MDAzYTRjYzg1YTp7Il9hdXRoX3VzZXJfaWQiOiIxNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzkxYjk4MGIwN2M0M2FhZGNiMDk2ZjhhYjZlZjczMTY2OTgwOTZhYiJ9', '2018-06-15 06:26:04.476939');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_batchgroups`
--

CREATE TABLE `tbl_batchgroups` (
  `id` int(11) NOT NULL,
  `batchName` varchar(255) NOT NULL,
  `ranking` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_batchgroups`
--

INSERT INTO `tbl_batchgroups` (`id`, `batchName`, `ranking`) VALUES
(1, 'Smoke Vienna', 1),
(2, 'Russian', 2),
(3, 'Smokie', 3),
(4, 'Red Vienna', 4),
(5, 'French Polony', 14),
(6, 'Beef Griller', 5),
(7, 'Chilli Griller', 7),
(8, 'PnP Prem CCV', 10),
(9, 'PnP Prem CV', 9),
(10, 'PnP Prem PSV', 8),
(11, 'Smoked Griller', 6),
(12, 'Chicken Polony', 15),
(13, 'PnP NN CV', 11),
(14, 'Combos', 12),
(15, 'Hampers', 13),
(16, 'Labels', 20),
(17, 'PnP Prem CCP', 17),
(18, 'PnP Prem CP', 16),
(19, 'Liver Snack', 19),
(20, 'Special Garlic', 18);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_productlist`
--

CREATE TABLE `tbl_productlist` (
  `id` int(11) NOT NULL,
  `productID` varchar(20) NOT NULL,
  `prodDescription` varchar(255) DEFAULT NULL,
  `packaging` int(11) DEFAULT NULL,
  `unitWeight` double DEFAULT NULL,
  `packageWeight` double DEFAULT NULL,
  `productOnHold` int(11) DEFAULT NULL,
  `batchRanking` int(11) DEFAULT NULL,
  `batchgroup_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tbl_productlist`
--

INSERT INTO `tbl_productlist` (`id`, `productID`, `prodDescription`, `packaging`, `unitWeight`, `packageWeight`, `productOnHold`, `batchRanking`, `batchgroup_id`) VALUES
(1, 'CBG2', 'Beef Griller Chilled  2kg (Vacuum)', 6, 2, 2, 0, 3, 6),
(2, 'CBG500', 'Beef Griller Chilled 500g (Vacuum - Box )', 7, 0.5, 8, 0, 1, 6),
(3, 'CHG2', 'Chilli Griller 2kg (Vacuum)', 6, 2, 2, 0, 3, 7),
(4, 'CHG500', 'Chilli Griller 500g (Vacuum - Box)', 7, 0.5, 8, 0, 1, 7),
(5, 'CP1', 'Chicken Polony 1 kg (Box)', 2, 1, 18, 0, 3, 12),
(6, 'CP105', 'Chicken Polony 500g (10 in a bag)', 5, 0.5, 5, 0, 1, 12),
(7, 'CP2', 'Chicken Polony 2 kg (Box)', 2, 2, 18, 0, 4, 12),
(8, 'CP500', 'Chicken Polony 500g (Box)', 2, 0.5, 21, 0, 2, 12),
(9, 'CV1NN', 'Chicken Vienna No Name PnP 1 kg', 1, 1, 12, 0, 2, 13),
(10, 'CV500NN', 'Chicken Vienna No Name PnP 500g', 7, 0.5, 5, 0, 1, 13),
(11, 'ER1', 'Russian 1 kg (Vacuum - Box)', NULL, 1, 14, 0, 2, 2),
(12, 'ER2', 'Russian 2 kg (Bag)', NULL, 2, 2, 0, 5, 2),
(13, 'ER5', 'Russian 5 kg (Bag)', NULL, 5, 5, 0, 6, 2),
(14, 'ER500', 'Russian 500g (Vacuum)', NULL, 0.5, 7.5, 0, 1, 2),
(15, 'ERV2', 'Russian 2 kg (Vacuum)', NULL, 2, 2, 0, 4, 2),
(16, 'FLR', 'Footlong Russian 2 kg (Bag)', NULL, 2, 2, 0, 11, 2),
(17, 'FLRV', 'Footlong Russian 2 kg (Vacuum)', NULL, 2, 2, 0, 10, 2),
(18, 'FP1', 'French Polony 1 kg (Box)', NULL, 1, 18, 0, 6, 5),
(19, 'FP3', 'French Polony 3 kg (Box)', NULL, 3, 27, 0, 8, 5),
(20, 'FP105', 'French Polony 500g (Sak van 10)', NULL, 0.5, 5, 0, 3, 5),
(21, 'FP2', 'French Polony 2 kg (Box)', NULL, 2, 18, 0, 7, 5),
(22, 'FP250', 'French Polony 250g (Box)', NULL, 0.25, 18, 0, 2, 5),
(23, 'FP250S', 'French Polony 250g (Box)', NULL, 0.25, 7, 0, 1, 5),
(24, 'FP500', 'French Polony 500g (Box)', NULL, 0.5, 21, 0, 4, 5),
(25, 'FP750', 'French Polony 750g (Box)', NULL, 0.75, 13.5, 0, 5, 5),
(26, 'FRV1', 'Freshers Red Vienna 1 kg (Vacuum)', NULL, 1, 15, 0, 8, 4),
(27, 'FRVV2', 'Freshers Red Vienna 2 kg (Vacuum)', NULL, 2, 18, 0, 9, 4),
(28, 'FSSV2', 'Freshers Smokies 2 kg  (Vacuum)', NULL, 2, 2, 0, 11, 3),
(29, 'FSV1', 'Freshers Smoked Vienna 1 kg (Vacuum)', NULL, 1, 15, 0, 13, 1),
(30, 'FSVV2', 'Freshers Smoked Vienna 2 kg  (Vacuum)', NULL, 2, 2, 0, 14, 1),
(31, 'GC1.5', 'Griller Combo 1.5 kg (Vacuum)', NULL, 1.5, 1.5, 0, 1, 14),
(32, 'Lables', 'Labels', NULL, 0, 0, 0, 1, 16),
(33, 'LS500', 'Liver Snack 500g (Sak van 10)', NULL, 0, 5, 0, 1, 19),
(34, 'MAXI', 'Maxi Hamper', NULL, 4, 4, 0, 2, 15),
(35, 'MER1', 'Macro Russian 1 kg (Vacuum)', NULL, 1, 14, 0, 7, 2),
(36, 'MER5', 'Macro Russian 5 kg (Vacuum)', NULL, 5, 20, 0, 9, 2),
(37, 'MFLRV2', 'Macro Footlong Russian 2kg (Vacuum)', NULL, 2, 14, 0, 8, 2),
(38, 'MINI', 'Mini Hamper', NULL, 3, 3, 0, 1, 15),
(39, 'MRV1', 'Macro Red Vienna 1 kg (Vacuum)', NULL, 1, 15, 0, 10, 4),
(40, 'MRV5', 'Macro Red Vienna 5 kg (Vacuum)', NULL, 5, 20, 0, 11, 4),
(41, 'MSS1', 'Macro Smokie 1 kg (Vacuum)', NULL, 1, 14, 0, 12, 3),
(42, 'MSS5', 'Macro Smokie 5 kg (Bag)', NULL, 5, 20, 0, 14, 3),
(43, 'MSSV2', 'Macro Smokie 2 kg (Vacuum)', NULL, 2, 14, 0, 13, 3),
(44, 'MSV1', 'Macro Smoke Vienna 1 kg (Vacuum)', NULL, 1, 15, 0, 10, 1),
(45, 'MSV5', 'Macro Smoke Vienna 5 kg (Bag)', NULL, 5, 20, 0, 12, 1),
(46, 'MSVV2', 'Macro Smoke Vienna 2 kg (Vacuum)', NULL, 2, 18, 0, 11, 1),
(47, 'OFP2', 'OBC French Polony 2 kg', NULL, 2, 18, 0, 9, 5),
(48, 'PCCP750', 'PnP Prem Chicken Cheese Polony 750g', NULL, 0.75, 7.5, 0, 1, 17),
(49, 'PCCV1', 'PnP Prem Chicken Cheese Vienna 1 kg (Vacuum)', NULL, 1, 10, 0, 2, 8),
(50, 'PCCV500', 'PnP Prem Chicken Cheese Vienna 500g (Vacuum)', NULL, 0.5, 5, 0, 1, 8),
(51, 'PCP900', 'PnP Prem Chicken Polony 900g', NULL, 0.9, 9, 0, 1, 18),
(52, 'PCV1', 'PnP Prem Chicken Vienna 1 kg (Vacuum)', NULL, 1, 10, 0, 2, 9),
(53, 'PCV500', 'PnP Prem Chicken Vienna 500g (Vacuum)', NULL, 0.5, 5, 0, 1, 9),
(54, 'PDS500', 'PnP Deli Smokie 500g (Vacuum)', NULL, 0.5, 7.5, 0, 9, 3),
(55, 'PDV500', 'PnP Deli Smoke Vienna 500g (Vacuum)', NULL, 0.5, 8, 0, 8, 1),
(56, 'PPSV1', 'PnP Prem Smoke Vienna 1 kg (Vacuum)', NULL, 1, 10, 0, 2, 10),
(57, 'PPSV500', 'PnP Prem Smoke Vienna 500g (Vacuum)', NULL, 0.5, 5, 0, 1, 10),
(58, 'PSS2', 'PnP No Name Smokie 2 kg (Vacuum)', NULL, 2, 16, 0, 10, 3),
(59, 'PSV2', 'PnP No Name Smoke Vienna 2 kg (Vacuum)', NULL, 2, 16, 0, 9, 1),
(60, 'PVP3', 'PnP Hamper 3 kg', NULL, 3, 3, 0, 3, 15),
(61, 'PVP4', 'PnP Hamper 4 kg', NULL, 4, 4, 0, 4, 15),
(62, 'RG500', 'Red Griller 500g (Vacuum - Box)', NULL, 0.5, 8, 0, 12, 4),
(63, 'RGV2', 'Red Griller 2 kg (Vacuum)', NULL, 2, 2, 0, 14, 4),
(64, 'RV1', 'Red Vienna 1 kg (Vacuum)', NULL, 1, 15, 0, 2, 4),
(65, 'RV1NN', 'PnP No Name Red Vienna 1 kg (Vacuum)', NULL, 1, 12, 0, 7, 4),
(66, 'RV2', 'Red Vienna 2 kg (Bag)', NULL, 2, 2, 0, 4, 4),
(67, 'RV5', 'Red Vienna 5 kg (Bag)', NULL, 5, 5, 0, 5, 4),
(68, 'RV500', 'Red Vienna 500g (Vacuum)', NULL, 0.5, 8, 0, 1, 4),
(69, 'RV500NN', 'PnP No Name Red Vienna 500 g (Vacuum)', NULL, 0.5, 5, 0, 6, 4),
(70, 'RVV2', 'Red Vienna 2 kg (Vacuum)', NULL, 2, 2, 0, 3, 4),
(71, 'S/R Lables', 'Shoprite Labels', NULL, 0, 0, 0, 2, 16),
(72, 'SG2', 'Smoke Griller 2 kg (Vacuum)', NULL, 2, 2, 0, 3, 11),
(73, 'SG500', 'Smoke Griller 500g (Vacuum)', NULL, 0.5, 8, 0, 1, 11),
(74, 'SPG500', 'Special Garlic Polony 500g', NULL, 0.5, 5, 0, 1, 20),
(75, 'SRS2', 'Shoprite Smokie 2 kg (Vacuum) ???', NULL, 2, 2, 0, 7, 3),
(76, 'SS2', 'Smokies 2 kg (Bag)', NULL, 2, 2, 0, 4, 3),
(77, 'SS5', 'Smokies 5 kg (Bag)', NULL, 5, 5, 0, 5, 3),
(78, 'SS500', 'Smokies 500g (Vacuum)', NULL, 0.5, 8, 0, 1, 3),
(79, 'SSV2', 'Smokies 2 kg (Vacuum)', NULL, 2, 2, 0, 2, 3),
(80, 'SV1', 'Smoke Vienna 1 kg (Vacuum)', NULL, 1, 15, 0, 2, 1),
(81, 'SV1NN', 'PnP No Name Smoke Vienna 1 kg (Vacuum)', NULL, 1, 12, 0, 7, 1),
(82, 'SV2', 'Smoke Vienna 2 kg (Bag)', NULL, 2, 2, 0, 4, 1),
(83, 'SV5', 'Smoke Vienna 5 kg (Bag)', NULL, 5, 5, 0, 5, 1),
(84, 'SV500', 'Smoke Vienna 500g (Vacuum)', NULL, 0.5, 8, 0, 1, 1),
(85, 'SV500NN', 'PnP No Name Smoke Vienna 500 g (Vacuum)', NULL, 0.5, 5, 0, 6, 1),
(86, 'SVV2', 'Smoke Vienna 2 kg (Vacuum)', NULL, 2, 2, 0, 3, 1),
(87, 'VCBG2', 'Vencor Beef Griller Chilled 2 kg (Vacuum)', NULL, 2, 2, 0, 5, 6),
(88, 'VCHG2', 'Vencor Chilli Griller 2 kg (Vacuum)', NULL, 2, 2, 0, 5, 7),
(89, 'VERV2', 'Vencor Russian 2 kg (Vacuum)', NULL, 2, 2, 0, 3, 2),
(90, 'VSG2', 'Vencor Smoke Griller 2 kg (Vacuum)', NULL, 2, 2, 0, 5, 11),
(91, 'VSSV2', 'Vencor Smokie 2 kg (Vacuum)', NULL, 2, 2, 0, 3, 3),
(92, 'SRS2B', 'Shoprite Smokie 2 kg (Box)', 2, 2, 8, 0, 8, 3),
(93, 'SG2B', 'Smoke Griller 2 kg (Box)', 2, 2, 8, 0, 4, 11),
(94, 'CBG2B', 'Beef Griller Chilled 2 kg (Box)', 2, 2, 8, 0, 4, 6),
(95, 'RGV2B', 'Red Griller 2 kg (Box)', 2, 2, 8, 0, 15, 4),
(96, 'CHG2B', 'Chilli Griller 2 kg (Box)', 2, 2, 8, 0, 4, 7),
(97, 'GC1.5B', 'Griller Combo 1.5 kg (Box)', 2, 2, 7.5, 0, 2, 14),
(98, 'SRSS500B', 'Shoprite Smokie 500g (Box)', 2, 0.5, 8, 0, 6, 3),
(99, 'SG500B', 'Smoke Griller 500g (Box)', 2, 0.5, 8, 0, 2, 11),
(100, 'CBG500B', 'Beef Griller Chilled 500g (Box)', 2, 0.5, 8, 0, 2, 6),
(101, 'RG500B', 'Red Griller 500g (Box)', 2, 0.5, 8, 0, 13, 4),
(102, 'SRCG500B', 'Shoprite Chilli Griller 500g (Box)', 2, 0.5, 8, 0, 2, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `account_emailaddress_user_id_2c513194_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `key` (`key`),
  ADD KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`);

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `django_site`
--
ALTER TABLE `django_site`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`);

--
-- Indexes for table `tbl_batchgroups`
--
ALTER TABLE `tbl_batchgroups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `batchName` (`batchName`),
  ADD UNIQUE KEY `ranking` (`ranking`);

--
-- Indexes for table `tbl_productlist`
--
ALTER TABLE `tbl_productlist`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `productID` (`productID`),
  ADD KEY `tbl_productlist_batchgroup_id_fcd8c7f7_fk_tbl_batchgroups_id` (`batchgroup_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `django_site`
--
ALTER TABLE `django_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_batchgroups`
--
ALTER TABLE `tbl_batchgroups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `tbl_productlist`
--
ALTER TABLE `tbl_productlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`);

--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tbl_productlist`
--
ALTER TABLE `tbl_productlist`
  ADD CONSTRAINT `tbl_productlist_batchgroup_id_fcd8c7f7_fk_tbl_batchgroups_id` FOREIGN KEY (`batchgroup_id`) REFERENCES `tbl_batchgroups` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
