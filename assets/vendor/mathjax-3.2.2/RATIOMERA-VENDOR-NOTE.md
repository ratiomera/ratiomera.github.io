# MathJax 3.2.2

Ratiomera vendors the official `mathjax@3.2.2` npm distribution so mathematical
notation remains available without a third-party runtime request.

- Package: `mathjax`
- Version: `3.2.2`
- npm tarball integrity: `sha512-Bt+SSVU8eBG27zChVewOicYs7Xsdt40qm4+UpHyX7k0/O9NliPc+x77k1/FEsPsjKPZGJvtRZM1vO+geW0OhGw==`
- Runtime: CommonHTML (`es5/tex-chtml-full.js`)
- Runtime SHA-256: `91b005503c5d1f0958bf4d73ada1a3be33596b2c4ab5da22277f1b0d3149b5a4`
- Licence: Apache License 2.0, retained in `LICENSE`
- Licence SHA-256: `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`
- Source: <https://www.npmjs.com/package/mathjax/v/3.2.2>

The complete `es5` directory is retained because MathJax may load fonts,
accessibility modules, or TeX extensions relative to its entry point. Do not
prune individual files without an offline formula and accessibility audit.
