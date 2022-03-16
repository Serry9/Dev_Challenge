// Serricchio Hernán --- 2021

int main()

{

    float Pago=0, Saldo=0, Deposito=0, Saldo_mas=0, Saldo_menos=0, Pago_menos, Total=0;
    int op;

    printf("\t****************************\n");
    printf("\t*                          *\n");
    printf("\t*BIENVENIDO AL BANCO OFICAL*\n");
    printf("\t*                          *\n");
    printf("\t****************************\n\n");
    printf("\tIngresar Saldo Inicial\n\n");

    scanf("%g", &Pago);

    do

    {
        printf("\n\t Menu: 1: Depositar \n");
        printf("\t       2: Retirar \n");
        printf("\t       3: Ver Saldo \n");
        printf("\t       4: Realizar un pago \n");
        printf("\t       5: Salir \n");

        scanf("%d", &op);

        Total=(Pago+Deposito);

             switch (op) {

                case 1:
                printf("\t Ingresar suma a Depositar\n");

                scanf("%g", &Saldo_mas);
                Deposito += Saldo_mas;

                break;

                        case 2:
                        printf("\t Ingresar suma a Retirar \n");
                        scanf("\n\t %g", &Saldo_menos);

                            if( Saldo_menos > Total){
                                printf("\n\t ´´- Saldo a retirar es mayor al Deposito -´´ \n\n");
                            }
                                else{
                                    Deposito -= Saldo_menos;

                                    }

                        break;

                                case 3:

                                printf("\n\t Saldo es : $%g \n\t", Total);

                                break;

                                        case 4:
                                        printf("\t Realizar Pago \n");
                                        scanf("%g", &Pago_menos);

                                        if( Pago_menos > Total ){
                                            printf("\n\t ´´- Sin fondo suficiente -´´ \n\n");
                                            }
                                            else{
                                            Deposito -= Pago_menos;

                                            }

                                        break;
        }

    }

     while(op!=5);

    {
    printf("\t*************************\n");
    printf("\t* GRACIAS POR SU VISITA *\n");
    printf("\t*************************\n\n");

    }

return 0;
}
