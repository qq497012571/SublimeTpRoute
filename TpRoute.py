#coding:utf-8
import sublime
import sublime_plugin
import webbrowser
import re
import os


__author__ = '蒋力彬'
PACKAGE_NAME = 'TpRoute'


class TpRouteCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		self.settings = self.getSettings()
		self.host = self.settings.get('tp_host')
		ext = os.path.splitext(self.view.file_name())[1]

		self.view.run_command('save')

		if ext == '.html':
			self.openInView()

		if ext == '.php':
			self.openInController()

	def getSettings(self):
		return sublime.load_settings(PACKAGE_NAME + '.sublime-settings')


	def getParentDir(self, filename,level = 3,dir_name=''):
		if level == 0:
			return dir_name

		path,__dirname = os.path.split(filename)
		return self.getParentDir(path,level-1,__dirname)


	def openInView(self):
		moduleName = self.getParentDir(self.view.file_name(),4)
		controllerName = self.getParentDir(self.view.file_name(),2)
		action = self.getParentDir(self.view.file_name(),1).replace('.html','')

		self.host = self.host.replace('{m}', moduleName)
		self.host = self.host.replace('{c}', controllerName)
		self.host = self.host.replace('{a}', action)
		webbrowser.open(self.host)

	def openInController(self):
		# 解析类中方法
		actions = {}
		with open(self.view.file_name(), 'r',encoding = 'utf-8') as f:
			text = f.read()
			# 解析方法与参数
			m = re.findall(r'function\s+([\w\d_]+)\s*?\(([$\w\d_,="\']*?)\)',text)
			for action,param in m:
				actions[action] = self.parseParam(param)

		moduleName = self.getParentDir(self.view.file_name())
		controllerName = os.path.basename(self.view.file_name()).replace('Controller.class.php','').replace('.php','')
		
		for sel in self.view.sel():
			# 获取当前选中文字
			action = self.view.substr(sel)
			if action in actions.keys():
				param = actions[action]
				self.host = self.host.replace('{m}', moduleName)
				self.host = self.host.replace('{c}', controllerName)
				self.host = self.host.replace('{a}', action)
				webbrowser.open(self.host + '&' + param)


	# 解析参数
	def parseParam(self,paramStr):
		if not paramStr:
			return ''
		param = ''

		for s in paramStr.replace('$','').split(','):
			if len(s.split('=')) == 1:
				param += (s + '=&')

			if len(s.split('=')) == 2:
				k,v = s.split('=')
				param += ("%s=%s&" % (k,v))

		return param.rstrip('&').replace("'",'').replace('"','')