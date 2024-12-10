-- For testing database:
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS bird_recipes;
DROP SEQUENCE IF EXISTS bird_recipes_id_seq;
DROP TABLE IF EXISTS bird_sightings;
DROP SEQUENCE IF EXISTS bird_sightings_id_seq;


-- users table
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    -- profile_picture VARCHAR(255) DEFAULT '>INSERT PATH HERE<'
    password VARCHAR(255) NOT NULL
);

-- bird_recipes table
CREATE SEQUENCE IF NOT EXISTS bird_recipes_id_seq;
CREATE TABLE bird_recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    ingredients TEXT NOT NULL,
    description TEXT NOT NULL,
    date_created DATE,
    recipe_rating int,
    cooking_time INT NOT NULL,
    user_id int, 
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bird_sightings_id_seq;
    CREATE TABLE bird_sightings (
    id SERIAL PRIMARY KEY,
    bird_name VARCHAR(255) NOT NULL,
    -- image VARCHAR(255) DEFAULT '>INSERT PATH HERE<',
    date_spotted DATE,
    location VARCHAR(255),
    user_id int,
    bird_sighting_id int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    constraint fk_bird_sighting foreign key(bird_sighting_id) references bird_sightings(id) on delete cascade,
);

-- Seed data for users:
INSERT INTO users (username, email, password) VALUES 
('bird_lover', 'birdlover@example.com', 'password123'),
('avian_fanatic', 'avianfanatic@example.com', 'password123'),
('nature_watch', 'naturewatch@example.com', 'password123'),
('feather_seeker', 'featherseeker@example.com', 'password123'),
('wildlife_watcher', 'wildlifewatcher@example.com', 'password123');

-- Seed data for bird_recipes:
INSERT INTO bird_recipes (title, ingredients, description, date_created, recipe_rating, cooking_time, user_id) VALUES 
('Blue Jay Roast', 
    'Blue Jay meat, rosemary, garlic, olive oil, salt, pepper', -- ingredients
    'Marinate Blue Jay meat in olive oil and spices, then roast at 375°F for 45 minutes.', -- recipe description
    '2024-12-01', -- date_created
    5, -- rating
    45, -- cooking_time
    1 -- user_id
), 
('Cardinal Casserole', 
    'Northern Cardinal meat, potatoes, cream, cheese, onions', -- ingredients
    'Layer potatoes, cream, and Cardinal meat in a casserole dish, bake for 60 minutes.', -- recipe description
    '2024-12-02', -- date_created
    4, -- rating
    60, -- cooking_time
    1 -- user_id
), 
('Robin Stew', 
    'American Robin meat, carrots, celery, potatoes, broth, thyme', -- ingredients
    'Simmer Robin meat with vegetables and broth for a hearty stew.', -- recipe description
    '2024-12-03', -- date_created
    5, -- rating
    90, -- cooking_time
    2 -- user_id
), 
('Mourning Dove Pie', 
    'Mourning Dove meat, pie crust, gravy, peas, carrots', -- ingredients
    'Fill a pie crust with Dove meat and vegetables, then bake until golden brown.', -- recipe description
    '2024-12-04', -- date_created
    3, -- rating
    50, -- cooking_time
    2 -- user_id
), 
('Chickadee Skewers', 
    'Black-capped Chickadee meat, bell peppers, onions, barbecue sauce', -- ingredients
    'Thread Chickadee meat and veggies onto skewers, grill with barbecue sauce.', -- recipe description
    '2024-12-05', -- date_created
    4, -- rating
    30, -- cooking_time
    3 -- user_id
), 
('Woodpecker Stir Fry', 
    'Downy Woodpecker meat, soy sauce, garlic, ginger, mixed vegetables', -- ingredients
    'Stir fry Woodpecker meat and veggies with soy sauce and spices.', -- recipe description
    '2024-12-06', -- date_created
    5, -- rating
    20, -- cooking_time
    3 -- user_id
), 
('Finch Fricassée', 
    'House Finch meat, butter, cream, white wine, mushrooms', -- ingredients
    'Cook Finch meat in a creamy wine sauce with mushrooms.', -- recipe description
    '2024-12-07', -- date_created
    4, -- rating
    35, -- cooking_time
    4 -- user_id
), 
('Starling Soup', 
    'European Starling meat, onions, garlic, tomatoes, basil', -- ingredients
    'Slow-cook Starling meat with tomatoes and spices for a rich soup.', -- recipe description
    '2024-12-08', -- date_created
    3, -- rating
    120, -- cooking_time
    4 -- user_id
), 
('Sparrow Curry', 
    'White-throated Sparrow meat, curry spices, coconut milk, rice', -- ingredients
    'Simmer Sparrow meat in a spiced coconut milk curry, serve with rice.', -- recipe description
    '2024-12-09', -- date_created
    4, -- rating
    40, -- cooking_time
    5 -- user_id
), 
('Goldfinch Tagine', 
    'American Goldfinch meat, apricots, almonds, honey, spices', -- ingredients
    'Cook Goldfinch meat in a tagine with dried fruits and honey.', -- recipe description
    '2024-12-10', -- date_created
    5, -- rating
    75, -- cooking_time
    5 -- user_id
);

-- Seed data for bird_sightings
INSERT INTO bird_sightings (bird_name, date_spotted, location, user_id) VALUES 
('Blue Jay', '2024-12-01', 'Central Park', 1),
('Northern Cardinal', '2024-12-02', 'Central Park', 1),
('American Robin', '2024-12-03', 'Brooklyn Botanic Garden', 2),
('Mourning Dove', '2024-12-04', 'Brooklyn Botanic Garden', 2),
('Black-capped Chickadee', '2024-12-05', 'Golden Gate Park', 3),
('Downy Woodpecker', '2024-12-06', 'Golden Gate Park', 3),
('House Finch', '2024-12-07', 'Griffith Park', 4),
('European Starling', '2024-12-08', 'Griffith Park', 4),
('White-throated Sparrow', '2024-12-09', 'Yellowstone Park', 5),
('American Goldfinch', '2024-12-10', 'Yellowstone Park', 5);

