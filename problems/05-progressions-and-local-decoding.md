# Four-term arithmetic progressions and three-query local decoding

## Four-term progressions in $\mathbb F_5^n$

The target is an exponential saving $|A|\le(5-\varepsilon)^n$ for some absolute $\varepsilon>0$ whenever $A\subseteq\mathbb F_5^n$ contains no nonconstant four-term arithmetic progression. Consider the tensor
$$
T=\sum_{a,b\in\mathbb F_5} e_a\otimes e_{a+b}\otimes e_{a+2b}\otimes e_{a+3b}.
$$
Every balanced flattening is a $25\times25$ permutation matrix since any two distinct positions determine $a,b$. Every one-site flattening has rank $5$. Restricting all four sites of the grouped power $T^{\otimes n}$ to $A$ leaves exactly the diagonal tensor of size $|A|$.

**Sufficient geometric inequality.** Over a specified coefficient field, find a placement $S$ of positive width and an admissible Euclidean price for which $H(T;S)<W(S)\log_2 5$. By additivity and local monotonicity this implies $|A|\le 2^{nH(T;S)/W(S)}$, which gives the desired exponential saving. A strict price upper bound is the missing mathematical step. The progression coordinates lie in $\mathbb F_5$, and the field of tensor coefficients may be chosen separately. [Euclidean price theorem][geometry]

Fix any one progression coordinate to zero by a local coordinate covector. The remaining three coordinates are distinct nonzero multiples of the free difference $b$ in $\mathbb F_5$, so separate permutations of their bases identify the slice with a three-party diagonal of size five. This works in every coefficient field. For sites $x_1,\ldots,x_4$ and $S=\{x_1,\ldots,x_4\}$, monotonicity gives
$$
H(T;S)\ \ge\ \max_i W(\{x_j:j\ne i\})\log_2 5.
$$
Thus the proposed strict saving requires each of the four sites to lie outside the convex hull of the other three. In particular every collinear placement fails this test. Convex quadrilaterals and tetrahedra survive this necessary condition. Obtaining a strict upper bound there remains open.

## Three-query local decoding

Specify a fixed alphabet, message length $k$, constant tolerated corruption fraction $\delta>0$, and constant success advantage over random guessing. The target is a superpolynomial lower bound on codeword length $N$ for three-query locally decodable codes in the stated model. Binary linear codes form a precise initial class.

A tensor approach needs a map from the actual decoding constraints to a target and resource pair with controlled prices. The map must preserve which coordinate queries reconstruct which message bit, the decoder's success guarantee under adversarial corruption, and the parameters $k,N,\delta$. The progression tensor above supplies no such mapping. [Katz–Trevisan](https://doi.org/10.1145/335305.335315)

[geometry]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/paper.pdf
