apt-get update && apt-get install -y vim git build-essential tmux tree keepassx rustc cargo

ln -s .tmux.conf ~/.tmux.conf
ln -s vim/vimrc ~/.vimrc
mkdir ~/.vim
ln -s vim/syntax ~/.vim/syntax
ln -s .gitconfig ~/.gitconfig
ln -s .subversion ~/.subversion

cargo install rustfmt

echo "source ${HOME}/config/generic_profile" >> ${HOME}/.profile
