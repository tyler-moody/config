" set number of colors available
set t_Co=256
" curn off compatibility with vi
set nocp

" set up tabbing
set tabstop=2 " sets the width of a tab character
set softtabstop=2 " width of soft tabs (tabs made of spaces)
set shiftwidth=2 " how many cols of indentation to start/end when 
" autoindenting
set shiftround " forces << and >> to use multiples of shiftwidth
set backspace=indent,eol,start " allow backspaces through autoindentation
" set expandtab " expand all tabs to spaces
set smarttab " insert tabs at the start of a line using shiftwidth
set smartindent

" set up searching
set hlsearch " highlight search matches
set incsearch " show search matches as you type
set ignorecase " ignore case in "/" searches by default
set smartcase " if pattern contains uppercase, use case sensitive 
" search
set gdefault " global search & replace by default (not just first 
" occurrence)

" prettyness
set relativenumber " turn on line numbering - relative to current 
" position for easier navigation
set nu
set ruler " show line, column coordinates of the cursor in 
" the bottom-right
syntax on " turn on syntax highlighting
set showmatch " highlight matching parens
colorscheme solarized
set background=dark

" line length settings
set wrap
set formatoptions=qrn1
" set colorcolumn=81
" change the font in gvim
if has('gui_running')
set guifont=Courier_New:h9
endif

" features on/off
set nobackup " turn off backup files
set noswapfile " turn off swap files  
set nocompatible " turn off vi compatibility restrictions
set modelines=0 " some kind of security exploit prevention???

autocmd BufEnter *.txt syntax off " turn off syntax highlighting for 
" text files
autocmd BufEnter *.ld syntax off " turn off syntax highlighting for 
" loader directive files

" force use of hjkl instead of arrow keys
nnoremap <up> <nop>
nnoremap <down> <nop>
nnoremap <left> <nop>
nnoremap <right> <nop>
inoremap <up> <nop>
inoremap <down> <nop>
inoremap <left> <nop>
inoremap <right> <nop>
nnoremap j gj
nnoremap k gk

" turn off the help key (always hit this when reaching for <ESC
inoremap <F1> <ESC>
nnoremap <F1> <ESC>
vnoremap <F1> <ESC>

" leader key customizations
let mapleader=',' " change the leader key to comma
nnoremap <leader><space> :noh<cr> " clear search highlighting
nnoremap <leader>v <C-w>v<C-w>l " create a new vertical split
nnoremap <leader>s <C-w>s<C-w>j " create a new horizontal split
nnoremap <C-h> <C-w>h " make split navigation use hjkl
nnoremap <C-j> <C-w>j " make split navigation use hjkl
nnoremap <C-k> <C-w>k " make split navigation use hjkl
nnoremap <C-l> <C-w>l " make split navigation use hjkl
