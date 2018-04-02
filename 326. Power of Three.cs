// Given an integer, write a function to determine if it is a power of three.

// Follow up:
// Could you do it without using any loop / recursion?

// Credits:
// Special thanks to @dietpepsi for adding this problem and creating all test cases.

public class Solution {
    public bool IsPowerOfThree(int n) {
        if(n <=0 ) return false;
        int x = (int)(Math.Log(n,3) + 0.5);
        if(Math.Pow(3,x) == n)
            return true;
        else
            return false;
    }
}