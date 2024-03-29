import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lithium_enrichment_cost_calculator",
    version="develop",
    author="The lithium_enrichment_cost_calculator Development Team",
    author_email="mail@jshimwell.com",
    description="Create 3D fusion reactor CAD models based on input parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fusion-energy/lithium_enrichment_cost_calculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["numpy"],
)
