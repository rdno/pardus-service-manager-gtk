#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob

from setuptools import setup
i = [x for x in range(10)]
def get_icons():
    icons = []
    for size in glob.glob('icons/hicolor/*'):
        for folder in glob.glob(size+'/*'):
            icons.append(('share/'+folder, glob.glob(folder+'/*.png')))
    return icons

data_files = [
    ("share/applications", ["data/service-manager-gtk.desktop"])
]
data_files.extend(get_icons())

setup(name="pardus-service-manager-gtk",
      version="0.1",
      package_dir={"":"src"},
      packages = ["service_manager_gtk", "asma.addons"],
      scripts = ["src/service-manager-gtk.py"],
      description= "Pardus Service Manager's gtk port",
      author="Rıdvan Örsvuran",
      author_email="flasherdn@gmail.com",
      data_files=data_files
)
