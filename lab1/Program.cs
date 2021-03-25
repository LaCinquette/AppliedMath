using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Globalization;

namespace AppliedMathLab1
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Methods.FuncN> funcs = new List<Methods.FuncN>();
            List<(double a, double b, double e)> parameters = new List<(double a, double b, double e)>();
            List<double> parabolaMethodX2 = new List<double>();
            funcs.Add(Methods.Func1);   parameters.Add((0.1, 0.3, 0.00001));     parabolaMethodX2.Add(0.29);
            funcs.Add(Methods.Func2);   parameters.Add((-1.6, -1.2, 0.00001));   parabolaMethodX2.Add(-1.4);
            funcs.Add(Methods.Func3);   parameters.Add((-2, 1, 0.00001));        parabolaMethodX2.Add(-1.1);
            funcs.Add(Methods.Func4);   parameters.Add((2, 4, 0.00001));         parabolaMethodX2.Add(3);
            funcs.Add(Methods.Func5);   parameters.Add((3, 6.2, 0.00001));       parabolaMethodX2.Add(5);

            string path = @"F:\ITMO\AppliedMathLab1\AppliedMathLab1\results";
            DirectoryInfo directory = new DirectoryInfo(path);
            if (!directory.Exists)
            {
                directory.Create();
            }

            List<string> methodNames = new List<string>();
            methodNames.Add("DichotomyMethod");
            methodNames.Add("GoldenRatioMethod");
            methodNames.Add("FibonacciMethod");
            methodNames.Add("ParabolaMethod");
            methodNames.Add("BrentMethod");

            List<string> funcNames = new List<string>();
            funcNames.Add("1.txt");
            funcNames.Add("2.txt");
            funcNames.Add("3.txt");
            funcNames.Add("4.txt");
            funcNames.Add("5.txt");

            List<Methods.Method> methods = new List<Methods.Method>();
            List<string> paths = new List<string>();

            methods.Add(Methods.DichotomyMethod);      paths.Add(path + @"\" + funcNames[0]);
            methods.Add(Methods.GoldenRatioMethod);    paths.Add(path + @"\" + funcNames[1]);
            methods.Add(Methods.FibonacciMethod);      paths.Add(path + @"\" + funcNames[2]);
            methods.Add(Methods.ParabolaMethod);       paths.Add(path + @"\" + funcNames[3]);
            methods.Add(Methods.BrentMethod);          paths.Add(path + @"\" + funcNames[4]);

            NumberFormatInfo nfi = new NumberFormatInfo();
            nfi.NumberDecimalSeparator = ".";

            double x, y;
            for (int i = 0; i < Methods.Nfunctions; i++)
            {
                Methods.func = funcs[i];
                Methods.parameters = parameters[i];
                Methods.parabolaMethodX2 = parabolaMethodX2[i];

                FileStream txtfile = new FileStream(paths[i], FileMode.Create);
                txtfile.Close();

                StreamWriter writer = new StreamWriter(paths[i]);
                for (int j = 0; j < Methods.Nmethods; j++)
                {
                    x = methods[j](Methods.parameters.a, Methods.parameters.b, Methods.parameters.e);
                    y = Methods.CalculateFunc(x);

                    writer.WriteLine(methodNames[j]);
                    writer.WriteLine($"x_m: {x.ToString(nfi)}");
                    writer.WriteLine($"y_m: {y.ToString(nfi)}");
                    writer.WriteLine();
                }
                writer.Close();
            }

            Console.ReadKey();
        }
    }
}
