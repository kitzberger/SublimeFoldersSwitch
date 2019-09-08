# Sublime Text: Folders Switch

This plugins for Sublime Text allows you to switch between different `folders` mounts.

Usually you've got a project with a single path defined under `folders` in your *.sublime-project file with a giant directory tree displayed in sublimes sidebar.

For specific tasks it might be useful to switch to a simpler sidebar with only a couple of (sub)folders being displayed.

By pressing `ctrl+shift+y` you can reduce the sidebar to the folder of the currently opened file. This new `folders` configuration will be written to your projects *.sublime-project file as `folders_1`. The old configuration will be backuped to `folders_0`.

By pressing `ctrl+shift+0` you can always get back to the original state of your project.

By pressing `ctrl+shift+1` you can switch to the new configuration called `folders_2`. This will be a copy of the last.

By pressing `ctrl+shift+2` you can switch to a new configuration called `folders_2`. This will be a copy of the last.

By pressing `ctrl+shift+3` you can switch to a new configuration called `folders_3`. This will be a copy of the last.

By pressing `ctrl+shift+x` you can remove the folder of the currently opened file from the `folders_x` configuration.

## Keymap

You can define your own keymaps, the default keymap is:

```json
[
   { "keys": ["ctrl+shift+y"], "command": "add_current_folder_to_project_mount"},
   { "keys": ["ctrl+shift+x"], "command": "remove_current_folder_from_project_mount"},
   { "keys": ["ctrl+shift+1"], "command": "switch_to_project_mount", "args": { "mount": "1" }},
   { "keys": ["ctrl+shift+2"], "command": "switch_to_project_mount", "args": { "mount": "2" }},
   { "keys": ["ctrl+shift+3"], "command": "switch_to_project_mount", "args": { "mount": "3" }},
   { "keys": ["ctrl+shift+0"], "command": "cleanup_project_mounts"},
]
```

## Kudos

This plugin was heavily inspired by https://github.com/divinites/folder2project
