import converter

# Write in your username here in the format email/token
user = "cedilloj@adobe.com/token"

# Add in the base path for your repo here
base_path= "src"

# Write out your article ids here as a comma separated list
articles = [360041456192, 360040757112, 360047251111]


converter.get_published_articles(user, base_path, articles)








