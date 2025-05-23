/*
✅ n-Queen 문제 (텍스트 추출)
📘 문제 설명
이 문제는 n×n 체스 보드판에 n개의 queen을 서로 공격하지 못하도록 배치하는 방법을 찾아내는 문제이다.

아래 그림은 n이 4일 경우 queen을 서로 공격하지 못하게 배치한 한 예를 나타낸다.

📥 입력
정수 n이 입력으로 들어온다. (3 ≤ n ≤ 9)

📤 출력
서로 다른 총 경우의 수를 출력한다.
*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int count = 0;
int col[15]; // 최대 n=9이므로 여유있게 배열 크기 설정

// 유효한 위치인지 검사
int is_safe(int row) {
    for (int i = 0; i < row; i++) {
        if (col[i] == col[row] || abs(col[row] - col[i]) == row - i)
            return 0; // 같은 열 또는 대각선에 있으면 안됨
    }
    return 1;
}

// 백트래킹 함수
void solve(int row, int n) {
    if (row == n) {
        count++; // n개의 퀸 배치 성공
        return;
    }

    for (int i = 0; i < n; i++) {
        col[row] = i; // 현재 행에 퀸을 i열에 놓음
        if (is_safe(row)) {
            solve(row + 1, n);
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);

    count = 0;
    solve(0, n);

    printf("%d\n", count);
    return 0;
}
