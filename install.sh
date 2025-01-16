ln -s ${PWD}/tmux.conf ${HOME}/.tmux.conf 

git clone https://github.com/VundleVim/Vundle.vim.git ${HOME}/.vim/bundle/Vundle.vim
ln -s ${PWD}/vimrc ${HOME}/.vimrc
vim +PluginInstall +qall

echo 
echo "Go to https://github.com/zolrath/wemux if you want wemux"
