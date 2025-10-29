class Solution {
public:
    int romanToInt(string s) {
        std::unordered_map<char, int> um =
        {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
        int number = 0;
        for(int i=0;i<s.length();i++){
            if (i+1<s.length()){
                if (s[i] == 'I'){
                    if (s[i+1]=='V' || s[i+1]=='X'){number-=um[s[i]];}
                    else number+=um[s[i]];
                }
                else if (s[i] == 'X'){
                    if (s[i+1]=='L' || s[i+1]=='C'){number-=um[s[i]];}
                    else number+=um[s[i]];
                }
                else if (s[i] == 'C'){
                    if (s[i+1]=='D' || s[i+1]=='M'){number-=um[s[i]];}
                    else number+=um[s[i]];
                }
                else number+=um[s[i]];
            }
           else number+=um[s[i]]; 
        
            
        }
        return number;




    }
};