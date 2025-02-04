#include <stdio.h>
#include <limits.h>

#define MAX 100  // Maximum number of vertices

void primMST(int n, int graph[MAX][MAX]) {
    int selected[n];  // Tracks included vertices (1 = included, 0 = not included)
    int minEdge[n];   // Stores the minimum edge weight for each vertex
    int parent[n];    // Stores the MST structure
    int totalWeight = 0;

    // Initialize arrays
    for (int i = 0; i < n; i++) {
        minEdge[i] = INT_MAX;  // Set all edge weights to infinity
        selected[i] = 0;       // No nodes are included initially
    }

    minEdge[0] = 0;  // Start from vertex 0
    parent[0] = -1;  // Root has no parent

    for (int count = 0; count < n - 1; count++) {
        int min = INT_MAX, u;

        // Find the minimum edge vertex not yet included in MST
        for (int v = 0; v < n; v++) {
            if (!selected[v] && minEdge[v] < min) {
                min = minEdge[v];
                u = v;
            }
        }

        selected[u] = 1; // Include it in MST

        // Update minEdge values for adjacent vertices
        for (int v = 0; v < n; v++) {
            if (graph[u][v] && !selected[v] && graph[u][v] < minEdge[v]) {
                parent[v] = u;
                minEdge[v] = graph[u][v];
            }
        }
    }

    printf("Edges in MST:\n");
    for (int i = 1; i < n; i++) {
        printf("%d -- %d == %d\n", parent[i], i, graph[i][parent[i]]);
        totalWeight += graph[i][parent[i]]; // Add edge weight to total
    }
    
    printf("Total MST Weight: %d\n", totalWeight);
}

int main() {
    int n, numEdges;
    
    // Take user input for number of vertices and edges
    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter number of edges: ");
    scanf("%d", &numEdges);

    int graph[MAX][MAX] = {0};  // Initialize adjacency matrix with 0

    printf("Enter %d edges in format (source destination weight):\n", numEdges);
    for (int i = 0; i < numEdges; i++) {
        int src, dest, weight;
        scanf("%d %d %d", &src, &dest, &weight);
        graph[src][dest] = weight;
        graph[dest][src] = weight; // Since it's an undirected graph
    }

    primMST(n, graph);
    return 0;
}
