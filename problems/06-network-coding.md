# Multi-source network coding

Fix a directed acyclic network with finite link alphabets and independent sources. Each source has a prescribed set of receivers. In the zero-error model a code must implement every demanded recovery on every input. The target is an explicit capacity upper bound that separates a proposed rate vector from the ordinary cut-bound region. A vanishing-error capacity result additionally requires control of approximation in its communication model.

A deterministic causal code can be represented by local maps on a product of independent equality wires. Given the source inputs, the schedule determines a unique assignment to internal messages. For multicast, each independent source contributes a shared-label tensor on its sender and receivers. With link alphabet dimensions $r_e$ and source alphabet dimensions $q_i$, geometry yields
$$
\sum_i W(S_i)\log_2 q_i
\le \sum_e \ell_e\log_2 r_e,
$$
where $\ell_e$ is the Euclidean link length. Integrating the ordinary cut inequalities over hyperplanes gives exactly this expression. Each link contributes its projected separation measure, and each source contributes the measure of hyperplanes splitting its terminal set. [Hyperplane cut representation][geometry]

**Open target for this method.** Identify a source or coding resource representation that retains joint constraints lost by independent shared-label accounting. Prove a link from an actual code to that representation and exhibit a rate vector satisfying all ordinary cuts but excluded by the new price inequality. A network with a known non-Shannon bound gives a concrete comparison case. [Dougherty–Freiling–Zeger](https://doi.org/10.1109/TIT.2006.880997)

[geometry]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/build/intro.tex

### A bottleneck with one-way side information

Take sources $s_X,s_Y$, relays $u,v$, and receivers $r_X,r_Y$ demanding $X,Y$, respectively. Give each of the six arcs
$$
s_X\to u,\qquad s_Y\to u,\qquad u\to v,\qquad
v\to r_X,\qquad v\to r_Y,\qquad s_Y\to r_X
$$
unit capacity. The ordinary directed cut region is $[0,1]^2$. For a cut crossed by one demand in the outgoing direction, a path for that demand supplies a crossing arc. If both demands cross in that direction, $s_Y\to r_X$ and a crossing arc on the path $s_X\to u\to v\to r_X$ give two distinct arcs. The cut leaving $\{s_X\}$ bounds the first rate by one, and the cut leaving all vertices except $r_Y$ bounds the second rate by one. Adding the directed inequalities for a cut and its complement also gives the undirected split inequalities used in the hyperplane integration.

Let $\mathcal X,\mathcal Y$ be the source alphabets, let $\mathcal Z$ be the alphabet of $u\to v$, and let $g:\mathcal X\times\mathcal Y\to\mathcal Z$ be the message function on that arc for an actual deterministic code. Since $v$ sees only the message $Z=g(X,Y)$, the two recoveries can be written as $\beta(Z)=Y$ and $\alpha(Z,Y)=X$. The map $\alpha$ includes the side arc's local function of $Y$ and the relay's outgoing message to $r_X$. Define a graph tensor and a decoder matrix by
$$
G_{(x,y),z}=\mathbf 1\{g(x,y)=z\},
\qquad
D_{z,(a,b)}=\mathbf 1\{\beta(z)=b,\ \alpha(z,b)=a\}.
$$
In a zero-error code their contraction is $GD=I_{\mathcal X\times\mathcal Y}$. The unique $z=g(x,y)$ sets $b=y$ before the second decoder sets $a=x$. Hence $\lvert\mathcal Z\rvert\ge\lvert\mathcal X\rvert\lvert\mathcal Y\rvert$ by rank over any coefficient field. The use of indicator tensors accommodates arbitrary deterministic local functions, including nonlinear ones.

On $N$ uses the bottleneck has at most $2^N$ transcripts, so the rate region satisfies $R_X+R_Y\le 1$. Forwarding the concatenation of the two source words attains this sum-rate region, including by linear binary block codes. For independent uniform messages with individual average error probabilities $\epsilon_X,\epsilon_Y$, the composed decoder succeeds on the pair with probability at least $1-\epsilon_X-\epsilon_Y$. At most one source pair can be recovered correctly for each possible $z$, which gives
$$
\lvert\mathcal Z\rvert\ \ge\
(1-\epsilon_X-\epsilon_Y)\lvert\mathcal X\rvert\lvert\mathcal Y\rvert.
$$
The same counting bound holds for randomized codes by fixing their exogenous random seeds and averaging. Thus the vanishing-error region is also $R_X+R_Y\le 1$ with nonnegative rates. The ordinary cut point $(1,1)$ has a two-to-one gap in sum rate.

The contraction realizes the acyclic induced subgraph bound from index coding. For a common bottleneck and an acyclic set of receivers, fix sources outside that set and decode in an order in which each required side message has already been recovered. The resulting decoder factors the identity on the product alphabet through $\mathcal Z$. The remaining comparison with the Dougherty–Freiling–Zeger bound requires retaining dependencies among several intermediate messages. [Bar-Yossef, Birk, Jayram and Kol](https://doi.org/10.1109/TIT.2010.2103753)

### Two-variable projections can lose a recovery constraint

Take three independent uniform bits $X,Y,W$. A relay receiving all three can send either $Z=X\oplus Y$ or $Z=X\oplus W$. For both encoders, every two-variable marginal among $X,Y,W,Z$ is uniform on four outcomes. In the first case $H(X\mid Y,Z)=0$. In the second case $(X,Y,Z)$ is uniform and $H(X\mid Y,Z)=1$. Equivalently, sum the encoder graph tensor over $W$ and flatten it as rows $(y,z)$ and columns $x$. In the first case every row is twice one of the two coordinate vectors and both vectors occur, giving rank two over $\mathbb Q$. In the second case every row is $(1,1)$, giving rank one. Both maps are linear over $\mathbb F_2$.
