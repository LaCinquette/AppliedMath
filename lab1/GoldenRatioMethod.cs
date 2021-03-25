using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;

namespace AppliedMathLab1
{
    static partial class Methods
    {
        public static double GoldenRatioMethod(double l, double r, double e)
        {
            double c = (-1 + Math.Sqrt(5)) / 2;
            double left = l;
            double right = r;
            double x1 = left + (1 - c) * (right - left);
            double x2 = left + c * (right - left);
            var f1 = CalculateFunc(x1);
            var f2 = CalculateFunc(x2);

            int n = 2;
            List<double> s = new List<double>();

            while ((right - left) / 2 > e)
            {
                s.Add(Math.Abs(right - left));

                if (f1 > f2)
                {
                    left = x1;
                    x1 = x2;
                    f1 = f2;
                    x2 = left + c * (right - left);
                    f2 = CalculateFunc(x2);
                    n++;
                }
                else
                {
                    right = x2;
                    x2 = x1;
                    f2 = f1;
                    x1 = left + (1 - c) * (right - left);
                    f1 = CalculateFunc(x1);
                    n++;
                }
            }

            return (left + right) / 2;
        }
    }
}