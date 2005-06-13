#!/bin/sh -e
# $Id$
#
# wrapper to flare binary, which outputs parse results from flare
# does not need write permission in current directory.
# Requires: mktemp

if [ -f "$1" ]; then
	tmp=`mktemp -d ${TMPDIR:-/tmp}/flareXXXXXX`
	trap 'rc=$?; rm -rf $tmp; exit $rc' EXIT INT QUIT TERM

	cp "$1" "$tmp/file.swf"
	cd "$tmp"
	flare file.swf
	cat file.flr
else
	# propatate usage
	flare
fi
