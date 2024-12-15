from lib.recipe_templates.recipe_templetes import HERB_GLAZED_RECIPE
from lib.models.ingredients import Ingredient
from lib.models.steps import Step
from lib.models.sightings import Sighting
from lib.models.recipes import Recipe
import datetime

class RecipeService:
    def __init__(self, sightings_repo, recipes_repo, ingredients_repo, steps_repo, connection):
        self.sightings_repo = sightings_repo
        self.recipes_repo = recipes_repo
        self.ingredients_repo = ingredients_repo
        self.steps_repo = steps_repo
        self._connection = connection

    # heloer function to populate the template with given birdname --> move to utils folder later
    def _populate_bird_template(self, template, bird_name):
        populated = {
            "title": template["title"].replace("{BIRD}", bird_name),
            "cooking_time": template["cooking_time"],
            "ingredients": [],
            "steps": []
        }

        for ing in template["ingredients"]:
            populated["ingredients"].append({
                "ingredient_name": ing["ingredient_name"].replace("{BIRD}", bird_name)
            })

        for st in template["steps"]:
            populated["steps"].append({
                "step_order": st["step_order"],
                "step_description": st["step_description"].replace("{BIRD}", bird_name)
            })

        return populated
    
    async def create_recipe_from_bird_name(self, bird_name, user_id):
        try:
            # 1. Create a bird sighting
            new_sighting = Sighting(
                None, #id --> generated by database upon creation
                bird_name,
                None, # date_spotted --> auto set in repo
                None, # location --> defaults to "Unknown" in database
                user_id
            )
            # 2. Add sighting to database
            sighting_id = await self.sightings_repo.create_bird_sighting(new_sighting)
            if not sighting_id:
                raise Exception("Failed to create bird sighting.")
            
            # 3. Populate the template with the given bird name
            recipe_data = self._populate_bird_template(HERB_GLAZED_RECIPE, bird_name)

            # 3. Create the recipe in bird_recipes
            new_recipe = Recipe(
                None, #id
                recipe_data["title"], #recipe title
                None, # date_created --> auto set in repo
                None, # recipe_rating --> Default to 0 in the database
                recipe_data["cooking_time"], #cooking_time
                sighting_id # bird_sighting_id
            )
            recipe_id = await self.recipes_repo.create_recipe(new_recipe)
            if not recipe_id:
                raise Exception("Failed to create recipe.")
            
            # 5. Insert ingredients
            for ing in recipe_data["ingredients"]:
                ingredient = Ingredient(
                    None, #id
                    recipe_id,
                    ing["ingredient_name"] # ingredient_name
                )
                await self.ingredients_repo.create_new_ingredient(ingredient)

            # 6. Insert steps
            for stp in recipe_data["steps"]:
                step = Step(
                    None,
                    recipe_id,
                    stp["step_order"],
                    stp["step_description"]
                )
                await self.steps_repo.create_new_step(step)

            # Return the recipe_id 
            return recipe_id
        
        # hanDLE creation errors
        except Exception as e:
            print(f"Error creating recipe: {e}")
            return None