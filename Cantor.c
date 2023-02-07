#include<stdio.h>

int main()
{
    int n,k,s;
    while(scanf("%d",&n) == 1)
    {    
        k=0;
        s=0;
        while(s<n)
        {
            k++;
            printf("%d\n",k);
            s+=k;
            printf("%d\n",s);
        }
        if(k%2==1)
            printf("%d/%d",s-n+1,k+n-s);
        else
            printf("%d/%d",k+n-s,s-n+1);
    }
    
    return 0;
}