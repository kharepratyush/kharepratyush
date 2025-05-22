from datetime import datetime
import requests
import json
import os

USER_ID = "5baac880a732"   # find yours in the page's HTML under window.__APOLLO_STATE__
OUTPUT_DATA = os.path.join(os.path.dirname(__file__), '../docs/_data/medium_posts.json')


def fetch_page(to_cursor=None):
    url = f"https://medium.com/_/api/users/{USER_ID}/profile/stream"
    params = {"limit": 10}
    if to_cursor:
        params["to"] = to_cursor

    # Medium prefixes its JSON payload with )]}while(1);</x>
    r = requests.get(url, params=params)
    raw = r.text
    body = raw.split("])}while(1);</x>")[-1]
    return json.loads(body)

def parse_posts(data):
    posts = data["payload"]["references"]["Post"]
    users = data["payload"]["references"]["User"]
    result = []
    for pid, p in posts.items():
        title = p.get("title", "")
        subtitle = p.get("content", {}).get("subtitle", "")
        author_id = p.get("creatorId")
        author_name = users.get(author_id, {}).get("name", "")
        ts = p.get("firstPublishedAt", 0) / 1000
        published_on = datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        rt = p.get("virtuals", {}).get("readingTime", 0)
        tags = [t.get("slug") for t in p.get("virtuals", {}).get("tags", [])]
        url = f"https://medium.com/p/{pid}"
        result.append({
            "title": title,
            "subtitle": subtitle,
            "author_name": author_name,
            "published_on": published_on,
            "read_time": f"{rt:.1f}",
            "tags": tags,
            "url": url
        })
    return result


def main():
    all_posts = []
    data = fetch_page()
    all_posts.extend(parse_posts(data))
    to = data["payload"]["paging"]["next"].get("to")
    while to:
        data = fetch_page(to)
        all_posts.extend(parse_posts(data))
        to = data["payload"]["paging"]["next"].get("to")
    # Sort posts by published_on descending
    all_posts.sort(key=lambda x: x["published_on"], reverse=True)
    # Write to JSON for Jekyll data
    os.makedirs(os.path.dirname(OUTPUT_DATA), exist_ok=True)
    with open(OUTPUT_DATA, "w", encoding="utf-8") as f:
        json.dump(all_posts, f, ensure_ascii=False, indent=2)
    print(f"Exported {len(all_posts)} Medium posts to {OUTPUT_DATA}")

if __name__ == "__main__":
    main()

