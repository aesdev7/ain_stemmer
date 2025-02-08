from setuptools import setup, find_packages

# Application metadata
APP_NAME = 'ain_stemmer'
VERSION = '1.0.0'  # Update version as needed
AUTHOR = 'Ab Sultan'
AUTHOR_EMAIL = 'aesdev7@gmail.com'
DESCRIPTION = 'Classical Arabic verb stemmer based on Ibn Malik treatment set forth in him Lamyahto alafal.'
URL = 'https://github.com/aesdev7'

# Dependencies (if any)
REQUIRED_PACKAGES = [
    # Add required libraries here, for example:
    # 'PyQt5', 'tkinter', 'requests', 'numpy'
]

# GUI application entry points (for frameworks like PyQt or Tkinter)
ENTRY_POINTS = {
    'gui_scripts': [
        'ain_stemmer = ain_stemmer.main:main_function',  # Update with actual entry point
    ],
    # If CLI
    'console_scripts': [
        'ain_stemmer-cli = ain_stemmer.main:cli_entry',  # Update with actual entry point for CLI
    ]
}

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    entry_points=ENTRY_POINTS,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change this if using a different license
        'Operating System :: OS Independent',
    ],
)
