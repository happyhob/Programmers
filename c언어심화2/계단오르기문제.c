/*
💡 트리 구상하기
트리의 각 노드에는 현재 몇 칸을 올랐는지가 숫자로 저장된다.

왼쪽 자식으로 내려가는 건 1칸을 더 오르는 경우, 오른쪽 자식으로 내려가는 건 2칸을 더 오르는 경우라고 생각한다.

노드들을 탐색하며 노드의 숫자가 n이라면 (현재 n칸 올랐다면) 카운트를 1 증가시키고,
n보다 커졌다면 (n칸을 지나쳤다면) 종료한다.
*/

#include <stdio.h>

int count = 0;

// 현재 계단 위치가 step, 목표는 n
void climb(int step, int n) {
    if (step == n) {
        count++;
        return;
    }
    if (step > n) return;

    // 1칸 오르기
    climb(step + 1, n);
    // 2칸 오르기
    climb(step + 2, n);
}

int main() {
    int n;
    scanf("%d", &n);

    count = 0;
    climb(0, n);

    printf("%d\n", count);

    return 0;
}
