class Solution {
public:
    int countSpecialIntegers(vector<int>& nums) {
        unordered_map<int,vector<int>>mp;
        for(int i=0;i<nums.size();i++){
            mp[nums[i]].push_back(i);
        }
        int sol=0;
        for(auto x:mp){
            if(x.second.size() == 3 && abs(x.second[0] - x.second[1]) == abs(x.second[2] - x.second[1])){
                sol++;
            }
        }
        return sol;
    }
};