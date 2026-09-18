#include <iostream>
#include <string>
using namespace std;

void TableLogic(int **a, int size){
    for(int i=0; i<size; i++){
        if (i%2 == 0){
            a[0] [i]=0;
        } else
            a[0] [i]=1;
    }
    
    for(int i=0; i<size; i++){
        if (i%2 != 0){
            a[1] [i]=0;
        } else
            a[1] [i]=1;
    }
    
    for(int i=0; i<size; i++){
        if (i%2 == 0){
            a[2] [i]=0;
        } else
            a[2] [i]=1;
    }
    
    for(int i=3; i<(3+(size-6)); i++){
        for(int j=0; j<size; j++){
            a[i] [j]=0;
        }
    }
    
    for(int i=0; i<size; i++){
        if (i%2!=0){
            a[3+(size-6)] [i]=0;
        } else{
            a[3+(size-6)] [i]=2;
        }b
    }
    
    for(int i=0; i<size; i++){
        if (i%2==0){
            a[3+(size-5)] [i]=0;
        } else{
            a[3+(size-5)] [i]=2;
        }
    }
    
     for(int i=0; i<size; i++){
        if (i%2!=0){
            a[3+(size-4)] [i]=0;
        } else{
            a[3+(size-4)] [i]=2;
        }
    }
}

void PlayerTurn(int **a, int n){
    int size=n, turnos=0,jugador,piezafila,piezacolumna,movfila,movcolumna,tmp;
    
    do{
        
        cout << "\n";
        
        for(int k=0; k<n; k++){
            cout<<k<<"   ";
        }
        
        cout << "\n";
        
        for(int l=0; l<n; l++){
            cout<<"————";
        }
        
        cout << "\n";
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                
                if (a[i] [j] == 1){
                    cout << "✖" << " ❘ ";
                } else if (a[i] [j] == 2){
                    cout << "✪" << " ❘ ";
                } else if (a[i] [j] == 0){
                    cout << "☐" << " ❘ ";
                }
            }
            cout << i;
            cout << "\n";
            
            for(int m=0; m<n; m++){
                cout << "————";
            }
            
            cout << "\n";
        }
        
        if(turnos%2==0){
            jugador = 1;
        } else{
            jugador=2;  
        }
        
        cout << "\nTURNO JUGADOR #" << jugador;
        
        cout << "\nINGRESE FILA DE LA PIEZA QUE DESEA MOVER: ";
        cin >> piezafila;
        
        cout << "\nINGRESE COLUMNA DE LA PIEZA QUE DESEA MOVER: ";
        cin >> piezacolumna;
        
        cout << "\nINGRESE FILA DE LA POSICION DEL TABLERO AL QUE DESEA MOVER: ";
        cin >> movfila;
        
        cout << "\nINGRESE COLUMNA DE LA POSICION DEL TABLERO AL QUE DESEA MOVER: ";
        cin >> movcolumna;
        
        if(a[movfila] [movcolumna]==0){
            tmp=a[piezafila] [piezacolumna];
            a[piezafila] [piezacolumna]=0;
            a[movfila] [movcolumna]=tmp;
        } else{
            cout << "\nMOVIMIENTO NO VALIDO.";
        }
        
        if(jugador==1){
            if(a[movfila-1] [movcolumna-1]==2){
                a[movfila-1] [movcolumna-1]=0;
            }
            
            if(a[movfila-1] [movcolumna+1]==2){
                a[movfila-1] [movcolumna+1]=0;
            }
        }
        
         if(jugador==2){
            if(a[movfila+1] [movcolumna+1]==1){
                a[movfila+1] [movcolumna+1]=0;
            }
            
            if(a[movfila+1] [movcolumna-1]==1){
                a[movfila+1] [movcolumna-1]=0;
            }
        }
        
        turnos++;
    }
    
    while(true);
}

void WinnerPlayer(int **a, int z){
    string gana;
    int piezasUno=0;
    int piezasDos=0;
    
    for(int i=0; i<z; i++){
        for(int j=0; j<z; j++){
            if(a[i] [j] == 1){
                piezasUno++;
            }
        }
    }
    
    for(int i=0; i<z; i++){
        for(int j=0; j<z; j++){
            if(a[i] [j] == 2){
                piezasDos++;
            }
        }
    }
    
    if(piezasUno==0){
        gana=2;
    }
    
    if(piezasDos==0){
        gana=1;
    }
    
    cout << "EL GANADOR ES EL JUGADOR #" << gana;
}

int main()
{
    
    int **array=NULL,size;
    cout << "--- JUEGO DE DAMAS ---";
    size = 8;
    
    array = new int*[size];
    
    for(int i = 0; i < size; ++i){
        array[i] = new int[size];
    }
    cout << "\n------ EMPIEZE -------";
    
    TableLogic(array, size);
    PlayerTurn(array, size);
    WinnerPlayer(array, size);
    
    delete []array;
    return 0;
    
}