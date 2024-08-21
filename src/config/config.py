from enum import Enum, auto


# Enums
class Category(Enum):
    MUSIC = auto()
    VIDEO = auto()
    PODCAST = auto()

CATEGORY_FROM_STRING = {
    'MUSIC': Category.MUSIC,
    'VIDEO': Category.VIDEO,
    'PODCAST': Category.PODCAST
}


class Plan(Enum):
    FREE = auto()
    PERSONAL = auto()
    PREMIUM = auto()

PLAN_FROM_STRING = {
    "FREE": Plan.FREE,
    "PERSONAL": Plan.PERSONAL,
    "PREMIUM": Plan.PREMIUM
}


class TopUpType(Enum):
    FOUR_DEVICE = auto()
    TEN_DEVICE = auto()

TOPUP_TYPE_FROM_STRING = {
    "FOUR_DEVICE": TopUpType.FOUR_DEVICE,
    "TEN_DEVICE": TopUpType.TEN_DEVICE
}


# plan to duration mapping
PLAN_DURATION = {
    Plan.FREE: 1,
    Plan.PERSONAL: 1,
    Plan.PREMIUM: 3
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
MAX_TOPUP_LIMIT = 1
DATE_FORMAT="%d-%m-%Y"