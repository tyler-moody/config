url=$1
path=$(~/scripts/path_of_artifacts.py $url)
cd $path
$SHELL
