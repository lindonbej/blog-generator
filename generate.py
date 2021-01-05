import os
import sys
import shutil

content_directory = sys.argv[1]

if os.path.isdir("./dist"):
	shutil.rmtree("./dist")

os.mkdir("./dist")
os.mkdir("./dist/about")
os.mkdir("./dist/blog")
os.mkdir("./dist/story")
os.mkdir("./dist/essays")

with open("./dist/index.html", "w") as home_html_file:
	content_file = content_directory + '/index.txt'
	html = create_home_html(content_file)
	home_html_file.write(html)

# create index.html
# create about folder
# create blog folder
# create essays folder
# create story folder
# copy css files

def create_home_html(content_file):
	content = []
	with open(content_file) as file:
		content = file.readlines()

	page_title = 'Blaine Believes · Home'
	page_header = content[0]

	html_string = '<!doctype html>'
	html_string += '<html lang="en">'
	html_string += create_head_element(page_title)
	html_string += create_body_element()
	html_string += '</html>'
	return html_string

def create_head_element(title):
	head_string = ""
	with open("./templates/head.html") as head_template_file:
		head_string = head_template_file.read()
	head_string = minify_html(head_string)
	head_string = head_string.replace("<title></title>", "<title>{}</title>".format(title))
	return head_string

def create_body_element():
	body_string = '<body>'
	body_string += '</body>'
	return body_string

def minify_html(html_string):
	minified = html_string.replace('\n', '')
	minified = minified.replace('\t', '')
	return minified