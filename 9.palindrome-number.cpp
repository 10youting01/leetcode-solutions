class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0 || ((x%10==0)&&x!=0)) return false;

        int reversex = 0;
        while(x>reversex){
            reversex = (reversex*10) + (x%10);
            x /= 10;
        }
        if(reversex==x || x==(reversex/10)) return true;
        else return false;
    }
};
