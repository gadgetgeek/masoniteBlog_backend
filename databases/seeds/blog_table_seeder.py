"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "Java in 60 Seconds", "body": "this is my blog"})
        Blog.create({"title": "PHP in 60 Seconds", "body": "this is my blog2"})
        Blog.create({"title": "Python in 60 Seconds", "body": "this is my blog3"})
