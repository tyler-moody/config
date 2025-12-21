PATH=/opt/qumulo/toolchain/bin:$PATH
alias crd="./check_run.py --build --no-cunit-core-dumps"
alias crdq="./check_run.py --build --no-cunit-core-dumps --flavor debug --quark-plus-local"
alias crr="./check_run.py --build --no-cunit-core-dumps --flavor release"
alias crrq="./check_run.py --build --no-cunit-core-dumps --flavor release --quark-plus-local"
alias daily="source ${HOME}/config/scripts/daily.sh"
alias trg="tools/red_green.py"
alias signatures="build gen; signatures/tool.py --flavor=debug update"
alias hh="hg"
${HOME}/src/prebuild
