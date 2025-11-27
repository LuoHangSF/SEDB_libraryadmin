-- DROP DATABASE bookdb;

CREATE DATABASE IF NOT EXISTS bookdb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE bookdb;

-- 书籍信息表（价格字段保留 DECIMAL(10,2)，支持 9999.99）
CREATE TABLE book (
    book_id        VARCHAR(32)  NOT NULL PRIMARY KEY,
    b_name         VARCHAR(255) NOT NULL UNIQUE,
    author         VARCHAR(255) NOT NULL,
    publish_name   VARCHAR(255),
    price          DECIMAL(10,2) DEFAULT 0.00,
    publish_date   DATE,
    stock_in_date  DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 读者角色表（保持不变）
CREATE TABLE role (
    r_id       INT PRIMARY KEY,
    r_name     VARCHAR(255) NOT NULL UNIQUE,
    max_number INT,
    max_day    INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO role (r_id, r_name, max_number, max_day) VALUES
(1, '教师',   15, 180),
(2, '研究生', 10, 180),
(3, '本科生', 5,  60),
(4, '其他',   5,  30);

-- 管理员表（保持不变）
CREATE TABLE administer (
    a_id     INT PRIMARY KEY AUTO_INCREMENT,
    a_name   VARCHAR(255),
    password VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 新版读者表 (手机号为主键)
-- category 外键引用 role.r_name；face_id 预留
CREATE TABLE user (
    phone_number VARCHAR(32)  NOT NULL PRIMARY KEY,
    u_name       VARCHAR(255) NOT NULL,
    email        VARCHAR(255),
    category     VARCHAR(255) NOT NULL,
    password     VARCHAR(255) NOT NULL,
    face_id      VARCHAR(255) DEFAULT NULL,
    balance      DECIMAL(10,2) DEFAULT 0.00,
    sex          VARCHAR(50),
    unit         VARCHAR(255),
    FOREIGN KEY (category) REFERENCES role(r_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 借阅表：引用手机号
CREATE TABLE borrow (
    b_id         VARCHAR(32) NOT NULL,
    phone_number VARCHAR(32) NOT NULL,
    FOREIGN KEY (b_id) REFERENCES book(book_id),
    FOREIGN KEY (phone_number) REFERENCES user(phone_number)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 初始管理员账号
INSERT INTO administer (a_name, password) VALUES ('admin', 'admin');

-- 示例读者（密码随意，face_id 留空，类别选本科生）
INSERT INTO user (phone_number, u_name, email, category, password, face_id, balance, sex, unit)
VALUES ('13800000000', '示例用户', 'example@example.com', '本科生', 'admin', NULL, 0.00, '未知', '示例单位');

-- 可选示例书籍（如需添加）
INSERT INTO book (book_id, b_name, author, publish_name, price, publish_date, stock_in_date) VALUES
('D20080115x1', '三体',        '刘慈欣',     '重庆出版社',       59.62, '2008-01-15', CURDATE()),
('D20120801x2', '活着',        '余华',       '作家出版社',       22.78, '2012-08-01', CURDATE()),
('D20150701x3', 'C++ PRIMER PLUS', '史蒂芬·普拉达', '人民邮电出版社', 120.00, '2015-07-01', CURDATE()),
('D20211201x4', '人民日报',    '人民日报社', '人民日报社',       12.50, '2021-12-01', CURDATE()),
('D20100801x5', '资治通鉴',    '司马光',     '中华书局',         150.00, '2010-08-01', CURDATE()),
('D19980101x6', '红楼梦',      '曹雪芹',     '中华书局',         180.00, '1998-01-01', CURDATE());
-- 结束