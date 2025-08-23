from models.sightseeing import Sightseeing


class SightseeingService:
    __fake_sightseeings = [  # pseudo database
        Sightseeing("Statue of Liberty", "New York, NY"),  # id 1
        Sightseeing("Golden Gate Bridge", "San Francisco, CA"),  # id 2, etc.
        Sightseeing("Mount Rushmore", "Keystone, SD"),
        Sightseeing("Grand Canyon", "Arizona"),
        Sightseeing("Niagara Falls", "New York"),
        Sightseeing("White House", "Washington, DC"),
        Sightseeing("Disneyland", "Anaheim, CA"),
        Sightseeing("Empire State Building", "New York, NY"),
        Sightseeing("Times Square", "New York, NY"),
        Sightseeing("Yosemite National Park", "California"),
        Sightseeing("Las Vegas Strip", "Las Vegas, NV"),
    ]

    def get_sightseeings(self, skip: int, take: int) -> list[Sightseeing]:
        if skip < 0:
            raise ValueError("Skip cannot be negative")

        if take <= 0:
            raise ValueError("Take must be greater than zero")

        if skip >= len(self.__fake_sightseeings):
            return []

        if skip + take >= len(self.__fake_sightseeings):
            return self.__fake_sightseeings[skip:]
        else:
            return self.__fake_sightseeings[skip : skip + take]

    def get_sightseeing_by_id(self, id: int) -> Sightseeing:
        if id <= 0 or id > len(self.__fake_sightseeings):
            raise IndexError("Sightseeing ID out of range")

        return self.__fake_sightseeings[id - 1]

    def add_sightseeing(self, sightseeing: Sightseeing) -> int:
        id = len(self.__fake_sightseeings) + 1
        self.__fake_sightseeings.append(sightseeing)
        return id

    def try_update_sightseeing(self, id: int, sightseeing: Sightseeing) -> bool:
        if id <= 0 or id > len(self.__fake_sightseeings):
            return False

        self.__fake_sightseeings[id - 1] = sightseeing
        return True

    def try_delete_sightseeing(self, id: int) -> bool:
        if id <= 0 or id > len(self.__fake_sightseeings):
            return False

        del self.__fake_sightseeings[id - 1]
        return True
