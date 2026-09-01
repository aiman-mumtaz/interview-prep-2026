class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> s;
        for(auto x: nums){
            s.insert(x);
        }
        int ans=0;

        int tmp=1;
        for(auto x:s){
            if(s.find(x+1) == s.end()){
                ans = max(ans,tmp);
                tmp=1;
            }else{
                tmp++;
            }
        }
        return ans;
    }
};
