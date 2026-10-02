class Solution {
public:
    void gen(vector<string> &ans, int o, int c, string s){
        if(o == 0 && c == 0){
            ans.push_back(s);
            return;
        }
        if(o > 0){
            gen(ans,o-1,c,s+'(');
        }
        if(c > o){
            gen(ans,o,c-1,s+')');
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        gen(ans,n,n,"");
        return ans;
    }
};