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

**Open target.** Determine the exact rate for this pair, or match the leading $q\to\infty$ upper bound with explicit grouped local maps. A further comparison would determine what established spectral functionals already certify on the pair.

For the three-party EPR triangle, the logarithmic GHZ cost per unit wire dimension in the asymptotic tensor-rank model is $9/4$ under the cited matrix multiplication theorem. The distinct four-party rates above remain to be determined. [Matrix multiplication preprint][mm]

[mm]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf
