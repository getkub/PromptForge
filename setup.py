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
        "requests",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "llm-interface=llm_interface.web_app:main",
        ],
    },
) 