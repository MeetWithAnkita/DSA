// #include<stdio.h>
// #include<stdbool.h>
// #define MAX 100
// int board[MAX][MAX];
// void  printsolution(int N)
// {
//     for (int i=0 ; i<N; i++)
//     {
//         for(int j=0; j<N; j++)
//         {
//             printf("%d ",board[i][j]);
//         }
//         printf("\n");
//     }
// }
// bool isSafe(int row,int col,int N)
// {
//     for(int i = 0 ; i<col ; i++)
//     {
//         if(board[row][i])
//         return false;
//     }
//     for(int i=row, j=col ; i>=0 && j>=0 ; i--,j--)
//     {
//         if (board[i][j])
//         {
//             return false ;
//         }
//     }
//     for(int i =row, j=col ; i<N && j>=0  ; i++,j--)
//     {
//         if (board[i][j])
//         {
//             return false ;
//         }
//     }
//     return true ;
// }
// bool SQ(int col ,int N)
// {
//     if (col >= N)
//     {
//         return true ;
//     }
//     for (int i =0 ; i<N ; i++)
//     {
//         if (isSafe(i,col,N))
//         {
//             board[i][col] = 1 ;
//             if (SQ(col+1, N))
//             {
//                 return true ;
//             }
//             board[i][col]=0;
//         }
//     }
//     return false ;
// }
// int main()
// {
//     int N;
//     printf("Enter the size of chessboard :");
//     scanf("%d",&N);
//     if (N<4 || N>MAX)
//     {
//         printf("Invalid size of board.");
//         return 1 ;
//     }
//     for (int i=0 ; i<N;i++)
//     {
//         for(int j=0;j<N;j++)
//         {
//             board[i][j] = 0 ;
//         }
//     }
//     if (SQ(0,N))
//     {
//         printf("Solution exists:\n");
//         printsolution(N);
//     }
//     else
//     {
//         printf("Solution doesn't exit");
//     }
//     return 0 ;
// }

#include<stdio.h>
#include<stdbool.h>
#define MAX 100
int board[MAX][MAX];
int isSafe(int row, int col,int N)
{
    for(int i=0 ; i<col; i++)
    {
        if (board[row][i])
        {
            return false ;
        }
    }
    for(int i=row, j=col ; i>=0 && j>=0 ;i--,j-- )
    {
        if (board[i][j])
        {
            return false ;
        }
    }
    for(int i=row, j=col ; i<N && j>=0 ;i++,j-- )
    {
        if (board[i][j])
        {
            return false ;
        }
    }
    return true ;

}
int SQ(int col,int N)
{
    if (col >= N)
        return true ;
    
    for (int i =0; i<N ; i++)
    {
        if (isSafe(i,col,N))
        {
            board[i][col] = 1;
            if (SQ(col+1,N))
            {
                return true ;
            }
            board[i][col] = 0 ;     
        }
    }
    return false;
}
int main()
{
    int N ;
    printf("Enter the size of chessbard :");
    scanf("%d", &N);
    
    if (N<4 || N>MAX)
    {
        printf("Invalid input..");
    }

    for(int i=0 ; i<N; i++)
    {
        for(int j=0 ; j<N; j++)
        {
            board[i][j] = 0 ;
        }
    }

    if (SQ(0,N))
    {
        printf("The solution is :\n");
        for(int i=0 ; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                printf("%d ",board[i][j]);
            }
            printf("\n");
        }
    }
    else
    {
        printf("There has no solution .");
    }
    return 0 ; 

}