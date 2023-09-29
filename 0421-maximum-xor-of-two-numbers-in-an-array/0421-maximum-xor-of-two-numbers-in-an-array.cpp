
class TrieNode {
public:
    vector<TrieNode*> children;
    
    TrieNode() {
        children = vector<TrieNode*>(2, nullptr);
    }
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        unordered_map<int, vector<int>> dp;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            for (int j = 31; j >= 0; j--) {
                dp[i].push_back(num & 1);
                num >>= 1;
            }
        }
        
        TrieNode* root = new TrieNode();
        int ans = 0;
        
        for (int j = 0; j < nums.size(); j++) {
            vector<int>& bits = dp[j];
            
            TrieNode* cur = root;
            for (int ind = 31; ind >= 0; ind--) {
                int bit = bits[ind];
                if (!cur->children[bit]) {
                    cur->children[bit] = new TrieNode();
                }
                cur = cur->children[bit];
            }
            
            int temp = 0;
            cur = root;
            for (int ind = 31; ind >= 0; ind--) {
                int bit = bits[ind];
                int val = 0;
                int comp = 1 - bit;
                
                if (cur->children[comp]) {
                    cur = cur->children[comp];
                    val = comp;
                } else if (cur->children[bit]) {
                    cur = cur->children[bit];
                    val = bit;
                }
                
                temp <<= 1;
                temp ^= val;
            }
            
            ans = max(ans, nums[j] ^ temp);
        }
        
        return ans;
    }
};