# Lower bounds for the Ideal Proof System

## Target

Find an explicit family of unsatisfiable systems of bounded-degree equations over a specified field for which every Hilbert-like IPS certificate has superpolynomial arithmetic circuit size. In the linear-in-placeholders model a certificate consists of multipliers $A_i$ satisfying $\sum_i A_iF_i=1$. An unrestricted IPS certificate is a circuit $C(x,y)$ satisfying $C(x,0)=0$ and $C(x,F(x))=1$. The two models should be addressed with their respective quantifiers. [Grochow–Pitassi](https://arxiv.org/abs/1404.3820)

## Obstruction and geometric target

For $F_1=z$ and $F_2=z-1$, the certificate $y_1-y_2$ has constant size. For any polynomial $h(u)$,
$$
y_1-y_2+\bigl(y_1(z-1)-y_2z\bigr)h(u)
$$
is another valid certificate, and specializing it recovers $1-h(u)$. Thus a hard certificate can coexist with an easy proof of the same system. The Grochow–Pitassi implication from superpolynomial Hilbert-like IPS lower bounds to $\mathsf{VP}\ne\mathsf{VNP}$ leaves this issue open in the reverse direction.

A specific route is to construct a linear map on certificate coefficients that forces a high-price tensor for every valid multiplier tuple and maps every small circuit into a uniformly low-price class, with the map's evaluation and projection costs included. Restrictions to multilinear multipliers, particular partitions or particular degrees require their own model statement. [Andrews–Forbes](https://arxiv.org/abs/2112.00792)
