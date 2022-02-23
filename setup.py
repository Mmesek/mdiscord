import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = [i.strip() for i in f.readlines()]

setuptools.setup(
    name="mDiscord",
    version="1.0.0",
    author="Mmesek",
    description="Discord API Wrapper with type casting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mmesek/mdiscord",
    project_urls={
        "Bug Tracker": "https://github.com/Mmesek/mdiscord/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.7",
)
