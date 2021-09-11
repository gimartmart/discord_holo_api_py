import setuptools



setuptools.setup(
    name="discord-holo-api",
    version="1.3.0",
    author="mandarin",
    author_email="burjtyuu@gmail.com",
    description="Python module for API holo",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/gimartmart/discord_holo_api_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.6,",
)