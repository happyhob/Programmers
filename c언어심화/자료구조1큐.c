
#include <stdio.h>
#include <stdlib.h>

#define SIZE 10  // 큐의 최대 크기

int queue[SIZE];
int front = 0;
int rear = 0;

// 큐에 원소 추가
void put(int a) {
    if (rear < SIZE) {
        queue[rear] = a;
        rear++;
    } else {
        printf("Queue overflow!\n");
    }
}

// 큐에서 원소 제거
void get() {
    if (front < rear) {
        printf("%d\n", queue[front]);
        front++;
    } else {
        printf("Empty queue!\n");
    }
}

// 큐 출력 (front부터 rear까지)
void print() {
    for (int i = front; i < rear; i++) {
        printf("%d ", queue[i]);
    }
    printf("\n");
}

// 테스트용 main 함수
int main() {
    put(1);
    put(3);
    put(5);
    print();     // 1 3 5
    get();       // 1
    get();       // 3
    get();       // 5
    get();       // Empty queue!
    return 0;
}
