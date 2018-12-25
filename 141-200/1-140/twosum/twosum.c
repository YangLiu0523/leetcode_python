/*
 * =====================================================================================
 *       Filename:  twosum.c
 *    Description:  O(n^2)
 *        Version:  1.0
 *        Created:  2015年02月16日 16时10分33秒
 *       Revision:  none
 *       Compiler:  gcc
 *         Author:  Dai Yuanzhen (-), -
 *   Organization:  -
 * =====================================================================================
 */

int *twoSum(int numbers[], int n, int target) {
    int i,j,a[2];
    for(i=1;i<n;i++){
        for(j=0;j<i;j++){
            if(numbers[i]+numbers[j]==target){
                a[0]=j+1;
                a[1]=i+1;
                return a;
            }
        }
    }
}
