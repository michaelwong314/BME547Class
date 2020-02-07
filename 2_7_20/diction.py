def create_dictionary():
#   new_dictionary = {"day": "between sunrise and sunset",
#                    "food": "something to eat",
#                     "night":  "when the moon is out"}
    new_patient = {"last name": "Smith", "first name": "Bob", "age": 60, "married": False,"test results": [0, 16, 23, 2.3]}
    test_one = new_patient["test reults"][3]
    print(test_one)
    return new_dictionary

def read_dictionary(my_dict):
    my_key = "night"
    y = my_dict[my_key]
    print("The definition of {} is {}".format(my_key, y))
    return
    
def output_dictionary(in_dictionary):
    print("Variable type:")
    print(type(in_dictionary))
    print("Dictionary contents:")
    print(in_dictionary)

# __name__ == "__main__":
#   my_dictionary = create_dictionary()
#   output_dictionary(my_dictionary)

def save_Json(patient):
    import json
    filename = "patient_data.txt"
    out_file = open(filename, 'w')
    json.dump(patient, out_file)
    out_file.close()
    
if __name__ == "__main__":
    x = create_patient()
    save_Json(x)