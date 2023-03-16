PRAGMA foreign_keys = ON;

INSERT INTO USERS(username, password, profilepath)
VALUES ('lyuyong', 'lyuyong', '/static/images/profile.png');

INSERT INTO USERS(username, password, profilepath)
VALUES ('chengdai', 'chengdai', '/static/images/profile.png');

INSERT INTO RESUME(owner, filename, created)
VALUES ('lyuyong', 'pdf_1.jpg', CURRENT_TIMESTAMP);

INSERT INTO RESUME(owner, filename, created)
VALUES ('lyuyong', 'pdf_2.jpg', CURRENT_TIMESTAMP);

INSERT INTO RESUME(owner, filename, created)
VALUES ('lyuyong', 'pdf_3.jpg', CURRENT_TIMESTAMP);

INSERT INTO RESUME(owner, filename, created)
VALUES ('lyuyong', 'pdf_4.jpg', CURRENT_TIMESTAMP);

INSERT INTO RESUME(owner, filename, created)
VALUES ('chengdai', 'pdf_5.jpg', CURRENT_TIMESTAMP);

INSERT INTO RESUME(owner, filename, created)
VALUES ('chengdai', 'pdf_6.jpg', CURRENT_TIMESTAMP);