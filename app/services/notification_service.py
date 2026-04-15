from datetime import datetime

notifications: list[dict] = []


def notify_subscribers(subscribers: list, article_title: str, author_username: str) -> None:
    for user in subscribers:
        notifications.append({
            "user_id": user.id,
            "username": user.username,
            "message": f"New article '{article_title}' by {author_username}",
            "created_at": datetime.utcnow().isoformat()
        })


def get_notifications_for_user(user_id: int) -> list[dict]:
    return [n for n in notifications if n["user_id"] == user_id]