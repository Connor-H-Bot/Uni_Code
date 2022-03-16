CREATE TABLE GameTitle
(
  title INT NOT NULL,
  price INT NOT NULL,
  platform INT NOT NULL,
  release_year INT NOT NULL,
  PRIMARY KEY (title),
  PRIMARY KEY (platform),
  PRIMARY KEY (release_year)
);

CREATE TABLE GameLicense
(
  title INT NOT NULL,
  release_year INT NOT NULL,
  platform INT NOT NULL,
  license_id INT NOT NULL,
  PRIMARY KEY (license_id),
  FOREIGN KEY (title) REFERENCES GameTitle(title),
  FOREIGN KEY (release_year) REFERENCES GameTitle(release_year),
  FOREIGN KEY (platform) REFERENCES GameTitle(platform)
);

CREATE TABLE Gamer
(
  email INT NOT NULL,
  gamer_id INT NOT NULL,
  first_name INT NOT NULL,
  last_name INT NOT NULL,
  PRIMARY KEY (gamer_id),
  UNIQUE (email)
);

CREATE TABLE gameRental
(
  gamer_id INT NOT NULL,
  license_id INT NOT NULL,
  date_out INT NOT NULL,
  date_back INT NOT NULL,
  gamer_id INT NOT NULL,
  license_id INT NOT NULL,
  PRIMARY KEY (gamer_id),
  FOREIGN KEY (gamer_id) REFERENCES Gamer(gamer_id),
  FOREIGN KEY (license_id) REFERENCES GameLicense(license_id),
  UNIQUE (license_id)
);