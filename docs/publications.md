---
layout: page
title: "Blogs"
---

<style>
.site-container {
  max-width: 750px;
  margin: 0 auto;
  padding: 2em 1.5em 1.5em 1.5em;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.07);
}
.site-container h2 {
  color: #0077B5;
  font-weight: 700;
  margin-top: 1.5em;
}
.site-container .blog-list {
  padding: 0;
  margin: 0;
}
.site-container .blog-item {
  margin-bottom: 2.2em;
  padding-bottom: 1.2em;
  border-bottom: 1px solid #e0e0e0;
  list-style: none;
}
.site-container .blog-title {
  font-size: 1.15em;
  font-weight: 600;
  color: #222;
  margin-bottom: 0.2em;
}
.site-container .blog-meta {
  color: #0077B5;
  font-size: 0.98em;
  margin-bottom: 0.4em;
}
.site-container .blog-desc {
  font-size: 1.04em;
  color: #444;
  margin-bottom: 0.4em;
}
.site-container a {
  color: #0077B5;
  text-decoration: none;
  font-weight: 500;
}
.site-container a:hover {
  text-decoration: underline;
}
</style>

<div class="site-container">

<ul class="blog-list">
{% for post in site.data.medium_posts %}
  <li class="blog-item">
    <div class="blog-title">{{ post.title }}</div>
    <div class="blog-meta">{{ post.published_on }} · {{ post.author_name }} · ~{{ post.read_time }} min read</div>
    <div class="blog-desc">{{ post.subtitle }}</div>
    <a href="{{ post.url }}" target="_blank">Read on Medium</a>
  </li>
{% endfor %}
</ul>

</div>
