#include <stdio.h>
main()
{
   int i,n=-1;
   while(n<0)
   {
       printf("Enter Positive number:");
       scanf("%d",&n);
   }
   for(i=2;i<n;i++)
   {
       if(n%i==0) break;
   }
   if(n<=1) printf("Not Prime");
   else if (n==2) printf("Prime");
   else if(i==n) printf("Prime");
   else printf("Not Prime")
}