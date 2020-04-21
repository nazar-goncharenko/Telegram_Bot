-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 21, 2020 at 10:26 PM
-- Server version: 5.7.24
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `subject`
--

-- --------------------------------------------------------

--
-- Table structure for table `links`
--

CREATE TABLE `links` (
  `link_id` int(11) NOT NULL,
  `url` text,
  `rating` int(11) DEFAULT NULL,
  `reports` int(11) DEFAULT NULL,
  `topic_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `userId` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `links`
--

INSERT INTO `links` (`link_id`, `url`, `rating`, `reports`, `topic_id`, `title`, `userId`) VALUES
(1, 'http://difur.in.ua/studentam/lektsii/lc03/', NULL, NULL, 1, '1st order', NULL),
(2, 'https://yukhym.com/uk/prikladi-diferentsialnikh-rivnyan/neodnoridni-diferentsialni-rivnyannya-2-poryadku.html', NULL, NULL, 2, '2nd order', NULL),
(3, 'https://uk.wikipedia.org/wiki/%D0%A0%D1%8F%D0%B4_(%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0)', NULL, NULL, 3, 'Rows', NULL),
(4, 'https://en.wikipedia.org/wiki/Multiple_integral', NULL, NULL, 4, 'Double integrals', NULL),
(5, 'https://en.wikipedia.org/wiki/Probability_theory#Discrete_probability_distributions', NULL, NULL, 5, 'Probability', NULL),
(6, 'https://www.bincodes.com/bin-search/', NULL, NULL, 6, 'Bin search', NULL),
(7, 'https://www.perfect-english-grammar.com/', NULL, NULL, 7, 'Perfect grammar', NULL),
(8, 'https://learnenglish.britishcouncil.org/vocabulary', NULL, NULL, 8, 'British vocabulary', NULL),
(9, 'https://francais.lingolia.com/en/grammar', NULL, NULL, 9, 'Grammar', NULL),
(10, 'https://www.frenchpod101.com/french-word-lists/', NULL, NULL, 10, '100 core french words', NULL),
(11, 'https://learngerman.dw.com/en/grammar', NULL, NULL, 11, 'DW grammar', NULL),
(12, 'https://german.net/vocabulary/', NULL, NULL, 12, 'German vocabulary', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ssubject`
--

CREATE TABLE `ssubject` (
  `sSubject_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ssubject`
--

INSERT INTO `ssubject` (`sSubject_id`, `title`, `subject_id`) VALUES
(1, 'Diffuru', 1),
(2, 'Math analythis', 1),
(3, 'Probability theory', 1),
(4, 'Bin search', 2),
(5, 'English', 3),
(6, 'French', 3),
(7, 'German', 3);

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `subject_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`subject_id`, `name`) VALUES
(1, 'Math'),
(2, 'Programming'),
(3, 'Languages');

-- --------------------------------------------------------

--
-- Table structure for table `topic`
--

CREATE TABLE `topic` (
  `topic_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `ssubject_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `topic`
--

INSERT INTO `topic` (`topic_id`, `title`, `ssubject_id`) VALUES
(1, '1st order', 1),
(2, '2nd order', 1),
(3, 'Rows', 2),
(4, 'Double integrals', 2),
(5, 'Discrete probability distributions', 3),
(6, 'Bin search', 4),
(7, 'Grammar', 5),
(8, 'Vocabulary', 5),
(9, 'Grammaire', 6),
(10, 'Vocabulaire', 6),
(11, 'Grammatik', 7),
(12, 'Wortschatz', 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `links`
--
ALTER TABLE `links`
  ADD PRIMARY KEY (`link_id`),
  ADD KEY `topic_id` (`topic_id`);

--
-- Indexes for table `ssubject`
--
ALTER TABLE `ssubject`
  ADD PRIMARY KEY (`sSubject_id`),
  ADD KEY `title` (`title`) USING BTREE,
  ADD KEY `subject_id` (`subject_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`subject_id`);

--
-- Indexes for table `topic`
--
ALTER TABLE `topic`
  ADD PRIMARY KEY (`topic_id`),
  ADD KEY `title` (`title`) USING BTREE,
  ADD KEY `ssubject_id` (`ssubject_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `links`
--
ALTER TABLE `links`
  MODIFY `link_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `ssubject`
--
ALTER TABLE `ssubject`
  MODIFY `sSubject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `subject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `topic`
--
ALTER TABLE `topic`
  MODIFY `topic_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `links`
--
ALTER TABLE `links`
  ADD CONSTRAINT `links_ibfk_1` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`topic_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ssubject`
--
ALTER TABLE `ssubject`
  ADD CONSTRAINT `ssubject_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `topic`
--
ALTER TABLE `topic`
  ADD CONSTRAINT `topic_ibfk_1` FOREIGN KEY (`ssubject_id`) REFERENCES `ssubject` (`sSubject_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
