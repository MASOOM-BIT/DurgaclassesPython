from pymongo import MongoClient

# Connect to MongoDB running locally
client = MongoClient("mongodb://localhost:27017/")

try:
    # Connect to the "shop" database
    database = client["shop"]

    # Connect to the "products" collection
    products = database["products"]

    # Query for a product with the name "Dell Laptop"
    query = {"name": "Dell Laptop"}
    product = products.find_one(query)

    if product:
        print("Product Found:", product)
    else:
        print("No product found with the name 'Dell Laptop'")

except Exception as e:
    print("Error:", e)

finally:
    client.close()
