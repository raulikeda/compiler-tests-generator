#!/usr/bin/env bash

set -euo pipefail

src_dir="./output/syntax"
dst_dir="../compiler-testing-lib/compiler_testing_lib/syntax"

if [[ ! -d "$src_dir" ]]; then
	echo "Source directory does not exist: $src_dir"
	exit 1
fi


mkdir -p "$dst_dir"
# rm -rf "${dst_dir:?}"/*
echo "Copying files from $src_dir to $dst_dir"

cp -a "$src_dir"/. "$dst_dir"/

echo "Copied $src_dir to $dst_dir"
