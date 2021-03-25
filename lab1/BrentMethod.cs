using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppliedMathLab1
{
    static partial class Methods
    {
        public static double BrentMethod(double a, double b, double e)
        {
            double x, w, v, g, u;
            double r = (3 - Math.Sqrt(5)) / 2; //1-c
            double d_cur, d_prv;
            d_cur = d_prv = b - a;
            x = w = v = a + r * (b - a);
            double fx, fw, fv;
            fx = fw = fv = CalculateFunc(x);

            List<double> s = new List<double>();
            int n = 0;

            while (true)
            {
                n++;
                s.Add(Math.Abs(b - a));
                if (Math.Max(x - a, b - x) < e)
                {
                    return x;
                }
                g = d_prv / 2;
                d_prv = d_cur;

                double a1 = (fw - fx) / (w - x);
                double a2 = (double)1 / (v - w) * ((fv - fx) / (v - x) - a1);
                u = (double)1 / 2 * (x + w - a1 / a2);
                double fu = CalculateFunc(u);


                if (double.IsNaN(u) || (u < a || u > b) || Math.Abs(u - x) > g) //u == null
                {
                    if (x < (a + b) / 2)
                    {
                        u = x + r * (b - x);
                        d_prv = b - x;
                    }
                    else
                    {
                        u = x - r * (x - a);
                        d_prv = x - a;
                    }
                    fu = CalculateFunc(u);

                }
                d_cur = Math.Abs(u - x);
                if (fu > fx)
                {
                    if (u < x)
                    {
                        a = u;
                    }
                    else
                    {
                        b = u;
                    }

                    if (fu <= fw || w == x)
                    {
                        v = w;
                        fv = fw;
                        w = u;
                        fw = fu;
                    }
                    else
                    {
                        if (fu < fv || v == x || v == w)
                        {
                            v = u;
                            fv = fu;
                        }
                    }
                }
                else
                {
                    if (u < x)
                    {
                        b = x;
                    }
                    else
                    {
                        a = x;
                    }
                    v = w;
                    fv = fw;
                    w = x;
                    fw = fx;
                    x = u;
                    fx = fu;
                }
            }
        }
    }
}
