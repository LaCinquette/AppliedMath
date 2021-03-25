using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppliedMathLab1
{
    static partial class Methods
    {
        public static int Nfunctions = 5;
        public static int Nmethods = 5;
        public delegate double Method(double l, double r, double e);
        public delegate double FuncN(double x);
        public static FuncN func;
        public static (double a, double b, double e) parameters;
        public static double CalculateFunc(double x)
        {
            return func(x);
        }
        public static double Func1(double x)
        {
            return Math.Pow(x, Math.Pow(2, (double)1 / x - 3)) - Math.Log(x) - (double)1;
        }
        public static double Func2(double x)
        {
            return Math.Sin(Math.Pow(x, 4) - (double)1 / x);
        }
        public static double Func3(double x)
        {
            return (x * x * x * x + x * x * x + 3 * x + 10);
        }
        public static double Func4(double x)
        {
            return Math.Pow(Math.Cos(x), 5) * Math.Atan(x);
        }
        public static double Func5(double x)
        {
            return (Math.Sin(x) * Math.Pow(x, 3));
        }
    }
}
