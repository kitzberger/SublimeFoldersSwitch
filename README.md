# Sublime Text: Folders Switch

This plugin for Sublime Text allows you to easily switch between different `folders` mounts of the same project.

Usually you've got one huge project with a single path defined under `folders` in your `*.sublime-project` file with a giant directory tree displayed in Sublime Texts sidebar.

For specific tasks it might be useful to switch to a simpler sidebar with only a couple of (sub)folders being displayed at once.

The idea is to have several `folders` configurations within your `*.sublime-project` file and switch between them with a set of defined keyboard shortcuts.

## How to

By pressing `ctrl+alt+shift+1` you can create a new configuration called `folders_1`. This will be a copy of the currently used `folders` configuration. The old configuration will be backup'ed to `folders_0`. By pressing `ctrl+alt+shift+0` you can always get back to the original state of your project.

Now edit the `*.sublime-project` file manually (Edit / Edit Project) to define a set of different folders for this alternative `folders_1` configuration, so your file might look similar to the following JSON. I've configured `folders_1` to contain only the relevant paths for an arbitiary TYPO3 project and `folders_0` to contain the projects root folder.

```json
{
	"folders":
	[
		{
			"path": "/projects/my-typo3-project"
		}
	],
	"folders_0":
	[
		{
			"path": "/projects/my-typo3-project"
		}
	],
	"folders_1":
	[
		{
			"name": "My TYPO3 project: ext",
			"path": "/projects/my-typo3-project/app/html/typo3conf/ext"
		},
		{
			"name": "My TYPO3 project: sysext",
			"path": "/projects/my-typo3-project/app/html/typo3/sysext"
		}
	]
}
```

Don't edit `folders` directly. Always only edit the `folders_x` blocks, because `folders` will be overwritten with the contents of `folders_x` when hitting one of the switch shortcuts.

If you need more than one alternative `folders` configuration you can use `ctrl+alt+shift+2` and `ctrl+alt+shift+3` to create `folders_2` and `folders_3`. They will be initialize with the current `folders` setting and must be customized manually by editing the project file.

Have a look at the project file when pressing the shortcuts to fully understand what's happening.

## Keymap

You can define your own keymaps, the default keymap is:

```json
[
   { "keys": ["ctrl+alt+shift+1"], "command": "switch_to_project_mount", "args": { "mount": "1" }},
   { "keys": ["ctrl+alt+shift+2"], "command": "switch_to_project_mount", "args": { "mount": "2" }},
   { "keys": ["ctrl+alt+shift+3"], "command": "switch_to_project_mount", "args": { "mount": "3" }},
   { "keys": ["ctrl+alt+shift+0"], "command": "cleanup_project_mounts"},
]
```

## Kudos

This plugin was heavily inspired by https://github.com/divinites/folder2project
