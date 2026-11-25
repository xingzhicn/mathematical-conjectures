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

### A lower bound for mixtures of the three cuts

Let $q=2^n$, with $n\ge 1$, and index the four blocks by their base-$q$ digits. The table is then $T_{a b c d}=1/(1+a+qb+q^2c+q^3d)$ for $0\le a,b,c,d<q$. There is an absolute $c_0>0$ such that every decomposition across the three balanced cuts satisfies
$$
\operatorname{rank}_{AB\mid CD}(T_1)+
\operatorname{rank}_{AC\mid BD}(T_2)+
\operatorname{rank}_{AD\mid BC}(T_3)\ \ge\ c_0q.
$$
In particular $R\ge c_0q/3$. An upper bound is $R\le q\lceil q/3\rceil$. For that bound, split the values of $a$ into three classes of size at most $\lceil q/3\rceil$ and assign one restricted table, extended by zero, to each cut. The side containing $A$ then has at most $q\lceil q/3\rceil$ nonzero rows or columns.

**A prime with many disjoint digit quadruples.** Take primes $p\in(q^3,2q^3]$ and write $M_p=\lfloor q^4/p\rfloor$. The $M_p$ multiples $tp$ in the denominator range give the digit quadruples of $tp-1$. Their first digits are all distinct because $p$ is odd and $M_p\le q$. Their fourth digits are all distinct because successive values differ by $p>q^3$. Put an edge between two indices $t$ if their quadruples share either middle digit.

For indices with difference $1\le h<q$, equality of digit $s\in\{1,2\}$ requires $\operatorname{dist}(hp,q^{s+1}\mathbb Z)<q^s$. For $s=1$, put $g=\gcd(h,q^2)$. Multiplication by $h$ modulo $q^2$ has fibers of size $g$ over the multiples of $g$, so at most $2q+g\le 3q$ residue classes of $p$ can meet this condition. The Brun–Titchmarsh inequality bounds the primes in each reduced class modulo $q^2$ in the interval of length $q^3$ by $O(q/\log q)$. For $s=2$, the condition restricts $p$ to at most $h+1$ intervals, centered at $jq^3/h$ for $h\le j\le 2h$, each of length $2q^2/h\ge 2q$. Brun–Titchmarsh on these intervals gives $O(q^2/(h\log q))$ primes per interval. Thus at most $O(q^2/\log q)$ primes can have a collision at any fixed difference $h$. The implied constants are uniform in $h$ and $q$. [Montgomery and Vaughan, The large sieve](https://doi.org/10.1112/S0025579300004708)

The prime number theorem gives $\Theta(q^3/\log q)$ primes in the chosen interval. Each difference $h$ contributes at most $q$ edges per prime, so summing over $h<q$ gives $O(q)$ edges on average per prime. Choose a prime with $E=O(q)$ edges. The graph has $M_p\ge q/2$ vertices and an independent set of size at least $M_p^2/(2E+M_p)=\Omega(q)$. For example, a random vertex order retains a vertex whenever it precedes all its neighbors, giving expected size $\sum_v 1/(1+\deg v)\ge M_p^2/(2E+M_p)$.

**Reduction to a diagonal table.** Restrict each of the four digit sets to the digits of the selected $m=\Omega(q)$ quadruples and label each retained digit by its quadruple. Multiplication by $p$ makes every entry integral at $p$ because all denominators are at most $q^4<p^2$. Its reduction modulo $p$ is supported on the denominators divisible by $p$. The fourth digit of each multiple is unique among all multiples, so the restricted support consists exactly of the $m$ selected tuples. The resulting table is diagonal with coefficients $(t\bmod p)^{-1}\ne 0$ on the chosen tuples. For $q=8$, the prime $541$ and multiples indexed by $t=1,3,6,7$ give four such tuples.

**Rank transfer using the first partial derivatives.** Associate to the scaled restricted table the four-linear form $P$ in four sets of $m$ variables. A decomposition of the original table with total rank $r$ expresses $P$ over $\mathbb Q$ as a sum of at most $r$ products of two bilinear forms, by factoring each flattening into rank-one terms and then restricting. All first partials of $P$ vanish wherever the at most $2r$ factors simultaneously vanish. If $r<m$, the height bound for an ideal generated by $2r$ elements therefore gives dimension at least $4m-2r>2m$ for the common zero set of the partials over $\overline{\mathbb Q}$.

The dimension of that zero set cannot decrease on reduction modulo $p$. In each degree $e\ge 3$, the degree-$e$ part of the gradient ideal is the image of the matrix whose columns are the first partials multiplied by monomials of degree $e-3$. The matrix has entries in $\mathbb Z_{(p)}$, so its rank can only fall modulo $p$. The Hilbert function of the quotient can only grow, and its eventual growth determines its Krull dimension over either field. The reduced form is $\sum_{i=1}^m \lambda_i X_iY_iZ_iW_i$ with every $\lambda_i\ne 0$. All its partials vanish exactly when at least two variables are zero in each coordinate quadruple, a union of coordinate subspaces of dimension $2m$. This contradicts $r<m$ and proves the lower bound for all sufficiently large $q$. The constant $c_0$ can be decreased to include the remaining $q$, since $T$ is nonzero.

The argument uses the table forced on the Boolean cube, so the lower bound applies to each multiplier of $f$ in a Hilbert-like certificate in the specified decomposition model. The same singular-locus argument gives a linear lower bound when terms may use any complementary nonempty block sets. In that broader model expansion in the first block gives an upper bound of $q$, so an improvement beyond linear for the three balanced cuts must exploit those cuts. Translating the result to arithmetic circuit size still requires a bound on the decomposition price of tables produced by small arithmetic circuits.

Forbes, Shpilka, Tzameret and Wigderson plant a reciprocal gadget into a chosen variable cut using auxiliary selectors to obtain large coefficient dimension and restricted IPS circuit lower bounds. The proof here considers summands on all three cuts of one fixed table and uses the same coordinate restriction and prime reduction for the entire decomposition. [Forbes, Shpilka, Tzameret and Wigderson, Sections 5.4–5.5](https://arxiv.org/abs/1606.05050)
