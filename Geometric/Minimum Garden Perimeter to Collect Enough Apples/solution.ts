/*
 * We set the i is the current vertice
 * We need to calculate 4 vertice (i*2)*4
 * We need to calculate 4 point that // make with O(0,0) the line // Ox and Oy
 * Then we calculate between the middle and the vertice, * 8
 * Example for i = 5
 * 10 9 8 7 6 5 6 7 8 9 10
 * 9                    9
 * 8                    8
 * 7                    7
 * 6                    6
 * 5                    5
 * 6                    6
 * 7                    7
 * 8                    8
 * 9                    9
 * 10 9 8 7 6 5 6 7 8 9 10
 * So we will have 4 vertice is i*2*4
 * 4 special point is i * 4
 * from 9 -> 6, calculate dynamic by n(n+1)/2 wil calculate sum from 1 to n
*/


function minimumPerimeter(neededApples: number): number {
    let apples = 0
    let i = 0
    while(apples < neededApples) {
        i++
        apples += (i*2) * 4 + i * 4
        apples += ((i*2*(i*2 - 1)/2) - (i * (i + 1) / 2)) * 8 
    }
    return (i*2)*4
};
