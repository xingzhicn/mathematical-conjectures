# Mathematical Conjectures

A research agenda for applying Euclidean spectral prices to polynomial identity testing, multipartite entanglement, proof complexity, matrix rigidity, additive combinatorics, coding theory, and network information theory.

The cited preprints provide mathematical inputs for this agenda. Each problem page states which steps follow from those inputs and identifies the additional claim required to reach the target. The research notes make no priority claim for the proposed applications.

The [November 25 research batch](drafts/10_NEW_ROUTES_AND_CONJECTURES_20261125_001/README.md) investigated all six problems. Under the cited tensor curvature and Euclidean price theorems, the four-party exact conversion rate tends to $1/\sqrt2$ as the local dimension grows. The batch also derives a mixed-partition rank lower bound for a reciprocal IPS table and a sharp query bound for Boolean dominance when each update touches at most two cells.

| Problem | Concrete target |
| --- | --- |
| [Black-box polynomial identity testing](problems/01-black-box-pit.md) | Extend the Hamiltonian-cycle hardness transfer to polynomial-degree circuits in small characteristic. |
| [Multipartite entanglement](problems/02-multipartite-entanglement.md) | Determine the finite-dimensional rate for an explicit four-party transposition and construct maps attaining the large-dimension limit. |
| [Ideal Proof System](problems/03-ideal-proof-system.md) | Lower-bound the smallest certificate in a specified affine family of refutations. |
| [Matrix rigidity and range sums](problems/04-rigidity-and-range-sums.md) | Obtain a rank–sparsity tradeoff for an explicit matrix and justify its data structure consequences. |
| [Four-term progressions and local decoding](problems/05-progressions-and-local-decoding.md) | Test a four-site price inequality relevant to progression-free sets and identify a separate encoding for local decoding. |
| [Multi-source network coding](problems/06-network-coding.md) | Derive a capacity constraint that improves on cut bounds for an explicit instance. |

For a finite set of sites $S$ with positive diameter, the Euclidean price has the form $H(T)=W(S)\log_2 F_S(T)$, where $W$ is normalized mean width and $F_S$ is a spectral point. Local restrictions decrease price, tensor products add prices, and the logarithmic cost of combining $L$ summands at the same sites is at most $W(S)\log_2 L$ above the largest summand price. Applications that use coefficientwise limits must invoke the corresponding closed-sublevel result. [Euclidean tensor geometry preprint][geometry]

The PIT page contains both the general hardness-to-randomness route and a separate direct geometric hitting-set construction for a restricted class. A longer proof of the four-party example is available separately. [Four-party proof][fourparty]

[geometry]: https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/paper.pdf
[fourparty]: https://github.com/xingzhicn/four-party-tensor-conversion
