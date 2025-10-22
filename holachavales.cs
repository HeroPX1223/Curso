// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;

namespace Fernan {

 class Program {
    static void Main() {
        Console.Write("Ingresa el numero: ");
        string numer = Console.ReadLine();
        int numero = int.Parse(numer);  // Convierte el string a int
    
    if(numero % 2 == 0) {
        Console.Write("Par");
    }
    else if(numero % 3 == 0) {
        Console.Write("Impar");
    }
    }
        
}
}