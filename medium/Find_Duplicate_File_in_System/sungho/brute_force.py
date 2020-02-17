class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        tracker = {}

        for path in paths:
            element = path.split()
            directory = element[0]

            filenames = []
            for tmp in element[1:]:
                temp = tmp.split("(")[1]
                filename = tmp.split("(")[0]
                content = temp.split(")")[0]
                filenames.append(directory + filename)

                if content not in tracker:
                    tracker[content] = []
                    tracker[content].append(directory + '/' + filename)
                else:
                    tracker[content].append(directory + '/' + filename)

        rtnArray = []

        for key in tracker:
            if len(tracker[key]) > 1:
                rtnArray.append(tracker[key])

        return rtnArray