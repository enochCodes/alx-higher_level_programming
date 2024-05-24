-- File: 100-move_to_utf8.sql
-- Description: This script converts the hbtn_0c_0 database, the first_table table, and the name field in first_table to UTF8 (utf8mb4) with collation utf8mb4_unicode_ci.

-- Convert the database hbtn_0c_0 to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the first_table table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in first_table to UTF8
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

