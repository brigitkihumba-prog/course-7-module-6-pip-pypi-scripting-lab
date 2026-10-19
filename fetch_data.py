import requests


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))

    with open("api_result.txt", "w") as file:
        file.write(f"Title: {post.get('title', 'No title found')}\n")
        file.write(f"Body: {post.get('body', '')}\n")