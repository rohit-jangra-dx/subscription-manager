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

class Duration(Enum):
    TRIAL = 1   # 1 month
    MONTHLY = 1
    QUARTERLY = 3

#pricing
SUBSCRIPTION_PRICES = {
    Category.MUSIC:{
        Plan.FREE: 0,
        Plan.PERSONAL: 100,
        Plan.PREMIUM: 250
    },
    Category.VIDEO:{
        Plan.FREE: 0,
        Plan.PERSONAL: 200,
        Plan.PREMIUM: 500
    },
    Category.PODCAST:{
        Plan.FREE: 0,
        Plan.PERSONAL: 100,
        Plan.PREMIUM: 300
    }
}

TOPUP_PRICES = {
    TopUpType.FOUR_DEVICE: 50,
    TopUpType.TEN_DEVICE: 100
}

PLAN_DURATIONS = {
    Plan.FREE: Duration.TRIAL,
    Plan.PERSONAL: Duration.MONTHLY,
    Plan.PREMIUM: Duration.QUARTERLY
}

RENEWAL_REMINDER_DAYS = 10
MAX_SUBSCRIPTIONS_PER_CATEGORY = 1

