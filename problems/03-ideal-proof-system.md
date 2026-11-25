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

### A reciprocal table on four Boolean blocks

Over $\mathbb Q$, take the Boolean axioms and the linear equation $f(x)=1+\sum_{j=0}^{4n-1}2^j x_j=0$. Split the $4n$ variables into four blocks of $n$ each. In every Hilbert-like certificate, evaluation on the Boolean cube forces the multiplier of $f$ to have the same table $T(x)=1/f(x)$. For each of the three balanced block partitions its matrix entries are $1/(1+u+v)$, where $u,v$ are the binary-weight sums on the two sides. Within each side all $2^{2n}$ sums are distinct, and every denominator is positive. The Cauchy determinant formula gives rank $2^{2n}$ on each partition.

The next question is the least $R$ for which $T=T_1+T_2+T_3$ with the rank of $T_i$ at most $R$ on the $i$-th partition. Full rank on each separate partition leaves this sum question open. A lower bound for $R$ would apply to the corresponding restricted certificate model. A bound on ordinary IPS circuit size would additionally require a circuit-to-decomposition theorem. The subset-sum reciprocal has prior uses in restricted IPS lower bounds. [Forbes, Shpilka, Tzameret and Wigderson](https://arxiv.org/abs/1606.05050)
