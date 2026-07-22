class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() == 0) return 0;
        int left = 0;
        int longest = 0;
        unordered_map<char, int> char_idx;
        for(int right = 0; right < s.size(); right++){
            if(char_idx.count(s[right]) && char_idx[s[right]] >= left){
                left = char_idx[s[right]] + 1;
            }
            char_idx[s[right]] = right;

            if((right - left + 1) > longest){
                longest = right - left + 1;
            }
        }
        return longest;
    }
};

// 這一題的輸入是一個 string s，輸出是這個 string 當中最長不重複的子字串（substring）。

// Constraint（限制條件）：
// • string 的 length 是從 0 到 5 × 10⁴
// • 可能會包含任何英文字母、digit、symbols 跟 space
// • 要注意長度可能會為 0 的情況

// 解法思路：

// 1. 暴力解（Brute Force）：
//    以每一個字母當作開頭，往後去找以該字母為開頭最長的不重複子字串長度，最後比較出最長的長度並回傳。過程中可以用一個 HashMap 來維護、尋找不重複的子字串。

// 2. 更好的解法：Sliding Window
//    • 初始化左邊界 left 為 0（字串中 0 的位置）。
//    • 用一個 for 迴圈以 right 為右邊界，從 0 開始往後掃描。
//    • 同樣維護一個 HashMap，裡面存「字母」跟「該字母出現過的位置」。
//    • 如果發現新位置的字母（例如 A、B、C，當走到第二個 A 的時候，此時 left 在第一個 A，right 在第二個 A）已經在 HashMap 裡面，且它的位置是在目前的 window 當中，那就要縮減左邊界 left 到這個相同字母位置的右邊一格。
//    • 同時維護一個變數去記錄目前最長的不重複子字串長度，最終回傳這個最長長度。