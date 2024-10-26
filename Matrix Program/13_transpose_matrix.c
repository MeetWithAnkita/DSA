#include<stdio.h>
void main()
{
    int arr[100][100],i,j,r,c,A[100][100],temp;

    printf("Enter the row and column of a matrix: ");
    scanf("%d%d",&r,&c);
    printf("Enter the %d elements: ",(r*c));
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            scanf("%d",&arr[i][j]);
            A[i][j]=arr[i][j];
        }
    }
    printf("%d * %d matrix is: \n",r,c);
    for(i=0; i<r; i++)
    {
        for(j=0; j<c; j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    // transpose matrix 
    // 00 01 02
    // 10 11 12
    // 20 21 22
    for(i=0;i<r;i++)
    {
        for(j=i+1;j<c;j++)
        {
           if(i != j)
           {
                temp = arr[i][j];
                arr[i][j] = arr[j][i];
                arr[j][i] = temp ; 
           }
                        
        }
    }

    printf("The matrix after transpose:\n");
    for(i=0; i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
}