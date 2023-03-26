time = ""


def setup():
    size(100, 100)


def draw():
    background(0)
    # Every 30 frames request new data
    if (frame_count % 30 == 0):
        thread("requestData")
    text(time, 10, 50)

# This happens as a separate thread and can take as long as it wants


def request_data():
    global time
    json = load_json_object("http://time.jsontest.com/")
    time = json.get_string("time")
