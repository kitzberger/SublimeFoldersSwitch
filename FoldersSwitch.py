import sublime_plugin
import sublime
import os
import copy

class SwitchToProjectMountCommand(sublime_plugin.WindowCommand):
    def run(self, mount):
        print('Switch To Project Mount: ' + str(mount))

        win = sublime.active_window()
        data = win.project_data()

        if 'folders_0' not in data:
            data['folders_0'] = copy.deepcopy(data['folders'])

        foldersKey = 'folders_' + str(mount)
        if foldersKey in data:
            data['folders'] = data[foldersKey]
        else:
            data[foldersKey] = copy.deepcopy(data['folders'])
        data['currentMount'] = mount

        win.set_project_data(data)

class ProjectMountCommend(sublime_plugin.WindowCommand):
    def init(self):
        file_name = self.window.active_view().file_name()
        self.folder = os.path.abspath(os.path.dirname(file_name))
        self.data = sublime.active_window().project_data()

        # Create backup (if not preset yet)
        if 'folders_0' not in self.data:
            self.data['folders_0'] = copy.deepcopy(self.data['folders'])

        # Make sure we've got a currentMount variable
        if 'currentMount' not in self.data:
            self.data['currentMount'] = "1"

        # Create folders key
        self.foldersKey = 'folders_' + self.data['currentMount']

        # Create folders mount (if not preset yet)
        if self.foldersKey not in self.data:
            #self.data[self.foldersKey] = copy.deepcopy(self.data['folders'])
            self.data[self.foldersKey] = []

class AddCurrentFolderToProjectMountCommand(ProjectMountCommend):
    def run(self):
        self.init()

        # Add folder (if not preset yet)
        found = False
        for folders in self.data[self.foldersKey]:
            if folders['path'] == self.folder:
                found = True
        if not found:
            self.data[self.foldersKey].append({'follow_symlinks': True, 'path': self.folder})

        sublime.active_window().set_project_data(self.data)

        self.window.run_command("switch_to_project_mount", {"mount": self.data['currentMount']})

class RemoveCurrentFolderFromProjectMountCommand(ProjectMountCommend):
    def run(self):
        self.init()

        temp = None
        for folders in self.data[self.foldersKey]:
            if folders['path'] == self.folder:
                temp = folders
        if temp:
            self.data[self.foldersKey].remove(temp)

        sublime.active_window().set_project_data(self.data)

        self.window.run_command("switch_to_project_mount", {"mount": self.data['currentMount']})

class CleanupProjectMountsCommand(sublime_plugin.WindowCommand):
    def run(self):
        win = sublime.active_window()
        data = win.project_data()

        if 'folders_0' in data:
            print('Found folders_0!')
            data['folders'] = data['folders_0']
            data.pop('currentMount', None)
            win.set_project_data(data)
        else:
            print('No folders_0 found. Leaving everything as is!')
