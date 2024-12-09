import pytest #needs to be imported to allow for @pytest.mark.asyncho decorator
from models.users import User
from repositories.users_repo import UserRepository
from db.db_connection import AsyncDatabaseConnection #imported to allow async db connection 

"""
When we call get_all_users()
We get a list of User objects reflecting the seed data.
"""
#used to mark the test as an asynchronous function so that it can be properly run and awaited by pytest-asyncio
@pytest.mark.asyncio 
async def test_get_all_users(db_connection):
    #seed test database
    #use await as this takes time to set up db
    await db_connection.seed('db/seeds/birdfood_app.sql') 
    #Instantiate UserRepository object with connection to database   
    repository = UserRepository(db_connection) 
    #call get_all_users() method on repository object 
    #use await as this fucntion is a database query
    result = await repository.get_all_users()
    assert result == [
        User(1, 'bird_lover', 'birdlover@example.com', 'password123', 'uploads/default_photo.webp'),
        User(2, 'avian_fanatic', 'avianfanatic@example.com', 'password123', 'uploads/default_photo.webp'),
        User(3, 'nature_watch', 'naturewatch@example.com', 'password123', 'uploads/default_photo.webp'),
        User(4, 'feather_seeker', 'featherseeker@example.com', 'password123', 'uploads/default_photo.webp'),
        User(5, 'wildlife_watcher', 'wildlifewatcher@example.com', 'password123', 'uploads/default_photo.webp'),
    ]

"""
When we call get_single_user(<id>)
We get a single User object reflecting the seed data.
"""
@pytest.mark.asyncio
async def test_get_single_user(db_connection):
    await db_connection.seed('db/seeds/birdfood_app.sql') 
    repository = UserRepository(db_connection)   
    result = await repository.get_single_user(3)
    assert result == User(3, 'nature_watch', 'naturewatch@example.com', 'password123', 'uploads/default_photo.webp')

"""
When we call create_user
A new user is created and stored in the database
"""
@pytest.mark.asyncio
async def test_create_new_user(db_connection):
    await db_connection.seed('db/seeds/birdfood_app.sql')
    repository = UserRepository(db_connection)
    await repository.create_user(User(6, 'test_user', 'test_user@gmail.org', 'TestPassword123!', 'uploads/default_photo.webp'))
    result = await repository.get_all_users()
    assert result == [
        User(1, 'bird_lover', 'birdlover@example.com', 'password123', 'uploads/default_photo.webp'),
        User(2, 'avian_fanatic', 'avianfanatic@example.com', 'password123', 'uploads/default_photo.webp'),
        User(3, 'nature_watch', 'naturewatch@example.com', 'password123', 'uploads/default_photo.webp'),
        User(4, 'feather_seeker', 'featherseeker@example.com', 'password123', 'uploads/default_photo.webp'),
        User(5, 'wildlife_watcher', 'wildlifewatcher@example.com', 'password123', 'uploads/default_photo.webp'),
        User(6, 'test_user', 'test_user@gmail.org', 'TestPassword123!', 'uploads/default_photo.webp')
    ]

"""
When we call create_user without entering a username
An error message is returned and the user is NOT added to the database
"""
@pytest.mark.asyncio
async def test_create_new_user_with_username_error(db_connection):
    await db_connection.seed('db/seeds/birdfood_app.sql')    #seed test database
    repository = UserRepository(db_connection)      #Instantiate UserRepository object with connection to database
    response = await repository.create_user(User(6, '', 'test_user@gmail.org', 'TestPassword123!', 'uploads/default_photo.webp'))
    assert response == "Please provide a username"
    assert await repository.get_all_users() == [
        User(1, 'bird_lover', 'birdlover@example.com', 'password123', 'uploads/default_photo.webp'),
        User(2, 'avian_fanatic', 'avianfanatic@example.com', 'password123', 'uploads/default_photo.webp'),
        User(3, 'nature_watch', 'naturewatch@example.com', 'password123', 'uploads/default_photo.webp'),
        User(4, 'feather_seeker', 'featherseeker@example.com', 'password123', 'uploads/default_photo.webp'),
        User(5, 'wildlife_watcher', 'wildlifewatcher@example.com', 'password123', 'uploads/default_photo.webp'),
    ]

"""
When we call create_user without entering an email
An error message is returned and the user is NOT added to the database
"""
@pytest.mark.asyncio
async def test_create_new_user_with_email_error(db_connection):
    await db_connection.seed('db/seeds/birdfood_app.sql')    #seed test database
    repository = UserRepository(db_connection)      #Instantiate UserRepository object with connection to database
    response = await repository.create_user(User(6, 'test_user', '', 'TestPassword123!', 'uploads/default_photo.webp'))
    assert response == "Please provide an email address"
    assert await repository.get_all_users() == [
        User(1, 'bird_lover', 'birdlover@example.com', 'password123', 'uploads/default_photo.webp'),
        User(2, 'avian_fanatic', 'avianfanatic@example.com', 'password123', 'uploads/default_photo.webp'),
        User(3, 'nature_watch', 'naturewatch@example.com', 'password123', 'uploads/default_photo.webp'),
        User(4, 'feather_seeker', 'featherseeker@example.com', 'password123', 'uploads/default_photo.webp'),
        User(5, 'wildlife_watcher', 'wildlifewatcher@example.com', 'password123', 'uploads/default_photo.webp'),
    ]

"""
When we call create_user without entering a password
An error message is returned and the user is NOT added to the database
"""
@pytest.mark.asyncio
async def test_create_new_user_with_password_error(db_connection):
    await db_connection.seed('db/seeds/birdfood_app.sql')    #seed test database
    repository = UserRepository(db_connection)      #Instantiate UserRepository object with connection to database
    response = await repository.create_user(User(6, 'test_user', 'test@email.com', '', 'uploads/default_photo.webp'))
    assert response == "Please provide a password"
    assert await repository.get_all_users() == [
        User(1, 'bird_lover', 'birdlover@example.com', 'password123', 'uploads/default_photo.webp'),
        User(2, 'avian_fanatic', 'avianfanatic@example.com', 'password123', 'uploads/default_photo.webp'),
        User(3, 'nature_watch', 'naturewatch@example.com', 'password123', 'uploads/default_photo.webp'),
        User(4, 'feather_seeker', 'featherseeker@example.com', 'password123', 'uploads/default_photo.webp'),
        User(5, 'wildlife_watcher', 'wildlifewatcher@example.com', 'password123', 'uploads/default_photo.webp'),
    ]

"""
When we call update_user_password() 
The corresponding user password attribute is updated in the database
"""
@pytest.mark.asyncio
async def test_update_user_password(db_connection):
    await db_connection.seed('db/seeds/birdfood_app.sql')    #seed test database
    repository = UserRepository(db_connection)      #Instantiate UserRepository object with connection to database
    await repository.update_user_password(4, 'NewPassword!')
    assert await repository.get_single_user(4) == User(4, 'feather_seeker', 'featherseeker@example.com', 'NewPassword!', 'uploads/default_photo.webp')

"""
When we call update_user_email() 
The corresponding user email attribute is updated in the database
"""
@pytest.mark.asyncio
async def test_update_user_email(db_connection):
    await db_connection.seed('db/seeds/birdfood_app.sql')    #seed test database
    repository = UserRepository(db_connection)      #Instantiate UserRepository object with connection to database
    await repository.update_user_email(4, 'updated@email.co.uk')
    assert await repository.get_single_user(4) == User(4, 'feather_seeker', 'updated@email.co.uk', 'password123', 'uploads/default_photo.webp')

"""
When we call update_user_username() 
The corresponding user email attribute is updated in the database
"""
@pytest.mark.asyncio
async def test_update_user_username(db_connection):
    await db_connection.seed('db/seeds/birdfood_app.sql')    #seed test database
    repository = UserRepository(db_connection)      #Instantiate UserRepository object with connection to database
    await repository.update_user_username(4, 'new_username')
    assert await repository.get_single_user(4) == User(4, 'new_username', 'featherseeker@example.com', 'password123', 'uploads/default_photo.webp')


"""
When we call delete_user(<id>) 
The corresponding user is deleted from the database
"""
@pytest.mark.asyncio
async def test_delete_user(db_connection):
    await db_connection.seed('db/seeds/birdfood_app.sql')    #seed test database
    repository = UserRepository(db_connection)      #Instantiate UserRepository object with connection to database
    await repository.delete_user(4)
    assert await repository.get_all_users() == [
        User(1, 'bird_lover', 'birdlover@example.com', 'password123', 'uploads/default_photo.webp'),
        User(2, 'avian_fanatic', 'avianfanatic@example.com', 'password123', 'uploads/default_photo.webp'),
        User(3, 'nature_watch', 'naturewatch@example.com', 'password123', 'uploads/default_photo.webp'),
        User(5, 'wildlife_watcher', 'wildlifewatcher@example.com', 'password123', 'uploads/default_photo.webp'),
    ]
