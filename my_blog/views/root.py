from pyramid.view import view_config
import my_blog.resources
from my_blog.blogdata import BlogData
from pyramid.httpexceptions import HTTPFound
import re


@view_config(context='my_blog:resources.Root', renderer='home.jinja2')
@view_config(context='my_blog:resources.Root', renderer='home.jinja2', name='home')
def my_view(request):
    #get mongoDB posts
    blog_data = BlogData(request)
    posts = blog_data.get_recent_posts(10, 1)

    entries = []
    for post in posts:
        postDate = post[u'postDate'].strftime("%B %d %Y")
        entry = {'title': post[u'title'],
               'url': post[u'url'],
               'date': postDate,
                        'author': post[u'author'],
                        'blog_body': strip_tags(post[u'postText'][:1000]) + '...',
                        'tags': post[u'tags']}
        entries.append(entry)
    return {'cur_page': 'home', 'page_title': 'Welcome to Christian\'s Blog', 'entries': entries}

@view_config(context='my_blog:resources.Root', renderer='about.jinja2', name='about')
def about(request):
    return {'cur_page':'about'}

@view_config(context='pyramid.httpexceptions.HTTPNotFound', renderer='404_error.jinja2')
def not_found(request):
    return{'message': 'Error 404, Page Not Found',  'cur_page': '', 'page_title': 'Requested Page Not Found'}


def strip_tags(content):
    return re.sub('<[^<]*?>', '', content)
