# setup.py
from setuptools import setup, find_packages

setup(
    name="test_forestry",
    version="0.1.1",
    description="",
    author="Evgenii Kuriabov",
    author_email="evgenii@example.com",
    url="https://github.com/ZhKuriabov/test_rforestry",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-learn",
        "pandas",
        # добавь другие зависимости, если нужно
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
