How to set chaotic AUR for pacman
----------------------------------

Append (adding to the end of the file) to /etc/pacman.conf:

```vim
[chaotic-aur]
Include = /etc/pacman.d/chaotic-mirrorlist
```

ref: [Official website](https://aur.chaotic.cx/)
