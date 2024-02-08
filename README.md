# Python-Hydrogen-Wave-Function

Here I calculate and plot different electron probability density distributions for the Hydrogen Wave Function. The code is in Python, and only Numpy and Sympy are used to have better insight into different Legendre and Laguerre polynomials.

The wave function for a hydrogen atom is given by:

$$
\Psi_{nlm}(r, \theta, \phi) = R_{nl}(r) \cdot Y_{lm}(\theta, \phi)
$$

Where:
- **Ψ<sub>nlm</sub>(r, θ, φ)** is the wave function of the hydrogen atom,
- **R<sub>nl</sub>(r)** is the radial component that depends on the principal quantum number \(n\) and the angular momentum quantum number \(l\),
- **Y<sub>lm</sub>(θ, φ)** is the spherical harmonic function that depends on the magnetic quantum number \(m\) and the angular coordinates θ (theta) and φ (phi).

This approach utilizes Markdown's support for HTML-like tags (e.g., `<sub>` for subscripts) in plain text descriptions to maintain a clean and readable format. While this doesn't directly solve the issue of centering LaTeX rendered text, it provides a clear, accessible way to describe the components of the hydrogen atom's wave function without relying solely on LaTeX formatting, which can be unpredictable in GitHub's Markdown renderer.
