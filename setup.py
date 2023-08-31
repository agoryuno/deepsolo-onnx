from setuptools import setup, find_packages

setup(
    name='DeepSolo',
    version='0.1.3.2',
    author='Alex Goryunov',
    author_email='alex.goryunov@gmail.com',
    description='ONNX exporter for the DeepSolo model',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/agoryuno/deepsolo-onnx',
    license='MIT',
    packages=['DeepSolo'],  
    install_requires=[
        'numpy',
        'torch',
        'detectron2',
        'timm'
    ],
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
