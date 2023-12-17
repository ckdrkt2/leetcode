from sortedcontainers import SortedSet
from collections import defaultdict
from typing import List
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = {}
        self.cuisines = {}
        self.foods = defaultdict(SortedSet)

        for i in range(len(foods)):
            self.ratings[foods[i]] = ratings[i]
            self.cuisines[foods[i]] = cuisines[i]
            self.foods[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.cuisines[food]
        self.foods[cuisine].remove((-self.ratings[food], food))
        self.ratings[food] = newRating
        self.foods[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.foods[cuisine][0][1]
