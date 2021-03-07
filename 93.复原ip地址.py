#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n=len(s)
        ip_4=4
        ip_addrs=[0]*ip_4
        ans=[]
        def track_back(seg_id,seg_start):
            if seg_id==ip_4:
                if seg_start==n:
                    ip_addr=".".join([str(addr) for addr in ip_addrs])
                    
                    ans.append(ip_addr)
                return
            if seg_start==n:
                return 
            if s[seg_start]=='0':
                ip_addrs[seg_id]=0
                track_back(seg_id+1,seg_start+1)
            addr=0
            for seg_end in range(seg_start,n):
                addr=addr*10+(ord(s[seg_end])-ord('0'))
                if 0<addr<=255:
                    ip_addrs[seg_id]=addr
                    track_back(seg_id+1,seg_end+1)
                else:
                    break
        track_back(0,0)
        return ans
            

             


# @lc code=end

