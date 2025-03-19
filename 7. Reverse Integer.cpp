#include <cmath>
#include <string>
#include <algorithm>

class Solution {
    public:
        int reverse(int x) {
            std::string s = std::to_string(x);
            bool isNeg = false;
    
            std::reverse(s.begin(), s.end());
    
            if(s[s.length() - 1] == '-') {
                s.pop_back();
                s = "-" + s;
            }
    
            while (s.length() > 1 && s[s.length() - 1] == '0') {
                s.pop_back();
            }
    
            double tempd = std::stod(s);
    
            if ( -1 * std::pow(2, 31) <= tempd && tempd <= std::pow(2, 31) - 1)
            {
                return std::stoi(s);
            }
            
    
            return 0;
        }
};
