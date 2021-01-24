### Design Underground System
**Two Hashmap**
- [Concepts](images/)
- [Source code](source/Hashmap.py)
```python
class Journey:
    def __init__(self):
        self.duration = 0 
        self.travels = 0 
class UndergroundSystem:

    def __init__(self):
        # set up a hashmap[id] = (station, time)
        # set up a hashmap[(src, dest)] = (duration, trips)
        pass

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # store the station and the time of the traveling passenger
        pass

    def checkOut(self, id: int, stationName: str, t: int) -> None:        
        # get the beginning station and the time of the passenger  
        # accumulate the duration of travel between src and dest
        # cound the number of passengers traveling between src dest
        pass
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # get the accumulated duration and the number of trips from the src, dest
        # compute and return the average 
        pass
```