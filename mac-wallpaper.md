```sql
$ sqlite3 /Users/jas/Library/Application Support/Dock/desktoppicture.db
```

```bash

#   Update all Wallpapers
function wallpaper() {
    sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value = '$1'" && killall Dock 
}
```

[See here](https://apple.stackexchange.com/questions/40644/how-do-i-change-desktop-background-with-a-terminal-command)

```
$ cd /Users/jas/Library/Application Support/Dock/

$ sqlite3 desktoppicture.db

$ sqlite> .tables
data         displays     pictures     preferences  prefs        spaces

$ sqlite> SELECT * FROM data;
/System/Library/Desktop Pictures/Yosemite 4.jpg
```

[Python SQLite](https://www.geeksforgeeks.org/python-sqlite-select-data-from-table/)

