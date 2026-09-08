#include<stdio.h>
void merge(int a[],int l,int m,int u)
{
    int i,j,k ;
    int n1 = m-l+1 ; 
    int n2 = u-m ;

    int L[n1], R[n2];

    for (i=0 ; i<n1 ; i++)
    {
        L[i] = a[l+i];
    }
    for(j=0 ; j<n2 ; j++)
    {
        R[j] = a[m+1+j];
    }

    i=0, j=0 ,k=l ;
    while(i<n1 && j<n2)
    {
        if (L[i] <= R[j])
        {
            a[k] = L[i];
            i++ ; 
        }
        else
        {
            a[k] = R[j];
            j++ ;
        }
        k ++ ;
    }
    while(i<n1)
    {
        a[k] = L[i];
        i++ ; 
        k++ ;
    }
    while(j<n2)
    {
        a[k] = R[j];
        j++ ; 
        k++ ;
    }
    
}
void mergesort(int a[],int l,int u)
{
    if (l<u)
    {
        int m ; 
        m = (l+u)/ 2 ;
        mergesort(a,l,m);
        mergesort(a,m+1,u);
        merge(a,l,m,u);
    }
}

void main()
{
    int a[100],n,i,l,u ;
    printf("Enter the no of array :");
    scanf("%d",&n);
    printf("Enter the %d elements :",n);
    for(i=0; i <n ; i++)
    {
        scanf("%d",&a[i]);
    }
    printf("The sorted array is :\n");
    l= 0 ; u=n-1 ;
    mergesort(a,l,u);
    for(i=0 ; i<n; i++)
    {
        printf("%d ",a[i]);
    }
}




// //////////////////////////////////////////////////////////////////////
// // C program for Merge Sort
// #include <stdio.h>
// #include <stdlib.h>

// // Merges two subarrays of arr[].
// // First subarray is arr[l..m]
// // Second subarray is arr[m+1..r]
// void merge(int arr[], int l, int m, int r)
// {
// 	int i, j, k;
// 	int n1 = m - l + 1;
// 	int n2 = r - m;

// 	// Create temp arrays
// 	int L[n1], R[n2];

// 	// Copy data to temp arrays L[] and R[]
// 	for (i = 0; i < n1; i++)
// 		L[i] = arr[l + i];
// 	for (j = 0; j < n2; j++)
// 		R[j] = arr[m + 1 + j];

// 	// Merge the temp arrays back into arr[l..r
// 	i = 0;
// 	j = 0;
// 	k = l;
// 	while (i < n1 && j < n2) {
// 		if (L[i] <= R[j]) {
// 			arr[k] = L[i];
// 			i++;
// 		}
// 		else {
// 			arr[k] = R[j];
// 			j++;
// 		}
// 		k++;
// 	}

// 	// Copy the remaining elements of L[],
// 	// if there are any
// 	while (i < n1) {
// 		arr[k] = L[i];
// 		i++;
// 		k++;
// 	}

// 	// Copy the remaining elements of R[],
// 	// if there are any
// 	while (j < n2) {
// 		arr[k] = R[j];
// 		j++;
// 		k++;
// 	}
// }


// // l is for left index and r is right index of the
// // sub-array of arr to be sorted
// void mergeSort(int arr[], int l, int r)
// {
// 	if (l < r) {
// 		int m = l + (r - l) / 2;

// 		// Sort first and second halves
// 		mergeSort(arr, l, m);
// 		mergeSort(arr, m + 1, r);

// 		merge(arr, l, m, r);
// 	}
// }

// // Function to print an array
// void printArray(int A[], int size)
// {
// 	int i;
// 	for (i = 0; i < size; i++)
// 		printf("%d ", A[i]);
// 	printf("\n");
// }


// // DRIVER CODE
// int main()
// {
//    int arr[100],n,i;
//    printf("Enter the size of array:  ");
//    scanf("%d",&n); 
//    printf("Enter the elements :  ");
//    for(i=0;i<n;i++)
//    { 
//      scanf("%d",&arr[i]);
//    }

//    mergeSort(arr, 0, n - 1);
//    printf("Sorted array is \n");
//    printArray(arr, n);
//    return 0;
// }

