from extract import extract
from bronze import bronzeLayer, save_bronze
from silver import silver_layer, save_silver
from validations import (
    validate_orders,
    validate_customers,
    validate_products,
    validate_sellers
)
from gold import (
    create_customer_revenue,
    create_product_revenue,
    create_state_revenue,
    create_order_summary,
    create_monthly_revenue
)
from warehouse import(
    load_customer_revenue,
    load_product_revenue,
    load_monthly_revenue,
    load_state_revenue,
    load_order_summary
)
import logging as log

log.basicConfig(
    filename="logs/pipeline.log",
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

files = [

    (
        "./data/raw/olist_customers_dataset.csv",
        "customers",
        "./data/bronze/bronze_customers.csv",
        "./data/silver/silver_customers.csv"
    ),

    (
        "./data/raw/olist_geolocation_dataset.csv",
        "geolocation",
        "./data/bronze/bronze_geolocation.csv",
        "./data/silver/silver_geolocation.csv"
    ),

    (
        "./data/raw/olist_order_items_dataset.csv",
        "order_items",
        "./data/bronze/bronze_order_items.csv",
        "./data/silver/silver_order_items.csv"
    ),

    (
        "./data/raw/olist_order_payments_dataset.csv",
        "payments",
        "./data/bronze/bronze_order_payments.csv",
        "./data/silver/silver_order_payments.csv"
    ),

    (
        "./data/raw/olist_order_reviews_dataset.csv",
        "reviews",
        "./data/bronze/bronze_order_reviews.csv",
        "./data/silver/silver_order_reviews.csv"
    ),

    (
        "./data/raw/olist_orders_dataset.csv",
        "orders",
        "./data/bronze/bronze_orders.csv",
        "./data/silver/silver_orders.csv"
    ),

    (
        "./data/raw/olist_products_dataset.csv",
        "products",
        "./data/bronze/bronze_products.csv",
        "./data/silver/silver_products.csv"
    ),

    (
        "./data/raw/olist_sellers_dataset.csv",
        "sellers",
        "./data/bronze/bronze_sellers.csv",
        "./data/silver/silver_sellers.csv"
    ),

    (
        "./data/raw/product_category_name_translation.csv",
        "category_translation",
        "./data/bronze/bronze_product_category_translation.csv",
        "./data/silver/silver_product_category_translation.csv"
    )
]

log.info("Pipeline Started")
validators = {
    "orders": validate_orders,
    "customers": validate_customers,
    "products": validate_products,
    "sellers": validate_sellers
    }
for raw_path, dataset_name, bronze_path, silver_path in files:
    try:

        df = extract(raw_path)

        log.info(
            f"{dataset_name} loaded - Rows: {len(df)}"
        )

        # Bronze
        bronze_df = bronzeLayer(df,raw_path.split("/")[-1])

        save_bronze(
            bronze_df,
            bronze_path
        )

        log.info(
            f"{dataset_name} bronze created"
        )
        if dataset_name in validators:

            validators[dataset_name](bronze_df)

            log.info(f"{dataset_name} validation passed")

        # Silver
        silver_df = silver_layer(
            bronze_df,
            dataset_name
        )

        save_silver(
            silver_df,
            silver_path
        )

        log.info(
            f"{dataset_name} silver created"
        )

    except Exception as e:

        log.error(
            f"{dataset_name} failed: {e}"
        )

orders_df = extract("./data/silver/silver_orders.csv")
order_items_df = extract("./data/silver/silver_order_items.csv")
customer_df = extract("./data/silver/silver_customers.csv")
product_df = extract("./data/silver/silver_products.csv")
    
    
customer_revenue = create_customer_revenue(orders_df, order_items_df)
customer_revenue.to_csv("./data/gold/customer_revenue.csv", index=False)
log.info("Customer revenue created")

product_revenue = create_product_revenue(product_df, order_items_df)
product_revenue.to_csv("./data/gold/product_revenue.csv", index=False)
log.info("Product revenue created")

state_revenue = create_state_revenue(customer_df, orders_df, order_items_df)
state_revenue.to_csv("./data/gold/state_revenue.csv", index=False)
log.info("State revenue created")

order_summary = create_order_summary(orders_df, order_items_df)
order_summary.to_csv("./data/gold/order_summary.csv", index=False)
log.info("Order summary created")

monthly_revenue = create_monthly_revenue(orders_df, order_items_df)
monthly_revenue.to_csv("./data/gold/monthly_revenue.csv", index=False)  
log.info("Monthly revenue created")
        
        
        
log.info("Gold to Database pipeline started")

load_customer_revenue(customer_revenue)
log.info("customer revenue loaded in database")

load_product_revenue(product_revenue)
log.info("product revenue loaded in database")

load_monthly_revenue(monthly_revenue)
log.info("monthly revenue loaded in database")

load_state_revenue(state_revenue)
log.info("state revenue loaded in database")

load_order_summary(order_summary)
log.info("order summary loaded in database")
  
log.info("Pipeline Completed")