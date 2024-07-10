from setuptools import setup, find_packages

setup(
    name='zundaerror',
    version='0.0.0',
    packages=find_packages(),
    package_dir={'zundaerror': 'zundaerror'},
    description='Zundamon reports exceptions.',
    long_description='''Zundamon reports exceptions.
This requires VOICEVOX as localhost server.''',
    url='https://github.com/uesseu/zundaerror',
    author='Shoichiro Nakanishi',
    author_email='sheepwing@kyudai.jp',
    license='MIT',
    zip_safe=False,
)
