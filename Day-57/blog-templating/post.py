class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/bd948ffae277f4777aab"
        self.response = requests.get(blog_url)
        self.all_posts = response.json()
        return render_template("index.html", posts= all_posts)