inoremap jk <ESC> 
let mapleader = ","
filetype plugin indent on
syntax on
syntax enable 
set encoding=utf-8
execute pathogen#infect()
set number
set showcmd
filetype indent on
set wildmenu
set lazyredraw
set showmatch
set incsearch
set hlsearch
nnoremap <space> :nohlsearch<CR>
nnoremap B ^
nnoremap E $
nnoremap gV `[v`]


