class AppClassifier:
    @staticmethod
    def classify(name: str):
        if not name:
            return "UNKNOWN"

        name = name.lower()

        youtube_patterns = [
            "youtube",
            "googlevideo",
            "ytimg",
            "youtubei"
        ]

        if any(p in name for p in youtube_patterns):
            return "YOUTUBE"

        if "facebook" in name:
            return "FACEBOOK"

        if "google" in name:
            return "GOOGLE"

        if "github" in name:
            return "GITHUB"

        if "netflix" in name:
            return "NETFLIX"

        return "UNKNOWN"