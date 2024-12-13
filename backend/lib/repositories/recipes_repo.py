from lib.models.recipes import Recipe

class RecipeRepository():
        
        def __init__(self, connection): #require database connection when UserRepository object is created
            self._connection = connection

        async def get_all_recipes(self):
            rows = await self._connection.execute('SELECT * FROM bird_recipes ORDER BY id')
            recipes = []
            for row in rows:
                recipe = Recipe(row["id"], row["title"], row["ingredients"], row["description"], row["date_created"], row["recipe_rating"], row["cooking_time"], row["user_id"])
                recipes.append(recipe)
            return recipes
        
        async def get_single_recipe(self, id):
            rows = await self._connection.execute(
                'SELECT * FROM bird_recipes WHERE id = $1', [id])
            if not rows:
                return None  # Return None if no recipe is found
            row = rows[0]
            return Recipe(row["id"], row["title"], row["ingredients"], row["description"], row["date_created"], row["recipe_rating"], row["cooking_time"], row["user_id"])
        
        async def create_recipe(self, recipe):
        # This validation might be handles in the schema files later (not sure yet)
            if not recipe.title:
                return 'Please provide a title'
            if not recipe.ingredients:
                return 'Please provide a list of ingredients'
            if not recipe.description:
                return 'Please provide a recipe description'
            if not recipe.date_created:
                return 'Please provide a date created'
            if not recipe.recipe_rating:
                return 'Please provide a recipe rating'
            if not recipe.cooking_time:
                return 'Please provide a cooking time'
            if not recipe.user_id:
                return 'Please provide a user id'
            await self._connection.execute(
                'INSERT INTO bird_recipes (title, ingredients, description, date_created, recipe_rating, cooking_time, user_id) VALUES ($1, $2, $3, $4, $5, $6, $7)',
                [recipe.title, recipe.ingredients, recipe.description, recipe.date_created, recipe.recipe_rating, recipe.cooking_time, recipe.user_id])
            return None
        
        async def update_recipe_title(self, id, title):
            await self._connection.execute(
                'UPDATE bird_recipes SET title = $1 WHERE id = $2', 
                [title, id])
            return None
        
        async def update_recipe_ingredients(self, id, ingredients):
            await self._connection.execute(
                'UPDATE bird_recipes SET ingredients = $1 WHERE id = $2', 
                [ingredients, id])
            return None
        
        async def update_recipe_description(self, id, description):
            await self._connection.execute(
                'UPDATE bird_recipes SET description = $1 WHERE id = $2', 
                [description, id])
            return None
        
        async def update_recipe_date_created(self, id, date_created):
            await self._connection.execute(
                'UPDATE bird_recipes SET date_created = $1 WHERE id = $2', 
                [date_created, id])
            return None
        
        async def update_recipe_recipe_rating(self, id, recipe_rating):
            await self._connection.execute(
                'UPDATE bird_recipes SET recipe_rating = $1 WHERE id = $2', 
                [recipe_rating, id])
            return None
        
        async def update_recipe_cooking_time(self, id, cooking_time):
            await self._connection.execute(
                'UPDATE bird_recipes SET cooking_time = $1 WHERE id = $2', 
                [cooking_time, id])
            return None
        
        async def delete_recipe(self, id):
            await self._connection.execute(
                'DELETE FROM bird_recipes WHERE id = $1', [id])
            return None