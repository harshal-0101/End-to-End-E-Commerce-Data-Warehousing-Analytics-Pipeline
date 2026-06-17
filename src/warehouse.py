import logging as log
from database import engine
from sqlalchemy import types


log.basicConfig(
    filename="logs/pipeline.log",
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_customer_revenue(customer_df):
    customer_df.to_sql(name = "customer_revenue", con=engine, if_exists = "replace", index = False)
    return customer_df

def load_product_revenue(product_df):
    product_df.to_sql(name = "product_revenue", con = engine, if_exists = "replace", index = False)
    return product_df

def load_monthly_revenue(monthly_revenue):
    monthly_revenue.to_sql(name = "monthly_revenue", con = engine, if_exists = "replace", index = False)
    return monthly_revenue

def load_state_revenue(state_revenue):
    state_revenue.to_sql(name = "state_revenue", con = engine, if_exists = "replace", index = False)
    return state_revenue



dtype = {
    "order_id": types.Text(),
    "customer_id": types.Text(),
    "order_status": types.Text(),
    "order_purchase_timestamp": types.DateTime(),
    "items_count": types.BigInteger(),
    "total_order_value": types.Numeric(12,2)
}

def load_order_summary(order_summary):
    order_summary.to_sql(name = "order_summary", con = engine, if_exists = "replace", index = False, dtype = dtype)
    return order_summary