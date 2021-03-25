using System;
using System.Collections.Generic;
using System.Linq;

namespace AppliedMathLab1
{
    static partial class Methods
    {
        public static double DichotomyMethod(double l, double r, double e)
        {
            int n = 0;
            double left = l;
            double right = r;
            List<double> s = new List<double>();
            while ((right - left) / 2 > e)
            {
                double x1 = (left + right) / 2 - e / 2;
                double x2 = (left + right) / 2 + e / 2;
                s.Add(Math.Abs(right - left));
                List<string>[] arr;
                if (CalculateFunc(x1) > CalculateFunc(x2))
                {
                    left = x1;
                }
                else
                {
                    right = x2;
                }

                n += 1;
            }
            return (left + right) / 2;
        }
        
    }
}
