set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Chiel92/vim-autoformat'
Plugin 'jremmen/vim-ripgrep'
call vundle#end()

filetype plugin indent on
set whichwrap=<,>,[,],b,s       " must be set after filetype

let g:formatterpath=['/opt/qumulo/toolchain/bin']
autocmd BufWritePre *.rs : Autoformat
autocmd BufWritePre *.js : Autoformat
 
autocmd BufEnter * if &filetype == "" | setlocal ft=text | endif

set autoindent
set shiftwidth=4
set tabstop=4

set background=dark
syntax on

set expandtab

set hlsearch
set incsearch
set smartcase

set wildmenu

set nobackup
set noswapfile

set number

set laststatus=2

set mouse=a

set colorcolumn=100

let mapleader = ' '
" Rg for the token under the cursor
nnoremap <leader>f : Rg <C-R><C-W> --sort path -g '!infrastructure/data_warehouse/**' -g '!signatures'<CR>
" Same as above but omit test files
nnoremap <leader>g : Rg <C-R><C-W> --sort path -g '!infrastructure/data_warehouse/**' -g '!signatures' -g '!*test*'<CR>
inoremap jk <ESC>
nnoremap <leader>a : Autoformat <CR>


" Hop between related files
function GoToTest()
    let newfile = expand('%:r') . '_test.' . expand('%:e')
    execute "e " . fnameescape(l:newfile)
endfunc
function GoFromTest()
    let newfile = substitute(expand('%:r'), '_test$', '.' . expand('%:e'), '')
    execute "e " . fnameescape(l:newfile)
endfunc
function ToggleTestFile()
    " If in abc_test.xyz file, open abc.xyz
    " If in abc.xyz, open abc_test.xyz
    let base = expand('%:r')
    if base =~ '.*_test'
        call GoFromTest()
    else
        call GoToTest()
    end
endfunc

function GoToHeader()
    let newfile = expand('%:r') . '.h'
    execute "e " . fnameescape(l:newfile)
endfunc
function GoToSource()
    let newfile = expand('%:r') . '.c'
    execute "e " . fnameescape(l:newfile)
endfunc
function ToggleHeaderSource()
    " If in abc.c file, open abc.h
    " If in abc.h, open abc.c
    let ext = expand('%:e')
    if ext =~ 'c'
        call GoToHeader()
    else
        call GoToSource()
    end
endfunc

function GoToGen()
    let newfile = 'build/debug/' . expand('%') . '.gen.h'
    execute "e " . fnameescape(l:newfile)
endfunc

command T call ToggleTestFile()
command H call ToggleHeaderSource()
command C call ToggleHeaderSource()
command G call GoToGen()
