class Solution {
public:
    string validIPAddress(string queryIP) {
        // Check if the input is a valid IPv4 address
        if (isIPv4(queryIP)) {
            return "IPv4";
        }
        // Check if the input is a valid IPv6 address
        if (isIPv6(queryIP)) {
            return "IPv6";
        }
        // Neither IPv4 nor IPv6
        return "Neither";
    }

private:
    bool isIPv4(const string& ipString) {
        // IPv4 cannot be empty or end with a dot
        if (ipString.empty() || ipString.back() == '.') {
            return false;
        }
      
        // Split the string by dots
        vector<string> segments = split(ipString, '.');
      
        // IPv4 must have exactly 4 segments
        if (segments.size() != 4) {
            return false;
        }
      
        // Validate each segment
        for (const string& segment : segments) {
            // Segment cannot be empty or have leading zeros (except for "0" itself)
            if (segment.empty() || (segment.size() > 1 && segment[0] == '0')) {
                return false;
            }
          
            // Convert segment to integer and validate range [0, 255]
            int value = convertToInt(segment);
            if (value < 0 || value > 255) {
                return false;
            }
        }
      
        return true;
    }

    bool isIPv6(const string& ipString) {
        // IPv6 cannot be empty or end with a colon
        if (ipString.empty() || ipString.back() == ':') {
            return false;
        }
      
        // Split the string by colons
        vector<string> segments = split(ipString, ':');
      
        // IPv6 must have exactly 8 segments
        if (segments.size() != 8) {
            return false;
        }
      
        // Validate each segment
        for (const string& segment : segments) {
            // Each segment must be 1-4 characters long
            if (segment.size() < 1 || segment.size() > 4) {
                return false;
            }
          
            // Each character must be a valid hexadecimal digit
            for (char ch : segment) {
                if (!isxdigit(ch)) {
                    return false;
                }
            }
        }
      
        return true;
    }

    int convertToInt(const string& str) {
        int result = 0;
      
        // Convert string to integer, checking for non-digit characters
        for (char ch : str) {
            if (!isdigit(ch)) {
                return -1;  // Invalid character found
            }
          
            result = result * 10 + (ch - '0');
          
            // Early return if value exceeds 255
            if (result > 255) {
                return result;
            }
        }
      
        return result;
    }

    vector<string> split(const string& str, char delimiter) {
        vector<string> tokens;
        string token;
        istringstream stringStream(str);
      
        // Split the string by the delimiter using getline
        while (getline(stringStream, token, delimiter)) {
            tokens.push_back(token);
        }
      
        return tokens;
    }
};
