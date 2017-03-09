
-- Table for Papers
DROP TABLE IF EXISTS Paper;
CREATE TABLE IF NOT EXISTS Paper (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    bibtexKey VARCHAR(100) NOT NULL UNIQUE KEY,
    title VARCHAR(200) DEFAULT NULL,
    doi VARCHAR(200) DEFAULT NULL,
    bibtex longtext NOT NULL,
    preview longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Table for Authors
DROP TABLE IF EXISTS Author;
CREATE TABLE IF NOT EXISTS Author (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Table for paper author assignments
DROP TABLE IF EXISTS PaperAuthor;
CREATE TABLE IF NOT EXISTS PaperAuthor (
    paperId INT(11) NOT NULL,
    authorId INT(11) NOT NULL,
    PRIMARY KEY (paperId, authorId),
    KEY FK_Paper (paperId),
    KEY FK_Author (authorId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE PaperAuthor
    ADD CONSTRAINT FK_Author FOREIGN KEY (authorId) REFERENCES Author (id),
    ADD CONSTRAINT FK_Paper FOREIGN KEY (paperId) REFERENCES Paper (id);

INSERT INTO Paper (bibtexKey,title,doi,bibtex,preview) VALUES (N'Douglas+Adams1978', N'Hitchikers+Guide+to+the+Galaxy', N'', N'@BOOK{Douglas+Adams1978,  author = {Douglas+Adams},  title = {Hitchikers+Guide+to+the+Galaxy},  year = {1978}}', N'Douglas+Adams. <i>Hitchikers+Guide+to+the+Galaxy</i>. (1978).');
