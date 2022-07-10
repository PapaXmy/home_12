import json

def load_posts() -> list[dict]:
    with open('posts.json', 'r') as file:
        return json.load(file)

def get_posts_by_word(word: str) -> list[dict]:
    posts = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            posts.append(post)
    return posts

def add_post(post: dict) -> dict:
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w') as file:
        json.dump(posts, file)
    return post
