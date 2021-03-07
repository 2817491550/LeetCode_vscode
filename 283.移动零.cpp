/*
 * @lc app=leetcode.cn id=283 lang=cpp
 *
 * [283] 移动零
 */

// @lc code=start
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int counter_zero=0;
        for (int i=0; i<nums.size(); i++) {
            if(nums[i]==0)counter_zero++;
        }
        int j=0;
        for(int i=0; i<nums.size(); i++)
        {
            if(nums[i]!=0)nums[j++]=nums[i];
        }
        for(int i=0; i<counter_zero; i++)
        {
            nums[j+i]=0;
        }
    }
};
// @lc code=end

