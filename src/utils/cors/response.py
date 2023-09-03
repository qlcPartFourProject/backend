# add cors to response
def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response