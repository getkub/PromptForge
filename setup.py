from setuptools import setup, find_packages

setup(
    name="llm_interface",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "jinja2",
        "pyyaml",
    ],
    python_requires=">=3.8",
) 