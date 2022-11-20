CREATE TABLE category(
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description CHARACTER(60),
    picture TEXT,
    PRIMARY KEY(id) 
);

CREATE TABLE product(
    id SERIAL,
    name CHARACTER(60) NOT NULL,
    discontinued BOOLEAN NOT NULL,
    category_id INT,
    PRIMARY KEY (id)
);

ALTER TABLE  product
ADD CONSTRAINT fk_product_category
FOREIGN KEY (category_id)
REFERENCES category;