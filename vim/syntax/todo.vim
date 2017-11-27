if exists("b:current_syntax")
    finish
endif

syn case match

syn keyword alarm TODO
syn keyword aware WAIT
syn keyword mellow DONE
syn match bullets "\*"
syn match date "\d\@<!\d\{8}\d\@!"   " exactly eight digits
syn match date "\d\{4}-\d\{2}-\d\{2}" " hyphen separated y-m-d

let b:current_syntax = "todo"

hi def link alarm Error
hi def link aware Todo
hi def link mellow Structure
hi def link bullets Function
hi def link date String
