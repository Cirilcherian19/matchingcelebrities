from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Ciril cherian",
    description="A small package for Which Bollywood Celebrity You look like? Deep Learning Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cirilcherian19/matchingcelebrities.git",
    author_email="cirilcherian009@gmail.com",
    packages=["src"],
    python_requires=">=3.9",
    install_requires=[
        'mtcnn',
        'tensorflow',
        'keras',
        'keras-vggface',
        'keras_applications',
        'PyYAML',
        'tqdm',
        'scikit-learn',
        'streamlit',
        'bing-image-downloader'
    ]
)