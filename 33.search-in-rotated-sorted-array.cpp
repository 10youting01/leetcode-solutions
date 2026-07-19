            else if (nums[mid] >= nums[left]){ // 因為 mid 取值偏向左半邊，所以要歸到左半邊處理
                if (target >= nums[left] && target <= nums[mid]){
            } else {
                    right = mid;
                } else {
                    left = mid + 1;
                }
                if (target >= nums[mid] && target <= nums[right]){
                    left = mid;
                } else{
                    right = mid - 1;
            if (nums[mid] == target) return mid;
            int mid = (left + right) / 2; // 偏向左半邊，因為取下界
        while (left < right){

        int right = nums.size() - 1;
        int left = 0;
    int search(vector<int>& nums, int target) {
                }
            }
        }
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right){
            int mid = (left + right) / 2; // 偏向左半邊，因為取下界
            if (nums[mid] == target) return mid;
            else if (nums[mid] >= nums[left]){ // 因為 mid 取值偏向左半邊，所以要歸到左半邊處理
                if (target >= nums[left] && target <= nums[mid]){
                    right = mid;
                } else {
                    left = mid + 1;
                }
            } else {
                if (target >= nums[mid] && target <= nums[right]){
                    left = mid;
                } else{
                    right = mid - 1;
                }
            }
        }
        if (nums[left] == target){
            return left;
        } else{
            return -1;
        }
    }
};