from setuptools import find_packages, setup

package_name = 'py_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='launchspider',
    maintainer_email='danylo.bezruchenko@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = py_package.my_first_node:main",
            "robot_news_station = py_package.robot_news_station:main",
            "smartphone = py_package.smartphone:main",
            "number_publisher = py_package.number_publisher:main",
            "number_courier = py_package.number_courier:main",
            "add_two_ints_server = py_package.add_two_ints_server:main",
            "add_two_ints_client_no_oop = py_package.add_two_ints_client_no_oop:main",
            "add_two_ints_client = py_package.add_two_ints_client:main",
            "hardware_status_publisher = py_package.hw_status_publisher:main"
        ],
    },
)
