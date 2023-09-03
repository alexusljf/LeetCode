/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const Map = {}
    for(var i=0;i<nums.length;i++){
        const complement = target-nums[i];
        if (complement in Map){
            return [Map[complement],i];
        }
        Map[nums[i]]=i;
    }
    return [];

};