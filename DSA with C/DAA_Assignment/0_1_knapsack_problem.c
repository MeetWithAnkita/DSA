#include<stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapsack(int w, int weight[], int profit[], int n) {
    if (n == 0 || w == 0)
        return 0;
    if (weight[n - 1] > w)
        return knapsack(w, weight, profit, n - 1);
    else
        return max(profit[n - 1] + knapsack(w - weight[n - 1], weight, profit, n - 1), knapsack(w, weight, profit, n - 1));
}

int main() {
    int profit[10], weight[10], n, i, w;

    printf("Enter the number of objects: ");
    scanf("%d", &n);
    printf("Enter the profits of the objects: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &profit[i]);
    }
    printf("Enter the weights of the objects: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &weight[i]);
    }
    printf("Enter the maximum weight: ");
    scanf("%d", &w);

    printf("Maximum profit: %d\n", knapsack(w, weight, profit, n));
    return 0;
}



