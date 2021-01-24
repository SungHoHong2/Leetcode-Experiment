class Journey:
    def __init__(self):
        self.duration = 0
        self.travels = 0


class UndergroundSystem:

    def __init__(self):
        # set up a hashmap[id] = (station, time)
        self.check_in_data = dict()
        # set up a hashmap[(src, dest)] = (duration, trips)
        self.journey_data = collections.defaultdict(Journey)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # store the station and the time of the traveling passenger
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # get the beginning station and the time of the passenger
        src, time = self.check_in_data.pop(id)
        dest = stationName
        # accumulate the duration of travel between src and dest
        self.journey_data[(src, dest)].duration += (t - time)
        # cound the number of passengers traveling between src dest
        self.journey_data[(src, dest)].travels += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # get the accumulated duration and the number of trips from the src, dest
        journey = self.journey_data[(startStation, endStation)]
        # compute and return the average
        return journey.duration / journey.travels