/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : ffmpeg

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 25/08/2020 19:07:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for chang_video_speed
-- ----------------------------
DROP TABLE IF EXISTS `chang_video_speed`;
CREATE TABLE `chang_video_speed`  (
  `year` tinyint UNSIGNED NOT NULL COMMENT '年（两位）',
  `month` tinyint UNSIGNED NOT NULL COMMENT '月（两位）',
  `day` tinyint UNSIGNED NOT NULL COMMENT '日（两位）',
  `hour` tinyint UNSIGNED NOT NULL COMMENT '时（两位）',
  `minute` tinyint UNSIGNED NOT NULL COMMENT '分（两位）',
  `second` tinyint UNSIGNED NOT NULL COMMENT '秒（两位）',
  `path` varchar(4096) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '原始视频路径',
  `speed` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '所要倍速的速度',
  `duration` decimal(13, 2) UNSIGNED NOT NULL COMMENT '原始视频时长（秒）',
  `oldSize` decimal(13, 0) UNSIGNED NOT NULL COMMENT '原始视频大小（B）',
  `newSize` decimal(13, 0) UNSIGNED NOT NULL COMMENT '新视频大小（B）',
  `oldFPS` decimal(4, 0) UNSIGNED NOT NULL COMMENT '原始视频帧率',
  `newFPS` decimal(4, 0) UNSIGNED NOT NULL COMMENT '新视频帧率',
  `oldWidth` decimal(6, 0) UNSIGNED NOT NULL COMMENT '原始视频宽度',
  `oldHeigh` decimal(6, 0) UNSIGNED NOT NULL COMMENT '原始视频长度',
  `newWidth` decimal(6, 0) UNSIGNED NOT NULL COMMENT '新视频宽度',
  `newHeigh` decimal(6, 0) UNSIGNED NOT NULL COMMENT '新视频长度'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of chang_video_speed
-- ----------------------------

-- ----------------------------
-- Table structure for clear_chang_video_speed
-- ----------------------------
DROP TABLE IF EXISTS `clear_chang_video_speed`;
CREATE TABLE `clear_chang_video_speed`  (
  `times` decimal(65, 0) NULL DEFAULT NULL,
  `items` decimal(65, 0) NULL DEFAULT NULL,
  `oldDuration` decimal(65, 0) NULL DEFAULT NULL,
  `newDuration` decimal(65, 0) NULL DEFAULT NULL,
  `oldSize` decimal(65, 0) NULL DEFAULT NULL,
  `newSize` decimal(65, 0) NULL DEFAULT NULL,
  `oldFPS` decimal(65, 0) NULL DEFAULT NULL,
  `newFPS` decimal(65, 0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of clear_chang_video_speed
-- ----------------------------
INSERT INTO `clear_chang_video_speed` VALUES (11, 894, 1632790, 1191600, 112113454870, 41646462154, 51804, 11564);

-- ----------------------------
-- Table structure for clear_del_str
-- ----------------------------
DROP TABLE IF EXISTS `clear_del_str`;
CREATE TABLE `clear_del_str`  (
  `times` decimal(65, 0) NULL DEFAULT NULL,
  `items` decimal(65, 0) NULL DEFAULT NULL,
  `oldCharacters` decimal(65, 0) NULL DEFAULT NULL,
  `newCharacters` decimal(65, 0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of clear_del_str
-- ----------------------------
INSERT INTO `clear_del_str` VALUES (26, 1965, 73173, 44588);

-- ----------------------------
-- Table structure for del_str
-- ----------------------------
DROP TABLE IF EXISTS `del_str`;
CREATE TABLE `del_str`  (
  `year` tinyint UNSIGNED NOT NULL COMMENT '年（两位）',
  `month` tinyint UNSIGNED NOT NULL COMMENT '月（两位）',
  `day` tinyint UNSIGNED NOT NULL COMMENT '日（两位）',
  `hour` tinyint UNSIGNED NOT NULL COMMENT '时（两位）',
  `minute` tinyint UNSIGNED NOT NULL COMMENT '分（两位）',
  `second` tinyint UNSIGNED NOT NULL COMMENT '秒（两位）',
  `fatherDir` varchar(10240) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '父目录',
  `oldName` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '原名',
  `newName` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '新名'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of del_str
-- ----------------------------

-- ----------------------------
-- Table structure for t
-- ----------------------------
DROP TABLE IF EXISTS `t`;
CREATE TABLE `t`  (
  `f` float(12, 11) NULL DEFAULT NULL,
  `d` double(17, 16) NULL DEFAULT NULL,
  `d65_0` decimal(65, 0) NULL DEFAULT NULL,
  `d65_30` decimal(65, 30) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
