echo "source ${PWD}/bashrc" >> ${HOME}/.bashrc

echo "source ${PWD}/gdbinit" >> ${HOME}/.gdbinit

git clone https://github.com/VundleVim/Vundle.vim.git ${HOME}/.vim/bundle/Vundle.vim
ln -s ${PWD}/vimrc ${HOME}/.vimrc
vim +PluginInstall +qall

ln -s ${PWD}/tmux.conf ${HOME}/.tmux.conf 

git clone https://github.com/zolrath/wemux.git /usr/local/share/wemux
ln -s /usr/local/share/wemux/wemux /usr/local/bin/wemux
cp /usr/local/share/wemux/wemux.conf.example ${PWD}/wemux.conf 
echo "host_list=(${USER})" >> ${PWD}/wemux.conf
sudo mv ${PWD}/wemux.conf /usr/local/etc/wemux.conf
