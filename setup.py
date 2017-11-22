"""
Flask-FCM
-------------

Flask Extension for using Firebase Cloud Messaging service
"""
from setuptools import setup


setup(
    name='Flask-FCM',
    version='0.2',
    url='https://github.com/senseobservationsystems/flask-fcm',
    author='Ricky Hariady',
    author_email='ricky@sense-os.nl',
    description='Flask Extension for using Firebase Cloud Messaging service',
    long_description=__doc__,
    py_modules=['flask_fcm'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'pyfcm==1.2.1'
    ]
)
