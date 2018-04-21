import Algorithmia

input = {
  "image": "data://.algo/deeplearning/ColorfulImageColorization/perm/algo6.jpg"
}
client = Algorithmia.client('sim/f3rUsgCEV4kvdOZXmLKcvGL1')
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.13')
print(algo.pipe(input))
