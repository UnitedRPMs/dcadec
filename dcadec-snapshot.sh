#!/bin/bash

set -x

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
date=$(date +%Y%m%d)
package=dcadec
branch=master
name=dcadec

pushd ${tmp}
git clone https://github.com/foo86/dcadec.git
cd ${package}
git checkout ${branch}
tag=$(git rev-list HEAD -n 1 | cut -c 1-7)
version=`git describe --tags | awk -F '-' '{print $1}' | tr -d 'v'`
git archive --prefix="${name}-${version}/" --format=tar master > "$pwd"/${name}-${version}-${date}-${tag}.tar



