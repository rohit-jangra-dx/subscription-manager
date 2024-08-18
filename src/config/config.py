from enum import Enum, auto


# Enums
class Category(Enum):
    MUSIC = auto()
    VIDEO = auto()
    PODCAST = auto()


class Plan(Enum):
    FREE = auto()
    PERSONAL = auto()
    PREMIUM = auto()


class TopUpType(Enum):
    FOUR_DEVICE = auto()
    TEN_DEVICE = auto()


# plan to duration mapping
PLAN_DURATION = {
    Plan.FREE: 1,
    Plan.PERSONAL: 1,
    Plan.PREMIUM: 3
}

PLAN_FROM_STRING = {
    "FREE": Plan.FREE,
    "PERSONAL": Plan.PERSONAL,
    "PREMIUM": Plan.PREMIUM
}

#pricing
SUBSCRIPTION_PRICES = {
    Category.MUSIC: {
        Plan.FREE: 0,
        Plan.PERSONAL: 100,
        Plan.PREMIUM: 250
    },
    Category.VIDEO: {
        Plan.FREE: 0,
        Plan.PERSONAL: 200,
        Plan.PREMIUM: 500
    },
    Category.PODCAST: {
        Plan.FREE: 0,
        Plan.PERSONAL: 100,
        Plan.PREMIUM: 300
    }
}

TOPUP_PRICES = {
    TopUpType.FOUR_DEVICE: 50,
    TopUpType.TEN_DEVICE: 100
}

RENEWAL_REMINDER_DAYS = 10
MAX_SUBSCRIPTIONS_PER_CATEGORY = 1
