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

## Progression tensor bounds from contraction and slice rank

For any two distinct sites $x_c,x_d$, let $L$ be their affine line and let $x_a,x_b$ be the remaining sites. Every isometry-invariant Euclidean price from Theorem 1.1 satisfies
$$
H(T;S)\ge \bigl(\operatorname{dist}(x_a,L)+\operatorname{dist}(x_b,L)\bigr)\log_2 5.
$$
Reflect a second copy of the placement through $L$, fixing $L$ pointwise and negating its orthogonal directions. Contract the two copies at both of the fixed sites using the coordinate pairings. The balanced flattening of $T$ is a permutation matrix, so agreeing at $c,d$ forces agreement at $a,b$. The output is the product of two independent size-five wires, each joining one remaining site to its reflected copy. The price of the input is $2H(T;S)$ and the price of the output gives the bound. This argument works over every coefficient field. [Euclidean price theorem][geometry]

For a rectangle with sides $a\ge b>0$, choose $L$ through a short side. Then $H(T;S)\ge 2a\log_2 5\ge W(S)\log_2 5$, since $W(S)=a+b$. A tetrahedron can also fail the strict price test. For the sites $(0,0,0),(0,1,0),(3,0,0),(3,1,1)$, the line through the first two sites gives a lower bound of $(3+\sqrt{10})\log_2 5$. Its hull is contained in the Minkowski sum of the $3$ by $1$ rectangle and a unit vertical segment, so $W(S)\le 5$.

The slice rank of $T^{\otimes n}$ is exactly $q=5^n$ over every coefficient field. If a decomposition uses $r_i$ slices at party $i$ with $\sum_i r_i<q$, let $U_i$ be the common annihilator of the one-party vectors in those slices. The tensor vanishes on $U_1\otimes U_2\otimes U_3\otimes U_4$. The $12\mid34$ flattening is a nondegenerate pairing, so
$$
q^2\ge \dim(U_1\otimes U_2)+\dim(U_3\otimes U_4)
\ge 2q^2-q\sum_i r_i+r_1r_2+r_3r_4>q^2,
$$
a contradiction. Slicing along any single party gives the upper bound $q$.

## Obstruction for sums of shared-label networks

Fix four sites $S$ of positive width $W=W(S)$ and diameter $D$. A summand in this construction is obtained by tensoring shared-label tensors $\Delta_{S_e}(d_e)$, with arbitrary auxiliary sites, then contracting and applying local maps at all the sites. Its supplied price is $C=\sum_e W(S_e)\log_2 d_e$. Two-site wires are included. For every $n\ge 1$, if a sum of such networks with supplied prices $C_1,\ldots,C_m$ equals $T^{\otimes n}$, then
$$
W\log_2\left(\sum_{j=1}^m 2^{C_j/W}\right)\ge W n\log_2 5.
$$
Thus the ordinary-sum price bound of the Euclidean price theorem cannot give a strict saving via this construction at a convex quadrilateral or tetrahedron. The statement holds over every coefficient field and for every placement. [Euclidean price theorem, Eq. (2.3)][geometry]

**Choose one balanced cut.** Let $m_1\le m_2\le m_3$ be the distance sums of the three pairings of the four terminals. On a line with sorted projections $y_1\le y_2\le y_3\le y_4$, the projected sums are $R-g,R+g,R+g$, where $R=y_4-y_1$ and $g=y_3-y_2$. The sum for any two distinct pairings is at least $2R$. Average over projections using the normalization that the mean projected length of a segment equals its length. It follows that $m_1+m_2\ge 2W$ and hence $m_2\ge W$. Take the balanced cut $B$ with the pairs realizing $m_1$ on its two sides. The cheaper cross-cut pairing costs $m_2$.

**Bound the rank a network can carry across this cut.** Write $w=\log_2 q$ for the logarithm of the common output dimension $q=5^n$, and let $R_B>0$ be the summand's flattening rank across $B$. Regard each shared label as a hyperedge with capacity $\log_2 d_e$ and attach the four output terminals by edges of capacity $w$ at zero distance. For any cut separating the two left output terminals from the two right output terminals, the rank is bounded above by the product of the crossing label dimensions. Fixing each crossing label expresses the summand as a sum of at most that many separable terms across the cut.

To apply max flow, replace each hyperedge by an arc of its capacity, add arcs from each incident vertex to its tail and from its head to each incident vertex, and give these added arcs capacity larger than $\sum_e\log_2 d_e+4w$. At fixed incident sides, a minimum cut through the gadget charges the hyperedge capacity once if its incident vertices occupy both sides and zero otherwise. Connect a common source to the two left output terminals and the two right output terminals to a common sink with the same large capacities. The cut-rank bound gives a flow of value $\log_2 R_B$. Decompose it into paths. A path through a hyperedge from one incident site to another travels a distance at most $\operatorname{diam}(S_e)\le W(S_e)$. The capacity bound and the triangle inequality thus give a total endpoint transportation cost at most $C$.

At most $w$ units leave or reach each terminal. Complete the path flow to $w$ units per terminal by adding $2w-\log_2 R_B$ units of direct transportation, at cost at most $D(2w-\log_2 R_B)$. Any full $2$ by $2$ transportation with these margins is a mixture of the two cross-cut pairings and costs at least $w m_2$. Consequently
$$
C\ge w m_2-D(2w-\log_2 R_B).
$$

**Return to the full progression tensor.** If $P=W\log_2(\sum_j 2^{C_j/W})$, rank subadditivity and the previous inequality bound the sum's rank across $B$ by
$$
q^2 2^{-w m_2/D}\sum_j 2^{C_j/D}\le q^2 2^{(P-wm_2)/D}.
$$
The last step uses $D\le W$, so the $\ell^{W/D}$ norm of $(2^{C_j/W})_j$ is at most its $\ell^1$ norm. The progression tensor has rank $q^2$ across $B$, giving the stronger bound $P\ge wm_2$. Any uniform price bound $P\le P_0<wm_2$ in the same local format forces rank strictly below $q^2$ and therefore also excludes the tensor from the Zariski closure by the determinantal equations. The obstruction concerns supplied prices for these constructions. A comparison with a common catalyst on both sides can subtract its price and requires a separate rank or price argument. The existence of a strict price saving in the remaining placements is open.

## Recovery matchings for binary linear codes

Let $C(x)_j=\langle g_j,x\rangle$ for $x\in\mathbb F_2^k$ and columns $g_j\in\mathbb F_2^k$. For each target bit $i$, take the recovery hypergraph on $[N]$ whose edges are the nonempty sets $J$ with $|J|\le 3$ and $\sum_{j\in J} g_j=e_i$. Suppose a randomized decoder, possibly adaptive, succeeds with probability at least $1/2+\eta$ on every message and received word within $t=\lfloor\delta N\rfloor$ errors, using at most three queries. Then each recovery hypergraph has a vertex-disjoint matching of size at least $\lceil(t+1)/3\rceil$.

Indeed, if a set $E$ of size at most $t$ hit all the recovery edges for bit $i$, use a uniform random message and replace the coordinates of $E$ by independent uniform bits. Fix the decoder's random seed and a possible query transcript. The transcript specifies values on its fixed path. At most three uncorrupted columns occur on that path and their span omits $e_i$. Conditional on the observed uncorrupted values, $x_i$ is uniform. The independent replaced values leave this conditional law unchanged, so the decoder succeeds with probability $1/2$ after averaging. A maximal matching therefore uses more than $t$ vertices, proving the bound. Conversely, if matchings of size at least $\alpha N$ exist for all bits, uniformly choosing a matching edge and taking the XOR decodes against $\delta'N$ corruptions with success at least $1-\delta'/\alpha$.

One can record the individual recoveries in a four-party tensor with the target bit on the first leg and the ordered query coordinates on the other three legs. Short edges can use distinct dummy labels carrying zero when needed within each matching, with at most $2N$ such labels reused across the bits. Then fixing a bit gives a diagonal slice of the size of its matching, up to separate relabelings in the three query slots. The span equations are external data attached to the query labels. They ensure every encoded edge recovers its labeled target, and the vertex disjointness gives the corruption guarantee above. The target-versus-queries flattening has rank $k$, since the support of each target row is nonempty and no query triple can recover two distinct bits by XOR.

The full parity recovery relation can have several completions for a pair of fixed queries. For example, for the binary linear code indexed by $v\in\mathbb F_2^3$ with generator columns $g_v=v$, the common ordered queries $0,e_3$ complete with $e_i+e_3$ for distinct targets $i=1,2$. The ordering of the ground set can place $0,e_3$ first. Four-term progression support has unique completion from any two slots. This rules out a coordinatewise injective embedding of the full parity recovery relation in the progression support. A useful comparison for arbitrary recovery matchings must still connect their geometry to both $k$ and $N$ with enough gain to prove a superpolynomial bound.

[geometry]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/paper.pdf
