# Matrix rigidity and static range sums

## Matrix rigidity

For an explicit $N\times N$ matrix $M_N$ over a specified field, write
$$
\mathcal R_{M_N}(r)=\min_{\operatorname{rank}B\le r}|\operatorname{supp}(M_N-B)|.
$$
The target is a Valiant-type bound $\mathcal R_{M_N}(\lfloor\varepsilon N\rfloor)\ge N^{1+\delta}$ for fixed $\varepsilon,\delta>0$, with an explicitness requirement appropriate to the field.

The rectangle construction repeats the row label on one side and the column label on the other. Its spectral price is known exactly for character tables. The Fourier result also allows simultaneous low-rank and sparse corrections in its specified circuit model. For any proposed new matrix family, prove a lower bound on its rectangle price and an upper bound for all decompositions under the desired rank and support budgets. The character-table theorem does not supply those estimates for Cauchy or curve-evaluation matrices. [Fourier preprint][fourier]

## Group-model range sums

Fix a universe, a family of orthogonal range queries, and an abelian group model. A stored cell is a prescribed linear combination of input weights. Each query is computed from a bounded number of stored cells using allowed group operations. For a field-linear nonadaptive version, the query incidence matrix factors as $M=QA$, where $A$ encodes the linear-space preprocessing and each row of $Q$ has at most $t$ nonzero entries.

Consider the Boolean-cube dominance incidence matrix $M=U^{\otimes k}$, with $U=\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)$ and $N=2^k$. There are exactly $N$ queries. With $N$ cells, storing their answers gives $A=M$, $Q=I_N$, and query cost $t=1$. A bound on cell count alone therefore allows the exact optimum of one probe.

A revised target also charges updates. Over a fixed field, require at most $u$ nonzeros in each column of $A$, so changing one input changes at most $u$ cells. For factorizations using $O(N)$ cells, determine the tradeoff between $u$ and the maximum row support $t$ of $Q$. The precomputed-answer construction has $u=N$. A geometric argument would have to bound the cost of sharing the same cell across different queries in this factorization.

[fourier]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-logarithmic-exponent-of-finite-Fourier-transforms-November-24-2026/paper.pdf

## 2026-11-25 results

### A square-price lower bound for depth-two Fourier circuits

For an $N\times N$ matrix $M$, let $P_M(L,W)$ be the price of its repeated-label tensor on the rectangle of height $L$ and width $W$, with the equal labels on the vertical sides. The square spectral value is $\Phi(M)=2^{P_M(1,1)/2}$ because the half-perimeter is $2$. Work over the algebraic closure of the coefficient field when applying the price. Every factorization $M=QA$ over the original field still holds there. The spectral value is subadditive on sums of matrices because the repeated-label tensor is linear in $M$ and an ordinary sum is a restriction of the direct sum. [Fourier preprint, Theorem 2.1 and equation (2.2)][fourier]

For cell $j$ write $p_j=\operatorname{nnz}(Q_{*,j})$ and $q_j=\operatorname{nnz}(A_{j,*})$. The repeated-label tensor of $Q_{*,j}A_{j,*}$ is the product of two length-one wires of dimensions $p_j$ and $q_j$. Its nonzero coefficients can be absorbed into local basis maps. Thus, omitting zero summands,
$$
\Phi(M)\le \sum_j\sqrt{p_jq_j}
\le\sqrt{\operatorname{nnz}(Q)\operatorname{nnz}(A)}
\le N\sqrt{tu}.
$$
For a split character table of a group of order $N$ invertible in the field, Theorem 2.2 gives $\Phi(M)=N^{(1+\sqrt{2})/2}$. Consequently every depth-two factorization, with any number of cells and arbitrary field coefficients, has
$$
\operatorname{nnz}(Q)+\operatorname{nnz}(A)\ge 2N^{(1+\sqrt{2})/2},
\qquad tu\ge N^{\sqrt{2}-1}.
$$
These inequalities count wires or maximum endpoint degrees in synchronous depth-two circuits. [Fourier preprint, Theorem 2.2][fourier]

The same inequality gives a rigidity bound at a smaller rank. For $M=B+Z$ with $\operatorname{rank} B\le r$, write $B$ as a sum of at most $r$ rank-one matrices and $Z$ as a sum of its individual rows. Then $\Phi(B)\le rN$ and $\Phi(Z)\le\sqrt{N\lvert\operatorname{supp}Z\rvert}$. For the same character tables this gives
$$
\mathcal R_M(r)\ge \frac{\bigl(N^{(1+\sqrt2)/2}-rN\bigr)_+^2}{N}.
$$
In particular $\mathcal R_M(r)\ge N^{\sqrt2}/4$ for $r\le N^{(\sqrt2-1)/2}/2$. The estimate becomes vacuous at ranks proportional to $N$.

### Boolean zeta non-rigidity and rectangle price

Complementing the row labels of $M=U^{\otimes k}$ gives the disjointness matrix. In the deletion method of Alman, take $a=\max(0,\lfloor k/2-c_\varepsilon\sqrt{k}\rfloor)$ and keep the block on disjointness labels with both weights at least $a$. The part removed has rank at most $2\sum_{i<a}\binom{k}{i}\le\varepsilon N$ for a sufficiently large constant $c_\varepsilon$, by a binomial tail bound. In the retained block a row with label $x$ can only contain a column label $y\subseteq [k]\setminus x$ of weight at least $a$. Its support and, by symmetry, each column support have size at most $\sum_{j\le k-2a}\binom{k}{j}$. Hence for each fixed $0<\varepsilon<1$ over every field,
$$
\mathcal R_{U^{\otimes k}}(\lfloor\varepsilon N\rfloor)
\le N\,2^{O_\varepsilon(\sqrt{k}\log k)}=N^{1+o(1)}.
$$
This rules out a Valiant bound with fixed positive exponents for the Boolean zeta family. [Alman, Lemma 5.1 and Theorem 5.2][alman-rigidity]

The rectangle price of this family is strictly below the character-table price whenever $L>0$. To see this, decompose the zeta matrix by row and column weights $ak$ and $bk$ with $0\le b\le a\le1$ and set $d=a-b$. In a given block the row and column labels have at most $2^{kh(a)}$ and $2^{kh(b)}$ possible values, respectively, where $h$ denotes binary entropy in bits. Supplying the labels at the center on the two triangles costs at most $k(L+\sqrt{L^2+W^2})(h(a)+h(b))/2$. Alternatively, a common label for each supported pair costs at most $k(L+W)(h(d)+1-d)$. The latter follows by counting the three coordinate patterns $(1,1),(1,0),(0,0)$ at frequencies $b,d,1-a$. Concavity gives $h(a)+h(b)\le 2h((1-d)/2)$. There are at most $(k+1)^2$ summands, so subadditivity of the spectral value costs at most $2(L+W)\log_2(k+1)$ above the largest price. Using $P_{U^{\otimes k}}=kP_U$ and letting $k$ tend to infinity gives
$$
P_U(L,W)\le \max_{0\le d\le1}\min\left\{
 (L+\sqrt{L^2+W^2})h((1-d)/2),\ (L+W)(h(d)+1-d)
\right\} < L+\sqrt{L^2+W^2}
\quad(L>0).
$$
The first bound in the minimum attains the character-table price only at $d=0$, where the second equals $L+W$. The strict gap follows by compactness. Scaling the entries by $z^{|x|-|y|}$ through separate row and column maps and letting $z$ tend to zero leaves the identity, so closed price sublevels also give $P_U(L,W)\ge L+W$. At the square the depth-two inequality would give $tu\ge N^{P_U(1,1)-2}$ for this family. A strictly positive square-price excess above $2$ remains open here. [Fourier preprint, Theorems 2.1 and 2.2][fourier]

### Sharp worst-case query order for update bound two

For $M_{x,y}=\mathbf{1}_{y\subseteq x}$ on the $k$-cube, let $t$ be the maximum query support in any exact field-linear factorization with update support $u\le2$. Every such factorization satisfies $t\ge (3/2-o(1))N/k$, with any number of cells. There is a construction with exactly $N$ cells and $t=O(N/k)$ over every field. On the subsequence $k=2^r-1$, $r\ge3$, the construction has $t=3N/[2(k+1)]$ and attains the asymptotic constant $3/2$. By transposing and complementing both index sets, the corresponding bounds hold with $t$ and $u$ exchanged. At $u=1$ the columns of $A$ must use distinct cells since $M$ is invertible, and the all-ones query gives the exact minimum $t=N$. The dual endpoint gives $u=N$ at $t=1$.

**Lower bound.** Let $J$ be the support of the all-ones query $[k]$, so $|J|\le t$. Every column of $A$ meets $J$ and has at most one nonzero outside it. Because $A$ has column rank $N$, at least $N-|J|$ cells outside $J$ are active. Keep one distinct input representative $y$ for each such cell $\ell(y)$. Each representative has exactly one additional cell $j(y)\in J$, with $Q_{[k],j(y)}A_{j(y),y}=1$.

For query $x_i=[k]\setminus\{i\}$, the contribution from $j(y)$ alone is $Q_{x_i,j(y)}/Q_{[k],j(y)}$. For each $j\in J$, let $b_j\in\{0,1\}^k$ indicate the coordinates at which this quotient equals $1$. A coordinate where $b_{j(y)}$ differs from the true label $z_y=\mathbf{1}_{[k]\setminus y}$ requires probing $\ell(y)$. The retained external cells are distinct. In addition, each of the $|b_j|$ coordinates equal to $1$ requires probing $j$. Thus for any subset $G$ of the retained inputs, the $k$ queries have total probe count at least
$$
\sum_{j\in J}\left( |b_j| + \sum_{y\in G:\,j(y)=j} d_H(z_y,b_j)\right).
$$
Take $G$ to be the representatives with $|z_y|\ge\lambda+2$ for $\lambda=\lfloor k/2-k^{2/3}\rfloor$, so $|G|\ge N-t-o(N)$ by a binomial tail bound. If $|b_j|<\lambda$, every one of its $g$ assigned labels in $G$ has distance at least two. If $|b_j|\ge\lambda$, at most one assigned label has distance zero and at most $k+1$ have distance at most one. For all sufficiently large $k$ the contribution of this cell and its assigned external probes is at least
$$
\lambda+\max\{g-1,\,2g-k-2\}\ge
\left(1+\frac{\lambda-1}{k+1}\right)g.
$$
For the inequality, use the first term when $g\le k+1$ and the second when $g\ge k+1$. The factor on the right is at most two, so it also applies when $|b_j|<\lambda$. Summing and rearranging $kt\ge (1+(\lambda-1)/(k+1))(N-t-o(N))$ proves the bound.

**Construction.** First take $k=2^r-1$ with $r\ge3$. Let $H$ be the binary parity-check matrix with columns all the nonzero vectors of $\mathbb F_2^r$. The code $C=\ker H$ has $N/(k+1)$ codewords. Every string lies in the radius-one Hamming ball of exactly one $c\in C$, since a nonzero syndrome specifies a unique bit to flip. For each ball store its sum and each noncentral singleton. This uses exactly $N$ field cells, and each update changes at most two. To answer a query with forbidden coordinate set $S=[k]\setminus x$, take a ball sum whenever its center has no bit in $S$ and add or subtract the individual mismatches. The coefficients are in $\{0,1,-1\}$ and the center never needs a correction.

Write $d=|S|$ and let $C_i$ count centers with $i$ ones on $S$. The number of probes equals $(1+d)C_0+C_1$. To evaluate it, let $V$ be the span of the columns of $H$ outside $S$ and $h_0=\operatorname{codim}V$. The projection of $C$ to $S$ has as its image the kernel of $v\mapsto H_Sv\bmod V$, a map of rank $h_0$. Fibers of the projection therefore have equal size $|C|2^{h_0-d}$. A projected singleton is possible exactly when its column belongs to $V$. There are $d-d_0$ such columns, where $d_0=2^r-2^{r-h_0}$ counts columns outside $V$. Consequently the probe count divided by $|C|$ is $(1+2d-d_0)2^{h_0-d}$. If $h_0=0$, this expression has maximum $3/2$ at $d=1$, which occurs because removing a single column leaves a spanning set. If $h_0\ge1$, its maximum over $d\ge d_0$ is $(1+d_0)2^{h_0-d_0}$. For $r=3$ the three values are $5/8,7/16,1/2$. For $r\ge4$ they are at most $2^{2r-2^{r-1}}\le1$. This proves the exact maximum probe count. For arbitrary $k\ge7$, apply the construction on $\ell$ coordinates for the largest $\ell=2^r-1\le k$, and tensor with the raw-input scheme on the other coordinates. The result has exactly $N$ cells and $t\le 3N/[2(\ell+1)]$.

Tensoring the seven-bit construction $(u,t)=(2,24)$ with its transpose after index complementation gives $u=t=48$ on fourteen bits. Repeating that block, with a raw-input scheme on fewer than fourteen residual bits, gives
$$
\max(u,t)=O\bigl(N^{\log_2(48)/14}\bigr)=O(N^{0.39893})
$$
with exactly $N$ cells. The coordinate split gives $\max(u,t)=2^{\lceil k/2\rceil}$ with the same storage. More generally, tensoring the update-two construction on $s$ comparable coordinate blocks gives $u\le2^s$ and $t=O_s(N/k^s)$ with $N$ cells for each fixed positive integer $s$.

The unrestricted-width depth-two literature also concerns this very matrix, via the disjointness row permutation. Alman and Li give a maximum endpoint degree bound with asymptotic exponent $1/3$. Ye improves it to $O(N^{0.3199})$ using degree transfer and hole fixing and separately obtains $O(N^{1.2449})$ total wires. The degree and wire bounds optimize different objectives and allow arbitrary middle width. The $N$-cell construction above gives an explicit bound under the cell budget. The general worst-case tradeoff with $O(N)$ cells, including a matching lower bound for growing $u$, remains unresolved here. [Alman and Li, Corollary 6.3][alman-li] [Ye, Theorem 1.1 and Section 2.3][ye]

[alman-rigidity]: https://arxiv.org/abs/2102.11992
[alman-li]: https://arxiv.org/abs/2509.14489v1
[ye]: https://arxiv.org/abs/2603.15565v2
