#!/bin/bash

if [ $# -ne 2 ]; then
    echo "USAGE: $0 <dir-to-add> <final-iso-path>";
    exit 1;
fi

hdiutil makehybrid -o "$2" "$1" -iso -joliet
