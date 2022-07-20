
CREATE TABLE shows (
    name VARCHAR(255) default NULL,
    release_date YEAR(4) default NULL,
    id INT(8) UNSIGNED default NULL,
    PRIMARY KEY (name)
);