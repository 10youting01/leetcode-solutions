class Solution {
public:
    int climbStairs(int n) {
        if(n==1) return 1;
        else if(n==2) return 2;
        int step_one = 1;
        int step_two = 2;
        for(int i=3; i<n+1; i++){
            int temp1 = step_two;
            step_two += step_one;
            step_one = temp1;
        }
        return step_two;
    }
};
