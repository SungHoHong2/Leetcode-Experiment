class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # set up the map that uses the content as the key and the list of filenames as the value
        tracker = collections.defaultdict(list)
        # iterate the paths from the input
        for path in paths:
            # split the paths into (directory, filenames)
            element = path.split()
            # place the directory
            directory = element[0]
            # iterate the filenames
            for tmp in element[1:]:
                temp = tmp.split("(")[1]
                # get the filename
                filename = tmp.split("(")[0]
                # get the content
                content = temp.split(")")[0]
                # store the content as the key and value as the list
                tracker[content].append(directory+'/'+filename)
        # return files that contain duplicates or return an empty array if no duplicates exists
        return [ v for v in tracker.values() if len(v) > 1]