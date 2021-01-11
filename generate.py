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

generate_homepage()

# create index.html
# create about folder
# create blog folder
# create essays folder
# create story folder
# copy css files

def generate_homepage():
	welcome_content_file = content_directory + '/index.txt'
	preview_1_content_file = ""
	preview_2_content_file = ""
	post_content_file = ""

	welcome_content = get_content(welcome_content_file)
	preview_1_content = get_content(preview_1_content_file)
	preview_2_content = get_content(preview_2_content_file)
	post_content = get_content(post_content_file)

	with open("./dist/index.html", "w") as home_html_file:
		html = create_home_html(welcome_content, preview_1_content, preview_2_content, post_content)
		home_html_file.write(html)

def create_home_html(welcome_content_file, preview_1_content_file, preview_2_content_file, post_content_file):
	page_title = 'Blaine Believes · Home'

	html_string = '<!doctype html>'
	html_string += '<html lang="en">'
	html_string += create_head_element(page_title)
	html_string += create_home_body_element(welcome_content, preview_1_content, preview_2_content, post_content)
	html_string += '</html>'
	return html_string

def create_head_element(title):
	head_string = ""
	with open("./templates/head.html") as head_template_file:
		head_string = head_template_file.read()
	head_string = minify_html(head_string)
	head_string = head_string.replace("<title></title>", "<title>{}</title>".format(title))
	return head_string

def create_home_body_element(welcome, preview_1, preview_2, post):
	body_string = '<body>'
	body_string += '<div class="container">'
	body_string += create_header_element()
	body_string += create_nav_element()
	body_string += create_welcome_banner(welcome_content)
	body_string += create_row(create_preview_block(preview_1), create_preview_block(preview_2))
	body_string += '</div>'
	body_string += create_main_element(post)
	body_string += create_footer_element()
	body_string += '</body>'
	return body_string

def get_content(filename):
	content = []
	with open(filename) as file:
		content = file.readlines()
	return content

def minify_html(html_string):
	minified = html_string.replace('\n', '')
	minified = minified.replace('\t', '')
	return minified