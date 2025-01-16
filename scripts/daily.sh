HOME=/home/tmoody
SRC=${HOME}/src
TOOLS=${HOME}/tools
LINKING_CACHE=${HOME}/linking_cache

cd ${SRC}
qonstruct/cache_tool.py trim --entry-mtime "2 days ago" ${LINKING_CACHE}
hg qpop -a && hg fetch
${SRC}/prebuild
sudo apt autoremove -y
qpkg sweep
qpkg sync

${SRC}/tools/clean_build.sh
${SRC}/tools/rm_merge_remnants.sh

hg fetch --cwd ${TOOLS}; pkill -f hg.real; pkill -f hg

chmod 600 infrastructure/id_rsa

build all_objects tags
