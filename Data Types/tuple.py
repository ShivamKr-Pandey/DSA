fullname = ("Shivam", "Kumar", "Pandey")
print(type(fullname))

def converted_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = converted_seconds(5000)
# print(type(result))
# print(result)

# Unpacking the Tuple

hours, minutes , seconds = result
# print(hours, minutes, seconds)

hours, minutes, seconds = converted_seconds(2000)
print(hours, minutes, seconds)

