import setuptools

"""

python3 setup.py sdist

# to test
cd dist && python3 –m pip install *

twine upload --repository-url=https://test.pypi.org/legacy/ dist/*

https://test.pypi.org/project/ivostoy-test-pkg/1.0.0/

pip install -i https://test.pypi.org/simple  ivostoy-test-pkg

"""
from ivostoy_test_pkg.MyDate import MyDate

if __name__ == '__main__':
    p = setuptools.find_packages()
    print(p)

    d = MyDate(2021, 1, 23)
    print(d)
    print(d.add_days(40))
    print(d.isoweekday())