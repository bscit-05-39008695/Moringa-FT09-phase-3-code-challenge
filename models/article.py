class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self._author_id = author_id
        self._magazine_id = magazine_id
        self._author = None
        self._magazine = None

    def __repr__(self):
        return f'<Article {self.title}>'
        @property
        def id(self):
            return self._id
        @id.setter
        def id(self, id):
            self._id = id

            @property
            def title(self):
                return self._title
            @title.setter
            def title(self, title):
                self._title = title

                @property
                def content(self):
                    return self._content
                @content.setter
                def content(self, content):
                    self._content = content

                    @property
                    def author_id(self):
                        return self._author_id
                    @author_id.setter
                    def author_id(self,author_id):
                        self._author_id = author_id

                        @property
                        def magazine_id(self):
                            return self._magazine_id
                        @magazine_id.setter
                        def magazine_id(self, magazine_id):
                            self.magazine_id = magazine_id
