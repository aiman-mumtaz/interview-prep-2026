class Solution {
public:
    bool isValid(string s) {
        if(s.size() % 2 != 0){
            return false;
        }
        stack<char>st;
        for(auto x: s){
            if(x == '{' || x == '[' || x == '('){
                st.push(x);
            }else{
                if(!st.empty()){
                    char ch = st.top();
                    if(x == '}' && ch != '{'){
                        return false;
                    }
                    if(x == ')' && ch != '('){
                        return false;
                    }
                    if(x == ']' && ch != '['){
                        return false;
                    }
                    st.pop();
                }else{
                    return false;
                }
            }
        }
        return st.empty() ? true:false;
    }
};
