PATH=/opt/qumulo/toolchain/bin:$PATH
alias crd="./check_run.py --build --no-cunit-core-dumps"
alias crr="./check_run.py --build --no-cunit-core-dumps--flavor release"
alias crd-cfw='./check_run.py --build --no-cunit-core-dumps --flavor debug --quark-plus-local --quark-broker quark-broker-cfw.eng.qumulo.com:9999'
alias crd-csq='./check_run.py --build --no-cunit-core-dumps --flavor debug --quark-plus-local --quark-broker quark-broker-csq.eng.qumulo.com:9999'
alias trg="tools/red_green.py"
alias qmount="for host in {gravytrain,iss}.eng.qumulo.com; do sudo ${HOME}/scripts/mount.sh \$host; done"
alias signatures='build gen; generate/signatures.py --flavor=debug update'
${HOME}/src/prebuild
