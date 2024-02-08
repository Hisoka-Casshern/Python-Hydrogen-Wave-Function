# Python-Hydrogen-Wave-Function

Here I calculate and plot different electron probability density distributions for the Hydrogen Wave Function. The code is in Python, and only Numpy and Sympy are used to have better insight into different Legendre and Laguerre polynomials.

The wave function for a Hydrogen atom is given by:
<p>
$$
\Large \mathbf{\Psi_{nlm}(r, \theta, \phi)} = \mathbf{R_{nl}(r)} \cdot \mathbf{Y_{lm}(\theta, \phi)}
$$
</p>

Where:
- Ψ<sub>nlm</sub>(r, θ, φ) is the wave function of the hydrogen atom,
- R<sub>nl</sub>(r) is the radial component that depends on the principal quantum number \(n\) and the angular momentum quantum number \(l\),
- Y<sub>lm</sub>(θ, φ) is the spherical harmonic function that depends on the magnetic quantum number \(m\) and the angular coordinates θ (theta) and φ (phi).

<br />
The probability density is defined as:
<p>
$$
\large \mathbf{\rho} = |\mathbf{\Psi}|^2
$$
</p>

<br />
The full Normalized Radial Component of the Hydrogen Wave Function is given by :

<p>
$$
 \Large R_{nl}(r)= \sqrt{\left(\frac{2}{na_0}\right)^3 \frac{(n-l-1)!}{2n(n+l)!}} \cdot e^{-\frac{r}{na_0}} \cdot \left(\frac{2r}{na_0}\right)^l \cdot L_{n-l-1}^{2l+1}\left(\frac{2r}{na_0}\right) 
$$
</p>
where:
<br />
- n is the principal quantum number,
<br />
- l is the angular momentum quantum number,
<br />
- r is the radial distance,
<br />
- L<sub>(n-l-1)</sub><sup>(2l+1)</sup>(x) represents the associated Laguerre polynomial of degree (n-l-1) and order (2l+1) evaluated at the raidus
<br />
- The other terms involve normalization and exponential decay

<br />
The full Normalized Angular Component of the Hydrogen Wave Function is given by :

<p>
$$
Y_{lm}(\theta, \phi) = \sqrt{\frac{(2l+1)}{4\pi} \frac{(l-m)!}{(l+m)!}} P_{l}^{m}(\cos(\theta)) e^{im\phi}
$$
</p>
where:
<br />
- n is the principal quantum number,
<br />
- l is the angular momentum quantum number,
<br />
- r is the radial distance,
<br />
- L<sub>(n-l-1)</sub><sup>(2l+1)</sup>(x) represents the associated Laguerre polynomial of degree (n-l-1) and order (2l+1) evaluated at the raidus
<br />
- The other terms involve normalization and exponential decay


