from setuptools import setup
from setuptools import find_packages

package_name = 'r2d2_ros2_web_gui'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'':'src'},
    #include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=True,
    author='Rico Castelo',
    author_email='ricorx7@gmail.com',
    maintainer='Rico Castelo',
    maintainer_email='ricorx7@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='R2D2 ROS2 Web User Interface from Rico.ai.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'r2d2_web_gui = r2d2.ros2.gui.web_gui_pub:main',
        ],
    },
)
