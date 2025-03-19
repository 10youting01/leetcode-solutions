class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0;
        bool numeric = false;
        for(int i=s.length()-1; i>=0; i--){
            if(s[i]!=' '){
                numeric = true;
                count++;
            } else if(s[i]==' ' && numeric){
                return count;
            }
        }
        return count;        
    }
};
