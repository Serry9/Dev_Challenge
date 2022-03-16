#include <stdio.h>
#include <stdlib.h>

int main()
{
    int numero, cont=-1, suma=0;
    float promedio;
    printf("\nCalcular la suma y el promedio de todos los\n");
    printf("numeros positivos que ingrese el usuario.\n");
    printf("Este ciclo finaliza con el ingreso de un numero 0 o menor que 0.\n\n");


    do

    {       printf("Ingrese un numero: ");
            fflush(stdin);
            scanf("%d", &numero);
            suma+=numero;
            cont++;
    }


    while(numero>0);
    printf("\t Suma de los numeros ingresados es: %d\n",suma);
    printf("\t Cantidad de numeros ingresados es: %d\n", cont);
    if(cont!=0){
        promedio=(float)suma/cont;
        printf("\t El promedio de los numeros ingresados es: %g\n", promedio);
    }
    return 0;
}