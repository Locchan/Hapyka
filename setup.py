from setuptools import setup

setup(
    name='Hapyka',
    version='0.0.1c',
    packages=['hapyka', 'hapyka.utils', 'hapyka.utils.handlers', 'hapyka.utils.handlers.text',
              'hapyka.utils.handlers.image', 'hapyka.utils.handlers.inline', 'hapyka.utils.handlers.command',
              'hapyka.classes', 'hapyka.dictionaries'],
    url='https://github.com/LkkCcc/Hapyka',
    license='GPLv2',
    author='Siarhei_Tsitou1',
    author_email='locchan@yandex.ru',
    install_requires=[
        'python-telegram-bot',
    ],
    scripts=['hapyka/hapyka.py'],
    description='Hapyka. Python implementation of Haruka tg bot'
)
