# Difficulty level: easy

# Given a string s, return true if it is a palindrome, otherwise return false.

#A palindrome is a string that reads the same forward and backward.
#It is also case-insensitive and ignores all non-alphanumeric characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
    
        while i < j:
     
            while i < j and not s[i].isalnum():
                i += 1
        
            while i < j and not s[j].isalnum():
                j -= 1
        
        
            if s[i].lower() != s[j].lower():
                return False
        
            i += 1
            j -= 1
    
        return True              
        

def main():
    # Create an instance of Solution
    sol = Solution()

    # Example 1: Removing elements
    s = "Was it a car or a cat I saw?"
    print(f"Original sentence: {s}")
    result = sol.isPalindrome(s)
    print(f"{result}\n")


if __name__ == "__main__":
    main()