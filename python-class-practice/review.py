review=[
    {
    "negative":"this ia a very bad product i order a month ago",
    "positive":"this product is very good go for it",
    "bad_products":["shoes","cricket bat"],
    "good_products":["books","mobile phones"]

    },
 ]
with open("review.txt","w")as file:
    for key,values in review[0].items():
        # if key in ["positive","good_products"]
        file.write(f"{key}:{values}\n")
# for i in review:
#     for key in i.keys():
#         print(key)
#     query=f"""create table if not exists product_review
#         {key[0]} varchar(100),
#         {key[0]} varchar(100),
#         {key[0]} varchar(100),
#         {key[0]} varchar(100)
#         """