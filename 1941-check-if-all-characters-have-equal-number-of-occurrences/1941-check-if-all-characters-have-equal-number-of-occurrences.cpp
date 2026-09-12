class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> freq;

        for(auto x:s){
            freq[x]++;
        }
        if(freq.size() == 0){
            return true;
        }
        int lastVal = freq[s[s.size()-1]];
        for(auto x: freq){
            if(x.second != lastVal){
                return false;
            }
        }
        return true;
    }
};