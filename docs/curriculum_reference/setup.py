from setuptools import setup, find_packages

setup(
    name="peers-osint-scanner",
    version="1.0.0",
    author="Md Peer Siddiqui",
    author_email="peersiddiqui@example.com",
    description="PEER'S OSINT Scanner — Modular Passive Reconnaissance Tool for Sqrock Cybersecurity Internship",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MdPeerSiddiqui/Peers-Osint-Scanner",
    packages=find_packages(),
    py_modules=["peers_scanner", "main"],
    install_requires=[
        "requests>=2.31.0",
        "python-whois>=0.9.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "peers-osint=peers_scanner:main",
            "peers-scanner=peers_scanner:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
)
