/*
📘 저울 추 문제
평형저울을 이용하여 1kg 이하의 물건의 무게를 재려고 한다. 준비되어 있는 추는
1g, 3g, 9g, 27g, 81g, 243g, 729g과 같이 7개의 추뿐이다.

평형저울의 양쪽 접시에 물건과 추를 적절히 놓음으로써 물건의 무게를 잴 수 있는데,
예를 들어, 25g의 물건을 재기 위해서는 다음과 같이 저울의 왼쪽에 물건을 올려놓으면 된다.

(도식: 왼쪽 접시에 25g 물건과 3g 추, 오른쪽 접시에 1g, 9g, 27g 추가 있음)

📌 문제
물건의 무게가 입력되었을 때, 양쪽 접시에 어떤 추들을 올려놓아 평형을 이루는지를 결정하는 프로그램을 작성하시오.

📥 입력
물건의 무게를 나타내는 하나의 정수 n이 입력된다. (1 ≤ n ≤ 1000)

n은 물건의 무게가 몇 g(그램)인지를 나타낸다.

📤 출력
저울의 왼쪽 접시와 오른쪽 접시에 올린 추를 0으로 구분하여 출력한다.

각 접시에 올린 추들은 무게가 가벼운 추부터 나열하며 공백으로 구분하여 출력한다.

물건의 무게는 왼쪽 접시의 처음에 표시한다.

*/


#include <stdio.h>
#include <stdlib.h>

int weights[7] = {1, 3, 9, 27, 81, 243, 729};
int left[7], right[7]; // 각 추를 왼쪽/오른쪽에 올렸는지 표시
int found = 0;

// 현재 단계 i, 왼쪽 총합, 오른쪽 총합
void dfs(int i, int leftSum, int rightSum, int target) {
    if (i == 7) {
        if (leftSum + target == rightSum) {
            found = 1;
            // 출력
            printf("%d ", target);
            for (int j = 0; j < 7; j++) {
                if (left[j]) printf("%d ", weights[j]);
            }
            printf("0 ");
            for (int j = 0; j < 7; j++) {
                if (right[j]) printf("%d ", weights[j]);
            }
            printf("\n");
        }
        return;
    }

    // 1. 추를 왼쪽에 올린다
    left[i] = 1; right[i] = 0;
    dfs(i + 1, leftSum + weights[i], rightSum, target);
    if (found) return;

    // 2. 추를 오른쪽에 올린다
    left[i] = 0; right[i] = 1;
    dfs(i + 1, leftSum, rightSum + weights[i], target);
    if (found) return;

    // 3. 추를 사용하지 않는다
    left[i] = 0; right[i] = 0;
    dfs(i + 1, leftSum, rightSum, target);
    if (found) return;
}

int main() {
    int n;
    scanf("%d", &n);
    dfs(0, 0, 0, n);
    if (!found)
        printf("측정 불가능한 무게입니다.\n");
    return 0;
}
