// There are two sorted arrays nums1 and nums2 of size m and n respectively.

// Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

// Example 1:
// nums1 = [1, 3]
// nums2 = [2]

// The median is 2.0
// Example 2:
// nums1 = [1, 2]
// nums2 = [3, 4]

// The median is (2 + 3)/2 = 2.5

public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int i=0,j=0;
        int len1 = nums1.Length;
        int len2 = nums2.Length;
        int length = len1+len2;
        int[] result = null;
        if(length == 0)
        {
            nums1[1] = 0;
        }
        else if(len1 == 0)
        {
            result = nums2;
        }
        else if(len2 == 0)
        {
            result = nums1;
        }
        else
        {
            result = new int[length];
            while(true)
            {
                if(i>=len1)
                {
                    for(int z=j;z<len2;z++)
                    {
                        result[i+z] = nums2[z];
                    }
                    break;
                }
                if(j>=len2)
                {
                    for(int z=i;z<len1;z++)
                    {
                        result[z+j] = nums1[z];
                    }
                    break;
                }

                
                if(nums1[i] < nums2[j])
                {
                    result[i+j] = nums1[i];
                    i++;
                }
                else
                {
                    result[i+j] = nums2[j];
                    j++;
                }
            }
            
        }

        if(length%2 == 0)
            return (double)(result[length/2] + result[length/2 - 1])/2;
        else
            return result[(length-1)/2];
    }
}