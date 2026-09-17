-- Full Stack Investigation System - Target Bank dataset
-- MySQL / phpMyAdmin compatible
-- Same data as locations.csv and targets.csv
-- Fictional target names used for training/exam purposes.

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `targets`;
DROP TABLE IF EXISTS `locations`;

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `locations` (
    `id` INT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `lat` DECIMAL(9,6) NOT NULL,
    `long` DECIMAL(9,6) NOT NULL,
    `country` VARCHAR(100) NOT NULL,
    `description` VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `targets` (
    `id` INT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL UNIQUE,
    `organization` VARCHAR(50) NOT NULL,
    `danger_level` INT NOT NULL,
    `rank` VARCHAR(50) NOT NULL,
    `last_known_location_id` INT NOT NULL,
    CONSTRAINT `fk_targets_last_location`
        FOREIGN KEY (`last_known_location_id`)
        REFERENCES `locations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `locations` (`id`, `name`, `lat`, `long`, `country`, `description`) VALUES
(1, 'Beirut Central', 33.8938, 35.5018, 'Lebanon', 'Dense urban area in central Beirut'),
(2, 'Beirut South', 33.8547, 35.5039, 'Lebanon', 'Southern urban district'),
(3, 'Tyre North', 33.2873, 35.2029, 'Lebanon', 'Area north of Tyre'),
(4, 'Tyre East', 33.27, 35.25, 'Lebanon', 'Eastern outskirts of Tyre'),
(5, 'Sidon Central', 33.5606, 35.3758, 'Lebanon', 'Central area of Sidon'),
(6, 'Sidon East', 33.558, 35.41, 'Lebanon', 'Eastern outskirts of Sidon'),
(7, 'Nabatieh Central', 33.3772, 35.4838, 'Lebanon', 'Central Nabatieh area'),
(8, 'Nabatieh South', 33.345, 35.485, 'Lebanon', 'Area south of Nabatieh'),
(9, 'Bint Jbeil', 33.1194, 35.4333, 'Lebanon', 'Town area in southern Lebanon'),
(10, 'Marjayoun', 33.3603, 35.5911, 'Lebanon', 'Town area in southeastern Lebanon'),
(11, 'Baalbek', 34.0058, 36.2181, 'Lebanon', 'Urban area in the Beqaa Valley'),
(12, 'Zahle', 33.8463, 35.902, 'Lebanon', 'Urban area in the Beqaa Valley'),
(13, 'Tripoli Central', 34.4367, 35.8497, 'Lebanon', 'Central Tripoli area'),
(14, 'Gaza City North', 31.535, 34.47, 'Palestinian Territories', 'Northern area of Gaza City'),
(15, 'Gaza City South', 31.495, 34.45, 'Palestinian Territories', 'Southern area of Gaza City'),
(16, 'Khan Yunis', 31.3462, 34.3063, 'Palestinian Territories', 'Urban area of Khan Yunis'),
(17, 'Rafah', 31.2969, 34.2455, 'Palestinian Territories', 'Urban area of Rafah'),
(18, 'Deir al-Balah', 31.418, 34.351, 'Palestinian Territories', 'Central Gaza area'),
(19, 'Jabalia', 31.528, 34.483, 'Palestinian Territories', 'Urban area of Jabalia'),
(20, 'Beit Lahia', 31.546, 34.495, 'Palestinian Territories', 'Northern Gaza area');

INSERT INTO `targets` (`id`, `name`, `organization`, `danger_level`, `rank`, `last_known_location_id`) VALUES
(1, 'Cedar Falcon', 'hezbollah', 8, 'regional_commander', 8),
(2, 'Silver Ridge', 'hamas', 5, 'intelligence_officer', 16),
(3, 'Night Lantern', 'hezbollah', 2, 'field_commander', 5),
(4, 'Blue Cedar', 'hamas', 9, 'communications_officer', 17),
(5, 'Desert Echo', 'hezbollah', 6, 'team_leader', 2),
(6, 'Iron Compass', 'hamas', 3, 'logistics_officer', 18),
(7, 'Green Tower', 'hezbollah', 10, 'operative', 12),
(8, 'Quiet River', 'hamas', 7, 'regional_commander', 19),
(9, 'Stone Harbor', 'hezbollah', 4, 'intelligence_officer', 9),
(10, 'Red Valley', 'hamas', 1, 'field_commander', 20),
(11, 'Northern Star', 'hezbollah', 8, 'communications_officer', 6),
(12, 'Copper Hill', 'hamas', 5, 'team_leader', 14),
(13, 'Hidden Cedar', 'hezbollah', 2, 'logistics_officer', 3),
(14, 'Gray Horizon', 'hamas', 9, 'operative', 15),
(15, 'Silent Bridge', 'hezbollah', 6, 'regional_commander', 13),
(16, 'Amber Field', 'hamas', 3, 'intelligence_officer', 16),
(17, 'Black Pine', 'hezbollah', 10, 'field_commander', 10),
(18, 'White Dune', 'hamas', 7, 'communications_officer', 17),
(19, 'Eastern Gate', 'hezbollah', 4, 'team_leader', 7),
(20, 'Olive Shadow', 'hamas', 1, 'logistics_officer', 18),
(21, 'River Hawk', 'hezbollah', 8, 'operative', 4),
(22, 'Mountain Echo', 'hamas', 5, 'regional_commander', 19),
(23, 'Delta Cedar', 'hezbollah', 2, 'intelligence_officer', 1),
(24, 'Sand Falcon', 'hamas', 9, 'field_commander', 20),
(25, 'Coastal Stone', 'hezbollah', 6, 'communications_officer', 11),
(26, 'Winter Lantern', 'hamas', 3, 'team_leader', 14),
(27, 'Southern Ridge', 'hezbollah', 10, 'logistics_officer', 8),
(28, 'Blue Horizon', 'hamas', 7, 'operative', 15),
(29, 'Iron Valley', 'hezbollah', 4, 'regional_commander', 5),
(30, 'Cedar Point', 'hamas', 1, 'intelligence_officer', 16),
(31, 'Night Harbor', 'hezbollah', 8, 'field_commander', 2),
(32, 'Golden Dune', 'hamas', 5, 'communications_officer', 17),
(33, 'Silent Tower', 'hezbollah', 2, 'team_leader', 12),
(34, 'Red Compass', 'hamas', 9, 'logistics_officer', 18),
(35, 'Olive Falcon', 'hezbollah', 6, 'operative', 9),
(36, 'Gray Bridge', 'hamas', 3, 'regional_commander', 19),
(37, 'Copper River', 'hezbollah', 10, 'intelligence_officer', 6),
(38, 'Eastern Cedar', 'hamas', 7, 'field_commander', 20),
(39, 'Black Horizon', 'hezbollah', 4, 'communications_officer', 3),
(40, 'Silver Field', 'hamas', 1, 'team_leader', 14),
(41, 'Desert Lantern', 'hezbollah', 8, 'logistics_officer', 13),
(42, 'Northern Pine', 'hamas', 5, 'operative', 15),
(43, 'Stone Falcon', 'hezbollah', 2, 'regional_commander', 10),
(44, 'Quiet Valley', 'hamas', 9, 'intelligence_officer', 16),
(45, 'Amber Ridge', 'hezbollah', 6, 'field_commander', 7),
(46, 'Coastal Echo', 'hamas', 3, 'communications_officer', 17),
(47, 'White Harbor', 'hezbollah', 10, 'team_leader', 4),
(48, 'Green Compass', 'hamas', 7, 'logistics_officer', 18),
(49, 'Delta Tower', 'hezbollah', 4, 'operative', 1),
(50, 'Winter Cedar', 'hamas', 1, 'regional_commander', 19);
