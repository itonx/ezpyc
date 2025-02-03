from setuptools import setup, find_packages

setup(
    name="ezpyc",
    version="0.1.1",
    author="Icebreaker",
    author_email="ayrton.94.e@gmail.com",
    description="Easy Python Commands",
    long_description=open("README.md", encoding='utf8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/itonx/ezpyc",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11"
)