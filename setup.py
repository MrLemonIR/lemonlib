from setuptools import setup, find_packages

setup(
    name="lemonlib",
    version="0.1.0",
    author="MrLeMoNIR",
    author_email="",
    description="کتابخانه‌ای برای ساده‌تر کردن کدنویسی پایتون",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MrLemonIR/lemonlib",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
