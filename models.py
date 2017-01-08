from django.db import models

class BlogPost(models.Model):
	title = models.CharField(max_length=80, db_index='True') #database indexing for title
	slug = models.SlugField(max_length=80, db_index='True')	#database indexing for slug
	blog_text = models.TextField()
	pub_date = models.DateTimeField('Date Published')

	def __str__(self):
		return self.title

	@permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Comments(models.Model):
	blog_post = models.ForeignKey(BlogPost)
	commment_text = models.CharField(max_length=300, help_text='Add a comment')
	
	
		
