class Solution {
public:
    bool isPal(string s){
        int i=0,j=s.length()-1;
        while(i<=j){
            if(!isalnum(s[i]) || s[i] ==' '){
                i++;
            }
            else if(!isalnum(s[j]) || s[j] == ' '){
                j--;
            }
            else if(tolower(s[i]) != tolower(s[j])){
                return false;
            }else{
                i++;
                j--;
            }
        }
        return true;
    }
    string firstPalindrome(vector<string>& words) {
        for(auto x:words){
            if(isPal(x)){
                return x;
            }
        }
        return "";
    }
};