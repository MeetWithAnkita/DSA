#include <stdio.h>
#define MAX_EDGES 100
typedef struct {
    int src, dest, weight;
} Edge;

void sortEdges(Edge edges[], int numEdges) {
    for (int i = 0; i < numEdges - 1; i++) {
        for (int j = i + 1; j < numEdges; j++) {
            if (edges[i].weight > edges[j].weight) {
                Edge temp = edges[i];
                edges[i] = edges[j];
                edges[j] = temp;
            }
        }
    }
}

int findParent(int parent[], int node) {
    while (parent[node] != node)
        node = parent[node];
    return node;
}

void kruskal(int n, Edge edges[], int numEdges) {
    int parent[n];
    for (int i = 0; i < n; i++)
        parent[i] = i;

    sortEdges(edges, numEdges);

    int mstWeight = 0;
    printf("Edges in MST:\n");

    for (int i = 0; i < numEdges; i++){
        int u = findParent(parent, edges[i].src);
        int v = findParent(parent, edges[i].dest);

        if (u != v) {
            parent[v] = u       ;
            printf("%d -- %d == %d\n", edges[i].src, edges[i].dest, edges[i].weight)        ;
            mstWeight += edges[i].weight  ;
        }
    }
    printf("Total MST Weight: %d\n", mstWeight);
}

int main() {
    // int n = 4,i;
    // Edge edges[] = {
    //     {0, 1, 10},
    //     {0, 2, 6},
    //     {0, 3, 5},
    //     {1, 3, 15},
    //     {2, 3, 4}
    // };
    // int numEdges = 5;


    int n, numEdges;    
    // Take user input for number of vertices and edges
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    
    printf("Enter number of edges: ");
    scanf("%d", &numEdges);

    Edge edges[numEdges];

    // Taking input for edges
    printf("Enter edges in format (source destination weight):\n");
    for (int i = 0; i < numEdges; i++) {
        scanf("%d %d %d", &edges[i].src, &edges[i].dest, &edges[i].weight);
    }

    kruskal(n, edges, numEdges);

    return 0;
}
