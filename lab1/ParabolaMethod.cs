using System;
using System.Threading;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppliedMathLab1
{
    static partial class Methods
    {
        public static double parabolaMethodX2;
        public static double ParabolaMethod(double l, double r, double e)
        {
            double a1, a2, x1, x2, x3, xm, xm_prev, f1, f2, f3, fm;

            x1 = l;
            x3 = r;
            x2 = parabolaMethodX2;
            f1 = CalculateFunc(x1);
            f2 = CalculateFunc(x2);
            f3 = CalculateFunc(x3);
            xm = r + e + 1;

            int n = 0;
            List<double> s = new List<double>();

            do
            {
                n++;
                a1 = (f2 - f1) / (x2 - x1);
                a2 = (double)1 / (x3 - x2) * ((f3 - f1) / (x3 - x1) - a1);
                s.Add(Math.Abs(x3 - x1));
                xm_prev = xm;
                xm = (double)1 / 2 * (x1 + x2 - a1 / a2);
                fm = CalculateFunc(xm);
                if (x1 < xm && xm < x2 && x2 < x3)
                {
                    if (fm >= f2)
                    {
                        x1 = xm;
                        f1 = fm;
                    }
                    else
                    {
                        x3 = x2;
                        f3 = f2;
                        x2 = xm;
                        f2 = fm;
                    }
                }
                else
                {
                    if (f2 >= fm)
                    {
                        x1 = x2;
                        f1 = f2;
                        x2 = xm;
                        f2 = fm;
                    }
                    else
                    {
                        x3 = xm;
                        f3 = fm;
                    }
                }
            }
            while (Math.Abs(xm - xm_prev) > e);
            
            return xm;
        }
    }
}
