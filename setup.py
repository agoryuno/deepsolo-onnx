from setuptools import setup, find_packages


with open("requirements.txt", "r") as f:
    requirements = [r for r in f.read().splitlines() if r[:3] != "git"]

setup(
    name='DeepSolo',
    version='0.1.3.3',
    author='Alex Goryunov',
    author_email='alex.goryunov@gmail.com',
    description='ONNX exporter for the DeepSolo model',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/agoryuno/deepsolo-onnx',
    license='MIT',
    packages=find_packages(),  
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
