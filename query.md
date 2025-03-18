# SQL query문

/*
*********************************************************************
편의점 상품 데이터베이스
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;
/*!40101 SET SQL_MODE=''*/;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `store` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `store`;

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `itemcode` VARCHAR(20) NOT NULL PRIMARY KEY,  -- 상품 코드
  `name` VARCHAR(100) NOT NULL,  -- 상품명
  `price` DECIMAL(10,2) NOT NULL,  -- 가격
  `quantity` INT NOT NULL DEFAULT 0,  -- 재고 수량
  `date` DATETIME DEFAULT CURRENT_TIMESTAMP  -- 상품 입고 날짜
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `products` */

INSERT INTO `products` (`itemcode`, `name`, `price`, `quantity`, `date`) VALUES
('P001', '콜라', 1500.00, 50, NOW()),
('P002', '사이다', 1500.00, 40, NOW()),
('P003', '삼각김밥 참치마요', 1200.00, 30, NOW()),
('P004', '삼각김밥 불고기', 1200.00, 35, NOW()),
('P005', '컵라면 신라면', 1800.00, 25, NOW()),
('P006', '컵라면 진라면', 1700.00, 20, NOW()),
('P007', '초코바', 2000.00, 15, NOW()),
('P008', '감자칩', 2500.00, 10, NOW()),
('P009', '생수 500ml', 1000.00, 100, NOW()),
('P010', '생수 2L', 2000.00, 80, NOW()),
('P011', '우유 1L', 2500.00, 50, NOW()),
('P012', '두유', 1800.00, 60, NOW()),
('P013', '햄버거', 3500.00, 20, NOW()),
('P014', '샌드위치', 3000.00, 25, NOW()),
('P015', '도시락', 5000.00, 15, NOW()),
('P016', '치킨', 8000.00, 10, NOW()),
('P017', '핫도그', 2800.00, 30, NOW()),
('P018', '아이스크림', 2000.00, 40, NOW()),
('P019', '커피 캔', 1500.00, 35, NOW()),
('P020', '에너지드링크', 2500.00, 20, NOW());

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
