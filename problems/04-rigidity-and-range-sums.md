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
