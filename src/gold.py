import pandas as pd

def create_customer_revenue(orders_df, order_items_df):

    merged_df = pd.merge(orders_df, order_items_df, on="order_id")

    customer_revenue = merged_df.groupby("customer_id").agg(
        total_orders=("order_id", "nunique"),
        total_revenue=("price", "sum")
    ).reset_index()

    customer_revenue.rename(columns={"price": "total_revenue"}, inplace=True)

    return customer_revenue

def create_product_revenue(products_df, order_items_df):
    
    merged_df = pd.merge(products_df, order_items_df, on="product_id")

    product_revenue = merged_df.groupby(["product_id", "product_category_name"]).agg(
        quantity_sold=("order_id", "count"),
        total_revenue=("price", "sum")
    ).reset_index()

    return product_revenue

def create_monthly_revenue(orders_df, order_items_df):

    merged_df = pd.merge(
        orders_df,
        order_items_df,
        on="order_id"
    )

    merged_df["order_purchase_timestamp"] = pd.to_datetime(
        merged_df["order_purchase_timestamp"]
    )

    merged_df["month_year"] = (
        merged_df["order_purchase_timestamp"]
        .dt.to_period("M")
    )

    monthly_revenue = (
        merged_df.groupby("month_year")
        .agg(total_revenue=("price", "sum"))
        .reset_index()
    )

    monthly_revenue["month_year"] = (
        monthly_revenue["month_year"]
        .dt.to_timestamp()
    )

    return monthly_revenue

def create_state_revenue(customers_df, orders_df, order_items_df):

    merged_df = pd.merge(orders_df, order_items_df, on="order_id")
    merged_df = pd.merge(merged_df, customers_df, on="customer_id")

    state_revenue = merged_df.groupby("customer_state").agg(
        total_revenue=("price", "sum")
    ).reset_index()

    state_revenue.rename(columns={"price": "total_revenue"}, inplace=True)

    return state_revenue

def create_order_summary(orders_df, order_items_df):

    merged_df = pd.merge(orders_df, order_items_df, on="order_id")

    order_summary = merged_df.groupby([
            "order_id",
            "customer_id",
            "order_status",
            "order_purchase_timestamp"
        ]).agg(
            items_count=("product_id", "count"),
            total_order_value=("price", "sum")
            ).reset_index()

    order_summary.rename(columns={"price": "total_order_value"}, inplace=True)

    return order_summary