#include <stdio.h>
main()
{
    float height, base, area;
    printf("Enter height");
    scanf("%f",&height);
    
    printf("Enter Base");
    scanf("%f",&base);
    
    area = 0.5*height*base;
    
    printf("area of triangle is :%f",area);
}