using System;

namespace SEMANA1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Menu(); 
        }
        static void Menu()
        {
            int opcion;
            do
            {
                Console.WriteLine("\n----- Menú de ejercicios -----");
                Console.WriteLine("1. Ejercicio 1");
                Console.WriteLine("2. Ejercicio 2");
                Console.WriteLine("3. Ejercicio 3");
                Console.WriteLine("4. Ejercicio 4");
                Console.WriteLine("5. Ejercicio 5");
                Console.WriteLine("0. Salir");
                Console.Write("Seleccione una opción: ");
                opcion = Convert.ToInt32(Console.ReadLine());
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
                    case 0:
                        Console.WriteLine("Saliendo del programa...");
                        break;
                    default:
                        Console.WriteLine("Opción inválida. Intente nuevamente.");
                        break;
                }
            } while (opcion != 0);
        }   
        static void ejer1()
        {
            string nombre, carrera; //declarando variables
            Console.Write("Ingrese su nombre: ");
            nombre = Console.ReadLine();
            Console.Write("Ingrese su carrera: ");
            carrera = Console.ReadLine();

            //Imprimir valores
            Console.WriteLine($"\n{nombre}, bienvenido al curso de {carrera}."); // "\n" genera saltos de vista
        }
        static void ejer2()
        {
           Console.WriteLine("\"Pablo\"");
        }
        static void ejer3()
        {
            Console.Write("Ingrese número x: ");
            int x = int.Parse(Console.ReadLine());

            Console.Write("Ingrese número x: ");
            int y = Convert.ToInt32(Console.ReadLine());

            double resu = x / (double)y;

            Console.WriteLine("Suma: " + (x + y));
            Console.WriteLine("Resta: " + (x - y));
            Console.WriteLine("Multiplicación: " + (x + y));
            Console.WriteLine("División: " + resu);
        }
        static void ejer4()
        {
            Console.Write("Ingrese un número decimal: ");
            double num = Convert.ToDouble(Console.ReadLine());

            double raiz2 = Math.Sqrt(num); //"sqrt" es para raiz cuadra. Nos estamos apoyando en la librería "Math"
            int redo = (int)Math.Round(num,0); //"se tiene que hacer explicito utilizando "(int)" al inicio, si no, va a aparecer error."
            double cubo = Math.Pow(num, 3); //Para visualizar un número al cubo
            double raiz3 = Math.Pow(num, 1/3d); //"d" al agregar la d se especifica que te devuelva el número en decimal; si no, no lo hace.

            Console.WriteLine($"Raiz: {raiz2}");
            Console.WriteLine($"Redondeado: {redo}");
            Console.WriteLine($"Al cubo: {cubo}");
            Console.WriteLine($"Raiz cúbica: {raiz3}");
        }
        static void ejer5()
        {
            Console.Write("Ingrese número: ");
            string num = Console.ReadLine();

            int entero =int.Parse(num);
            double deci = double.Parse(num);

            Console.WriteLine("Resto: ", +entero%2);
            Console.WriteLine("División ", +(deci/3));
        }
    }
}
