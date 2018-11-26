/*
 Navicat Premium Data Transfer

 Source Server         : bilibili
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : article_spider

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 26/11/2018 09:18:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zhihu_question
-- ----------------------------
DROP TABLE IF EXISTS `zhihu_question`;
CREATE TABLE `zhihu_question`  (
  `zhihu_id` int(11) NOT NULL,
  `topics` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_time` datetime(0) DEFAULT NULL,
  `update_time` datetime(0) DEFAULT NULL,
  `answer_num` int(11) NOT NULL DEFAULT 0,
  `comments_num` int(11) NOT NULL DEFAULT 0,
  `watch_user_num` int(11) NOT NULL DEFAULT 0,
  `click_num` int(11) NOT NULL DEFAULT 0,
  `crawl_time` datetime(0) NOT NULL,
  `crawl_update_time` datetime(0) DEFAULT NULL,
  PRIMARY KEY (`zhihu_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
