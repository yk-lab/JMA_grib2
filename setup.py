from setuptools import setup

setup(
    package_dir = {'': 'jma_grib2'},
    use_scm_version=True,
    setup_requires=[
        "setuptools_scm"
    ]
)
