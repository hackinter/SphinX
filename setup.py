#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

# ASCII Art
ascii_art = r"""
███████╗██████╗ ██╗  ██╗██╗███╗   ██╗██╗  ██╗
██╔════╝██╔══██╗██║  ██║██║████╗  ██║╚██╗██╔╝
███████╗██████╔╝███████║██║██╔██╗ ██║ ╚███╔╝ 
╚════██║██╔═══╝ ██╔══██║██║██║╚██╗██║ ██╔██╗ 
███████║██║     ██║  ██║██║██║ ╚████║██╔╝ ██╗
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
"""

print(ascii_art)

setup(
    name='sphinx',
    version='1.0.1',  # সংস্করণ আপডেট করা হয়েছে
    description='An advanced HTTP parameter discovery suite for security assessments',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='HACKINTER',  # আপনার নাম
    author_email='ceh.ec.counselor147@gmail.com',  # আপনার ইমেল
    license='Apache License 2.0',  # লাইসেন্স আপডেট করা হয়েছে
    url='https://github.com/hackinter/sphinx',  # গিটহাব URL
    download_url='https://github.com/hackinter/sphinx/archive/v1.0.1.zip',  # ডাউনলোড URL আপডেট করা হয়েছে
    zip_safe=False,
    packages=find_packages(),
    package_data={'sphinx': ['db/*']},
    install_requires=[
        'requests',
        'dicttoxml',
        'ratelimit'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'License :: OSI Approved :: Apache License 2.0',
        'Programming Language :: Python :: 3.6',  # সংস্করণ আপডেট
    ],
    entry_points={
        'console_scripts': [
            'sphinx = sphinx.__main__:main'  # নাম আপডেট
        ]
    },
    keywords=['sphinx', 'bug bounty', 'http', 'pentesting', 'security'],
)
