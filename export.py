from rules import Rules
from statistics import Statistics


class Export(object):
    @staticmethod
    def save(statistics: Statistics, file_name):
        file = open(f"export/{file_name}.csv", "w")
        file.write(statistics.get_headline_str())
        for day in range(len(statistics.exposed)):
            file.write(statistics.get_single_day_str(day))
        file.close()
