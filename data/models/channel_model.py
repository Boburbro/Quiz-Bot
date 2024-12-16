class Channel:
    def __init__(self, id: int, title: str, link: str):
        self.id = id
        self.title = title
        self.link = link

    def __repr__(self):
        return f"Channel(id={self.id}, title='{self.title}', link='{self.link}')"


