#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
	echo "Usage: $0 <lang>"
	exit 1
fi

lang="$1"
src_dir="./output/$lang"
dst_dir="../compiler-testing-lib/compiler_testing_lib/languages/$lang"

if [[ ! -d "$src_dir" ]]; then
	echo "Source directory does not exist: $src_dir"
	exit 1
fi


mkdir -p "$dst_dir"
rm -rf "${dst_dir:?}"/*
echo "Copying files from $src_dir to $dst_dir"

cp -a "$src_dir"/. "$dst_dir"/

echo "Copied $src_dir to $dst_dir"
