using System;

namespace primmat
{
    public abstract class IMetod
    {
        public double CalculateFunc(double x)
        {
            //return (Math.Sin(x) * Math.Pow(x, 3));
            return (Math.Pow(x, Math.Pow(2, 1/x-3)) - Math.Log(x) - 1);
            //return Math.Sin(x * x * x * x - 1 / x);
        }

        public abstract double CalculateMinimum(double l, double r, double e);
    }
}