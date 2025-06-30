from Models.sightseeing import Sightseeing

class SightseeingPage:
    def __init__(self, sightseeings: list[Sightseeing], previous_page:str="", next_page:str="") -> None:
        self.sightseeings = sightseeings
        self.previous_page = previous_page
        self.next_page = next_page