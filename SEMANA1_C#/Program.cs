using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer2();
            Console.ReadKey();
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
            Console.Write("Ingrese número x: ");
            int x = int.Parse(Console.ReadLine());

            Console.Write("Ingrese número x: ");
            int y = Convert.ToInt32(Console.ReadLine());

            double resu = x / (double)y;

            Console.WriteLine("Suma: "+(x+y));
            Console.WriteLine("Resta: "+ (x-y));
            Console.WriteLine("Multiplicación: "+ (x+y));
            Console.WriteLine("División: "+ resu);
        }
        static void ejer3()
        {

        }
        static void ejer4()
        {

        }
        static void ejer5()
        {

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
