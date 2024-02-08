# Python-Hydrogen-Wave-Function

Here I calculate and plot different electron probability density distributions for the Hydrogen Wave Function. The code is in Python, and only Numpy and Sympy are used to have better insight into different Legendre and Laguerre polynomials.

The wave function for a hydrogen atom is given by:

$$
\Psi_{nlm}(r, \theta, \phi) = R_{nl}(r) \cdot Y_{lm}(\theta, \phi)
$$
<p align="left">t $$\Psi_{nlm}(r, \theta, \phi) = R_{nl}(r) \cdot Y_{lm}(\theta, \phi)$$> </p>

Where:
- **Ψ<sub>nlm</sub>(r, θ, φ)** is the wave function of the hydrogen atom,
- **R<sub>nl</sub>(r)** is the radial component that depends on the principal quantum number \(n\) and the angular momentum quantum number \(l\),
- **Y<sub>lm</sub>(θ, φ)** is the spherical harmonic function that depends on the magnetic quantum number \(m\) and the angular coordinates θ (theta) and φ (phi).

The wave function of the hydrogen atom in polar coordinates (r, θ, φ) is given by:

$$
\Psi_{n,\ell,m}(r,\theta,\phi) = R_{n,\ell}(r) \cdot Y_{\ell}^{m}(\theta,\phi)
$$

Where:

- \( \Psi_{n,\ell,m}(r,\theta,\phi) \) is the wave function of the electron.
- \( R_{n,\ell}(r) \) is the radial component that depends only on the distance from the nucleus, \( r \).
- \( Y_{\ell}^{m}(\theta,\phi) \) are the spherical harmonics which account for the angular part of the wave function and depend on the angles \( \theta \) and \( \phi \).
- \( n \) is the principal quantum number.
- \( \ell \) is the azimuthal quantum number (or angular momentum quantum number).
- \( m \) is the magnetic quantum number.

Each of these components plays a crucial role in describing the state of an electron in a hydrogen atom.

**Radial Component \( R_{n,\ell}(r) \)**

This part of the wave function describes how the amplitude of the wave function changes with distance from the nucleus. It involves the Laguerre polynomials and the effective nuclear charge.

**Spherical Harmonics \( Y_{\ell}^{m}(\theta,\phi) \)**

The spherical harmonics describe the angular part of the wave function, which determines the shape of the electron's orbit around the nucleus. They depend on the azimuthal and magnetic quantum numbers, \( \ell \) and \( m \), which describe the electron's angular momentum.


The wave function of the hydrogen atom in polar coordinates (r, θ, φ) is given by:

**Ψ<sub>nlm</sub>(r, θ, φ)** = R<sub>nl</sub>(r) · Y<sub>l<sup>m</sup></sub>(θ, φ)

Where:

- **Ψ<sub>nlm</sub>(r, θ, φ)** is the wave function of the electron.
- **R<sub>nl</sub>(r)** is the radial component that depends only on the distance from the nucleus, r.
- **Y<sub>l<sup>m</sup></sub>(θ, φ)** are the spherical harmonics which account for the angular part of the wave function and depend on the angles θ (theta) and φ (phi).
- **n** is the principal quantum number.
- **l** is the azimuthal quantum number (or angular momentum quantum number).
- **m** is the magnetic quantum number.

Each of these components plays a crucial role in describing the state of an electron in a hydrogen atom.

## Radial Component R<sub>nl</sub>(r)

This part of the wave function describes how the amplitude of the wave function changes with distance from the nucleus. It involves the Laguerre polynomials and the effective nuclear charge.

## Spherical Harmonics Y<sub>l<sup>m</sup></sub>(θ, φ)

The spherical harmonics describe the angular part of the wav
