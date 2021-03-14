import os
import sys
import shutil

def generate_site_files():
	content_directory = sys.argv[1]

	if os.path.isdir("./dist"):
		shutil.rmtree("./dist")

	os.mkdir("./dist")
	os.mkdir("./dist/about")
	os.mkdir("./dist/blog")
	os.mkdir("./dist/story")
	os.mkdir("./dist/essays")

	generate_homepage(content_directory)
	# create about folder
	# create blog folder
	# create essays folder
	# create story folder
	shutil.copy("./css/blog.css", "./dist")
	shutil.copy("/css/bootstrap.min.css", "./dist")

def generate_homepage(content_directory):
	welcome_content_file = content_directory + '/index.txt'
	preview_1_content_file = content_directory + '/story/1.txt'

	# latest_essay_filename = get_greatest_lexicographic_filename(content_directory + '/essays')
	# preview_2_content_file = content_directory + '/essays/' + latest_essay_filename
	preview_2_content_file = content_directory + '/essays/placeholder.txt'

	latest_blog_post_filename = get_greatest_lexicographic_filename(content_directory + '/blog-posts')
	post_content_file = content_directory + '/blog-posts/' + latest_blog_post_filename

	welcome_content = get_content(welcome_content_file)
	preview_1_content = get_content(preview_1_content_file)
	preview_2_content = get_content(preview_2_content_file)
	post_content = get_content(post_content_file)

	html = create_home_html(welcome_content, preview_1_content, preview_2_content, post_content)

	with open("./dist/index.html", "w") as home_html_file:
		home_html_file.write(html)

def get_greatest_lexicographic_filename(directory_path):
	filenames = os.listdir(directory_path)
	filenames.sort()
	if len(filenames) == 0:
		return None
	return filenames[-1]

def create_home_html(welcome_content, preview_1_content, preview_2_content, post_content):
	page_title = 'Blaine Believes · Home'

	html_string = '<!doctype html>'
	html_string += '<html lang="en">'
	html_string += create_head_element(page_title)
	html_string += create_home_body_element(welcome_content, preview_1_content, preview_2_content, post_content)
	html_string += '</html>'
	return html_string

def create_head_element(title):
	head_string = get_template_string("./templates/head.html")
	head_string = head_string.replace("##title##", title)
	return head_string

def create_home_body_element(welcome, preview_1, preview_2, post):
	body_string = '<body>'
	body_string += '<div class="container">'
	body_string += create_header_element()
	body_string += create_nav_element()
	body_string += create_welcome_banner(welcome)
	body_string += create_preview_row(preview_1, "My Story", preview_2, "Essays")
	body_string += '</div>'
	body_string += create_main_element(post)
	body_string += create_footer_element()
	body_string += '</body>'
	return body_string

def create_header_element():
	return get_template_string("./templates/header.html")

def create_nav_element():
	return get_template_string("./templates/nav.html")

def create_welcome_banner(content):
	banner_string = get_template_string("./templates/welcome-banner.html")
	banner_string = banner_string.replace("##h1##", content[0])
	banner_string = banner_string.replace("##p##", content[1])
	return banner_string

def create_preview_row(element1, heading1, element2, heading2):
	row_string = get_template_string("./templates/preview-row.html")
	row_string = row_string.replace("##heading1##", heading1)
	row_string = row_string.replace("##title1##", element1[0])
	row_string = row_string.replace("##text1##", truncate_string(element1[1]))
	row_string = row_string.replace("##heading2##", heading2)
	row_string = row_string.replace("##title2##", element2[0])
	row_string = row_string.replace("##text2##", truncate_string(element2[1]))
	return row_string

def create_main_element(main_content):
	main_string = get_template_string("./templates/main.html")
	main_string = main_string.replace("##content##", main_content)
	return main_string

def create_footer_element():
	return get_template_string("./templates/footer.html")

def get_template_string(filename):
	template = ""
	with open(filename) as file:
		template = file.read()
	return minify_html(template)

def get_content(filename):
	lines = []
	with open(filename) as file:
		lines = file.readlines()
	content = []
	for line in lines:
		if line != "\n":
			content.append(line)
	return content

def minify_html(html_string):
	minified = html_string.replace('\n', '')
	minified = minified.replace('\t', '')
	return minified

def truncate_string(str):
	if len(str) > 100:
		return str[:95] + ". . ."
	else:
		return str

if __name__ == "__main__":
	generate_site_files()