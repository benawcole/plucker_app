from lib.models.sightings import Sighting
import datetime

class SightingRepository():
    def __init__(self, connection):
        self._connection = connection

    # get all sightings
    async def get_all_sightings(self):
        rows = await self._connection.execute('SELECT * FROM bird_sightings ORDER BY id')
        sightings = []
        for row in rows:
            sighting = Sighting(row["id"], row["bird_name"], row["date_spotted"], row["location"], row["user_id"])
            sightings.append(sighting)
        return sightings

    # get single sighting by id
    async def get_sighting_by_id(self, id):
        sightings = await self._connection.execute(
            'SELECT * FROM bird_sightings WHERE id = $1', [id]
            )
        if not sightings:
            return None
        else:
            sighting = sightings[0]
            return Sighting(sighting["id"], sighting["bird_name"], sighting["date_spotted"], sighting["location"], sighting["user_id"]  )

    # get all sightings by location
    async def get_sightings_by_location(self, location):
        rows = await self._connection.execute(
            'SELECT * FROM bird_sightings WHERE location = $1', [location]
        )
        sightings = []
        if not rows:
            return None
        else: 
            for row in rows:
                sighting = Sighting(row["id"], row["bird_name"], row["date_spotted"], row["location"], row["user_id"])
                sightings.append(sighting)
            return sightings
            
    # get all sightings by date_spotted
    async def get_sightings_by_date_spotted(self, date_spotted):
        rows = await self._connection.execute(
            'SELECT * FROM bird_sightings WHERE date_spotted = $1', [date_spotted]
        )
        sightings = []
        if not rows:
            return None
        else:
            for row in rows:
                sighting = Sighting(row["id"], row["bird_name"], row["date_spotted"], row["location"], row["user_id"])
                sightings.append(sighting)
            return sightings

    # get all sightings by bird_name
    async def get_sightings_by_bird_name(self, bird_name):
        rows = await self._connection.execute(
            'SELECT * FROM bird_sightings WHERE bird_name = $1', [bird_name]
        )
        sightings = []
        if not rows:
            return None
        else:
            for row in rows:
                sighting = Sighting(row["id"], row["bird_name"], row["date_spotted"], row["location"], row["user_id"])
                sightings.append(sighting)
            return sightings


    # get all sightings by user_id
    async def get_sightings_by_user_id(self, user_id):
        rows = await self._connection.execute(
            'SELECT * FROM bird_sightings WHERE user_id = $1', [user_id]
        )
        sightings = []
        if not rows:
            return None
        else:
            for row in rows:
                sighting = Sighting(row["id"], row["bird_name"], row["date_spotted"], row["location"], row["user_id"])
                sightings.append(sighting)
            return sightings if len(sightings) > 1 else sightings[0]

    # create bird_sighting
    async def create_bird_sighting(self, sighting):
        date_spotted = datetime.datetime.now().date().strftime('%Y-%m-%d')

        sighting_id = await self._connection.execute(
            '''
            INSERT INTO bird_sightings (bird_name, date_spotted, location, user_id)
            VALUES ($1, $2, $3, $4)
            RETURNING id
            ''',
            [sighting.bird_name, date_spotted, sighting.location, sighting.user_id])
        
        return sighting_id

    # delete bird sighting
    async def delete_bird_sighting(self, id):
        await self._connection.execute(
            'DELETE FROM bird_sightings WHERE id = $1', [id]
        )
        return None
    
    #update bird sighting by id and name
    async def update_sighting_bird(self, id, bird_name):
        await self.db_connection.execute(
            'UPDATE bird_sightings SET bird_name = $1 WHERE id = $2', 
            [bird_name, id])
        return None