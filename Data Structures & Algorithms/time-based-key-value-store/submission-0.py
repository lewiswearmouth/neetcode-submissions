class TimeMap:

 

    def __init__(self):

        self.dictionary= {} # key=str, value=[list of [value, timestamp]]

 

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.dictionary:

            self.dictionary[key] = []

        self.dictionary[key].append([value, timestamp])

 

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        values = self.dictionary.get(key, [])

       

        left, right = 0, len(values)-1

 

        while left<=right:

            mid = (left+right)//2

 

            if(values[mid][1] == timestamp):

                return values[mid][0]

            elif(values[mid][1] < timestamp):

                res = values[mid][0]

                left = mid + 1

            else:

                right = mid - 1

 

        return res