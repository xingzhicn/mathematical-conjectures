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

A specific test is the Boolean-cube dominance incidence matrix $U^{\otimes k}$, with $U=\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)$. Establish a lower bound on $t$ when the number of rows of $A$ is $O(2^k)$. The missing link is an inequality that charges shared preprocessing in the actual factorization. A decomposition into low rank plus sparse error requires an additional argument, and a result for this matrix and model has its own scope.

[fourier]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-logarithmic-exponent-of-finite-Fourier-transforms-November-24-2026/paper.pdf
