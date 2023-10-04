// https://www.eolymp.com/en/problems/1453

#include <iostream>

using namespace std;

#define INFINITY 30000

void bellmanFord(int nNodes, int* edges, int nEdges, int src)
{
    int *dist = new int[nNodes];

    for (int i = 0; i < nNodes; i++)
    {
        dist[i] = INFINITY;
    }

    dist[src] = 0;

    int u, v, w;
    for (int i = 0; i < nNodes - 1; i++)
    {
        for (int j = 0; j < nEdges; j++)
        {
            u = edges[j * 3] - 1;
            v = edges[j * 3 + 1] - 1;
            w = edges[j * 3 + 2];

            if (dist[u] != INFINITY && dist[u] + w < dist[v])
            {
                dist[v] = dist[u] + w;
            }
        }
    }

    for (int j = 0; j < nEdges; j++)
    {
        u = edges[j * 3] - 1;
        v = edges[j * 3 + 1] - 1;
        w = edges[j * 3 + 2];        

        if (dist[u] != INFINITY && dist[u] + w < dist[v])
        {   
            cout << 0 << ' ';
            for (int i = 0; i < nNodes - 2; i++)
            {
                cout << 30000 << ' ';        
            }

            cout << 30000 << endl;
            return;
        }
    }

    for (int i = 0; i < nNodes - 1; i++)
    {
        cout << dist[i] << ' ';        
    }

    cout << dist[nNodes - 1] << endl;
}

int main()
{
    int nNodes, nEdges;

    cin >> nNodes >> nEdges;

    int *edges = new int[nEdges * 3];    

    for (int i = 0; i < nEdges; i++)
    {
        for (int j=0; j<3; j++) {            
            cin >> edges[i * 3 + j];
        }        
    }

    bellmanFord(nNodes, edges, nEdges, 0);
}