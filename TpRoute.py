import sublime
import sublime_plugin
import webbrowser
import re
import os


__author__ = '蒋力彬'
PACKAGE_NAME = 'TpRoute'


class TpRouteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = self.getSettings()
		filename = self.view.file_name()

		host = ''
		if settings.get('tp_host'):
			host = settings.get('tp_host')

		self.view.run_command('save')

		# 获取当前文件里的所有方法名
		actions = []
		with open(filename, 'r') as f:
			text = f.read()
			# 匹配方法名
			m = re.findall(r'function\s+([\w\d_]+)',text)
			if m :
				actions = m

		moduleName = self.getTpModuleName(filename)
		controllerName = os.path.basename(filename).replace('Controller.class.php','').replace('.php','')

		for sel in self.view.sel():
			# 获取当前选中文字
			action = self.view.substr(sel)
			if action in actions:
				actionName = actions[actions.index(action)]

				host = host.replace('{m}', moduleName)
				host = host.replace('{c}', controllerName)
				host = host.replace('{a}', actionName)

				webbrowser.open(host)

	def getSettings(self):
		return sublime.load_settings(PACKAGE_NAME + '.sublime-settings')


	def getTpModuleName(self, filename,level = 3,dir_name=''):
		if level == 0:
			return dir_name

		path,__dirname = os.path.split(filename)
		return self.getTpModuleName(path,level-1,__dirname)
