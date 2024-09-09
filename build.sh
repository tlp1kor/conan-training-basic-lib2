#!/bin/bash

# Define build directory
build_dir=__build

# Remove old build directory if exists
rm -rf $build_dir

# Create new build directory
mkdir -p $build_dir

# Get the full path to the directory where the script is located
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Profile file to be used
profile=./conan_profiles/profile_x86_debug

# Install dependencies (including fmt)
conan install $ROOT_DIR -pr:a $profile --build=missing

conan create $ROOT_DIR -pr:a $profile