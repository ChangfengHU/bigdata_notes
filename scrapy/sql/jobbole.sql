/*
Navicat MySQL Data Transfer

Source Server         : 本地
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : jianshu

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-01-19 15:04:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jobbole
-- ----------------------------
DROP TABLE IF EXISTS `jobbole`;
CREATE TABLE `jobbole` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creat_data` datetime DEFAULT NULL,
  `title` varchar(255) NOT NULL COMMENT '文章标题',
  `url` varchar(255) DEFAULT NULL COMMENT '文章路径',
  `url_object_id` varchar(255) DEFAULT NULL COMMENT '文章加密路径',
  `front_image_url` varchar(255) DEFAULT NULL COMMENT '文章封片图片地址',
  `front_image_path` varchar(255) DEFAULT NULL,
  `comment_nums` int(20) DEFAULT NULL COMMENT '评论数',
  `fav_nums` int(20) DEFAULT NULL COMMENT '收藏数',
  `praise_nums` int(20) DEFAULT NULL COMMENT '点赞数',
  `tags` varchar(255) DEFAULT NULL COMMENT '标签类别',
  `comment` longtext COMMENT '文章内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
