-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 20, 2022 at 02:11 PM
-- Server version: 8.0.27
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--
CREATE DATABASE IF NOT EXISTS `library` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `library`;

-- --------------------------------------------------------

--
-- Table structure for table `arrival`
--

CREATE TABLE `arrival` (
  `arrivalId` int NOT NULL,
  `bookId` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `dateArrived` date NOT NULL,
  `timeArrived` time NOT NULL,
  `quantity` int NOT NULL,
  `employeeId` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `arrival`
--

INSERT INTO `arrival` (`arrivalId`, `bookId`, `dateArrived`, `timeArrived`, `quantity`, `employeeId`) VALUES
(1, '9780547647135', '2021-12-19', '17:59:07', 2, 1),
(4, '9780547647135', '2022-01-02', '21:30:00', 2, 1),
(5, '9780132943260', '2022-01-06', '12:21:00', 5, 1),
(6, '9780547491127', '2022-01-06', '12:24:00', 3, 1),
(7, '9781119405375', '2022-01-13', '18:59:00', 2, 1),
(8, '9780132943260', '2022-01-20', '11:39:00', 1, 1),
(9, '9780132943260', '2022-01-20', '11:50:00', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `author`
--

CREATE TABLE `author` (
  `authorId` int NOT NULL,
  `firstName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `lastName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `dateofBirth` date DEFAULT NULL,
  `gender` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `emailAddress` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nationality` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `preferredLanguage` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `author`
--

INSERT INTO `author` (`authorId`, `firstName`, `lastName`, `dateofBirth`, `gender`, `emailAddress`, `nationality`, `preferredLanguage`) VALUES
(1, 'Ron', 'Larson', '1941-10-31', 'Male', 'ronlarson@gmail.com', 'American', 'English'),
(2, 'Roger', 'Beck', '1950-12-12', 'Male', 'rbbeck@eiu.edu', 'American', 'English'),
(4, 'Thomas', 'Connolly', '1949-09-06', 'Male', 'tconnolly@gmail.com', 'American', 'English'),
(5, 'Stephen', 'King', '1947-09-21', 'Male', 'steph_king@mail.com', 'American', 'English'),
(6, 'George', 'Martin', '1948-09-20', 'Male', 'Grrmbooks@georgerrmartin.com', 'American', 'English'),
(7, 'Jeremy', 'Blum', '1992-01-15', 'Male', 'jblum@mail.com', 'American', 'English'),
(9, 'Mahesh', 'Venkitachalam', '1974-06-20', 'Male', 'venkitachalam@gmail.com', 'Indian', 'English'),
(10, 'Laura', 'Igual', '1980-07-10', 'Female', 'ligual@ub.edu', 'Spanish', 'English');

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `bookid` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `bookPicture` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `bookTitle` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `bookReleaseYear` int DEFAULT NULL,
  `authorId` int NOT NULL,
  `publisherId` int NOT NULL,
  `genreId` int NOT NULL,
  `bookLanguage` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `bookPages` int NOT NULL,
  `bookQuantityTotal` int NOT NULL DEFAULT '0',
  `bookQuantityAvailable` int NOT NULL DEFAULT '0',
  `bookPrice` int NOT NULL,
  `bookSellPrice` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`bookid`, `bookPicture`, `bookTitle`, `bookReleaseYear`, `authorId`, `publisherId`, `genreId`, `bookLanguage`, `bookPages`, `bookQuantityTotal`, `bookQuantityAvailable`, `bookPrice`, `bookSellPrice`) VALUES
('9780132943260', '9780132943260.jpg', 'Database Systems: A Practical Approach to Design, Implementation, and Management, 6th Edition', 2014, 4, 6, 4, 'English', 1374, 5, 5, 750000, 800000),
('9780547491127', '9780547491127.jpg', 'World History: Patterns of Interaction, Student Edition Survey', 2010, 2, 2, 2, 'English', 1105, 3, 3, 900000, 950000),
('9780547647135', '9780547647135.jpg', 'Larson Algebra 1 (Common Core Edition)', 2012, 1, 1, 1, 'English', 756, 2, 2, 850000, 900000),
('9781119405375', '9781119405375.jpg', 'Exploring Arduino: Tools and Techniques for Engineering Wizardry', 2019, 7, 7, 4, 'English', 478, 1, 1, 250000, 300000),
('9781593276041', '9781593276041.jpg', 'Python Playground: Geeky Projects for the Curious Programmer', 2015, 9, 8, 4, 'English', 327, 0, 0, 70000, 100000),
('9783319500164', '9783319500164.jpg', 'Introduction to Data Science: A Python Approach to Concepts, Techniques and Applications', 2017, 10, 9, 4, 'English', 215, 0, 0, 860000, 900000);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customerId` int NOT NULL,
  `FirstName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `LastName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `dateofBirth` date NOT NULL,
  `gender` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `phoneNumber` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `emailAddress` varchar(255) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customerId`, `FirstName`, `LastName`, `dateofBirth`, `gender`, `phoneNumber`, `emailAddress`) VALUES
(1, 'Bulan', 'Wati', '1991-12-11', 'Female', '+62 856 2399 5678', 'bulanwati@gmail.com'),
(2, 'Zulfikar', 'Ibrahim', '1951-06-06', 'Male', '+62 813 2428 7099', 'zulfikarr@gmail.com'),
(3, 'Setiawan', 'Putra', '1985-04-18', 'Male', '+62 816 5489 9090', 'setia_one@gmail.com'),
(4, 'Hartono', 'Lesmono', '1976-06-16', 'Male', '+62 814 7543 2099', 'lesmono@email.co.id'),
(5, 'Susila', 'Ardhana', '1955-11-24', 'Male', '+62 813 8932 1454', 'tindakan_asusila@email.com');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `employeeId` int NOT NULL,
  `FirstName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `LastName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `dateofBirth` date NOT NULL,
  `gender` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `phoneNumber` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `emailAddress` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `homeAddress` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employeeId`, `FirstName`, `LastName`, `dateofBirth`, `gender`, `phoneNumber`, `emailAddress`, `homeAddress`) VALUES
(1, 'Galihffffff', 'Kamulyan', '2001-05-14', 'Male', '+62 813 2428 6048', 'akmal11hakim@gmail.com', 'Jl. Cempaka Putih Tengah No.51, Cempaka  Putih, Jakarta Pusat, Jakarta'),
(2, 'Akmal', 'Hakim', '2002-05-14', 'Male', '+62 816 4321 5678', 'galih11kamulyan@gmail.com', 'Jl. Panti Asuhan Ceger Pondok Aren No. 14, Pondok Aren, Tangerang Selatan, Banten'),
(3, 'Kusuma', 'Irawan', '1986-02-19', 'Male', '+62 812 5342 7585', 'kirawan@gmail.com', 'Jl. Pangeran No. 13, Jakarta Selatan, Jakarta'),
(4, 'Pangeran', 'Andrianshah', '1976-05-20', 'Male', '+62 812 4621 8978', 'pashah@gmail.com', 'Jl. Shah Alam No. 21, Jakarta Utara, Jakarta');

-- --------------------------------------------------------

--
-- Table structure for table `genre`
--

CREATE TABLE `genre` (
  `genreId` int NOT NULL,
  `genreName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `genreDescription` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `genre`
--

INSERT INTO `genre` (`genreId`, `genreName`, `genreDescription`) VALUES
(1, 'Mathematics', 'Involving numbers and calculations'),
(2, 'History', 'Learning past events and their significances'),
(3, 'Comedy', 'Making readers laughs from silly jokes'),
(4, 'Computer', 'Technology, application, function, and maintenance of computers'),
(5, 'Horror', 'Scary stories which may or may not scare you');

-- --------------------------------------------------------

--
-- Table structure for table `lending`
--

CREATE TABLE `lending` (
  `lendId` int NOT NULL,
  `dateBorrowed` date NOT NULL,
  `dueDate` date NOT NULL,
  `dateReturned` date DEFAULT NULL,
  `bookId` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `employeeId` int NOT NULL,
  `customerId` int NOT NULL,
  `charge` int NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'Being Lended'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lending`
--

INSERT INTO `lending` (`lendId`, `dateBorrowed`, `dueDate`, `dateReturned`, `bookId`, `employeeId`, `customerId`, `charge`, `status`) VALUES
(1, '2021-12-19', '2021-12-26', '2022-01-03', '9780547647135', 1, 3, 8000, 'Closed'),
(5, '2022-01-03', '2022-01-10', '2022-01-06', '9780547647135', 1, 1, 0, 'Closed'),
(9, '2022-01-06', '2022-01-13', '2022-01-07', '9780547491127', 1, 4, 0, 'Closed'),
(10, '2022-01-04', '2022-01-11', '2022-01-13', '9780132943260', 1, 2, 2000, 'Closed'),
(11, '2022-01-20', '2022-01-20', '2022-01-21', '9780132943260', 1, 4, 0, 'Closed');

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `publisherId` int NOT NULL,
  `publisherName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `publisherHeadquarter` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `publisherFullAddress` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `publisherEstablishedYear` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `publisher`
--

INSERT INTO `publisher` (`publisherId`, `publisherName`, `publisherHeadquarter`, `publisherFullAddress`, `publisherEstablishedYear`) VALUES
(1, 'Holt McDougal', 'New York', '3 Park Ave, New York, NY 10016, USA', 1960),
(2, 'Houghton Mifflin Harcourt', 'Boston', '125 High Street Boston, MA 02110 USA', 1995),
(3, 'Gagas Media', 'Jakarta', 'Jl. H. Montong No.57, RT.6/RW.3, Ciganjur, Kec. Jagakarsa, Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12630', 2003),
(4, 'Gramedia Pustaka Utama', 'Jakarta', 'Jl. Palmerah Barat 29-37 10270, RT.1/RW.2, Gelora, Tanah Abang, Jakarta Pusat, Jakarta 10270', 1974),
(5, 'Penerbit Erlangga', 'Jakarta', 'Jl. H. Baping No.100, RW.9, Ciracas, Kec. Ciracas, Daerah Khusus Ibukota Jakarta 13740', 1952),
(6, 'Pearson', 'London', '80 Strand, London, WC2R 0RL', 1998),
(7, 'Wiley', 'Hoboken', '111 River Street Hoboken, NJ 07030 USA', 1998),
(8, 'No Starch Press', 'San Francisco', '245 8th Street San Francisco, CA 94103 USA', 1994),
(9, 'Springer Publishing', 'New York', '11 W 42nd St Fl 15 New York, NY 10036 USA', 1950);

-- --------------------------------------------------------

--
-- Table structure for table `selling`
--

CREATE TABLE `selling` (
  `sellId` int NOT NULL,
  `dateSold` date NOT NULL,
  `timeSold` time NOT NULL,
  `bookId` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `employeeId` int NOT NULL,
  `customerId` int NOT NULL,
  `price` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `selling`
--

INSERT INTO `selling` (`sellId`, `dateSold`, `timeSold`, `bookId`, `employeeId`, `customerId`, `price`) VALUES
(1, '2021-12-19', '18:13:34', '9780547647135', 1, 2, 900000),
(5, '2022-01-05', '11:59:00', '9780547647135', 1, 1, 900000),
(6, '2022-01-02', '12:48:00', '9780132943260', 1, 3, 800000),
(7, '2022-01-13', '18:59:00', '9781119405375', 1, 4, 300000),
(8, '2022-01-20', '11:52:00', '9780132943260', 1, 2, 800000);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `picture` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `employeeId` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `picture`, `employeeId`) VALUES
('galih', '$2b$12$4RtFFapYe2psq0e0OCFnAu3s7yPRJ3dpMVjLbGufX/hhXTVNk.DWC', 'galih.png', 1),
('kirawan', '$2b$12$z9U52aEZBV8RcZXIkeejZeeEhEhqZwSJuebJojWJBOKTuw/ZQLDtK', 'kirawan.png', 3),
('mal', '$2b$12$NQShBPnUJ96gRj52ddVAMu/3EWyZ3G1Ibq0YpSJ.RMO7idOV9Uqni', NULL, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arrival`
--
ALTER TABLE `arrival`
  ADD PRIMARY KEY (`arrivalId`),
  ADD KEY `bookId` (`bookId`),
  ADD KEY `employeeId` (`employeeId`);

--
-- Indexes for table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`authorId`),
  ADD UNIQUE KEY `emailAddress` (`emailAddress`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`bookid`),
  ADD KEY `authorId` (`authorId`),
  ADD KEY `publisherId` (`publisherId`),
  ADD KEY `genreId` (`genreId`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customerId`),
  ADD UNIQUE KEY `emailAddress` (`emailAddress`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employeeId`),
  ADD UNIQUE KEY `emailAddress` (`emailAddress`);

--
-- Indexes for table `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`genreId`),
  ADD UNIQUE KEY `genreName` (`genreName`);

--
-- Indexes for table `lending`
--
ALTER TABLE `lending`
  ADD PRIMARY KEY (`lendId`),
  ADD KEY `bookId` (`bookId`),
  ADD KEY `customerId` (`customerId`),
  ADD KEY `employeeId` (`employeeId`);

--
-- Indexes for table `publisher`
--
ALTER TABLE `publisher`
  ADD PRIMARY KEY (`publisherId`),
  ADD UNIQUE KEY `publisherName` (`publisherName`),
  ADD KEY `publisherName_2` (`publisherName`);

--
-- Indexes for table `selling`
--
ALTER TABLE `selling`
  ADD PRIMARY KEY (`sellId`),
  ADD KEY `bookId` (`bookId`),
  ADD KEY `customerId` (`customerId`),
  ADD KEY `employeeId` (`employeeId`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`),
  ADD KEY `employeeId` (`employeeId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arrival`
--
ALTER TABLE `arrival`
  MODIFY `arrivalId` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `author`
--
ALTER TABLE `author`
  MODIFY `authorId` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customerId` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `employeeId` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `genre`
--
ALTER TABLE `genre`
  MODIFY `genreId` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `lending`
--
ALTER TABLE `lending`
  MODIFY `lendId` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `publisher`
--
ALTER TABLE `publisher`
  MODIFY `publisherId` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `selling`
--
ALTER TABLE `selling`
  MODIFY `sellId` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `arrival`
--
ALTER TABLE `arrival`
  ADD CONSTRAINT `arrival_ibfk_1` FOREIGN KEY (`bookId`) REFERENCES `book` (`bookid`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `arrival_ibfk_2` FOREIGN KEY (`employeeId`) REFERENCES `employee` (`employeeId`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `book_ibfk_1` FOREIGN KEY (`authorId`) REFERENCES `author` (`authorId`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `book_ibfk_2` FOREIGN KEY (`publisherId`) REFERENCES `publisher` (`publisherId`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `book_ibfk_3` FOREIGN KEY (`genreId`) REFERENCES `genre` (`genreId`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `lending`
--
ALTER TABLE `lending`
  ADD CONSTRAINT `lending_ibfk_1` FOREIGN KEY (`bookId`) REFERENCES `book` (`bookid`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `lending_ibfk_2` FOREIGN KEY (`customerId`) REFERENCES `customer` (`customerId`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `lending_ibfk_3` FOREIGN KEY (`employeeId`) REFERENCES `employee` (`employeeId`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `selling`
--
ALTER TABLE `selling`
  ADD CONSTRAINT `selling_ibfk_1` FOREIGN KEY (`bookId`) REFERENCES `book` (`bookid`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `selling_ibfk_2` FOREIGN KEY (`customerId`) REFERENCES `customer` (`customerId`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `selling_ibfk_3` FOREIGN KEY (`employeeId`) REFERENCES `employee` (`employeeId`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`employeeId`) REFERENCES `employee` (`employeeId`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
