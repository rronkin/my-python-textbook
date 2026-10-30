# The Python Architecture: Why It Works So Elegantly

**A free online book on how Python really works: the data model, dunder methods, protocols, descriptors and CPython internals, explained for engineers coming from MATLAB, C and DSP.**

**[Read it online](https://rronkin.github.io/my-python-textbook/)** · **[Download the PDF](https://rronkin.github.io/my-python-textbook/the-python-architecture.pdf)**

Python's elegance comes from one design decision: the syntax is fixed, but what the syntax *does* is decided by your objects. This book starts from that idea and follows it down to the C structs in CPython and up to a working signal-processing block.

## Questions it answers

- How does `self` get filled in, when Python has no special machinery for methods?
- What is a descriptor, and how do `property`, `classmethod` and `staticmethod` use them?
- Why does `3 * Gain(2)` work, when `int` was written decades before your class?
- Why does giving one object its own `__len__` do nothing?
- Why can two small methods make `for`, `in`, `reversed`, `sorted` and `max` all work on your class?
- Why does `x * my_object` sometimes return a slow NumPy array of dtype `object`, and how do you stop it?
- How do you build a MATLAB System object in Python, with nontunable properties and `setupImpl`/`stepImpl`?
- Is Python fast enough compared with MATLAB, and when do you need Numba, CuPy, Cython or pybind11?

## Who it's for

Engineers who can already write Python, or who are moving to it from MATLAB, C, C++ or Java, and want to understand why it behaves as it does. The examples come from DSP and GNSS work, such as filters, delay lines and streaming large recordings, but the Python applies to any field.

## What's inside

1. [The Core Philosophy: Fixed Syntax, Pluggable Behavior](https://rronkin.github.io/my-python-textbook/#1-the-core-philosophy-fixed-syntax-pluggable-behavior): dunder methods and protocols
2. [Under the Hood: The C-Struct Architecture](https://rronkin.github.io/my-python-textbook/#2-under-the-hood-the-c-struct-architecture): `PyObject`, reference counting and garbage collection
3. [The Grand Unification: Two Pillars and a Keystone](https://rronkin.github.io/my-python-textbook/#3-the-grand-unification-two-pillars-and-a-keystone): descriptors, bound methods and namespaces
4. [Deep Dive: First-Class Objects](https://rronkin.github.io/my-python-textbook/#4-deep-dive-first-class-objects): closures, and Python compared with C, C++ and Java
5. [Conceptual Paradigm: Python as a Plugin Architecture](https://rronkin.github.io/my-python-textbook/#5-conceptual-paradigm-python-as-a-plugin-architecture): duck typing and abstract base classes
6. [The Data Model, Protocols and Dunder Methods](https://rronkin.github.io/my-python-textbook/#6-the-data-model-protocols-and-dunder-methods): operator dispatch, context managers and `__array_ufunc__`
7. [Python as an ICD: The Client/Supplier Dynamic](https://rronkin.github.io/my-python-textbook/#7-python-as-an-icd-the-clientsupplier-dynamic): the data model as an interface contract
8. [The Golden Rule of Dunders](https://rronkin.github.io/my-python-textbook/#8-the-golden-rule-of-dunders): when to call them directly, and when not to
9. [Practical Synthesis: The MATLAB System Object in Python](https://rronkin.github.io/my-python-textbook/#9-practical-synthesis-the-matlab-system-object-in-python): a full worked example with a delay line
10. [IDE Integration and Essential Protocols: The Cheat Sheet](https://rronkin.github.io/my-python-textbook/#10-ide-integration-and-essential-protocols-the-cheat-sheet): type hints, generators and `__slots__`
11. [Performance Reality: Python vs. MATLAB](https://rronkin.github.io/my-python-textbook/#11-performance-reality-python-vs-matlab): NumPy overhead, Numba, CuPy and GPU code
12. [Epilogue: Why "Data Model"?](https://rronkin.github.io/my-python-textbook/#12-epilogue-why-data-model)

## Building it yourself

The book is one Markdown file, [`The Python Architecture Why It Works So Elegantly.md`](The%20Python%20Architecture%20Why%20It%20Works%20So%20Elegantly.md). [`build.py`](build.py) turns it into the website and PDF in `_site/`, and every push to `main` deploys them to GitHub Pages.

PDF generation needs [WeasyPrint's system dependencies](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation). With those installed, using Python 3.12:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows (Git Bash): source .venv/Scripts/activate
pip install -r requirements.txt
python build.py
```
