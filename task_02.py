# the function reads a text file from a given location and adds the values from the 
# file to a dictionary with the keys provided in cats_info_keys. As a result it returns 
# the list of dictionaries. The text file should contain info in the following format:
#
#           60b90c1c13067a15887e1ae1,Tayson,3\n
#           60b90c2413067a15887e1ae2,Vika,1\n
#           60b90c2e13067a15887e1ae3,Barsik,2\n
#           60b90c3b13067a15887e1ae4,Simon,12\n
#           60b90c4613067a15887e1ae5,Tessi,5


def get_cats_info(path):
    try:
        cats_info_keys = ["id", "name", "age"]
        result = []
        with open(path, "r", encoding="UTF-8") as cats_info:
            for cats_info_values in cats_info:
                cats_info_values = cats_info_values.strip()
                cats_info_values = cats_info_values.split(',')
                result.append(dict(zip(cats_info_keys, cats_info_values)))
            return result
    except FileNotFoundError:
        print(f"FileNotFoundError: No such file or directory: {path}")


if __name__ == '__main__':
    get_cats_info()
