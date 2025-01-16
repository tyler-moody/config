#!/bin/bash

set -ex

SERVER="$1"
BASE="$(echo "$SERVER" | awk -F. '{print $1}')"

for mount in $(showmount -e "$SERVER" | grep -E 'everyone|home' | cut -d' ' -f 1); do
    mkdir -p "/mnt/$BASE$mount"
    mount -t nfs -onfsvers=3,nolock "$SERVER:$mount" "/mnt/$BASE$mount"
done
