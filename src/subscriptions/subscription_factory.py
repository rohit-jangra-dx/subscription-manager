from datetime import datetime
from src.subscriptions.Subscription import Music, Video, Podcast
from src.config.config import Category, Plan


def subscription_factory(category: Category, plan: Plan, start_date: datetime):
    if category == Category.MUSIC:
        return Music(plan=plan, start_date=start_date)
    elif category == Category.VIDEO:
        return Video(plan=plan, start_date=start_date)
    elif category == Category.PODCAST:
        return Podcast(plan=plan, start_date=start_date)
    else:
        raise ValueError(f"Unsupported category: {category}")
