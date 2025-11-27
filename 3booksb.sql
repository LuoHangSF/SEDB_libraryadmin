-- 新版数据库初始化脚本
-- 如果数据库已存在且你想重建，可先手动 DROP DATABASE bookdb;

CREATE DATABASE IF NOT EXISTS bookdb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE bookdb;

-- 书籍信息表（新版）
-- 字段说明：
-- book_id: 主键，字符串格式，如 D20250826x20
-- b_name: 书名
-- author: 作者
-- publish_name: 出版社
-- price: 价格，保留两位小数
-- publish_date: 出版日期
-- stock_in_date: 采购入库日期（入库当天日期）
CREATE TABLE book (
    book_id        VARCHAR(32)  NOT NULL PRIMARY KEY,
    b_name         VARCHAR(255) NOT NULL UNIQUE,
    author         VARCHAR(255) NOT NULL,
    publish_name   VARCHAR(255),
    price          DECIMAL(10,2) DEFAULT 0.00,
    publish_date   DATE,
    stock_in_date  DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 读者角色表（原样保留）
CREATE TABLE role (
    r_id       INT PRIMARY KEY,
    r_name     VARCHAR(255),
    max_number INT,
    max_day    INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO role (r_id, r_name, max_number, max_day) VALUES
(1, '教师',   15, 180),
(2, '研究生', 10, 180),
(3, '本科生', 5,  60),
(4, '其他',   5,  30);

-- 用户信息表（原样保留）
CREATE TABLE user (
    u_id         INT PRIMARY KEY AUTO_INCREMENT,
    u_name       VARCHAR(255),
    password     VARCHAR(255),
    sex          VARCHAR(255),
    balance      DECIMAL(10,2) DEFAULT 0.00,
    phone_number VARCHAR(255),
    r_id         INT,
    unit         VARCHAR(255),
    FOREIGN KEY (r_id) REFERENCES role(r_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 管理员表（原样保留）
CREATE TABLE administer (
    a_id     INT PRIMARY KEY AUTO_INCREMENT,
    a_name   VARCHAR(255),
    password VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 借阅表（b_id 改为 VARCHAR(32)，引用 book.book_id）
CREATE TABLE borrow (
    b_id VARCHAR(32) NOT NULL,
    u_id INT NOT NULL,
    FOREIGN KEY (b_id) REFERENCES book(book_id),
    FOREIGN KEY (u_id) REFERENCES user(u_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 示例书籍数据（仅示例：BookID 根据出版日期简单生成，你可按真实入库顺序重新定义）
-- 规则示例：D + 出版日期YYYYMMDD + x序号
-- stock_in_date 暂设为当前日期 CURDATE()，也可改成 publish_date 或具体入库日
INSERT INTO book (book_id, b_name, author, publish_name, price, publish_date, stock_in_date) VALUES
('D20080115x1', '三体',        '刘慈欣',     '重庆出版社',       59.62, '2008-01-15', CURDATE()),
('D20120801x2', '活着',        '余华',       '作家出版社',       22.78, '2012-08-01', CURDATE()),
('D20150701x3', 'C++ PRIMER PLUS', '史蒂芬·普拉达', '人民邮电出版社', 120.00, '2015-07-01', CURDATE()),
('D20211201x4', '人民日报',    '人民日报社', '人民日报社',       12.50, '2021-12-01', CURDATE()),
('D20100801x5', '资治通鉴',    '司马光',     '中华书局',         150.00, '2010-08-01', CURDATE()),
('D19980101x6', '红楼梦',      '曹雪芹',     '中华书局',         180.00, '1998-01-01', CURDATE());

-- 示例管理员
INSERT INTO administer (a_name, password) VALUES ('admin', 'admin');

-- 示例用户（角色 3：本科生）
INSERT INTO user (u_name, password, sex, balance, phone_number, r_id, unit) VALUES
('陈恒硕', 'sbchenhengshuo', '男', 0.00, '13604660566', 3, '吉林大学');

-- 后续如果需要示例借阅记录，可添加：
-- INSERT INTO borrow (b_id, u_id) VALUES ('D20080115x1', 1);