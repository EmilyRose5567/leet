class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.length()-1;
        int length = 0;
        if (s[i] == ' '){
            while (s[i] == ' '){i--;}
        }
        while (s[i] != ' '){
            length++;
            i--;
            if (i < 0){break;}
        }
        return length;

    }
};