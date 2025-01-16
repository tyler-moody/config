echo "source ${PWD}/bashrc" >> ${HOME}/.bashrc

git clone https://github.com/VundleVim/Vundle.vim.git ${HOME}/.vim/bundle/Vundle.vim
ln -s ${PWD}/vimrc ${HOME}/.vimrc
vim +PluginInstall +qall

ln -s ${PWD}/tmux.conf ${HOME}/.tmux.conf 

echo 
echo "Go to https://github.com/zolrath/wemux if you want wemux"
