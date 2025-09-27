class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #Create a dict to keep track of the number of occurrences
        track_dict = dict()

        for n in arr:
            if n not in track_dict:
                track_dict[n] = 1
            else:
                track_dict[n] += 1

        #Compare the number of values vs the length of the set of values
        return len(track_dict.values()) == len(set(track_dict.values()))