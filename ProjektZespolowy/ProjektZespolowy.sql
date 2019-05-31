-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 29, 2019 at 12:19 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ProjektZespolowy`
--

-- --------------------------------------------------------

--
-- Table structure for table `czlonkowie`
--

CREATE TABLE `czlonkowie` (
  `osobaosoba_id` int(11) NOT NULL,
  `grupagrupa_id` int(11) NOT NULL,
  `czy_lider` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_polish_ci;

--
-- Dumping data for table `czlonkowie`
--

INSERT INTO `czlonkowie` (`osobaosoba_id`, `grupagrupa_id`, `czy_lider`) VALUES
(40, 16, 1),
(41, 17, 1),
(42, 18, 1),
(43, 19, 1);

-- --------------------------------------------------------

--
-- Table structure for table `firma`
--

CREATE TABLE `firma` (
  `firma_id` int(11) NOT NULL,
  `nazwa` varchar(50) COLLATE utf16_polish_ci NOT NULL,
  `opis` varchar(255) COLLATE utf16_polish_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `czy_aktywna` tinyint(1) DEFAULT NULL,
  `miejscowosc` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `ulica` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `numer_budynku` varchar(20) COLLATE utf16_polish_ci DEFAULT NULL,
  `numer_mieszkania` varchar(20) COLLATE utf16_polish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_polish_ci;

--
-- Dumping data for table `firma`
--

INSERT INTO `firma` (`firma_id`, `nazwa`, `opis`, `email`, `czy_aktywna`, `miejscowosc`, `ulica`, `numer_budynku`, `numer_mieszkania`) VALUES
(1, 'testowa', NULL, NULL, 1, NULL, NULL, NULL, NULL),
(2, 'Samsung', NULL, NULL, 1, NULL, NULL, NULL, NULL),
(3, 'Nowa', NULL, NULL, 1, NULL, NULL, NULL, NULL),
(4, 'Nokia', NULL, NULL, 1, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `grupa`
--

CREATE TABLE `grupa` (
  `grupa_id` int(11) NOT NULL,
  `projektProjekt_id` int(11) DEFAULT NULL,
  `nazwa` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `opis` varchar(255) COLLATE utf16_polish_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `liczba_czlonkow` int(11) NOT NULL,
  `stan_zapisu` int(11) NOT NULL,
  `data_zgloszenia` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_polish_ci;

--
-- Dumping data for table `grupa`
--

INSERT INTO `grupa` (`grupa_id`, `projektProjekt_id`, `nazwa`, `opis`, `email`, `liczba_czlonkow`, `stan_zapisu`, `data_zgloszenia`) VALUES
(16, 20, NULL, '223216@pwr.edu.pl', '223216@pwr.edu.pl', 1, 3, NULL),
(17, 20, NULL, '123123@pwr.edu.pl', '123123@pwr.edu.pl', 1, 3, NULL),
(18, 11, NULL, '321321@pwr.edu.pl', '321321@pwr.edu.pl', 1, 1, '2019-05-29 12:17:59'),
(19, 23, NULL, '222222@pwr.edu.pl', '222222@pwr.edu.pl', 1, 3, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `osoba`
--

CREATE TABLE `osoba` (
  `id` int(11) NOT NULL,
  `imie` varchar(50) COLLATE utf16_polish_ci NOT NULL,
  `nazwisko` varchar(50) COLLATE utf16_polish_ci NOT NULL,
  `email` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `telefon` varchar(13) COLLATE utf16_polish_ci DEFAULT NULL,
  `rok` int(11) DEFAULT NULL,
  `specialnosc` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `login` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `haslo` varchar(60) COLLATE utf16_polish_ci DEFAULT NULL,
  `numer_indeksu` int(11) DEFAULT NULL,
  `rodzaj_konta` smallint(6) NOT NULL,
  `stan_konta` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_polish_ci;

--
-- Dumping data for table `osoba`
--

INSERT INTO `osoba` (`id`, `imie`, `nazwisko`, `email`, `telefon`, `rok`, `specialnosc`, `login`, `haslo`, `numer_indeksu`, `rodzaj_konta`, `stan_konta`) VALUES
(16, 'Jan', 'Nowak', 'Jannow@gmail.com', NULL, NULL, NULL, 'Jannow', '$2b$12$u2IqYLnhelCMLCsx7d90neiUDUrN5DmnDIEAgTkR4w76y//1VJAx6', NULL, 3, 1),
(22, 'pwr', 'pwr', 'pwrpwr@o2.pl', NULL, NULL, NULL, 'pwrpwr', '$2b$12$yHI/raU2BueBI/vpoXOqT.n.fuVT0T1YUFGAXOnm.w8WQ07CZeClS', NULL, 2, NULL),
(30, 'test', 'test', 'testtest@o2.pl', NULL, NULL, 'ZastepczyProwadzacy', 'testtest', '$2b$12$lEqb3f9.jZ.Kl4vaDoKC7.Tp3OevuR8F8kv89/xT/6FxUkOfa5BTe', 225443, 3, 1),
(39, 'Nokiowy', 'Noki', 'Nokia@email.com', NULL, NULL, NULL, 'noknok', '$2b$12$epgUIDlgsXaH2du5QjwYdeU1eghePG2xso5KxxMN2UhO2NwWGT2Im', NULL, 3, 1),
(40, 'Lid', 'Gru', '223216@pwr.edu.pl', NULL, NULL, NULL, 'lidgru', '$2b$12$qzFX.7bIbp2mxFWfIL7MjOFi/0.SMk6E8IlM1zUW5fJ2kTOyTMiIu', 223216, 1, NULL),
(41, 'stu', 'stu', '123123@pwr.edu.pl', NULL, NULL, NULL, 'stustu', '$2b$12$lDP/J.LB.8NoRkeX.B1z3O2AozbctYHS035JC.MsBOcxqPQZkuiQK', 123123, 1, NULL),
(42, 'wol', 'wol', '321321@pwr.edu.pl', NULL, NULL, NULL, 'wolwol', '$2b$12$sqMoPIEmdwVkf3FBpQTnzO6wOA3MCoPKYRXkMblZwxEYGTQo7lJ/C', 321321, 1, NULL),
(43, 'Nowy', 'Student', '222222@pwr.edu.pl', NULL, NULL, NULL, 'grugru', '$2b$12$ErxHh92EOVGqsVP0.whUQ.wl7fsoXCu1aNiDKj6vgdsoWqnHDR/Sm', 222222, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `pracownicy_firmy`
--

CREATE TABLE `pracownicy_firmy` (
  `osobaosoba_id` int(11) NOT NULL,
  `firmafirma_id` int(11) NOT NULL,
  `czy_glowny` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_polish_ci;

--
-- Dumping data for table `pracownicy_firmy`
--

INSERT INTO `pracownicy_firmy` (`osobaosoba_id`, `firmafirma_id`, `czy_glowny`) VALUES
(16, 3, 1),
(39, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `projekt`
--

CREATE TABLE `projekt` (
  `projekt_id` int(11) NOT NULL,
  `firmafirma_id` int(11) DEFAULT NULL,
  `osobaosoba_id` int(11) NOT NULL,
  `semestr` varchar(50) COLLATE utf16_polish_ci NOT NULL,
  `tytul` varchar(100) COLLATE utf16_polish_ci NOT NULL,
  `komentarz` text COLLATE utf16_polish_ci,
  `opis` text COLLATE utf16_polish_ci NOT NULL,
  `naklad_czasu` varchar(50) COLLATE utf16_polish_ci NOT NULL,
  `max_studentow` smallint(6) NOT NULL,
  `min_studentow` smallint(6) NOT NULL,
  `max_grup` smallint(6) NOT NULL,
  `ilosc_zapisanych_grup` int(11) NOT NULL,
  `status` smallint(6) NOT NULL,
  `opiekun_nazwisko` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `opiekun_imie` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `opiekun_email` varchar(50) COLLATE utf16_polish_ci DEFAULT NULL,
  `data_zgloszenia` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_polish_ci;

--
-- Dumping data for table `projekt`
--

INSERT INTO `projekt` (`projekt_id`, `firmafirma_id`, `osobaosoba_id`, `semestr`, `tytul`, `komentarz`, `opis`, `naklad_czasu`, `max_studentow`, `min_studentow`, `max_grup`, `ilosc_zapisanych_grup`, `status`, `opiekun_nazwisko`, `opiekun_imie`, `opiekun_email`, `data_zgloszenia`) VALUES
(11, NULL, 30, 'brak', 'Brak projektu', NULL, 'brak', 'brak', 10, 1, 1, 0, 1, NULL, NULL, NULL, NULL),
(20, 4, 39, 'letni 2018/2019', 'Projekt Nokia', '', 'To jest projekt z konta NokNok', '50 -100 h', 4, 1, 2, 2, 4, NULL, NULL, NULL, '2019-05-23'),
(21, 3, 16, 'Zimowy', 'LoRa transceiver for unmanned aerial vehicle', '', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eros metus, luctus sit amet volutpat at, feugiat non metus. Sed et mauris massa. Donec sollicitudin tellus neque, a luctus quam pulvinar a. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec sodales neque odio, a euismod lorem placerat et. Phasellus faucibus consectetur nisl. Mauris et imperdiet odio. In eleifend, ipsum et semper sagittis, massa orci euismod erat, vitae semper massa lectus ac ante. Curabitur at mi placerat, semper tellus et, maximus massa. Praesent non lectus mollis, sagittis nisl vel, facilisis diam.\r\n\r\nCurabitur suscipit erat a turpis efficitur, a laoreet massa pretium. Curabitur aliquet ex sed blandit varius. Donec posuere mi ac lectus pulvinar, ac congue elit iaculis. Suspendisse potenti. Nullam tempor quam a risus sollicitudin, et fringilla turpis posuere. Vestibulum ullamcorper nunc id nulla ornare, ac faucibus diam eleifend. Nam interdum, arcu eu lacinia consequat, massa ante finibus dui, ac mattis nulla mi sed lectus. Etiam accumsan eu leo non rhoncus. Etiam sollicitudin suscipit nulla ac porta. Fusce sit amet libero ultricies, hendrerit nibh nec, fermentum lacus.', '100-200h', 5, 2, 1, 0, 2, NULL, NULL, NULL, '2019-05-23'),
(23, 3, 16, 'Zimowy', 'Nowy test ilosci grup', '', 'To jest test dodawania wiecej niz jdnej grupy do projektu', '123-222', 4, 1, 4, 1, 3, NULL, NULL, NULL, '2019-05-23');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `czlonkowie`
--
ALTER TABLE `czlonkowie`
  ADD PRIMARY KEY (`osobaosoba_id`,`grupagrupa_id`),
  ADD KEY `idx_czlonkowie__osobaosoba_id` (`osobaosoba_id`),
  ADD KEY `fk_czlonkowie__grupagrupa_id` (`grupagrupa_id`);

--
-- Indexes for table `firma`
--
ALTER TABLE `firma`
  ADD PRIMARY KEY (`firma_id`);

--
-- Indexes for table `grupa`
--
ALTER TABLE `grupa`
  ADD PRIMARY KEY (`grupa_id`),
  ADD KEY `FKgrupa891664` (`projektProjekt_id`);

--
-- Indexes for table `osoba`
--
ALTER TABLE `osoba`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `login` (`login`),
  ADD UNIQUE KEY `numer_indeksu` (`numer_indeksu`);

--
-- Indexes for table `pracownicy_firmy`
--
ALTER TABLE `pracownicy_firmy`
  ADD PRIMARY KEY (`osobaosoba_id`,`firmafirma_id`),
  ADD KEY `idx_pracownicy_firmy__osobaosoba_id` (`osobaosoba_id`),
  ADD KEY `fk_pracownicy_firmy__firmafirma_id` (`firmafirma_id`);

--
-- Indexes for table `projekt`
--
ALTER TABLE `projekt`
  ADD PRIMARY KEY (`projekt_id`),
  ADD KEY `FKprojekt5523` (`firmafirma_id`),
  ADD KEY `Prowadzacy Projekt PWR` (`osobaosoba_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `firma`
--
ALTER TABLE `firma`
  MODIFY `firma_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `grupa`
--
ALTER TABLE `grupa`
  MODIFY `grupa_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `osoba`
--
ALTER TABLE `osoba`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `projekt`
--
ALTER TABLE `projekt`
  MODIFY `projekt_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `czlonkowie`
--
ALTER TABLE `czlonkowie`
  ADD CONSTRAINT `FKczlonkowie400752` FOREIGN KEY (`osobaosoba_id`) REFERENCES `osoba` (`id`),
  ADD CONSTRAINT `FKczlonkowie542576` FOREIGN KEY (`grupagrupa_id`) REFERENCES `grupa` (`grupa_id`),
  ADD CONSTRAINT `fk_czlonkowie__grupagrupa_id` FOREIGN KEY (`grupagrupa_id`) REFERENCES `grupa` (`grupa_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_czlonkowie__osobaosoba_id` FOREIGN KEY (`osobaosoba_id`) REFERENCES `osoba` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `grupa`
--
ALTER TABLE `grupa`
  ADD CONSTRAINT `FKgrupa891664` FOREIGN KEY (`projektProjekt_id`) REFERENCES `projekt` (`projekt_id`);

--
-- Constraints for table `pracownicy_firmy`
--
ALTER TABLE `pracownicy_firmy`
  ADD CONSTRAINT `FKpracownicy766288` FOREIGN KEY (`firmafirma_id`) REFERENCES `firma` (`firma_id`),
  ADD CONSTRAINT `FKpracownicy932837` FOREIGN KEY (`osobaosoba_id`) REFERENCES `osoba` (`id`),
  ADD CONSTRAINT `fk_pracownicy_firmy__firmafirma_id` FOREIGN KEY (`firmafirma_id`) REFERENCES `firma` (`firma_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_pracownicy_firmy__osobaosoba_id` FOREIGN KEY (`osobaosoba_id`) REFERENCES `osoba` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `projekt`
--
ALTER TABLE `projekt`
  ADD CONSTRAINT `FKprojekt5523` FOREIGN KEY (`firmafirma_id`) REFERENCES `firma` (`firma_id`),
  ADD CONSTRAINT `Prowadzacy Projekt PWR` FOREIGN KEY (`osobaosoba_id`) REFERENCES `osoba` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
