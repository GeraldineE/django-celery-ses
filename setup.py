from setuptools import setup, find_packages
from svcelery_email import __version__


setup(
    name='django-celery-ses',
    version=__version__,
    description="django-celery-ses",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django,celery,mail',
    author='tzangms',
    author_email='tzangms@streetvoice.com',
    url='http://github.com/StreetVoice/django-celery-ses',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
