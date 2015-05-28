from application import app
from application.controllers import update_similarity, recommend_webtoon

# app.run()
update_similarity.update_similarity()
recommend_webtoon.similarity_loading()
app.run(host = '0.0.0.0', port = 5007)

