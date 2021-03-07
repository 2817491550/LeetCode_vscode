/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] 验证回文串
 */

// @lc code=start
class Solution {
public:
   bool isPalindrome(string s) {
        int len=s.size();
        string strs;
    
        for(int i=0;i<len;i++)
        {
            if(s[i]<='9'&&s[i]>='0'||s[i]>='a'&&s[i]<='z'||s[i]<='Z'&&s[i]>='A')
            {
                if(s[i]>='A'&&s[i]<='Z'){
                    s[i]+=32;
                }
                strs+=s[i];
            }
            else{
                continue;
            }
        }
        bool flag=true;
        for(int i=0;i<strs.size()/2;i++)
        {
            if(strs[i]!=strs[strs.size()-i-1])
            {
                flag=false;
            }

        }
        return flag;

    }
};
// @lc code=end

