import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ml_project",
    author="Denis Shibitov",
    author_email="ttwtest1@gmail.com",
    description="MADE MLOps homework 1",
    keywords="mlops, homework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/made-mlops-2022/denis_shibitov",
    # package_dir={"": "ml_project"},
    packages=['ml_project'],
    version="0.1.1",
    classifiers=[
        "Development Status :: early start",
        "Natural Language :: English",
        "Programming Language :: Python",
    ],
    python_requires=">=3.7",
    install_requires=[
        "matplotlib",
        "pandas",
        "numpy",
        "scikit-learn",
        "pandas",
        # "dvc[s3]",
        "marshmallow_dataclass",
        # "mlflow",
    ],
    extras_require={
        # "dev": [
        #     "wemake-python-styleguide",
        #     "mypy",
        #     "black",
        #     "jupyterlab",
        #     "seaborn",
        #     "types-PyYAML",
        # ],
        # "tests": [
        #     "sdv",
        #     "pytest",
        #     "pytest-dotenv",
        # ],
    },
    # entry_points={
    #     'console_scripts': [
    #         'classification = ml_project.__main__:main',
    #     ],
    # },
)
