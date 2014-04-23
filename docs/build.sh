#!/usr/bin/env bash

rm -rf build
rm -rf source/api
sphinx-apidoc -e -o source/api ..
sphinx-build -c . source/ build
