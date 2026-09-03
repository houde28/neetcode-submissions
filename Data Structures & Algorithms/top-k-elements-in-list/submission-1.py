class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for each in nums:
            if each in dictionary:
                dictionary[each] += 1
            else:
                dictionary[each] = 1
        result=[]
        sorted_dict= sorted(dictionary,key=dictionary.get,reverse=True)


        return sorted_dict[:k]
