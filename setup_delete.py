from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: Apache Software License',
]

setup(
    name="test_gammagl",
    version="0.1",
    author="zhou guangyu",
    author_email="1029175863@qq.com",
    maintainer="zhou guangyu",
    license="Apache-2.0 License",
    url="https://github.com/gyzhou2000/setup",
    download_url="https://github.com/gyzhou2000/setup",
    python_requires='>=3.6',
    packages=find_packages(),
    classifiers=classifiers
)