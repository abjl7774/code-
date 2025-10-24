#include <stdio.h>
#include <math.h>
double f(double x)
{
    return pow(x, 3) - 2 * x - 1;
}
int main()
{
    double a = 0.0, b = 2.0;
    double tol = 1e-4;
    int iteration_count = 0;
    double c, fc;
    if (f(a) * f(b) >= 0)
    {
        printf("初始区间[%.2f, %.2f]内无实根或根不唯一，请调整区间！\n", a, b);
        return 1;
    }
    printf("迭代次数\t   a值\t\t   b值\t\t   中点c\t   f(c)\t\t区间长度|b-a|\n");
    printf("--------------------------------------------------------------------------\n");
    while (fabs(b - a) > tol)
    {
        c = (a + b) / 2;
        fc = f(c);
        iteration_count++;
        printf("%d\t\t%.8f\t%.8f\t%.8f\t%.8f\t%.8f\n",
               iteration_count, a, b, c, fc, fabs(b - a));
        if (f(a) * fc < 0)
        {
            b = c;
        }
        else
        {
            a = c;
        }
    }
    double root = (a + b) / 2;
    printf("--------------------------------------------------------------------------\n");
    printf("迭代结束！\n");
    printf("方程在[0, 2]内的近似根为：%.8f\n", root);
    printf("总迭代次数：%d\n", iteration_count);
    printf("精度达到：10^-4\n");
    return 0;
}
