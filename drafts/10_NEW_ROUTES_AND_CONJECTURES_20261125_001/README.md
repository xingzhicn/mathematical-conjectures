# Six applications of Euclidean tensor geometry

The user authorized a batch on six existing problems on November 25, 2026. Work began at approximately 15:27 Shanghai time. Elapsed member effort, computation time, the prior cumulative investment, and the remaining budget are unmeasured. The six entries count problems. Each linked problem page owns its mathematical results.

| Problem and record | Owner | Question under investigation |
| --- | --- | --- |
| [1. Black-box PIT](../../problems/01-black-box-pit.md) | Primary agent | Can an explicit product hitting set improve the code construction, and what benchmark should it beat? |
| [2. Four-party conversion](../../problems/02-multipartite-entanglement.md) | Primary agent | Can five source copies give two targets, or can a block protocol improve the asymptotic lower bound? |
| [3. IPS](../../problems/03-ideal-proof-system.md) | GPT-6.2 Sol, max | Does the reciprocal table remain expensive under sums across three balanced partitions? |
| [4. Rigidity and range sums](../../problems/04-rigidity-and-range-sums.md) | GPT-6.2 Sol, max | What update and query costs can a shared linear data structure attain or exclude? |
| [5. Progressions and local decoding](../../problems/05-progressions-and-local-decoding.md) | GPT-6.2 Sol, max | Which placements or transformations of the progression tensor can yield a strict price saving? |
| [6. Network coding](../../problems/06-network-coding.md) | GPT-6.2 Sol, max, after problem 3 | On a network with an established cut gap, can an intermediate-message tensor retain the needed joint constraints? |

## Results recorded at 15:40 Shanghai time

1. [Black-box PIT](../../problems/01-black-box-pit.md) gives an explicit $O(R^2N^2)$ benchmark by opposite-pair contraction. Generic product queries attain $O(RN^2)$ over an algebraically closed field. The small-characteristic hybrid reconstructs a Frobenius power of the hard source. Hardness for those powers remains open.
2. [Four-party conversion](../../problems/02-multipartite-entanglement.md) derives $\lim_{q\to\infty}R(X_q,Y_q)=1/\sqrt2$ from the cited preprint and Strassen duality. A separate constructive protocol attains a lower bound tending to $1/2$. Two restricted approaches to five-to-two conversion were excluded. The general five-copy test remains open.
3. [IPS](../../problems/03-ideal-proof-system.md) proves an $\Omega(2^n)$ total rank bound for the three balanced partitions of a forced rational reciprocal table. An independent read-only review checked the prime-counting, specialization and gradient-ideal steps. General circuit-size lower bounds remain open.
4. [Rigidity and range sums](../../problems/04-rigidity-and-range-sums.md) gives a square-price depth-two bound for character tables and a sharp leading constant for Boolean dominance queries with update support at most two on Hamming lengths. An independent read-only review checked both bounds and the finite controls. The tradeoff at growing update support remains open.
5. [Progressions and local decoding](../../problems/05-progressions-and-local-decoding.md) proves a shared-label network obstruction at every placement, gives direct reflection lower bounds at specified placements, and derives disjoint parity recovery sets from adaptive binary linear decoding. The progression and code-length targets remain open.
6. [Network coding](../../problems/06-network-coding.md) derives a known acyclic index-coding bound by contracting the actual decoder tensors, and exhibits two encoders with identical pair marginals and different recovery behavior. A geometric treatment of multiple intermediate messages giving a non-Shannon bound remains open.

The primary agent checked the statements of the curvature theorem and Strassen's spectral theorem used in problem 2. Its rate proof has not received independent review. The [exact finite checks](check_pit_and_swap.py) reproduce matrix-query controls and the routed four-party maps. Each page gives the mathematical scope and sources. Literature comparisons are selective.
