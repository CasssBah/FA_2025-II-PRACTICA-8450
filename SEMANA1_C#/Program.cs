using System;

namespace SEMANA1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Menú de opciones:");

            Console.WriteLine("\n1. Ejecutar ejer1");
            Console.WriteLine("2. Ejecutar ejer2");
            Console.WriteLine("3. Ejecutar ejer3");
            Console.WriteLine("4. Ejecutar ejer4");
            Console.WriteLine("5. Ejecutar ejer5");
            Console.WriteLine("6. Ejecutar ejer6");
            Console.WriteLine("7. Ejecutar ejer7");
            Console.WriteLine("8. Ejecutar ejer8");
            Console.WriteLine("9. Ejecutar ejer9");
            Console.WriteLine("10. Ejecutar ejer10");
            
            Console.Write("\nElige una opción: ");
            int opcion = int.Parse(Console.ReadLine());

                switch (opcion)
                {
                    case 1:
                        ejer1();
                        break;
                    case 2:
                        ejer2();
                        break;
                    case 3:
                        ejer3();
                        break;
                    case 4:
                        ejer4();
                        break;
                    case 5:
                        ejer5();
                        break;
                    case 6:
                        ejer6();
                        break;
                    case 7:
                        ejer7();
                        break;
                    case 8:
                        ejer8();
                        break;
                    case 9:
                        ejer9();
                        break;
                    case 10:
                        ejer10();
                        break;
                    case 0:
                        Console.WriteLine("Saliendo del programa.");
                        break;
                    default:
                        Console.WriteLine("Opción no válida.");
                        break;
                }
            

        }
        static void ejer1() 
        {
            string nombre, carrera;

            Console.Write("Introduzca su nombre: ");
            nombre = Console.ReadLine();

            Console.Write("Introduzca su carrera: ");
            carrera = Console.ReadLine();

            Console.WriteLine($"\n{nombre}, Bienvenido al curso de Fundamentos de Algoritmos de {carrera}.");

        }
        static void ejer2()
        {
            Console.WriteLine($"Tu nombre es: " + "\"Jeremy\"");
        }
        static void ejer3() 
        {
            Console.Write("Ingrese numero x: ");
            int x = int.Parse( Console.ReadLine() );

            Console.Write("Ingrese numero y: ");
            int y = int.Parse( Console.ReadLine() ) ;

            double resu = x/y ;

            Console.WriteLine("Suma: " + (x+y));
            Console.WriteLine("Resta: " + (x - y));
            Console.WriteLine("Multiplicación: " + (x * y));
            Console.WriteLine("División: " + (resu));

        }
        static void ejer4()
        {
            Console.Write("Ingrese un número decimal: ");
            double num = double.Parse(Console.ReadLine());

            double raiz_cuadrada = Math.Sqrt(num);
            double cubo = Math.Pow(num, 3);
            double redondeado = Math.Round(num);
            double raiz_cubica = Math.Pow(num, 1.0/3.0);

            Console.WriteLine($"Raiz cuadrada: {raiz_cuadrada}");
            Console.WriteLine($"Redondeado: {redondeado}");
            Console.WriteLine($"Cubo: {cubo}");
            Console.WriteLine($"Raiz cubica: {raiz_cubica}");

        }
        static void ejer5()
        {
            Console.Write("Escriba un numero(texto): ");
            string num = Console.ReadLine();

            int entero = int.Parse(num);
            double deci = double.Parse(num);

            Console.WriteLine($"Resto: {entero % 2}");
            Console.WriteLine($"División: {deci / 3}");

        }
        static void ejer6() 
        { 
        
        }
        static void ejer7() 
        { 
        
        }
        static void ejer8() 
        { 
        
        }
        static void ejer9() 
        { 
        
        }
        static void ejer10() 
        { 
        
        }

    }
}
