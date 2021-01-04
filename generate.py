import os
import shutil

if os.path.isdir("./dist"):
    shutil.rmtree("./dist")

os.mkdir("./dist")
os.mkdir("./dist/about")
os.mkdir("./dist/blog")
os.mkdir("./dist/story")
os.mkdir("./dist/essays")

with open("./dist/index.html", "w") as home_html_file:
    write_home_html(home_html_file)

def write_home_html(home_html_file):
    home_html_file.write('<!doctype html>\n')
    home_html_file.write('<html lang="en">')
    write_home_head(home_html_file, 1)
    write_home_body(home_html_file, 1)
    home_html_file.write('</html>')

def write_home_head(home_html_file, indents):
    pass

def write_home_body(home_html_file, indents):
    pass

# create dist folder
# create index.html
# create about folder
# create blog folder
# create essays folder
# create story folder
# copy css files