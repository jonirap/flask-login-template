class WorldGrid(object):
    """
    This class represent a world grid.
    You can add and get people to the grid and see people in specific areas.
    """

    DEGREES = 360
    KM_PER_DEGREE = 111
    MINUS_MINUS = 0
    MINUS_PLUS = 90
    PLUS_MINUS = 180
    PLUS_PLUS = 270
    RANGES = [(-1, -1), (0, -1), (-1, 0), (0, 0), (0, 1), (1, 0), (1, 1)]

    def __init__(self, resolution=10):
        """
        Ctor. Can add a list of people to the grid or create an empty world.

        :param people: list of people
        :type people: list
        """
        self.cubes = self.KM_PER_DEGREE / resolution
        self.world = self._create_world()
        self.people_locations = {}

    def _create_world(self):
        """
        This function creates an empty world with the given resolution.

        :return: an empty list of lists
        """
        return [[[] for j in xrange(self.DEGREES * self.cubes)]
                for i in xrange(self.DEGREES * self.cubes)]

    def add_person(self, person):
        """
        This function converts a persons location to numbers and adds him to the relevant place in the world.

        :param person: the person (dict with id, longitude and latitude and whatever else you want)
        """
        if person['id'] in self.people_locations:
            self.remove_person(person)
        longitude, latitude = self._degrees_to_numbers(person['longitude'], person['latitude'])
        i, j = int(round(longitude * self.cubes)), int(round(latitude * self.cubes))
        self.world[i][j].append(person)
        self.people_locations[person['id']] = (i, j)

    def remove_person(self, person):
        """
        This function checks if we already added that person before and removes previous
        tries.
        """
        i, j = self.people_locations[person['id']]
        for resident in self.world[i][j]:
            if resident['id'] == person['id']:
                self.world[i][j].remove(resident)
                break
        del self.people_locations[person['id']]

    def add_people(self, people):
        for person in people:
            self.add_person(person)

    def get_nearby_people(self, person):
        longitude, latitude = self._degrees_to_numbers(person['long'], person['lat'])
        i, j = int(round(longitude * self.cubes)), int(round(latitude * self.cubes))
        return [person for add_i, add_j in self.RANGES for person in self.world[i + add_i][j + add_j]]

    def _degrees_to_numbers(self, longitude, latitude):
        """
        converts degrees to 360 number range

        :type longitude: float
        :type latitude: float
        :return: the converted location
        """
        if longitude > 0 and latitude > 0:
            return longitude + self.PLUS_MINUS, latitude + self.PLUS_PLUS
        elif longitude > 0 and latitude < 0:
            return longitude + self.PLUS_MINUS, latitude + self.PLUS_MINUS
        elif longitude < 0 and latitude > 0:
            return longitude + self.MINUS_PLUS, latitude + self.MINUS_PLUS
        return longitude + self.MINUS_MINUS, latitude + self.MINUS_MINUS
