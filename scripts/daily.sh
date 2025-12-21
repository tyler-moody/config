HOME=/home/tmoody
SRC=${HOME}/src
TOOLS=${HOME}/tools
LINKING_CACHE=${HOME}/linking_cache

${HOME}/config/scripts/cleanup_snaps.sh
sudo journalctl --vacuum-time=7d

cd ${SRC}
hg qpop -a 
hg up default
${SRC}/prebuild
hg fetch
${SRC}/prebuild
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y
qpkg sweep
qpkg sync

rm -rf build/tmp
${SRC}/tools/rm_merge_remnants.sh

hg fetch --cwd ${TOOLS}; pkill -f hg.real; pkill -f hg

chmod 600 infrastructure/id_rsa

sudo mount gravytrain.eng.qumulo.com:/ /mnt/gravytrain
sudo mount iss.eng.qumulo.com:/ /mnt/iss

cp -f /mnt/gravytrain/build/latest/src/tags ~/src

# Do this last, it's slow.
qonstruct/cache_tool.py trim --entry-mtime "2 days ago" ${LINKING_CACHE}
