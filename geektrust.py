from src.subscriptions.subscription_factory import subscription_factory
from src.config.config import Category, Plan
from datetime import  datetime
def main():
    datex = datetime.strptime("20-02-2022","%d-%m-%Y")
    x = subscription_factory(category=Category.MUSIC,plan=Plan.PERSONAL,start_date=datex)
    print(x.end_date)



if __name__ == "__main__":
    main()