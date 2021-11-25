
def improve_one(func):
    def inner(*args,**keyargs):
        
        func(*args)
        print(f"Im a better one of {args}")
    return inner

@improve_one
def Basic_func(name):
    print("Im basic")

Basic_func("Basic one")

