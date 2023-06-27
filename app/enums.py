from enum import Enum

class SortingOptions(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    RATING = "rating"

class Rating(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"