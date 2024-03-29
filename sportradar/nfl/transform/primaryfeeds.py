class PrimaryFeedsTransformer:
    """
    Class to transform player feeds data.

    Attributes:
        UNWANTED_KEYS(list): List of unwanted keys to be removed from the data dictonary.

    Args:
        data (dict): The game feeds data dictionary.

    Methods:
        transform_current_season_schedule: Transform the current schedule data
        ransform_current_week_schedule : Transform the current week schedule data
    """

    UNWANTED_KEYS = ["_comment"]

    def __init__(self, data: dict):
        self.data = data
        self.remove_unwanted_feeds()

    def remove_unwanted_feeds(self):
        for key in self.UNWANTED_KEYS:
            if key in self.data:
                self.data.pop(key)

    def transform_current_season_schedule(self):
        return self.data

    def transform_current_week_schedule(self):
        return self.data

    def transform_seasons_schedule(self):
        return self.data

    def transform_weekly_schedule(self):
        return self.data
