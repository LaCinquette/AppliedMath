using System;

namespace primmat
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var m1 = new DichotomyMethod();
            Console.WriteLine(m1.CalculateMinimum(0.1, 0.3, 0.00001));
            var m2 = new GoldenRatioMethod();
            Console.WriteLine(m2.CalculateMinimum(0.1, 0.3, 0.00001));
            var m3 = new FibonacciMethod();
            var m4 = new ParabolaMethod();
            var m5 = new BrentMethod();
            Console.WriteLine(m3.CalculateMinimum(0.1, 0.3, 0.00001));
            Console.WriteLine(m4.CalculateMinimum(0.1, 0.3, 0.00001));
            Console.WriteLine(m5.CalculateMinimum(0.1, 0.3, 0.00001));

        }
    }
}


/* [3, 6.2] 5
 
*/