class MetadataRouter:

    KEYWORDS = {
        "author": [
            "author",
            "who wrote"
        ],

        "page_count": [
            "pages",
            "page count",
            "how many pages"
        ],

        "title": [
            "title"
        ],

        "creator": [
            "creator"
        ],

        "producer": [
            "producer"
        ],

        "subject": [
            "subject"
        ]
    }

    @classmethod
    def get_field(
        cls,
        question
    ):

        question = question.lower()

        for field, keywords in cls.KEYWORDS.items():

            for keyword in keywords:

                if keyword in question:

                    return field

        return None