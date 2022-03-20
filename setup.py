from setuptools import setup

setup(
    name='Hapyka',
    version='0.0.1e',
    packages=['hapyka', 'hapyka.utils', 'hapyka.utils.handlers', 'hapyka.utils.handlers.text',
              'hapyka.utils.handlers.image', 'hapyka.utils.handlers.inline', 'hapyka.utils.handlers.command',
              'hapyka.classes', 'hapyka.dictionaries'],
    url='https://github.com/LkkCcc/Hapyka',
    license='GPLv2',
    author='Siarhei_Tsitou1',
    author_email='locchan@yandex.ru',
    install_requires=[
        'python-telegram-bot',
        'hvac'
    ],
    scripts=['hapyka/hapyka_main.py'],
    description='Hapyka. Python implementation of Haruka tg bot'
)
