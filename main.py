from rembg import remove
input_path = 'pexels-simon-robben-614810.jpg'
output_path = 'pexels-simon-robben-new.jpg'

with open(input_path,'rb') as i:
    with open (output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)