using System;
using System.Collections.Generic;
using System.ComponentModel;

namespace primmat
{
    public class GoldenRatioMethod : IMetod
    {
        private static readonly double c = (-1 + Math.Sqrt(5))/2;

        public override double CalculateMinimum(double l, double r, double e)
        {
            double left = l;
            double right = r;
            double x1 = left + (1 - c) * (right - left) ;
            double x2 = left + c * (right - left);
            var f1 = CalculateFunc(x1);
            var f2 = CalculateFunc(x2);
            
            while ((right - left)/2 > e)
            {
                if (f1 > f2)
                {
                    left = x1;
                    x1 = x2;
                    f1 = f2;
                    x2 = left + c * (right - left);
                    f2 = CalculateFunc(x2);
                }
                else
                {
                    right = x2;
                    x2 = x1;
                    f2 = f1;
                    x1 = left + (1 - c) * (right - left) ;
                    f1 = CalculateFunc(x1);
                }
            }
            
            return (left + right)/2;
        }
    }
}