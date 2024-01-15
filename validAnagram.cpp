#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        // Base case, if they are not the same length then they can't be anagrams
        if (s.length() != t.length()){
            return false;
        }
        // Maps to store the <letter, occurrences of this letter> for both strings
        std::unordered_map<char, int> umap;
        std::unordered_map<char, int> umap2;

        for (int i = 0; i < s.length(); i++){
         // map umap stores the letters and their occurrences for string s
            if (umap.find(s[i]) == umap.end()){
                umap[s[i]] = 1;
            }
            else{
                umap[s[i]]++;
            }
            // map umap2 stores the letters and their occurrences for string t
            if (umap2.find(t[i]) == umap2.end()){
                umap2[t[i]] = 1;
            }
            else{
                umap2[t[i]]++;
            }

        }
      
        // if both maps are equal then they store the same letters and number of occurrences and therefore both strings are anagrams
        if (umap == umap2){
            return true;
        }
        return false;
    }
};
