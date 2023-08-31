from setuptools import setup, find_packages

setup(
    name='DeepSolo',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A deep learning-based package for XYZ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/agoryuno/deepsolo-onnx',
    license='MIT',
    packages=['DeepSolo'],  # Explicitly setting the packages
    install_requires=[
        'numpy',
        'torch',
        'detectron2',
        'timm'
        # Add other dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
