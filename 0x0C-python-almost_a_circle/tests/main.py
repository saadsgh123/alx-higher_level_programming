def get_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    saad = {"arg3": 3, "arg2": "two", "arg1": 5}
    get_args(**saad)
