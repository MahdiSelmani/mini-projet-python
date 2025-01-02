-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 02 jan. 2025 à 20:52
-- Version du serveur : 8.3.0
-- Version de PHP : 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `recruitmentdb`
--

-- --------------------------------------------------------

--
-- Structure de la table `candidate`
--

DROP TABLE IF EXISTS `candidate`;
CREATE TABLE IF NOT EXISTS `candidate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `job_id` int NOT NULL,
  `resume_path` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cover_letter_path` text,
  `experience` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `job_id` (`job_id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `candidate`
--

INSERT INTO `candidate` (`id`, `name`, `email`, `job_id`, `resume_path`, `cover_letter_path`, `experience`) VALUES
(22, 'mahdi selmani', 'selmani@gmail.com', 1, 'cv_Mahdi_SELMANI_En_.pdf', 'TD1_questions.docx', 1);

-- --------------------------------------------------------

--
-- Structure de la table `job`
--

DROP TABLE IF EXISTS `job`;
CREATE TABLE IF NOT EXISTS `job` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `skills` text NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `job`
--

INSERT INTO `job` (`id`, `title`, `description`, `skills`, `is_active`) VALUES
(1, 'Full Stack Developer', 'Design, develop, and maintain web and desktop applications with a focus on performance, scalability, and reliability.\r\nBuild responsive user interfaces using ReactJS, Angular, and JavaFX frameworks.\r\nDevelop and optimize back-end solutions using Spring Boot, ExpressJS, and Hibernate.\r\nIntegrate with third-party APIs and services for enhanced functionality (e.g., Google Maps API, Stripe).\r\nImplement RESTful APIs and manage database integration using MySQL, MongoDB, and Oracle.\r\nWork collaboratively in an Agile Scrum environment, contributing to sprint planning, daily stand-ups, and retrospectives.\r\nConduct unit tests, bug fixes, and performance optimizations to ensure high-quality software delivery.\r\nCollaborate with cross-functional teams to deliver innovative solutions for internal and client-facing applications.\r\nKeep up to date with the latest industry trends and technologies to bring new ideas and improvements to the team.\r\nRequirements:\r\n\r\nBachelor’s or Master’s degree in Software Engineering or a related field.\r\nProven experience with JavaSE 8/11, JavaScript (ES6/ES2015), and TypeScript.\r\nStrong knowledge of front-end frameworks like ReactJS, Angular, HTML5, CSS3, and Bootstrap.\r\nHands-on experience with back-end technologies such as Spring 5, NodeJs, ExpressJs, and Hibernate.\r\nExperience with database management and design, particularly with MySQL, MongoDB, and Oracle.\r\n', 'html, css, js, react, angular', 1),
(4, 'Test job', 'test description', 'java, html ,css ', 1),
(8, 'Developpeur full stack', 'Nous recherchons un Développeur Full Stack passionné et dynamique pour rejoindre notre équipe innovante. En tant que membre clé de notre équipe de développement, vous serez responsable de la création et de la maintenance des applications web de bout en bout. Vous travaillerez sur des projets stimulants et participerez à toutes les étapes du développement, depuis la conception jusqu\'à la mise en production.', 'JavaScript, TypeScript, Java, Python, Scala, SQL, MongoDB, Oracle, MySQL, Express, Node.js, Spring, Spring Boot', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
