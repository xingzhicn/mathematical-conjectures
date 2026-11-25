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
