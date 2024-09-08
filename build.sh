#!/bin/bash

# Get the full path to the directory where the script is located
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Profile file to be used
profile=./conan_profiles/profile_x86_debug

conan create $ROOT_DIR -pr:a $profile