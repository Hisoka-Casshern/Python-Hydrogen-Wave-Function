# Python-Hydrogen-Wave-Function
Here I calcluate and plot different electron probability density distributions for Hydrogen Wave Function. Code is in Python and only Numpy and Sympy are used to have better insight into different Legendre and Lagurre polynomials.<br />

The wave function for a hydrogen atom is given by:

$$
\Psi_{nlm}(r, \theta, \phi) = R_{nl}(r) \cdot Y_{lm}(\theta, \phi)
$$
<br />
where:
**The Cauchy-Schwarz Inequality**
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$
\Psi_{nlm}(r, \theta, \phi)

- \( \Psi_{nlm}(r, \theta, \phi) \) is the wave function of the hydrogen atom,
- \( R_{nl}(r) \) is the radial component that depends on the principal quantum number \(n\) and the angular momentum quantum number \(l\),
- \( Y_{lm}(\theta, \phi) \) is the spherical harmonic function that depends on the magnetic quantum number \(m\) and the angular coordinates \(\theta\) (theta) and \(\phi\) (phi).
$$
