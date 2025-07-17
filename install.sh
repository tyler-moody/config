if ! cat ${HOME}/.bashrc | grep -q "source ${PWD}/bashrc"; then
    echo "source ${PWD}/bashrc" >> ${HOME}/.bashrc
fi

if ! cat ${HOME}/.gdbinit | grep -q "source ${PWD}/gdbinit"; then
    echo "source ${PWD}/gdbinit" >> ${HOME}/.gdbinit
fi

if ! test -d "${HOME}/scripts" ; then
    ln -s ${PWD}/scripts ${HOME}/scripts
fi

ln -s ${PWD}/digrc ${HOME}/.digrc

mkdir -p ${HOME}/linking_cache
ln -s ${PWD}/qumulorc ${HOME}/.qumulorc

git clone https://github.com/VundleVim/Vundle.vim.git ${HOME}/.vim/bundle/Vundle.vim
ln -s ${PWD}/vimrc ${HOME}/.vimrc
if ! test -f "${HOME}/.vim/after/syntax/c.vim" && test -d ${HOME}/src ; then
    echo "c.vim"
    mkdir -p ${HOME}/.vim/after/syntax
    ln -s ${HOME}/src/tools/editors/vim/after/syntax/c.vim ${HOME}/.vim/after/syntax/c.vim
fi
if ! test -f "${HOME}/.vim/plugin/figlet.vim" && test -d ${HOME}/src ; then
    echo "figlet.vim"
    mkdir -p ${HOME}/.vim/plugin
    ln -s ${HOME}/src/tools/editors/vim/plugin/figlet.vim ${HOME}/.vim/plugin/figlet.vim
fi
vim +PluginInstall +qall

ln -s ${PWD}/tmux.conf ${HOME}/.tmux.conf 

ln -s ${PWD}/hgrc ${HOME}/.hgrc

sudo git clone https://github.com/zolrath/wemux.git /usr/local/share/wemux
sudo ln -s /usr/local/share/wemux/wemux /usr/local/bin/wemux
cp /usr/local/share/wemux/wemux.conf.example ${PWD}/wemux.conf 
echo "host_list=(${USER})" >> ${PWD}/wemux.conf
sudo mv ${PWD}/wemux.conf /usr/local/etc/wemux.conf

# Install nfs-common for showmount, used by scripts/mount.sh
sudo apt update && sudo apt install nfs-common -y
