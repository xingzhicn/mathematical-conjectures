# Multipartite entanglement conversion

Use exact grouped local linear restrictions over $\mathbb C$. The conversion rate $R(U,V)$ is the supremum of $k/m$ for restrictions of $U^{\otimes m}$ to $V^{\otimes k}$. The physical interpretation is a nonzero-probability SLOCC branch with no required success-probability bound. Deterministic LOCC and high-success-probability approximation have different acceptance conditions. [Universal points in the asymptotic spectrum of tensors](https://arxiv.org/abs/1709.07851)

Let $\Phi_{ij}$ denote the dimension-$q$ equality tensor on parties $i,j$. Set
$$
X_q=\Phi_{12}\Phi_{34}+2\Phi_{14}\Phi_{23},\qquad
Y_q=\Phi_{13}\Phi_{24}+2\Phi_{14}\Phi_{23}.
$$
Their labeled bipartition ranks coincide and their normalized single-party marginals are maximally mixed. The party swap gives equality of the two directional rates. A unit square places the two source matchings on sides, so their sum costs at most $2\log_2 q+2$. Projections onto two disjoint $\lfloor q/2\rfloor$-element coordinate sets isolate a diagonal matching in $Y_q$. Consequently
$$
R(X_q,Y_q)\le\frac{\log_2 q+1}{\sqrt2\log_2\lfloor q/2\rfloor},\qquad q\ge4 .
$$
The bound is strictly below one at $q=64$. [Proof](https://github.com/xingzhicn/four-party-tensor-conversion)

There is an exact three-copy protocol giving $R(X_q,Y_q)\ge 1/3$. Contract parties 1 and 4 of an auxiliary $X_q$ against the same coordinate covector $e_j^*$. The coefficient matrix left at parties 2 and 3 is $2I+e_je_j^{\mathsf T}$. It is invertible over $\mathbb C$, so a local map gives one dimension-$q$ equality wire between them. Two auxiliary copies give two such wires. On a third, intact copy, contract party 2's input against its endpoint of the first wire and party 3's input against its endpoint of the second, using equality covectors. The free endpoints now carry the two exchanged indices. This gives exactly $Y_q$ under grouped local maps. The protocol does not use the price theorem.

### A joint exact protocol on a square

Put $d=\lfloor q/2\rfloor$, $s=\lceil\sqrt q\rceil$ and $w=s^2$. Call the matching $12,34$ horizontal and $14,23$ vertical. From one $X_q$ we can extract either pure matching with wire dimension $d$. For the horizontal matching, project 1 and 2 onto the same $d$ coordinates and 3 and 4 onto disjoint $d$ coordinates. This kills the vertical term. Reversing the roles extracts the vertical matching, up to a removable scalar.

For a single output, first prepare the diagonal matching on a square with one wire of dimension $w$ on each side. Use both two-edge paths for each diagonal, routing one dimension-$s$ label along each path. Each side carries exactly two labels. At an intermediate vertex use an equality covector to join consecutive edge labels. Each diagonal then has dimension $s^2$, which its two endpoints truncate to $q$. A second possible output uses just the two vertical edges, each with dimension $q$, to prepare the vertical matching.

The same square can prepare their coherent sum. Tag the two horizontal edges and one of the vertical edges by taking the direct sum of their two branch spaces. The horizontal dimensions are $w+1$ each and the tagged vertical dimension is $w+q$. The other vertical edge has dimension $w$ and can serve either branch. Each vertex enforces agreement among its incident tags and applies the local map for their common value. The three tagged edges form a spanning tree, so only the two globally consistent choices survive. A factor of two at one vertex in the vertical branch gives precisely $Y_q$. This is one grouped local linear map per party, including the superposition.

For even $k$, alternate the tagged vertical edge among the $k$ outputs. With $a$ horizontal and $b$ vertical source copies, it suffices that
$$
d^a\ge(w+1)^k,\qquad d^b\ge [w(w+q)]^{k/2}.
$$
The powers are dimensions of independent wires, so coordinate truncation realizes every finite protocol specified by these inequalities. Choosing the two integer ceilings and taking large even $k$ gives
$$
R(X_q,Y_q)\ \ge\
\frac{\log_2 d}{\log_2(w+1)+\tfrac12\log_2(w(w+q))}.
$$
At $q=64$, eight copies of each orientation give six outputs, and the asymptotic bound is about $0.3993$. At $q=256$, five copies of each orientation give four outputs. As $q$ grows the lower bound tends to $1/2$. The construction uses routing and coherent local control.

**The five-copy test.** In a five-to-two protocol that first extracts these pure matchings from each copy, the two cuts separating opposite sides of the square would require $d^{2a}\ge q^4$ and $d^{2b}\ge q^4$, since every balanced flattening of $Y_q$ has rank $q^2$. As $d<q$, each of $a,b$ must be at least three. A second obstruction applies to protocols that leave parties 1 and 4 of two designated data copies untouched and use the other three copies solely to create a bipartite ancilla at 2 and 3. The data state has full rank across $14\mid23$, so the effective operation on 2 and 3 must be the swap on local dimension $q^2$. Its operator Schmidt rank is $q^4$, by expansion in matrix units. Local maps assisted by a pure ancilla of Schmidt rank $K$ give an operator of Schmidt rank at most $K$, by expanding the ancilla in Schmidt terms. Here $K\le q^3$. Both arguments leave general five-to-two grouped maps open.

### Optimality of the square as a single price comparison

For any four Hilbert-space sites write $h,v,z$ for the total lengths of the horizontal, vertical and diagonal matchings. Put $A=\max(h,v)$ and $B=\max(z,v)$. Extracting either source matching and bounding the target's sum give
$$
H(X_q)\ge A\log_2 d,\qquad H(Y_q)\le B\log_2 q+W.
$$
Write $u=x_3-x_1$ and $v'=x_4-x_2$. The triangle inequality gives $\|u-v'\|\le h$ and $\|u+v'\|\le v$. The parallelogram identity and Cauchy–Schwarz imply $z^2=(\|u\|+\|v'\|)^2\le h^2+v^2$. Thus $B\le\sqrt2 A$. A spanning tree of the four sides can distribute one shared bit, giving $W\le h+v\le2A$. For every nonconstant placement, even one depending on $q$, this yields
$$
\frac{H(X_q)}{H(Y_q)}
\ \ge\ \frac{\log_2 d}{\sqrt2\log_2 q+2}.
$$
The square gives the opposite asymptotic bound by the comparison at the beginning of this page. Hence the infimum of the single-placement Euclidean price ratios tends to exactly $1/\sqrt2$.

### The large-dimension conversion rate

Assume the curvature and Euclidean price theorems of the cited preprint. For exact grouped restrictions over $\mathbb C$, with $q\ge4$ and $d=\lfloor q/2\rfloor$, the following bounds imply the limit
$$
\frac{\log_2 d}{\sqrt2\log_2 q+3/2}
\ \le\ R(X_q,Y_q)=R(Y_q,X_q)\
\le\frac{\log_2 q+1}{\sqrt2\log_2 d},
\qquad
\lim_{q\to\infty}R(X_q,Y_q)=\frac1{\sqrt2}.
$$
The copy rate here is first taken at fixed $q$. The lower bound uses spectral duality and gives existence of exact block conversions. The explicit square protocol above has limiting rate at least $1/2$. [Curvature theorem][curvature] · [Strassen's asymptotic spectrum, as recalled by Christandl, Vrana and Zuiddam](https://arxiv.org/abs/1709.07851)

**All four-party spectral points obey the required distance inequality.** Let $F$ be any monotone semiring homomorphism on four-party tensors, normalized by $F(\Delta_4(2))=2$, and set $H_F=\log_2 F$. Its six binary-wire prices are distances in a pseudometric whose metric quotient embeds isometrically in a CAT(0) space, by the curvature theorem. Write $a,b,c,e$ for the cyclic side lengths, $s_1,s_2$ for the diagonals, and put $h=a+c$, $v=b+e$, $z=s_1+s_2$. The CAT(0) quadrilateral inequality and the Ptolemy inequality give, respectively,
$$
s_1^2+s_2^2\le a^2+b^2+c^2+e^2,\qquad s_1s_2\le ac+be.
$$
Adding twice the second bound to the first gives $z^2\le h^2+v^2$. These inequalities also hold for coincident sites. In particular $B=\max(z,v)\le\sqrt2 A$ for $A=\max(h,v)$. The cheapest three-edge spanning tree obtained by deleting one side has length at most $3(h+v)/4$. Such a tree supplies $\Delta_4(2)$, of normalized log price one. Thus $1\le 3A/2$. [Wire prices and spanning trees][calculus] · [CAT(0) spaces and Ptolemy's inequality](https://doi.org/10.1093/imrn/rnm100)

By the coordinate projections of the two source matchings, $H_F(X_q)\ge A\log_2 d$. By the ordinary-sum inequality on the target, $H_F(Y_q)\le B\log_2 q+1$. The target also restricts to $\Delta_4(2)$ by the construction below and the party transposition, so its log price is positive. Combining the inequalities gives the stated lower bound on $H_F(X_q)/H_F(Y_q)$ simultaneously for every $F$.

**Passing from the spectrum to exact maps.** Write $X=X_q$ and $Y=Y_q$. For positive integers $m,k$ with $k/m$ below that uniform bound, every spectral point satisfies $F(Y^{\otimes k})\le F(X^{\otimes m})$. Theorem 1.1 and the definition in §1.1 of Christandl, Vrana and Zuiddam give exact restrictions from $X^{\otimes m(n+o(n))}$ to $Y^{\otimes kn}$. Equivalently, in the formulation with a subexponential direct-sum overhead, an auxiliary $\Delta_4(L_n)$ with $\log_2 L_n=o(n)$ can be paid for from the source. To see this, take distinct indices $i,j,l,t$. At parties $1,2,3,4$ retain respectively the ordered pairs $(i,l),(i,t),(j,t),(j,l)$. The horizontal term of $X$ retains just the first coordinate at every party. The vertical term retains just the second. Rescaling one output basis vector gives $\Delta_4(2)$. Thus $\lceil\log_2 L_n\rceil$ extra source copies supply $\Delta_4(L_n)$. The resulting exact rates approach $k/m$. Taking the supremum proves the lower bound under the page's definition of $R$. The square upper bound proves the limit by squeezing. The precise rate at any specified finite $q$, an explicit protocol attaining the limiting constant, and the unrestricted five-to-two test remain open here.

For the three-party EPR triangle, the logarithmic GHZ cost per unit wire dimension in the asymptotic tensor-rank model is $9/4$ under the cited matrix multiplication theorem. The distinct four-party rates above remain to be determined. [Matrix multiplication preprint][mm]

[mm]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf
[curvature]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/build/curvature.tex#L170-L180
[calculus]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/build/prices.tex
