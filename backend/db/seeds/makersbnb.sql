DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password text
);

-- id | name | description | price_per_night | availability  | user_id

CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price int,
    user_id int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
    CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    listing_id int,
    user_id int,
    check_in text,
    check_out text,   
    status VARCHAR(50) DEFAULT 'pending',
    constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    constraint fk_listing foreign key(listing_id) references listings(id) on delete cascade
);


INSERT INTO users (username, email, password) VALUES ('Harman1', 'h@email.com', 'password123');
INSERT INTO users (username, email, password) VALUES ('Naomi2', 'n@mail.co.uk', 'password123');
INSERT INTO users (username, email, password) VALUES ('Doug3', 'doug@email.com', 'password123');
INSERT INTO users (username, email, password) VALUES ('aaron4', 'aaron@mail.co.uk', 'password123');

INSERT INTO listings(name, description, price, user_id) VALUES ('Alpine Retreat Lodge', 'A cozy, rustic lodge in the mountains featuring three bedrooms, a fireplace, and a hot tub with scenic woodland views.', 220, 4);
INSERT INTO listings(name, description, price, user_id) VALUES ('City Chic Loft', 'A sleek, modern loft in the heart of the city with an open floor plan and panoramic views, ideal for urban adventurers.', 200, 2);
INSERT INTO listings(name, description, price, user_id) VALUES ('Seaside Serenity', 'A peaceful coastal retreat with stunning ocean views, a private balcony, and luxurious modern amenities.', 100, 1);

INSERT INTO bookings (listing_id, user_id, check_in, check_out, status) VALUES (1, 2, '2024-11-30', '2024-12-01', 'pending');
INSERT INTO bookings (listing_id, user_id, check_in, check_out, status) VALUES (1, 3, '2024-12-03', '2024-12-04', 'pending');
INSERT INTO bookings (listing_id, user_id, check_in, check_out, status) VALUES (2, 3, '2024-12-06', '2024-12-07', 'pending');
INSERT INTO bookings (listing_id, user_id, check_in, check_out, status) VALUES (2, 4, '2024-12-07', '2024-12-08', 'pending');
INSERT INTO bookings (listing_id, user_id, check_in, check_out, status) VALUES (3, 4, '2024-12-12', '2024-12-13', 'pending');
INSERT INTO bookings (listing_id, user_id, check_in, check_out, status) VALUES (3, 2, '2024-12-24', '2024-12-25', 'pending');