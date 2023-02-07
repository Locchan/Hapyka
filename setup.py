from setuptools import setup

setup(
    name='Hapyka',
    version='1.1.2',
    packages=['hapyka', 'hapyka.config', 'hapyka.utils', 'hapyka.utils.handlers', 'hapyka.utils.handlers.text',
              'hapyka.utils.handlers.image', 'hapyka.utils.handlers.inline', 'hapyka.utils.handlers.command',
              'hapyka.classes', 'hapyka.dictionaries', 'hapyka.database', 'hapyka.database.models'],
    url='https://github.com/LkkCcc/Hapyka',
    license='GPLv2',
    author='Locchan',
    author_email='locchan@yandex.ru',
    install_requires=[
        'python-telegram-bot>=13, <20',
        'hvac',
        'sqlalchemy'
    ],
    scripts=['hapyka/hapyka_main.py'],
    description='Hapyka. Python implementation of Haruka tg bot'
)
