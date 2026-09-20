class Solution {
public:
    int reverseDegree(string s) {
        int ans=0;
        int i=1;
        for(auto x : s){
            ans += i*(26 - (x - 'a'));
            i++;
        }
        return ans;
    }
};