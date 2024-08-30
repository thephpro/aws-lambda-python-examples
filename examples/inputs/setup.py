thon
from setuptools import setup, find_packages

setup(
    name="inputs",
    version="0.1.0",  # Specify your package version
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    description="A brief description of your package",  # Short description
    long_description=open('README.md').read(),  # Read long description from README
    long_description_content_type='text/markdown',  # Specify the markdown format
    url="https://github.com/yourusername/inputs",  # Replace with your project URL
    packages=find_packages('src/inputs'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify minimum Python version
    install_requires=[
        # List your package dependencies here
    ],
)