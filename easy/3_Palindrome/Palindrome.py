from typing import List, Dict

class Solution(object):

    # Note that if you are doing any string operations, you are wrong
    def isPalindrome(self, x: int) -> bool:
        strnum = str(x)

        if x < 0:
            return False

        if strnum == strnum[::-1]:
            return True
        else:
            return False



# public boolean isPalindrome(int x) {
#     String str = String.valueOf(x);
#     int start = 0;
#     int end = str.length() - 1;
#     while(start < end){
#         if(str.charAt(start++) != str.charAt(end--)) return false;
#     }
#     return true;
# }

def main():
    print(Solution().isPalindrome(121))

if __name__ == "__main__":
    main()
