using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppliedMathLab1
{
    static partial class Methods
    {
        public static double FibonacciMethod(double l, double r, double e)
        {
            int c = NSearch(l, r, e);
            double left = l;
            double right = r;
            double x1 = (double)left + (double)FibonacciSequence(c) / FibonacciSequence(c + 2) * (right - left);
            double x2 = (double)left + (double)FibonacciSequence(c + 1) / FibonacciSequence(c + 2) * (right - left);
            double f1 = CalculateFunc(x1);
            double f2 = CalculateFunc(x2);

            List<double> s = new List<double>();
            int n = 0;

            while (right - left > e && left < right)
            {
                n++;
                s.Add(Math.Abs(left - right));
                if (f1 > f2)
                {
                    c--;
                    left = x1;
                    x1 = x2;
                    x2 = (double)left + (double)FibonacciSequence(c + 1) / FibonacciSequence(c + 2) * (right - left);
                    f1 = f2;
                    f2 = CalculateFunc(x2);

                }
                else
                {
                    c--;
                    right = x2;
                    x2 = x1;
                    x1 = (double)left + (double)FibonacciSequence(c) / FibonacciSequence(c + 2) * (right - left);
                    f2 = f1;
                    f1 = CalculateFunc(x1);
                }

            }
            return (left + right) / 2;
        }

        private static int FibonacciSequence(int n)
        {
            return (int) Math.Round((Math.Pow(((1 + Math.Sqrt(5)) / 2), n) - Math.Pow(((1 - Math.Sqrt(5)) / 2), n)) / (Math.Sqrt(5)), 0);
        }

        private static int NSearch(double a, double b, double e)
        {
            int i = 1;
            while (FibonacciSequence(i + 2) <= (b - a) / e)
            {
                i++;
            }
            return i;
        }
    }
}
