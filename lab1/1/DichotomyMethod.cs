using System;
using System.Collections.Generic;

namespace primmat
{
    public class DichotomyMethod : IMetod
    {

        public DichotomyMethod()
        {
        }

        public override double CalculateMinimum(double l, double r, double e)
        {
            double left = l;
            double right = r;
            while ((right - left)/2 > e )
            {
                double x1 = (left + right) / 2 - e/2;
                double x2 = (left + right) / 2 + e/2;
                if (CalculateFunc(x1) > CalculateFunc(x2))
                {
                    left = x1;
                }
                else
                {
                    right = x2;
                }
            }
            
            return (left + right)/2;
        }
        
    }
}
