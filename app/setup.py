from setuptools import setup, find_packages

app_dependencies = [
    "bottle==0.12.20",
    "gunicorn==20.0.4",
    "inject==4.0.0",
    "requests>=2.0.0",
    "bottle-swagger-2==2.0.8"
]

dev_dependencies = [
    "pytest",
    "pylint",
    "wheel"
]

setup(
    name="webapp",
    version="0.0.1",
    description="This is web app based on bottle.",
    author="Name",
    author_email="name@name.com",
    url="https://git.ilb.ru/ilb.ru/webapp",
    packages=find_packages(),
    python_requires=">=3.6",
    package_data={
        "": ["*.json", "*.yaml", "*.xml", "*.wav", "*.sh", "*.jpg"]
    },
    install_requires=app_dependencies,
    extras_require={
        "dev": dev_dependencies,
    },
    entry_points={
        "console_scripts": [
            "webapp=webapp.__main__:main"
        ]
    }
)
